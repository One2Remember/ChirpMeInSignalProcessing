import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from scipy.stats import linregress


def get_slope(file_path, latency_seconds):
    sample_rate, data = wavfile.read(file_path)  # load the data
    a = np.mean(data.T, axis=0)  # convert to mono track
    Pxx, freqs, bins, im = plt.specgram(a, NFFT=1024, Fs=sample_rate)
    Pxx = Pxx.T
    maxFreqIndices = np.argmax(Pxx, axis=1)
    frequencies = freqs[maxFreqIndices]

    # TODO: find latency index in bins
    chop_off = int(len(bins) * 0.2)
    slope, intercept, r_value, p_value, std_err = linregress(bins[chop_off:-chop_off], frequencies[chop_off:-chop_off])
    return slope

def print_spectrogram(file_path):
    sample_rate, data = wavfile.read(file_path)  # load the data
    a = np.mean(data.T, axis=0)  # convert to mono track
    plt.specgram(a, NFFT=1024, Fs=sample_rate)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()

def print_max_frequencies(file_path):
    sample_rate, data = wavfile.read(file_path)  # load the data
    a = np.mean(data.T, axis=0)  # convert to mono track
    Pxx, freqs, bins, im = plt.specgram(a, NFFT=1024, Fs=sample_rate)
    plt.clf()
    Pxx = Pxx.T
    maxFreqIndices = np.argmax(Pxx, axis=1)
    frequencies = freqs[maxFreqIndices]
    plt.plot(bins, frequencies)
    plt.show()

if __name__ == '__main__':
    file_path = 'recording_3_clean.wav'
    print(get_slope(file_path, 0.1))
    print_spectrogram(file_path)
    print_max_frequencies(file_path)

