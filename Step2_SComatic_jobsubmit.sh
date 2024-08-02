#!/bin/bash

#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=12G
#SBATCH --partition=uoa-compute
#SBATCH --job-name=BaseCellCounter
#SBATCH --output=BaseCellCounter-%j.log

##SBATCH --mail-type=begin        # send email when job begins
##SBATCH --mail-type=end          # send email when job ends
##SBATCH --mail-user=t13sb23@abdn.ac.uk

# module load mamba
# source ~/.bash_profile
# source ~/.bashrc

# mamba deactivate



mamba activate mycondaspace1
 
python /uoa/home/t13sb23/sharedscratch/my_project/SComatic/scripts/BaseCellCounter/BaseCellCounter.py --bam $1 \
    --ref $3 \
    --chrom chr20 \
    --out_folder $4 \
    --min_bq 30 \
    --tmp_dir $2 \
    --nprocs 16

rm -rf $2

