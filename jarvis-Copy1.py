#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install pyttsx3')


# In[13]:


get_ipython().system('pip install SpeechRecognition')


# In[14]:


get_ipython().system('pip install wikipedia')


# In[16]:


get_ipython().system('pip install openai')


# In[18]:


get_ipython().system('pip install pyaudio')


# In[ ]:





# In[55]:


import pyttsx3
import speech_recognition as sr
import datetime
import os 
engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices', voices[1].id)

#text to speak
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
#voice to text    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
        
    try:
        print("Recognition....")
        query = r.recognize_google(audio,language="en-in")
        print(f"user said: {query}")
        
    except Exception as e:
        speak("i didnt get you,can you repeat again....")
        return "none"
    return query

#to wish
def wish():
    hour= int(datetime.datetime.now().hour)
        
        
    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("how can i help you sir")
    
    
if __name__=="__main__":
    #speak("hello bro ")
    wish()
   # takecommand()
   # while True:
    if 1:
        query=takecommand().lower()
        
        #logic buliding for task
        
        if "open notepad" in query:
            notepad_path = "C:\\Windows\\notepad.exe"
            os.startfile(notepad_path)
        elif "open chrome" in query:
            chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome_path)



# In[ ]:





# In[ ]:




