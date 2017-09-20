#!/usr/bin/env python3
"""Create a recording with arbitrary duration.

PySoundFile (https://github.com/bastibe/PySoundFile/) has to be installed!

"""
import argparse
import tempfile
import queue
import sys

MICROPHONE = 0
# MICROPHONE = 'Blue Snowball'
AUDIO_CAPTURES = 'audio/captures'


def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args()

def recordAudio():
    try:
        import sounddevice as sd
        import soundfile as sf


        '''
        video control
        make sure the android video camera is already pointed to subject
        '''
        import subprocess


        # print(subprocess.call('adb devices', shell=True))
        # # print(subprocess.call('adb shell "am start -a android.media.action.VIDEO_CAPTURE"', shell=True)) # start the video camera
        # print(subprocess.call('adb shell input keyevent 66', shell=True))

        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])
        if args.filename is None:
            args.filename = tempfile.mktemp(prefix='audio_',
                                            suffix='.wav', dir=AUDIO_CAPTURES)
        q = queue.Queue()

        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            if status:
                print(status, file=sys.stderr)
            q.put(indata.copy())

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                          channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=MICROPHONE,
                                channels=args.channels, callback=callback):
                print('#' * 80)
                print('press Ctrl+C to stop the recording')
                print('#' * 80)
                while True:
                    file.write(q.get())

    except KeyboardInterrupt:

        print('\nRecording finished: ' + repr(args.filename))
        parser.exit(0)

    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))


'''
record AUDIO

$ python record.py [stream | <capture_id>]
'''
if __name__ == "__recordAudio__":
    recordAudio()
