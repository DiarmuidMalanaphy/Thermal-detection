import cv2
import numpy as np
'''
Collection of basic human detection filters
detect_moving objects is pretty robust 
  -- It doesn't select the centre of a person which is an issue.
  -- It's very useful as it quite accurately returns an array of all moving rectangles.

detect_stationary_objects would be better replaced with a k-means cluster for small images of humans with thermal imagery.
   -- I've looked through papers looking for a dataset for this, the majority tend to use YOLO
   -- I'll try and apply YOLO however it doesn't seem fit for purpose.

'''

def detect_moving_Objects(prev_frame, current_frame):
    # Get the difference between frames
    frame_diff = cv2.absdiff(prev_frame, current_frame)
    # Threshold the image, this is the most tricky part because two different images
    # could have different illuminations and lightings
    # I could use a gradient filter but this works.
    _, moving_thresh = cv2.threshold(frame_diff, 80, 235, cv2.THRESH_BINARY)
    # Thresholding the difference
    kernel_size = 9
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    #morphological closing (dilation followed by erosio)
    # Useful because it generates a cleaner outline of a person.
    filtered = cv2.morphologyEx(moving_thresh, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.dilate(filtered, None, iterations=1)
    # dilate again
    # Canny edge detection is good for getting the edges of a person
    edges = cv2.Canny(dilated,100,240)
    dilated = cv2.dilate(edges, None, iterations=2)
    # The dilation allows me to be less conservative with the contours.
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw bounding boxes for moving objects
    # Collect all the bounding rectangles from the contours
    detections = []
    
    for contour in contours:
        if cv2.contourArea(contour) > 150:
            x, y, w, h = cv2.boundingRect(contour)
            detections.append((x, y, w, h))
    return detections



def detect_stationary_figure(snapshot):
    '''
    Functionally this is incredibly weak - The only way that the moving object one is the frame difference.
    I'll try this again in YOLO.
    '''
    _, thresh = cv2.threshold(snapshot, 130, 235, cv2.THRESH_BINARY)
    kernel_size = 9
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

        # Apply morphological opening (erosion followed by dilation)
    filtered = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
    dilated = cv2.dilate(filtered, None, iterations=1)
          
    edges = cv2.Canny(dilated,120,250)
    dilated = cv2.dilate(edges, None, iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)>200:
            return(True)
    return(False)