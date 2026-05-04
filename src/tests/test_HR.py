from spacemed.calc_heart_rate import calc_heart_rate

import numpy as np


def test_calc_heart_rate_basic():
    time = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    peaks = [1, 3, 4, 5, 7, 9]

    hr = calc_heart_rate(time, peaks)

    expected = np.array([30.0, 60.0, 60.0, 30.0, 30.0])

    assert np.allclose(hr, expected)
    # whether two arrays are approximately equal


def test_calc_heart_rate_single_peak():
    time = np.array([0, 1, 2])
    peaks = [1]

    hr = calc_heart_rate(time, peaks)

    assert len(hr) == 0
