#!/bin/bash
#SBATCH --job-name="plot HR"
#SBATCH --partition="compute"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00

# the stuff we are going to do (this is a shell script)
pwd
source /etc/profile.d/conda.sh
conda activate spacemed
sm_plot_heart /home/elth11/SpaceMed-2026/elth11/data/pulse_data.csv -o results.png

