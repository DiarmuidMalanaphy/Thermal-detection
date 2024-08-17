import cv2

'''
The use case of this function is because the rectangles seemed to only be around a subjects 
hand or their feet, expanding the box made the rectangles more robust.

Grouping them is also a key step here, it makes it so the rectangles are less flashy because before it would select 
a subjects hand and then select their foot meaning the boxes would dash back and forth.
'''
def expand_and_group_rectangles(human_rectangles, colour_frame, expand_margin=2, group_threshold=1, eps=1):
    all_rectangles = []
    
    for (x, y, w, h) in human_rectangles:
        #create an expanded rectangle
        x1, y1 = max(x - expand_margin, 0), max(y - expand_margin, 0)
        x2, y2 = min(x + w + expand_margin, colour_frame.shape[1]), min(y + h + expand_margin, colour_frame.shape[0])
        #Expand the borders of the rectangle.
        expanded_rect = (x1, y1, x2 - x1, y2 - y1)
        all_rectangles.append(expanded_rect)

    # Group the rectangles
    grouped,_ = cv2.groupRectangles(all_rectangles, group_threshold,eps)

    return grouped




def getSnapshotOfRectangles(rectangles, image, group_rectangles=True, group_threshold=1, eps=0.1,expansion_factor = 0.25,with_rectangles = False):
    if group_rectangles:
        # Prepare the rectangles for groupRectangles()
        cv2.groupRectangles(rectangles, group_threshold, eps)
    

    snapshots = []
    for (x, y, w, h) in rectangles:
        # Calculate the expanded region
        x1 = max(x - int(w * expansion_factor), 0)
        y1 = max(y - int(h * expansion_factor), 0)
        x2 = min(x + w + int(w * expansion_factor), image.shape[1])
        y2 = min(y + h + int(h * expansion_factor), image.shape[0])

        # Extract the expanded region from the image
        snapshot = image[y1:y2, x1:x2]
        if with_rectangles:
            snapshots.append((snapshot, (x, y, w, h)))
        else:
            snapshots.append(snapshot)

    return snapshots


def filter_non_overlapping_rectangles(prev_rects, grouped_rectangles):
    non_overlapping_rects = []
    for prev_rect in prev_rects:
        if not any(do_rectangles_overlap(prev_rect, current_rect) for current_rect in grouped_rectangles):
            non_overlapping_rects.append(prev_rect)
    return non_overlapping_rects
def do_rectangles_overlap(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2
    
    
    if x1 > x2 + w2 or x2 > x1 + w1:
        return False
    
    if y1 > y2 + h2 or y2 > y1 + h1:
        return False
    return True

