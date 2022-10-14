#import text speech library
import pyttsx3
engine=pyttsx3.init()
phr=[]

#open , read text file and add it to a list
with open("read.txt") as file:                              
    for lines in file:
        phr.append(lines.rstrip())

        #speech a text file
        for speech in file:
            print(speech , end="")
            this=speech
            
            #control a voice speed
            engine.setProperty("rate",150)
            voices=engine.getProperty("voices")
            
            #change voice
            engine.setProperty('voice',voices[1].id)
            engine.say(this)
            
            engine.runAndWait()

file.close()



