import matplotlib.pyplot as plt
import numpy as np
from scipy.fftpack import fft
from scipy.signal import stft, spectrogram
from scipy.io import wavfile  # get the api
from scipy.stats import linregress

FRAME_LENGTH = 1024
SAMPLE_RATE = 44100
FREQ_RES = SAMPLE_RATE / FRAME_LENGTH

LOW_FREQ = 12000
HIGH_FREQ = 13000



def getFrameTime(frame_number):
    return frame_number * FRAME_LENGTH / SAMPLE_RATE

def getBinFrequency(bin):
    return bin * FREQ_RES

# return index just before insertion point in float list
def floatSearch(list, value):
    i = 0
    while(i < len(list) and value > list[i]):
        i += 1
    return i - 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    sample_rate, data = wavfile.read('recording_3_clean.wav')  # load the data
    a = np.mean(data.T, axis=0)  # convert to mono track
    Pxx, freqs, bins, im = plt.specgram(a, NFFT=1024, Fs=SAMPLE_RATE)#, noverlap=900)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

    Pxx = Pxx.T

    maxFreqIndices = np.argmax(Pxx, axis=1)
    frequencies = freqs[maxFreqIndices]

    chop_off = int(len(bins) * 0.2)

    slope, intercept, r_value, p_value, std_err = linregress(bins[chop_off:-chop_off], frequencies[chop_off:-chop_off])

    print(slope)

    plt.plot(bins, frequencies)
    plt.show()

    # lowInd = floatSearch(freqs, LOW_FREQ)
    # highInd = floatSearch(freqs, HIGH_FREQ)
    #
    # normTimeLow = lowInd / len(freqs)
    # normTimeHigh = highInd / len(freqs)
    #
    # print(bins)


    # KEEP
    # frequencies, times, spectrogram = spectrogram(a, sample_rate, nfft=1024, noverlap=900, nperseg=1024)
    # plt.pcolormesh(times, frequencies, 10*np.log10(spectrogram))
    # plt.ylabel('Frequency [Hz]')
    # plt.xlabel('Time [sec]')
    # plt.show()
