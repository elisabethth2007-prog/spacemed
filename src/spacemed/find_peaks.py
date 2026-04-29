import numpy


def find_peaks(data, w):

    peaks = []
    for i in range(len(data)):
        start = max(i - w, 0)
        end = min(i + w, len(data))
        window = data[start:end]
        max_pos = numpy.argmax(window) + start
        if i == max_pos:
            peaks.append(i)

    return peaks
