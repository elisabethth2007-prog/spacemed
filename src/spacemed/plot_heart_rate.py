from pathlib import Path
from matplotlib import pyplot
import argparse
from . import read_pulse
from . import find_peaks
from . import calc_heart_rate
from . import __version__
import numpy

def arg_parser():
  parser = argparse.ArgumentParser()
  parser.add_argument(
    "data", type=Path,
    help="the name of the input file")
  parser.add_argument(
    "-o", "--output", type=Path, default="hr.png",
    help="write output to file")
  parser.add_argument(
    "--version", action="version",
    version=f'%(prog)s {__version__}')
  return parser

def main():
  parser = arg_parser()
  args = parser.parse_args()
  indata = Path("../data/pulse_data.csv")
  outname = Path("heart_rate.pdf")

  time, absorption = read_pulse(indata)
  absorption = numpy.array(absorption)
  time = numpy.array(time)

  peaks = find_peaks(absorption, 50)
  hr = calc_heart_rate(time,peaks)
  
  fig, axs= pyplot.subplots(2, figsize=(10,8), sharex=True)
  axs[0].plot(time, absorption)
  axs[0].plot(time[peaks], absorption[peaks],"ro")
  axs[0].set_ylabel("absorption")
  axs[0].set_title("raw data")
  
  axs[1].plot(time[peaks[1:]], hr, 'r-')  # align HR with intervals
  axs[1].set_ylabel("Heart Rate [bpm]")
  axs[1].set_xlabel("Time [s]")
  axs[1].set_title("mean HR")


  pyplot.savefig(outname)

if __name__ == '__main__':
  main()
