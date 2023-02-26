import cv2
import os
import shutil
import numpy as np
import base64

def convert_frames(url:str, rpath:str):
    capture = cv2.VideoCapture(url)
    frameNr = 0
    frames_url = []
    while (True):
    
        success, frame = capture.read()
        if success:
            
            file_to_write = rpath + '/frame_'+str(frameNr)+'_S1ep4.jpg'
            cv2.imwrite(file_to_write, frame)
            frames_url.append(file_to_write)

        else:
            break
    
        frameNr = frameNr+1
        #print("Frame rate:", capture.get(cv2.CAP_PROP_FPS))
        
    capture.release()
    return frames_url




def convert_grayscale_match(frames:list[str]):

    # Iterate over the images in the folder
    bright_points=[]
    count=0
    for frame in frames:
        # Read the image
        image = cv2.imread(frame)
        #print(image)
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Find the minimum and maximum values in the image
        (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(gray_image, mask=None)

        # The brightest point will be the maximum value
        brightest_point = max_loc
        lowest_point = min_loc
        bright_points.append(brightest_point)
        count=count+1
    print("!!!!!!!!!!!!! the count of refernce frames", count)
    return bright_points
refv1='D:/code/S1r/s1ep4r.mp4'
rpath='D:/code/S1r/frames'
frames = convert_frames(refv1, rpath)
images = convert_grayscale_match(frames)
#print(images)

#Note: the brightest points from the refernce video should be stored in the database

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


def convert_grayscale_query(frames:list[str], ref_brightest_points: list[tuple], output_dir: str):
    matched_images = []
    for frame in frames:
        # Read the image
        image = cv2.imread(frame)
        # Convert the image to grayscale
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Find the minimum and maximum values in the image
        (min_val, max_val, min_loc, max_loc) = cv2.minMaxLoc(gray_image, mask=None)

        # The brightest point will be the maximum value
        brightest_point = max_loc
        
        # Check if brightest point matches any of the reference image's brightest points
        for ref_brightest_point in ref_brightest_points:
            if brightest_point == ref_brightest_point:
                # Save matching frame to output directory
                # Note: try to highlight matched point if time permits
                output_file = os.path.join(output_dir, os.path.basename(frame))
                cv2.imwrite(output_file, image)
                
                # Add the matched image to the list of matched images
                retval, buffer = cv2.imencode('.jpg', image)
                jpg_as_text = base64.b64encode(buffer)
                matched_images.append(brightest_point)
                break

    return matched_images

qvd1='D:/code/S1q/s1ep4query.mp4'
qpath='D:/code/S1q/frames'
opath='D:/code/S1m'
framesq = convert_frames(qvd1, qpath)
imageq = convert_grayscale_query(framesq,images, opath)
print("the matched images are",imageq)