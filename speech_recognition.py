import speech_recognition as sr

recognizer = sr.Recognizer()

def transcribe_audio(file_path):
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        return text

file_path = "C:/Users/hemu/Downloads/sample-3.wav"
result = transcribe_audio(file_path)
print("Transcription:\n", result)
