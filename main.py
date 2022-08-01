import os
import glob
from moviepy.editor import (
    AudioFileClip,
    CompositeAudioClip,
    VideoFileClip,
    concatenate_videoclips,
)
from datetime import datetime

now = datetime.now()

# ### SETTINGS - Modify this to your preferences ###
video_speed = 1  # Speed for all videos. Leave as 1 for normal speed
video_fade_secs = 1  # Video fade in and out duration in seconds.
audio_fade_secs = 1  # Audio fade in and out duration in seconds.
audio_overlap_secs = 0  # Number of seconds between audio clips where both clips overlap. Leave as 0 for no overlap.

# ### CLEANUP ###
# removes temporary files from previous interupted executions
file_list = glob.glob("./final_*TEMP_MPY_wvf_snd.mp3", recursive=False)
for file in file_list:
    try:
        os.remove(file)
    except OSError:
        print("Error while deleting file")

# ### MAIN ###
# get list of audio files
audio_dir = "audio"
audio_files = [
    audio_dir + "/" + file
    for file in os.listdir(audio_dir)
    if file.endswith(".mp3")
]
if len(audio_files) == 0:
    raise Exception(f"No audio files were found in the {audio_dir} directory.")

# get list of video files
video_dir = "video"
video_files = [
    video_dir + "/" + file
    for file in os.listdir(video_dir)
    if file.endswith(".mp4")
]
if len(video_files) == 0:
    raise Exception(f"No video files were found in the {video_dir} directory.")


# Create list of audio clips
audio_list = []
audio_num = 1
currentDuration = 0
for audio in audio_files:
    if audio_num == 1:
        audio_list.append([AudioFileClip(audio), 0])
    else:
        audio_list.append([AudioFileClip(audio), currentDuration])
    currentDuration = currentDuration + audio_list[-1][0].duration - audio_overlap_secs
    audio_num = audio_num + 1

# Merge list of audio clips into one single audio clip
audioclips = CompositeAudioClip(
    [
        audio[0]
        .set_start(audio[1])
        .audio_fadein(audio_fade_secs)
        .audio_fadeout(audio_fade_secs)
        for audio in audio_list
    ]
)

# Create list of video clips
video_list = []
video_num = 1
currentDuration = 0
for video in video_files:
    if video_num == 1:
        video_list.append([VideoFileClip(video).speedx(factor=video_speed), 0])
    else:
        video_list.append(
            [VideoFileClip(video).speedx(factor=video_speed), currentDuration]
        )
    currentDuration = currentDuration + video_list[-1][0].duration
    video_num = video_num + 1

# apply fadein and fadeout effects to video clips
video_list = [
    video[0].fadein(video_fade_secs).fadeout(video_fade_secs) for video in video_list
]

# Merge list of video clips into one single clip
videoclips = concatenate_videoclips(video_list, method="compose")

# Adds audioclips audio to video clips and overriding videoclips existing audio
videoclips.audio = audioclips

# Loops video clips for the duration of the audio clips
looped = videoclips.loop(duration=audioclips.duration)
# Adds fadeout at the end of the merged video
looped = looped.fadeout(video_fade_secs)

print("This 2 lengths should match:")
print("Audio length:", audioclips.duration, "seconds")
print("Video length:", looped.duration, "seconds")

# Creates final video file
looped.write_videofile("output/final_" + now.strftime("%H.%M.%S_%d.%m.%Y" + ".mp4"))
