import sys
import pathlib
import moviepy.editor as mpy

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
        pFilePath = pathlib.Path(photo_file)
        if pFilePath.suffixes == '.jpg' or '.png' or '.gif':
            print(photo_file)
            yield photo_file

def avMerge(song, photo, num):
    video = mpy.ImageClip(f"{photo}")
    audio = mpy.AudioFileClip(f"{song}")
    video = video.set_audio(audio)
    video = video.set_duration(audio.duration)
    print("Video duration is" + str(video.duration))
    print(audio.duration)
    video.write_videofile("songfile" + str(num) + ".mp4", fps=24)


# loop through music folder
num=0

for music_file in music_dir.iterdir():
    print(music_file)
    mFilePath = pathlib.Path(music_file)
    if mFilePath.suffix == '.mp3':
        avMerge(music_file, next(photo_list()), num)
        num += 1

