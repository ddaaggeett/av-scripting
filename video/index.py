

import numpy as np
import cv2
import os, sys

VIDEO_CAPTURES = 'data/'
FILE_EXTENSION = ".mp4"
TEST_NAME = "_test_video"


def captureStreamOnly():
    '''
    opens webcam and begins streaming
    '''

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here

        some = cv2.resize(frame, (480, 270))  # Resize image

        gray = cv2.cvtColor(some, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def recordVideo(a_name=TEST_NAME):
    '''
    opens webcam, begins streaming and saves to file a_name
    '''



    if a_name == TEST_NAME:
        print("\nvideo test\n")
        newFile = a_name + FILE_EXTENSION
    else:
        print("\ninit video capture\n")
        newFile = VIDEO_CAPTURES + a_name + FILE_EXTENSION



    # Checks and deletes the output file
    # You cant have a existing file or it will through an error
    if os.path.isfile(newFile):
        os.remove(newFile)


    cap = cv2.VideoCapture(0)

    # important for out to equal the specs of the camera device
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    height = int(cap.get(4)) # 4 is height index
    width = int(cap.get(3)) # 4 is width index

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(newFile,fourcc, fps, (width, height)) # frame must equal the camera dimensions

    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:

            # write the flipped frame
            out.write(frame)

            some = cv2.resize(frame, (480, 270))                    # Resize image
            gray = cv2.cvtColor(some, cv2.COLOR_BGR2GRAY)

            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break

    # Release everything if job is finished
    cap.release()
    out.release()
    cv2.destroyAllWindows()

'''
record VIDEO
'''
if __name__ == "__main__":
    recordVideo()
