from gtts import gTTS
import os

file = open("info.txt","r").read().replace("\n"," ")

language = 'es-us'

speech = gTTS(text = str(file), lang=language, slow = False)

speech.save("texto-info.mp3")

os.system("start Resultado_Audio.mp3")