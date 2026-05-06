from matplotlib import pyplot
import nibabel
import numpy
import scipy.signal

def normalise(data):
    norm = (data - numpy.mean(data))
    norm = norm / numpy.std(data)
    return norm


def build_signal(fMRI):
    fmri = nibabel.load(fMRI)
    s_one = numpy.array([1]*5 + [0]*5)  
    nt = fmri.shape[-1] 
    signal = numpy.tile(s_one, int(numpy.ceil(nt/10)))
    signal = signal[:nt]
    return signal


def cross_correlation(signal, fMRI, voxel):
    fmri = nibabel.load(fMRI)
    fmri_data = fmri.get_fdata()

    data = fmri_data[voxel[0], voxel[1], voxel[2], :]
    cross = scipy.signal.correlate(
        normalise(data), normalise(signal),
        mode="same")
    lags = scipy.signal.correlation_lags(
        len(data), len(signal),
        mode="same")
    pyplot.plot(lags, cross)
    p = numpy.argmax(cross)
    lag = lags[p]
    return p, lag
