import audio.rec as audio
import visual.rec as video

import _thread

# Create two threads as follows
try:
   _thread.start_new_thread( video.recordVideo, ("videoooo", ) )
   _thread.start_new_thread( audio.recordAudio, () )
except:
   print ("Error: unable to start thread")

while 1:
   pass
