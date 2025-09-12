import psutil
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit as kit
from gtts import gTTS
import os
import pygame



voice=sr.Recognizer()
isWaked=False

from gtts import gTTS
import pygame
import tempfile
import os

def googlespeak(text, lang="en"):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            filename = fp.name

        tts = gTTS(text=text, lang=lang, slow=False)
        tts.save(filename)

        if not pygame.mixer.get_init():
            pygame.mixer.init()
            
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        os.remove(filename)

    except Exception as e:
        print("Error in gTTS:", e)

        
        
def speak(text):
     engine=pyttsx3.init()
     engine.setProperty("rate", 130)
     engine.setProperty("volume", 1.0)
     engine.say(text)
     engine.runAndWait()
     engine.stop()
     
def close_app(app_name):

    app_name = app_name.lower()
    closed = False
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and proc.info['name'].lower() == app_name:
                proc.terminate()  # gentle termination
                closed = True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
        

def handleInstructions(instruction:str):
    if('kya hal ha' in instruction.lower()):
        googlespeak('Main tek ap sunao')
        
    if ("shutdown" in instruction.lower() or "close laptop" in instruction.lower() or
        "poweroff" in instruction.lower()):
        googlespeak("Are you sure you want to shut down?")
        
        with sr.Microphone() as source:
            try:
                print('Listening...')
                audio = voice.listen(source, timeout=5, phrase_time_limit=3)
                confirm:str = voice.recognize_google(audio)
    
                if 'yes' in confirm.lower():
                    googlespeak("Shutting down")
                    os.system("shutdown /s /t 1")
                else:
                    googlespeak("Okay, I will not shut down")

            except sr.UnknownValueError:
                googlespeak("I could not understand, canceling shutdown")
            except sr.WaitTimeoutError:
                googlespeak("You didn’t respond, canceling shutdown")
       
    if "play" in instruction:
                song = instruction.lower().replace("play", "").replace('nobita',"")
                googlespeak(f"Playing {song} on YouTube")
                kit.playonyt(song)

    elif "search" in instruction:
                query = instruction.lower().replace("search", "").replace('nobita',"")
                googlespeak(f"Searching {query} on Google")
                kit.search(query) 
                
    if('whatsapp' in instruction.lower()):
          os.system("start shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App")
                
    if ('open google' in instruction.lower() or 'open the google' in instruction.lower()):
        googlespeak('Opening the google')
        os.startfile(r'C:\Program Files\Google\Chrome\Application\chrome.exe')
    elif 'youtube' in instruction.lower():
        googlespeak('Opening the youtube')
        webbrowser.open(f"https://www.youtube.com/")
    elif 'facebook' in instruction.lower():
        googlespeak('Opening the facebook')
        webbrowser.open(f"https://www.facebook.com/")
    elif 'linkedin' in instruction.lower():
        googlespeak('Opening the linkedin')
        webbrowser.open(f"https://www.linkedin.com/")
    elif 'chatgpt' in instruction.lower():
        googlespeak('Opening the chatgpt')
        webbrowser.open(f"https://www.chatgpt.com/")
    elif 'postman' in instruction.lower():
        os.startfile(r'C:\Users\MR\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Postman\Postman.lnk')
        
    if('close google' in instruction.lower() or 'close the google' in instruction.lower()):
        close_app('chrome.exe')
        
   
    if 'create a folder' in instruction.lower():
        try:
            # Extract folder name from instruction, default if none
            folder_name = "NewFolder"
            if "named" in instruction.lower():
                folder_name = instruction.lower().split("named")[-1].strip()

            # Create folder in current working directory (where you currently are)
            current_path = os.getcwd()
            print(current_path)
            os.makedirs(os.path.join(current_path, folder_name), exist_ok=True)
            googlespeak(f"Folder '{folder_name}' created at: {current_path}")

        except Exception as e:
            print("Error creating folder:", e)

        
while True:
    with sr.Microphone() as source:
        print('Sleeping...')       
        try:
            audio=voice.listen(source,timeout=3,phrase_time_limit=3)
            usersay:str=voice.recognize_google(audio)
            
            if('nobita' in usersay.lower().strip()):
                 print('Waking...')
                 googlespeak('Gee Abdul Rehman')
                 print('Waked')
                 isWaked=True
                 while isWaked:
                    print('Listening...')
                    
                    try:
                        audio=voice.listen(source,timeout=3,phrase_time_limit=3)
                        usersay:str=voice.recognize_google(audio)
                        
                        if('hey nobita'==usersay.lower() or 'nobita'==usersay.lower() or 'hi nobita'==usersay.lower()):
                            googlespeak('Gee Abdul Rehman')
                        
                        if('nobita so jao' in usersay.lower() or 'so jao' in usersay.lower() or 'nobita good bye' in usersay.lower() or
                            'good bye' in usersay.lower()):
                            googlespeak('Ok good bye')
                            isWaked=False
                            break
                                                
                        handleInstructions(usersay)
                    except sr.WaitTimeoutError:
                        print("You didn’t say anything, try again...")

                    except sr.UnknownValueError:
                        print("Could not understand audio")

                    except sr.RequestError as e:
                        print("Could not request results; {0}".format(e))
                            
        except sr.WaitTimeoutError:
            print("You didn’t say anything, try again...")

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))