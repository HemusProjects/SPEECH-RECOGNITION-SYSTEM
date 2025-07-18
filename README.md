# SPEECH-RECOGNITION-SYSTEM

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* :  NAGISETTY HEMANTH SAI

*INTERN ID* : CT04DG2507

*DOMAIN* : AI(ARTIFICIAL INTELLIGENCE)

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

#DESCRIPTION OF THE PROJECT

This project is a simple and functional speech-to-text converter built using Python. Its main job is to take an audio file—specifically a .wav file—and turn the spoken words in it into written text. It uses a Python library called speech_recognition, which makes working with audio and speech data easy and efficient.

At the core of the system is a small script that loads the audio file, sends it to Google’s online speech recognition engine, and returns the transcribed text. The system doesn’t need any complex setup or training of models—it uses a pre-trained engine (Google’s Web Speech API), which already understands spoken language well.

Let’s walk through how it works:

You provide a .wav file that contains someone speaking.

The Python program reads this audio using the speech_recognition library.

It then sends this audio to Google’s speech recognition service.

The service processes the audio and returns the text version of what was said.

The program prints this transcription for you to see.

The main function, transcribe_audio(file_path), takes the file path of the audio as input. Inside this function, we use AudioFile to read the sound file. The record() method captures all the spoken content from the file, and then recognize_google() does the heavy lifting of converting it into text.

This setup is ideal for short clips—maybe someone saying a sentence or two—and it works great for quick transcriptions. Since the Google API is doing the actual speech recognition, you don’t need to worry about building or training a machine learning model. Everything happens in a few lines of code.

To make it work:

You’ll need a .wav audio file (you can convert from .mp3 using tools like ffmpeg).

You need an internet connection because the speech is sent to Google for processing.

You can run the Python script in any modern Python environment.

If you're planning to upload this to GitHub, you just need to include:

The Python script.

A sample .wav file (like sample-3.wav).

A brief README with instructions.

Keep in mind that file paths like /mnt/data/sample-3.wav are specific to the environment (like Google Colab), so if someone else wants to run your code on their computer, they should update the file path accordingly.

In summary, this project gives you a quick, easy way to convert spoken words into text using Python and a powerful pre-trained model from Google. It’s beginner-friendly, useful for many applications like note-taking, subtitles, accessibility tools, or just experimenting with speech tech.

# OUTPUT

Transcription:
 2 + 7 is less than
