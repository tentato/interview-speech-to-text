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
# wav2 = "Prof.Dr.Eckert2.wav"
filename = "Interview4.wav"
filename_reduce_noise = "Interview4_reduced.wav"

# load data
rate, data = wavfile.read(filename)
# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write(filename_reduce_noise, rate, reduced_noise)