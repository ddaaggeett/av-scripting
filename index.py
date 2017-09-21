# python3.6

import multiprocessing
import audio.rec as audio
import visual.rec as video

processAudio = multiprocessing.Process(target=audio.recordAudio)
processVideo = multiprocessing.Process(target=video.recordVideo, args=('newVid',))
processAudio.start()
processVideo.start()
