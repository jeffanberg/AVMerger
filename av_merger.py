import sys
import pathlib
import moviepy.editor as mpy

#Initialize fade in and out lengths in seconds. Adjust these to preference.
fadein_dur = 2
fadeout_dur = 2

# grab and initialize the argument directories
first_arg = sys.argv[1]
second_arg = sys.argv[2]
third_arg = sys.argv[3]

music_dir = pathlib.Path(first_arg)
photo_dir = pathlib.Path(second_arg)
save_dir = pathlib.Path(third_arg)

# check if save / exists, if not create; throw errors if photo or song dirs don't exist
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


def avMerge(song, photo):
    video = mpy.ImageClip(f"{photo}")
    audio = mpy.AudioFileClip(f"{song}")
    video = (video.set_audio(audio)
            .set_duration(audio.duration)
            .fadein(fadein_dur)
            .fadeout(fadeout_dur))
    video.write_videofile(str(pathlib.PurePath(str(save_dir), str(song.stem))) + ".mp4", fps=24)


# set up generator for the photos
gen = photo_list()

# loop through music folder
for music_file in music_dir.iterdir():
    print(music_file)
    mFilePath = pathlib.Path(music_file)
    if mFilePath.suffix == '.mp3':
        avMerge(music_file, next(gen))

