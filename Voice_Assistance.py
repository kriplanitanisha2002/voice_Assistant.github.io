import gtts
import playsound
text = "Welcome to Hansraj College"
sound = gtts.gTTS(text, lang='en')
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")