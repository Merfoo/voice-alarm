#!/usr/bin/env python3

from gtts import gTTS
import speech_recognition as sr
import os
import base64

def get_text_to_speech_filename(text_to_speech):
    return "{}.mp3".format(base64.urlsafe_b64encode(text_to_speech.encode("utf-8")).decode("utf-8"))

def create_text_to_speech_file(text_to_speech):
    tts = gTTS(text=text_to_speech, lang="en")
    tts.save(get_text_to_speech_filename(text_to_speech))

def play_text_to_speech_file(text_to_speech):
    os.system("mpg321 {}".format(get_text_to_speech_filename(text_to_speech)))

def main():
    text_to_continue = "what"

    wake_up_person_text = "wake up"
    create_text_to_speech_file(wake_up_person_text)

    annoy_person = "now you're awake'"
    create_text_to_speech_file(annoy_person)

    r = sr.Recognizer()
    m = sr.Microphone()

    # Adjust for background noise
    with m as source:
        r.adjust_for_ambient_noise(source)

    print("Minimum energy threshold: {}".format(r.energy_threshold))

    while True:
        play_text_to_speech_file(wake_up_person_text)
        print("Listening...")

        try:
            with m as source: 
                audio = r.listen(source, timeout=5)

            speech = r.recognize_google(audio)

        except KeyboardInterrupt:
            return
            
        except:
            continue

        if speech == text_to_continue:
            play_text_to_speech_file(annoy_person)
            break

        print(speech)

if __name__ == "__main__":
    main()