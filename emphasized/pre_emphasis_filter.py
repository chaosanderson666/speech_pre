import sys
import numpy as np
import scipy.io.wavfile
from scipy.fftpack import dct
import matplotlib.pyplot as plt

def emphasize(filename):
    sample_rate, origin = scipy.io.wavfile.read(filename)
    print(sample_rate); print(origin); print(type(origin)); print(origin.shape)

    pre_emphasis = 0.97
    emphasized = np.append(origin[0], origin[1:] - pre_emphasis * origin[:-1])
    emphasized = emphasized.astype(dtype=np.int16)
    print(emphasized); print(type(emphasized)); print(emphasized.shape)

    scipy.io.wavfile.write(filename.split('.', 1 )[0] + '_emphasized.wav', sample_rate, emphasized)
    
    return origin, emphasized, origin.shape[0]

def plot_wav(wav_data1, wav_data2, length):
    x1 = np.arange(length)
    y1 = wav_data1
    y2 = wav_data2
    
    fig=plt.figure(figsize=(12, 5))
    ax = fig.add_subplot(111)
    plt.plot(x1, y1, label='origin', color='blue')
    plt.plot(x1, y2, label='emphasized', color='red')
    ax.set_xlim(0, length)
    ax.set_ylim(-25000, 25000)

    ax.set_xlabel('Times')
    ax.set_ylabel('Amplitude')
    plt.legend(loc='upper right')
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print('need wav file name.')
        quit()
    wav_file = sys.argv[1]
    origin, emphasized, length = emphasize(wav_file)
    plot_wav(origin, emphasized, length)