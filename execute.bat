@echo off
title Run main.py
set run=true

if exist *TEMP_MPY_wvf_snd.mp3 del /F *TEMP_MPY_wvf_snd.mp3

if exist "music\*.mp3" (
    echo Audio found
) else (
    echo No audiofile (.mp3^) found in \music directory
    set run=false
)

if exist "video\*.mp4" (
    echo Video found

) else (
    echo No videofile (.mp4^) found in \music directory
    set run=false
)

if %run%==true (
    python main.py
) 

if exist *TEMP_MPY_wvf_snd.mp3 del /F *TEMP_MPY_wvf_snd.mp3

pause