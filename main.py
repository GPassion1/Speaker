from gtts import gTTS
from pygame import mixer
import time

mytext = input("Digite seu texto: ")

obj = gTTS(text=mytext, lang="pt", tld="com.br")

obj.save("Fala.mp3")
mixer.init()
mixer.music.load("Fala.mp3")
mixer.music.play()
while mixer.music.get_busy():
    time.sleep(1)

