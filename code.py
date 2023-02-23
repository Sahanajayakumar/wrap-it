#convert to frame
import cv2
 
capture = cv2.VideoCapture('D:\code\S1r\s1ep4r.mp4')
 
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'D:/code/S1r/frames/frame_{frameNr}_S1EP4.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
    #print("Frame rate:", capture.get(cv2.CAP_PROP_FPS))
      
 
capture.release()

import cv2
import os
import shutil

# Set the path to the folder containing the images
folder_path = 'D:/code/S1r/frames'
destination_dir = 'D:/code/S1r/brightest_points'

# Get a list of all the images in the folder
image_filenames = os.listdir(folder_path)

# Iterate over the images in the folder
for filename in image_filenames:
    # Read the image
    image = cv2.imread(os.path.join(folder_path, filename))
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Find the minimum and maximum values in the image
    (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(gray_image, mask=None)

    # The brightest point will be the maximum value
    brightest_point = max_loc
    lowest_point = min_loc
    print(brightest_point)
    print(filename)
    
    
    # Draw a circle at the brightest point
    cv2.circle(gray_image, brightest_point, radius=5, color=(0, 0, 0), thickness=10)
    cv2.circle(gray_image, lowest_point, radius=5, color=(255, 255, 255), thickness=10)
   # image_extensions = ['.jpg', '.png', '.gif']  # list of allowed image file extensions
    cv2.imwrite(os.path.join(destination_dir, filename), gray_image)
    
    
    #print(f'Brightest point location: {max_loc}')
    #print(f'Darkest point location: {min_loc}')
    
    # Display the image with the circle drawn on it
    ##cv2.waitKey(0)