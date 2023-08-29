# Imports go at the top
from microbit import *
import music
import songs

set_volume(95)
soul = Image('00000:'
             '09090:'
             '09990:'
             '00900:'
             '00000')

def flash ():
    music.play(['f6:1'])
    display.clear()
    music.play(['r:1'])
    display.show(soul)

def start_anim():
    music.set_tempo(bpm=240)
    sleep(2000) 
    display.show(soul)
    flash ()
    flash ()
    flash ()
    music.play(['d#6:1','g6:1','d6:1','f#6:1','c#6:1','f6:1'])
    sleep(2000)

def death_anim():
    sleep(2000)
    display.show(Image('00000:'
                       '90009:'
                       '99099:'
                       '09090:'
                       '00000'))
    music.play(['a#4:4','r:4'])
    display.show(Image('00000:'
                       '00000:'
                       '90009:'
                       '00000:'
                       '09090'))
    music.play(['a#4:2','g#4:2','a#4:2','g#4:2'])
    display.clear()
    sleep(2000)



start_anim()

music.set_tempo(bpm=120)
music.play(songs.megalovania)

death_anim()

music.set_tempo(bpm=115)
music.play(songs.determination)