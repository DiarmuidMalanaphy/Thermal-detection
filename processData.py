import uuid
import cv2
import numpy as np


def increaseContrast(image):
    _, thresholded_image = cv2.threshold(image, 140, 210, cv2.THRESH_TOZERO)
   
    # Apply histogram equalization to enhance the contrast
    equalized_image = cv2.equalizeHist(thresholded_image)
    return equalized_image







def save_snapshot_if_confirmed(snapshot):
    
    # Generate a unique filename

    filename = f"{uuid.uuid4()}.png"
    filepath = f"dataset/{filename}"
    
    
    cv2.imwrite(filepath, snapshot) 
    print(f"Snapshot would be saved as {filepath}")  
    return filepath
