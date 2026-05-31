#!/bin/bash
#SBATCH --job-name="lemon job"
#SBATCH --partition="compute"
#SBATCH --nodes=1
#SBATCH --cpus-per-task=10
#SBATCH --mem=40G
#SBATCH --time=01:00:00
#SBATCH --array=1-10

# the stuff we are going to do (this is a shell script)
echo "starting job ${SLURM_ARRAY_TASK_ID}"
date
sleep 200
echo done
date
