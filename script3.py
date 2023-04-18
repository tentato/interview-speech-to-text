# importing libraries 
import speech_recognition as sr 
import os 
from pydub import AudioSegment
from pydub.silence import split_on_silence
import noisereduce as nr
from scipy.io import wavfile

# filename = "Prof.Dr.Eckert.m4a"
# format = "m4a"
# wav = "Prof.Dr.Eckert.wav"
filename = "Interview6.m4a"
format = "m4a"
wav = filename.split(".")[0]+".wav"

sound = AudioSegment.from_file(filename, format)  
sound.export(wav, format="wav")