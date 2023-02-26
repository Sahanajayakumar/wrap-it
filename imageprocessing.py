# First convert the video into frames
#Second convert the frames into grayscale and store in db if it dpesnt exist
#Finally matching the frames wrt brightest point value

import cv2
import os
import shutil
import numpy as np
import base64

def convert_frames(url:str):
    capture = cv2.VideoCapture(url)
    frameNr = 0
    frames_url = []
    while (True):
    
        success, frame = capture.read()
    
        if success:
            file_to_write = f'D:/code/S1r/frames/frame_{frameNr}_S1EP4.jpg'
            cv2.imwrite(file_to_write, frame)
            frames_url.append(file_to_write)

        else:
            break
    
        frameNr = frameNr+1
        #print("Frame rate:", capture.get(cv2.CAP_PROP_FPS))
        
    capture.release()
    return frames_url

def convert_grayscale_match(frames:list[str]):
    destination_dir = 'D:/code/S1r/brightest_points'

    # Iterate over the images in the folder
    matched_images = []
    for frame in frames:
        # Read the image
        image = cv2.imread(os.path.join(frame,''))
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Find the minimum and maximum values in the image
        (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(gray_image, mask=None)

        # The brightest point will be the maximum value
        brightest_point = max_loc
        lowest_point = min_loc
        print(brightest_point)
        
         # find brightest point in image
        brightest_point_image = np.unravel_index(np.argmax(gray_image), gray_image.shape)
        
        # check if brightest points match
        if brightest_point == brightest_point_image:
            # save matching frame to output directory
            #Note: try to highlight matched point if time permits

            retval, buffer = cv2.imencode('.jpg', frame)
            jpg_as_text = base64.b64encode(buffer)
            matched_images.append(jpg_as_text)

    return matched_images
    #      Draw a circle at the brightest point
    #     cv2.circle(gray_image, brightest_point, radius=5, color=(0, 0, 0), thickness=10)
    #     cv2.circle(gray_image, lowest_point, radius=5, color=(255, 255, 255), thickness=10)
    #    image_extensions = ['.jpg', '.png', '.gif']  # list of allowed image file extensions
    #     cv2.imwrite(os.path.join(destination_dir, filename), gray_image)
frames = convert_frames('D:\code\S1r\s1ep4r.mp4')
images = convert_grayscale_match(frames)
print(images)
