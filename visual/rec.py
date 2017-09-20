

import numpy as np
import cv2
import os, sys

def captureStreamOnly():
    '''
    opens webcam and begins streaming
    '''

    cap = cv2.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here

        some = cv2.resize(frame, (480, 270))                    # Resize image

        gray = cv2.cvtColor(some, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def recordVideo(id):
    '''
    opens webcam, begins streaming and saves to file id
    '''

    FILE_OUTPUT = "captures/" + id + '.mp4'

    # Checks and deletes the output file
    # You cant have a existing file or it will through an error
    if os.path.isfile(FILE_OUTPUT):
        os.remove(FILE_OUTPUT)


    cap = cv2.VideoCapture(0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(FILE_OUTPUT,fourcc, 20.0, (1280, 720)) # frame must equal the camera dimensions

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

$ python record.py [stream | <capture_id>]
'''
if __name__ == "__main__":
    recordVideo(sys.argv[1])
