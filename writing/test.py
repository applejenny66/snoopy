import pyttsx
#import pyttsx3
"""
engine = pyttsx.init()
engine.say('hello world')
engine.say('start')
engine.runAndWait()
engine.say('start')
engine.endLoop()

engine.say('1')
engine.runAndWait()
engine.endLoop()
"""


def Txt2Voice(text):
    
    engine = pyttsx.init()
    engine.say(text)
    engine.runAndWait()

text='start'
Txt2Voice(text)
text2 = '1'
Txt2Voice(text2)
