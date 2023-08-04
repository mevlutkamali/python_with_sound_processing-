
import os
from gtts import gTTS

file = open('python_attempt.txt' , 'r').read()

speech = gTTS( text=file , lang='en' , slow=False)

# Türkçe dil komutu için """ lang='tr' """ komutu girilmelidir .

speech.save("speech.mp3")
os.system("speech.mp3")

print(" Finish ... ")