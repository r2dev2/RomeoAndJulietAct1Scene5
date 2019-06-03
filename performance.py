import vlc

effect_objects = []
song_names = ["knuckles.mp3", "Cantina.mp3", "Huliet.mp3", "Snap.mp3"]

for i, song in enumerate(song_names):
    effect_objects.append(vlc.MediaPlayer(song))
    print(i, song[:-4])

success = False
while not success:
    effect = effect_objects[int(input("effect number ")) - 1]
    effect.audio_set_volume(100)
    effect.play()
    stop = input("close effect(press enter) ")
    effect.pause()
    if stop == "quit":
        success = True
