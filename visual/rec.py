# ##########################################
# ##########################################
# # # capture video
# # ##########################################
import numpy as np
import cv2
# #
# # cap = cv2.VideoCapture(0)
# #
# # while(True):
# #     # Capture frame-by-frame
# #     ret, frame = cap.read()
# #
# #     # Our operations on the frame come here
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# #
# #     # Display the resulting frame
# #     cv2.imshow('frame',gray)
# #     if cv2.waitKey(1) & 0xFF == ord('q'):
# #         break
# #
# # # When everything done, release the capture
# # cap.release()
# # cv2.destroyAllWindows()
#
# ##########################################
# ##########################################
# # saving a video
# ##########################################
import numpy as np
import cv2

import os

FILE_OUTPUT = 'output.mp4'

# Checks and deletes the output file
# You cant have a existing file or it will through an error
if os.path.isfile(FILE_OUTPUT):
    os.remove(FILE_OUTPUT)


cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(FILE_OUTPUT,-1, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
#
# cap = cv2.VideoCapture('justpractice 001.mp4')
#
# while(cap.isOpened()):
#     ret, frame = cap.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(25):
#         break
#
# cap.release()
# cv2.destroyAllWindows()
