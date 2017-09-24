#!/usr/bin/python

import multiprocessing
import time
import audio.index as audio
import visual.index as video

stamp = time.strftime('%Y%m%d%H%M%S')

processAudio = multiprocessing.Process(target=audio.recordAudio, args=(stamp,))
processVideo = multiprocessing.Process(target=video.recordVideo, args=(stamp,))
processAudio.start()
processVideo.start()
