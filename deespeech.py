import speech_recognition as sr

deev = sr.Recognizer()

#voice = sr.AudioFile('OSR_us_000_0010_8k.wav')

voice = sr.Microphone()

print('Hello Divine. Please say something... ')

try:
    with voice as source:
        deev.adjust_for_ambient_noise(source)
        audio = deev.listen(source)

    output1 =  deev.recognize_google(audio, show_all=True)
    print(output1['alternative'][0]['transcript'])
except:
    print("oops! I didn't get you...")