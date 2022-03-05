# automerge-video-audio

Automatically merges a set of music files and video files into an unique mp4 video with faded transitions.

## Dependencies
* MoviePy - https://zulko.github.io/moviepy/ - python module used for video editing operations.
* EyeD3: https://eyed3.readthedocs.io/ - to read metadata from .mp3 files.

## Functionality

**Input:** takes all .mp4 video files from Videos Folder and .mp3 files from Music folder as input. 

**MoviePy** library used in main.py to concatenate clips and use  fade effects on video and audio transitions.

**Output:** .mp4 video file in Outputs folder.

**Execution** for quick deployment and executino I created a batfile that:
 * deletes old .mp3 temp files from interrupted executions;
 * checks if there are any audio and video files in the corresponding folders;
 * runs main.py after checking for input to create final video.

## Examples:

Here are a couple of videos created using Public Domein or permissive source material.

https://www.youtube.com/watch?v=yEbXGs8g9PI

[![Alt text](https://img.youtube.com/vi/yEbXGs8g9PI/0.jpg)](https://www.youtube.com/watch?v=yEbXGs8g9PI)

https://www.youtube.com/watch?v=OZPk7gKwtak

[![Alt text](https://img.youtube.com/vi/OZPk7gKwtak/0.jpg)](https://www.youtube.com/watch?v=OZPk7gKwtak)
