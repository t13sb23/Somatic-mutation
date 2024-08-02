#!/bin/bash
set -x

#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=12G
#SBATCH --partition=uoa-compute
#SBATCH --job-name=BaseCellCalling
#SBATCH --output=BaseCellCalling-%j.log

##SBATCH --mail-type=begin        # send email when job begins
##SBATCH --mail-type=end          # send email when job ends
##SBATCH --mail-user=t13sb23@abdn.ac.uk

module load mamba
source ~/.bash_profile
source ~/.bashrc

mamba deactivate

mamba activate mycondaspace1

python /uoa/home/t13sb23/sharedscratch/my_project/SComatic/scripts/BaseCellCalling/BaseCellCalling.step1.py \
     --infile $1 \
     --outfile $2 \
     --ref $3 \
     --min_cov 5 \
     --min_cells 5 \
     --min_ac_cells 2 \
     --min_ac_reads 3 \
     --max_cell_types 5 \
     --min_cell_types 1 \
     --fisher_cutoff 1 \
     # --alpha1 0.260288007167716 \
     # --beta1 173.94711910763732 \
     # --alpha2 0.08354121346569514 \
     # --beta2 103.47683488327257 \
     
     