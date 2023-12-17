import os
import pickle
import sys

import cv2
import numpy as np

from processData import increaseContrast
from rectangle_modifiers import expand_and_group_rectangles, getSnapshotOfRectangles
from filter_detectors import detect_moving_Objects, detect_stationary_figure, detect_stationary_objects


#from processData import
def Main(directory):

    # directory = "5a"
    # with open('data/kmeans_model.pkl', 'rb') as file:
        # kmeans_model = pickle.load(file)
    # List and sort the bitmap files
    contents = sorted([file for file in os.listdir(directory) if file.endswith('.bmp')])
    prev_frame = None
    prev_rects = None


    '''
    High level overview 
    1 - Step through each image in data to simulate video
    2 - Enhance each image by modifying the contrast and equalising the histogram.
    3 - Compare 2 frames and generate all moving objects by getting the frame difference
    4 - Generate the potentially unmoving targets by looking at previously identified humans and seeing if they match the profile of humans
    5 - Generate boxes for each detected person
    6 - Expand these boxes and group them together to form larger boxes.
    7 - Display the boxes over the original image - convert it to colour so we can see the lovely green boxes.

    '''


    #    1
    for count, filename in enumerate(contents):
        # Increment the frame counter

        file_path = os.path.join(directory, filename)
        curr_frame = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
        
        ''' 2 '''
        # Apply contrast enhancement to current frame
        enhanced_frame = increaseContrast(curr_frame)

        # Convert the enhanced frame to color for drawing rectangles
        colour_frame = cv2.cvtColor(curr_frame, cv2.COLOR_GRAY2BGR)

        
        # Frame differencing for moving objects
        if prev_frame is not None:
            ''' 3 '''
            moving_rectangles = detect_moving_Objects(prev_frame,enhanced_frame)
            ''' 4 '''
            stationary_rectangles = []
            if prev_rects is not None:
                stationary_rectangles = detect_stationary_objects(prev_rects,enhanced_frame) 
                # non_overlapping_rects = filter_non_overlapping_rectangles(prev_rects, grouped_rectangles)
                
            '''5'''
            human_rectangles = moving_rectangles + stationary_rectangles
                
            

            '''6'''
            # generate all rectangles a 
            
            all_rectangles = expand_and_group_rectangles(human_rectangles, colour_frame,expand_margin=1)


            #Draw the grouped rectangles on the color frame
            for (x, y, w, h) in all_rectangles:
                cv2.rectangle(colour_frame, (x, y), (x + w, y + h), (200, 0, 200), 2); 
                        
                
            
            
                
            # Display the original frame with rectangles
            '''7'''
            cv2.imshow('Detected Figures',  colour_frame)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
            
            prev_rects = human_rectangles
        # Update the previous frame for the next iteration
        prev_frame = enhanced_frame
        



    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        input_filename = sys.argv[1]
        Main(input_filename)
    else:
        print("Please provide a filename.")