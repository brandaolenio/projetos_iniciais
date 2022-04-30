from gtts import gTTS
from pygame import mixer
from time import sleep
import os

while True:
    frase = input('O que deseja falar? (Digite sair para fechar aplicação): ')
    if frase == "sair":
        print('Até mais! Ótimo dia!')
        break
    else:
        audio = gTTS(frase,  lang="pt-br", slow=False)
        audio.save('audio.mp3')
        mixer.init() 
        mixer.music.load("audio.mp3") 
        print('Falando...')
        mixer.music.play()
        sleep(1)
        mixer.music.unload()
        os.remove("audio.mp3")