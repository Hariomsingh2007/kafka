'''
Author : Hari om Singh
Date : 06-June -2017
Description: This will convert the audio to text

NOte : Internet is must as we are using the google module to find the translattion
'''

import speech_recognition as sr


def voice_read():
    r = sr.Recognizer()
    r.pause_threshold = 0.7
    r.energy_threshold = 400
    with sr.Microphone() as source:
        audio = r.listen(source)
        message = str(audio)
    try:

        Audio_Txt=r.recognize_google(audio)
        print(Audio_Txt)
        return Audio_Txt
    except sr.UnknownValueError:
        Audio_Txt='NULL'
        print("NULL")
        return Audio_Txt




def main():
        t=voice_read()
        return t


if __name__ == '__main__':
    while(1):
        main()


