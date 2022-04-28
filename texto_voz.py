from gtts import gTTS
from playsound import playsound
import os

while True:
  frase = str(input('O que deseja falar? (Digite sair para fechar aplicação): '))
  if frase == 'sair':
    break
  else:
    frase_gTTS = gTTS(frase,  lang="pt-br", slow=False)
    frase_gTTS.save('sample.mp3')
    print("Falando...")
    playsound('sample.mp3')
    os.remove('sample.mp3')