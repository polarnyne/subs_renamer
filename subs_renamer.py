import os
import glob

video_extension = ['.mkv', '.mp4', '.avi']
subs_extension = ['.srt', '.ass']

video_files = []
subs_files = []

for extension in video_extension: 
    video_files.extend(glob.glob('*' + extension))

video_files = [ext[:-4] for ext in video_files]

for extension in subs_extension:
    subs_files.extend(glob.glob('*' + extension))

counter = 0

for srt in subs_files:
    episode = video_files[counter]
    print(f'renaming {episode}')
    os.rename(srt, str(episode)+".srt" )
    counter += 1