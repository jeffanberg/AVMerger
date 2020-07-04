import sys
import pathlib
from PIL import Image
from moviepy.editor import *

# grab the arguments
first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]


# check if new/ exists, if not create
music_dir = pathlib.Path(first_arg)
photo_dir = pathlib.Path(second_arg)
save_dir = pathlib.Path(third_arg)

if save_dir.exists() is False:
    save_dir.mkdir()

if photo_dir.exists() is False:
    raise RuntimeError (f'Error: Photo directory does not exist. Try again.')

if music_dir.exists() is False:
    raise RuntimeError (f'Error: Music directory does not exist. Try again.')

#load up the array of photos to merge
def photo_list():
    for photo_file in photo_dir.iterdir():
        pFile = pathlib.Path(photo_file)
        if pFile.suffixes == '.jpg' or '.png' or '.gif':
            yield pFile

def avMerge(music_file, photo_file):
    video = ImageClip(photo_file)
    audio = AudioClip(music_file)
    video.set_audio(audio)


# loop through music folder
for music_file in music_dir.iterdir():
    mFile = pathlib.Path(music_file)
    if mFile.suffix == '.mp3':
        try:
            avMerge(mFile, photo_list())
        except:
            print('Something went wrong.')

# use a yield to loop through photo folder?

