from spacemed.find_peaks import find_peaks


def test_find_peaks_simple():
    data = [1, 3, 2, 1]
    w = 1

    peaks = find_peaks(data, w)

    assert peaks == [1]


def test_find_peaks_multiple():
    data = [1, 3, 1, 3, 1]
    w = 1

    peaks = find_peaks(data, w)

    assert peaks == [1, 3]


def test_find_peaks_long_w():
    data = [1, 3, 4, 1, 3, 1]
    w = 2

    peaks = find_peaks(data, w)

    assert peaks == [2]


def test_find_peaks_none():
    data = [5, 4, 3, 2, 1]
    w = 1

    peaks = find_peaks(data, w)

    assert peaks == [0]
