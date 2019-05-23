"""
Name:           Carlos Meza

Description:    
 Using the numpy fft function on wav file, remove low frequency fuzz by offsetting from middle to both  
 left and right by offset given amount. Then, output only the clean parts of the file by using only real values.

"""

import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt

def processFile(fn, offset) :
    # Read in wav file and perform FFT
    data, samplerate = sf.read(filename)
    fft = np.fft.fft(data)
    
    # Arange the data given and extract a midpoint
    x = np.arange(0, samplerate, samplerate/len(fft))
    mid = len(x)/2
    
    # Plot Original data w/ fft
    plt.subplot(121)
    plt.title('Original file w/ FFT')
    plt.plot(x, abs(fft))
    
    # Set variables to know when to stop offset to left and right
    i = int(mid - offset)
        
    # Offset all values starting at left and stopping once we reach right offset
    while(i < (mid + offset)):
        fft[i] = 0
        i += 1
        
    # Plot the new 'clean' sound w/ fft
    plt.subplot(122)
    plt.title('Cleaned file w/ FFT')
    plt.plot(x, abs(fft))  
    
    # Apply inverse of FFt to cleaned signal
    clean = np.fft.ifft(fft)
    
    # Get only real part of signal for new sound file
    clean = np.real(clean)
    sf.write('cleanMusic.wav', clean, samplerate)

    plt.show()

##############  main  ##############
if __name__ == "__main__":
    filename = "P_9_2.wav"
    offset = 10000

    # this function should be how your code knows the name of
    #   the file to process and the offset to use
    processFile(filename, offset)