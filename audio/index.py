#!/usr/bin/python
"""
TODO:
    $ pip3 install soudfile
    $ pip3 install sounddevice
    $ python3.6 rec.py
"""
import argparse
import tempfile
try:
    import Queue
except:
    import queue
import sys, os

MICROPHONE = 0
# MICROPHONE = 'Blue Snowball'
AUDIO_CAPTURES = 'data/'
FILE_EXTENSION = ".wav"
TEST_NAME = "_test_audio"


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

def recordAudio(a_name=TEST_NAME):
    '''
    video control
    make sure the android video camera is already pointed to subject
    '''

    import sounddevice as sd
    import soundfile as sf

    try:


        if a_name == TEST_NAME:
            print("\naudio test\n")
            newFile = a_name + FILE_EXTENSION
        else:
            print("\ninit audio capture\n")
            newFile = AUDIO_CAPTURES + a_name + FILE_EXTENSION



        # Checks and deletes the output file
        # You cant have a existing file or it will through an error
        if os.path.isfile(newFile):
            os.remove(newFile)
        if args.list_devices:
            print(sd.query_devices())
            parser.exit(0)
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])
        if args.filename != None:
            args.filename = tempfile.mktemp(prefix='test_', suffix='.wav', dir='')
        else:
            args.filename = newFile

        q = queue.Queue()

        def callback(indata, frames, time, status):
            """This is called (from a separate thread) for each audio block."""
            # if status:
            #     print(status, file=sys.stderr)
            q.put(indata.copy())

        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                          channels=args.channels, subtype=args.subtype) as file:
            try:
                with sd.InputStream(samplerate=args.samplerate, device='Blue Snowball',
                                channels=args.channels, callback=callback):
                    print('#' * 80)
                    print('press Ctrl+C to stop the recording')
                    print('#' * 80)
                    while True:
                        file.write(q.get())
            except:
                with sd.InputStream(samplerate=args.samplerate, device=0,
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
record audio

test:

    $ cd ../../ && python ./audio/rec.py <file_name>
'''
if __name__ == "__main__":
    recordAudio()
