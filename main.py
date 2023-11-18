import os
import time
from playsound import playsound
import playsound
import speech_recognition as sr
from gtts import gTTS
from selenium import webdriver
import requests
import random
from config import keys

def emailJoshLogin(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(k['gmailJoshUsername'])
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    time.sleep(0.5) 
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(k['gmailJoshPassword'])
    time.sleep(0.5) 
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    speak("done")
    time.sleep(3)

def emailJoshSchoolLogin(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(k['gmailJoshSchoolUsername'])
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span').click()
    time.sleep(0.5) 
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(k['gmailJoshSchoolPassword'])
    time.sleep(0.5) 
    driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span').click()
    speak("done")
    time.sleep(3)



def speak(text):
    
    a = gTTS(text=text, lang="en")
    filename = "va.mp3" 
    a.save(filename)
    playsound.playsound(filename)
    
    os.remove(filename)
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said

def playSong(search):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.youtube.com/')
    driver.find_element_by_xpath('//*[@id="search"]').send_keys(search)
    driver.find_element_by_xpath('//*[@id="search-icon-legacy"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="contents"]/ytd-video-renderer[1]').click()
    time.sleep(1)
def weather():
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://www.google.com/%')
    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input').send_keys("weather")

    driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]').click()
def openFuntech(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://funtech.co.uk/student/enrolments/login')
    driver.find_element_by_xpath('//*[@id="EnrolmentUsername"]').send_keys(k['funtechUsername'])
    driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[1]/form/div[3]/input').send_keys(k['funtechPassword'])
    driver.find_element_by_xpath('//*[@id="EnrolmentStudentLoginForm"]/div[4]/input').click()
    speak("done")
def firefly(k):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://seniorschool.ucs.org.uk/login/login.aspx?prelogin=https%3a%2f%2fseniorschool.ucs.org.uk%2fstudent-dashboard')
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(k['fireflyUsername'])
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(k['fireflyPassword'])
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/form/button').click()


speak("V C A is online")
t = "t"
while t == "t":
    text = get_audio()
    text = text.lower()
    if "hello" in text:
        speak("hey, how are you?") 

    if "i'm good" in text or "i am good" in text:
        speak("Great!")

    if "how are you" in text:
        speak("I am doing well, thanks for asking!, what would you like me to do for you today?")

    if "gmail login josh" in text.lower() or "email login josh" in text.lower():
        speak("ok, loging in.")
        emailJoshLogin(keys)

    if "play" in text:
        speak("what would you like to play?")
        txt = get_audio()
        if txt != "":
            split = text.split()
            print("playing: " + txt)
            speak("playing " + txt)
            playSong(txt)

    if "weather" in text:
        weather()
    if "funtech login" in text or "tech login" in text:
        openFuntech(keys)
    if "firefly login" in text or "fly login" in text:
        firefly(keys)
    if "gmail login school" in text.lower() or "email login school" in text.lower() or "email school login" in text.lower() or "gmail school login" in text.lower():
        speak("ok, loging in.")
        emailJoshSchoolLogin(keys)
    if "quit chrome" in text:
        try:
            driver.quit
        except Exception as e:
            print("error quiting chrome")
