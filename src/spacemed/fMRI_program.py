import argparse
import numpy as np
import nibabel as nib
from matplotlib import pyplot
from pathlib import Path
import scipy.signal
from cross_correl_MRI import normalise
from cross_correl_MRI import build_signal
from . import __version__

# Helper functions from module
# def normalise(data):
#    std = np.std(data)
#    if std == 0:
#        return data - np.mean(data)
#    return (data - np.mean(data)) / std


# def build_signal(fMRI):
#    fmri = nib.load(fMRI)
#    s_one = np.array([1] * 5 + [0] * 5)
#    nt = fmri.shape[-1]
#    signal = np.tile(s_one, int(np.ceil(nt / 10)))
#    return signal[:nt]


def arg_parser():
    parser = argparse.ArgumentParser(
        description="Comp. cross-correlation for fMRI slice"
    )
    parser.add_argument("fMRI", type=Path, help="Path to fMRI NIfTI file")
    parser.add_argument(
        "slice", type=int, default=0, help="index of slice to process")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="cross.png",
        help="Name of output image file",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser


def main():
    parser = arg_parser()
    args = parser.parse_args()

    # 1. Load Data
    img = nib.load(args.fMRI)
    data = img.get_fdata()
    nt = data.shape[-1]

    # Check if slice index valid (0-29 typical fMRI-dataset w/ e.g. 30 sl.)
    if args.slice >= data.shape[2]:
        print(f"Error: Slice index {args.slice} is out of bounds for axis 2.")
        return

    # 2. Build the reference signal
    ref_signal = build_signal(nt)
    ref_norm = normalise(ref_signal)

    # 3. Process the slice: compute correlation for every voxel in the 2D slice
    slice_data = data[:, :, args.slice, :]
    nx, ny, nt = slice_data.shape
    # shape: tuple, 3rd dimension has been sliced away,
    # nt already defined as time for build_signal

    # This matrix will store the maximum correlation value for each voxel
    # creates a new array (a grid) where every single entry is the number 0
    correlation_map = np.zeros((nx, ny))

    print(f"Processing slice {args.slice}...")
    for i in range(nx):
        for j in range(ny):
            voxel_ts = slice_data[i, j, :]  # make time series
            if np.all(voxel_ts == 0):  # Skip background voxels
                continue

            # Compute cross-correlation and fill array
            cross = scipy.signal.correlate(
                normalise(voxel_ts), ref_norm, mode="same")
            correlation_map[i, j] = np.max(cross)

    # 4. Display and Save
    pyplot.figure(figsize=(10, 8))
    pyplot.imshow(correlation_map.T, origin="lower", cmap="RdBu_r")
    pyplot.colorbar(label="Max Cross-Correlation")
    pyplot.title(f"Cross-correlation Map - Slice {args.slice}")
    pyplot.xlabel("Voxel X")
    pyplot.ylabel("Voxel Y")

    pyplot.savefig(args.output)
    print(f"Result saved to {args.output}")


if __name__ == "__main__":
    main()

# example: python fMRI_program.py brain_scan.nii.gz 15 result_map.png
