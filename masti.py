import pyttsx3 as pt
import random
import json
from pygame import mixer
import matplotlib as plt
import speech_recognition as sr

engine=pt.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

engine.setProperty("volume",1000)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


str2="Welcome people , I am EmiNEM 2, today i am gonna defeat the Rap God. do YOU THINK I AM SLOW. lETS see.  "

str1='''Rakim Lakim Shabazz 2Pac WA Cube hey Doc Ren Yella Eazy thank you they got Slim Inspired enough to one day grow up blow up and be in a positionTo meet Run DMC and induct them into the motherfuckin Rock nRoll Hall of FameEven though I walk in the church and burst in a ball of flames Only Hall of Fame I be inducted in is the alcohol of fameOn the wall of shameYou fags think its all a game til I walk a flock of flames Off of planking tell me what in the fuck are you thinking Little gay looking boyso gay I can barely say it with a straight face looking boy You witnessing a mass occur Like you watching a church gathering take place looking boy Oy vey that boys gay thats all they say looking boy You get a thumbs up pat on the back And a way to go from your label everyday looking boy Hey looking boy what you say looking boy I got a hell yeah from Dre looking boy Imma work for everything I have Never ask nobody for shit get outta my face looking boy Basically boy your never gonna be capable To keep up with the same pace looking boy'''
#count=0
engine.setProperty("rate",120)
speak(str2)
engine.setProperty("rate",10000)
speak(str1)

#while True:
#
#    speak(word)
#    count+=1
#    if count==100:
#        break
#    else:
#        continue