# -*- coding':' utf-8 -*-#
import json
import os
import re
import requests
import time
from gtts import gTTS
from playsound import playsound

if __name__ == '__main__':

    text = 'Overview of iTracker, our eye tracking CNN. Inputs include left eye, right eye, and face images detected and cropped from the original frame (all of size 224×224). '
    tts = gTTS(text)
    tts.save('hello.mp3')

    playsound('hello.mp3')