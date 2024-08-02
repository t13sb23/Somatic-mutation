#!/bin/bash
set -x

#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=12G
#SBATCH --partition=uoa-compute
#SBATCH --job-name=SingleCellGenotype
#SBATCH --output=SingleCellGenotype-%j.log

## SBATCH --mail-type=begin        # send email when job begins
## SBATCH --mail-type=end          # send email when job ends
## SBATCH --mail-user=t13sb23@abdn.ac.uk

# module load mamba
# source ~/.bash_profile
# source ~/.bashrc

# mamba deactivate
mamba activate mycondaspace1


python /uoa/home/t13sb23/sharedscratch/my_project/SComatic/scripts/SingleCellGenotype/SingleCellGenotype.py \
       --bam "$1" \
       --infile "$2" \
       --nprocs 16 \
       --ref "$3" \
       --meta "$4" \
       --outfile "$5" \
       --tmp_dir "$6"
rm -rf "$6"
