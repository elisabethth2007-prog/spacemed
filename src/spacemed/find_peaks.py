import numpy


def find_peaks(data, w):

    peaks = []
    for i in range(len(data)):
        start = max(i - w, 0)
        end = min(i + w + 1, len(data))
        window = data[start:end]
        max_pos = numpy.argmax(window) + start
        if data[i] == max(window) and window.count(data[i]) == 1:
            peaks.append(i)

    return peaks
