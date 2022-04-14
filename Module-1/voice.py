from playsound import playsound
from gtts import gTTS 
import os 
import time
def voice(myText):

    # Language we want to use 
    language = 'en'

    output = gTTS(text=myText, lang=language, slow=False)
    t=time.time()
    nm="output"+str(t)+".mp3"
    output.save(nm)
    playsound(nm)

