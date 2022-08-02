# Automerge Video & Audio

Automatically merges a set of music files and video files into an unique .mp4 video with faded transitions.

<strong>Overrides video files' audio</strong> with audio from audio files. Useful for creating music videos (examples at the [end](#examples) of this document).

### Merging video files
This script is not intended to be used as a video merge tool (audio will always be overwritten). For this purpose, you may use this [script](https://gist.github.com/tngaspar/9ba8f14a42f3e40f885aff13630ca5fe) instead.

## Requirements
* [MoviePy](https://zulko.github.io/moviepy/) - python module used for programmatic video editing.

## Installation

1. Clone the repository:
```bash
$ git clone https://github.com/tngaspar/automerge-video-audio.git
```
2. Install dependencies:


```bash
$ pip install -r requirements.txt
```
(Optional) - install dependencies in a [virtual environment](https://docs.python.org/3/library/venv.html).

## Execution
1. (Optional) Edit setup variables in the beginning of `main.py` according to your preferences. Alternatively, you can leave it as is and use the default settings.

```python
# ### SETTINGS - Modify this to your preferences ###
video_speed = 1  # Speed for all videos. Leave as 1 for normal speed
video_fade_secs = 1  # Video fade in and out duration in seconds.
audio_fade_secs = 1  # Audio fade in and out duration in seconds.
audio_overlap_secs = 0  # Number of seconds between audio clips where both clips overlap. Leave as 0 for no overlap.
```

2. Drop your `.mp3` audio files into the `audio/` directory and your `.mp4` video files into the `video/` directory.

```bash
video/
├── ...
├── sample-video1.mp4
├── sample-video2.mp4
└── sample-video3.mp4
audio/
├── ...
├── sample-audio1.mp3
└── sample-audio2.mp3
```

3. Run the `main.py` script:
```bash
$ python main.py
```
and wait for the execution to complete. 

You are able to see how long the execution will take to complete on the right side of the of the progress bar.
```bash
This 2 lengths should match:
Audio length: 16.04 seconds
Video length: 16.04 seconds
Moviepy - Building video output/final_21.11.18_01.08.2022.mp4.
MoviePy - Writing audio in final_21.11.18_01.08.2022TEMP_MPY_wvf_snd.mp3
MoviePy - Done.                                                                             
Moviepy - Writing video output/final_21.11.18_01.08.2022.mp4

t:  70%|████████████████████████████            | 338/482 [00:36<00:08, 16.11it/s, now=None]
```

4. After the execution is finished, you should find the final output .mp4 file on the `output/` directory.

## Examples:

https://www.youtube.com/watch?v=yEbXGs8g9PI

[![Alt text](https://img.youtube.com/vi/yEbXGs8g9PI/0.jpg)](https://www.youtube.com/watch?v=yEbXGs8g9PI)

https://www.youtube.com/watch?v=OZPk7gKwtak

[![Alt text](https://img.youtube.com/vi/OZPk7gKwtak/0.jpg)](https://www.youtube.com/watch?v=OZPk7gKwtak)

<p align="right">(<a href="#top">back to top</a>)</p>
