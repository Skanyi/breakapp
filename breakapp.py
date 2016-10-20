# create an app that opens my vlc player and play music
# Allow users to pick the music from their computer
#store in the database
# Next open ask user if to use the previous or select new
# if select previous play the music in the database randomly at each break
import webbrowser
import time
from flask import Flask, render_template
import subprocess
import os
import psycopg2
import songs_model as songs


app = Flask(__name__)
app.debug = True

breaks = 5
break_counts = 0



while break_counts < breaks:
    time.sleep(7200)
    #webbrowser.open('vlc')
    p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","\\F:\\ngoma\\" + 'Bongo Mix Final' + '.mp3'])
    #p = subprocess.Popen(["C:/Program Files (x86)/VideoLAN/VLC/vlc.exe","file:\\\Users\Dhruv\Desktop\Motivation\RiseShine.mp4"])
    break_counts += 1

if __name__ == '__main__':
    app.run()
