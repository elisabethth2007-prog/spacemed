from matplotlib import pyplot
import nibabel
import numpy
import scipy.signal

#fmri = nibabel.load(fMRI)
#fmri_data = fmri.get_fdata()

#voxel_ts = fmri_data[x, y, z, :] #make time series
#nt = fmri.shape[-1]
#module now only contains reusable functions,
#file loading happens in script


def normalise(data):
    norm = data - numpy.mean(data)
    norm = norm / numpy.std(data)
    return norm
    

def build_signal(nt):
    s_one = numpy.array([1] * 5 + [0] * 5)
    signal = numpy.tile(s_one, int(numpy.ceil(nt / 10)))
    return signal[:nt]


def cross_correlation(signal, voxel_ts):
    cross = scipy.signal.correlate(normalise(voxel_ts), normalise(signal), mode="same")
    lags = scipy.signal.correlation_lags(len(voxel_ts), len(signal), mode="same")
    pyplot.plot(lags, cross)
    p = numpy.argmax(cross)
    lag = lags[p]
    return p, lag
