#!/usr/bin/env python3

import os, time

from aiy.board import Board, Led

from pygame import mixer
from gtts import gTTS

playing = False
filepath = ''

def saying(text):
    gtts_say(text)     # gTTS Speech

def play_text(freq):
    global playing

    if (playing):
        old_pos = mixer.music.get_pos()
        mixer.quit()

    mixer.init(frequency=freq)
    mixer.music.load('temp.mp3')
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(1)
    mixer.quit()

    if (playing):
        mixer.init()
        mixer.music.load(filepath)
        mixer.music.play(-1, (old_pos / 1000))

def gtts_say(text):
    gtts = gTTS(text=text, lang='ko')
    gtts.save('temp.mp3')

    play_text(24000)