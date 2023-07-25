from pygame import mixer
mixer.init()
mixer.music.load("song.mp3")
mixer.music.set_volume (0.8)
mixer.music.play()
while True:
    print("Playing On & On")
    print("Press 'p'or 'P' to pause the music")
    print("Press 'r' or 'R' to Resume the music")
    print("Press 's' or 'S' to stop the music")
    value = input(" ")
    if value == 'p' or value == 'P':
        mixer.music.pause()
    elif value == 'r' or value == 'R':
        mixer.music.unpause()
    elif value == 's' or value == 'S':
        mixer.music.stop()
        break
    else:
        print("Invalid input. Try pressing ‘p’ for pause ‘r’ to resume, ‘s’ to stop instead")
