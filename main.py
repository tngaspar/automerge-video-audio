# %%
from moviepy.editor import * 
from datetime import datetime
now = datetime.now()

videoSpeed = 1
# %%

audio_folder='music'

audio_files = [audio_folder+'/'+img for img in os.listdir(audio_folder) if img.endswith(".mp3")]

#print(audio_files)

audios = []
audioNum = 1
currentDuration = 0
for audio in audio_files :
    if audioNum ==1:
        audios.append([AudioFileClip(audio), 0])
    else:
        audios.append([AudioFileClip(audio), currentDuration])
    currentDuration = currentDuration + audios[-1][0].duration-5
    audioNum = audioNum + 1

#print(audios)

# %%
audioClips = CompositeAudioClip([audio[0].set_start(audio[1]).audio_fadein(1).audio_fadeout(1) for audio in audios])
audioClips.duration

# %%
#concatenate_audioclips(audioClips)
#audioClips.write_audiofile('main.mp3')

# %%
video_folder='video'
video_files = [video_folder+'/'+img for img in os.listdir(video_folder) if img.endswith(".mp4")]
#print(video_files)

#gets [video, duration of last video]
videos = []
videoNum = 1
currentDuration = 0
for video in video_files :
   if videoNum == 1:
      videos.append([VideoFileClip(video).speedx(factor=videoSpeed), 0])
      
   else:
      videos.append([VideoFileClip(video).speedx(factor=videoSpeed), currentDuration])
   currentDuration = currentDuration + videos[-1][0].duration
   videoNum = videoNum + 1
#print(videos)


# %%
#videoclips = CompositeVideoClip([video[0].set_start(video[1]).crossfadein(2).crossfadeout(2) for video in videos])
videoclips = concatenate_videoclips([video[0].fadein(1).fadeout(1) for video in videos], method = 'compose')


# %%
videoclips.audio = audioClips

looped=videoclips.loop(duration=audioClips.duration)
looped = looped.fadeout(1)
print('Audio length: ',audioClips.duration/60)
print('Video length: ', looped.duration/60)
looped.write_videofile('output/final_'+ now.strftime("%H.%M.%S_%d.%m.%Y"+ ".mp4") , fps=24, threads = 4)



