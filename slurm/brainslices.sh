#!/bin/bash
#SBATCH --job-name="generate_brain_images"
#SBATCH --partition="compute"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00
#SBATCH --array=0-31
#SBATCH --output=logs/slice_%A_%a.out
#SBATCH --error=logs/slice_%A_%a.err

# the stuff we are going to do (this is a shell script)
pwd
source /etc/profile.d/conda.sh
conda activate spacemed
SLICE=${SLURM_ARRAY_TASK_ID}
sm_fMRI_prog \
/home/elth11/SpaceMed-2026/elth11/data/fmri-data/3_fMRI_TR2sec_3mm_3min.nii \
${SLICE} \
-o cross_map_${SLICE}.png
