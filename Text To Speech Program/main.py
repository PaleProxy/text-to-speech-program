import os
from gtts import gTTS

#Set file name and open file
filename = 'input.txt'
file = open(filename, 'r')

#Create empty string to store text
text = ''

#iterate through the lines of file and add them to text string
for line in file:
    text += line

file.close()

#convert text to speech
tts = gTTS(text)

#save speech to file and play
tts.save('speech1.mp3')
os.system('speech1.mp3')
