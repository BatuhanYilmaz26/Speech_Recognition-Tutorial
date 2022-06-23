import wave

# Waveform Audio File Format is an audio file format standard, developed by IBM and Microsoft, for storing an audio bitstream on PCs. 
# It is the main format used on Microsoft Windows systems for uncompressed audio.

# Audio signal parameters
# - number of channels --> 1 for mono, 2 for stereo
# - sample width --> 8 bits, 16 bits, 24 bits, 32 bits
# - frame rate/sample rate --> Samples per second, e.g. 44,100 Hz -> Means that we get 44,100 samples per second
# - number of frames --> Total number of samples in the audio file
# - values of a frame --> The values of the samples in the audio file

# Open a wave file
obj = wave.open("dont_speak-no_doubt.wav", "rb")

print("Number of channels: ", obj.getnchannels())
print("Sample width: ", obj.getsampwidth())
print("Frame rate: ", obj.getframerate())
print("Number of frames: ", obj.getnframes())
print("Parameters: ", obj.getparams())
print("Duration: ", obj.getnframes()/obj.getframerate(), " seconds")

frames = obj.readframes(-1) # Read all the frames
print(type(frames), type(frames[0])) 
print(len(frames)) # Length of the frames. The number of bytes in the frames multiplied by the sample width.

obj.close()

# Write wave file
obj_new = wave.open("dont_speak-no_doubt_new.wav", "wb")

obj_new.setnchannels(1) # Mono
obj_new.setsampwidth(2)
obj_new.setframerate(22050.0)
obj_new.writeframes(frames)
obj_new.close()