#!/bin/bash
# SBATCH --time=48:00:00

#SBATCH --cpus-per-task=1
#SBATCH --ntasks=1
#SBATCH --mem=12G
#SBATCH --job-name=bam1
#SBATCH --output=bam1-%j.log

##SBATCH --mail-type=begin        # send email when job begins
##SBATCH --mail-type=end          # send email when job ends
##SBATCH --mail-user=t13sb23@abdn.ac.uk

# module load mamba
# source ~/.bash_profile
# source ~/.bashrc

# mamba deactivate
mamba activate mycondaspace1
python /uoa/home/t13sb23/sharedscratch/my_project/SComatic/bam1.py $1 $2 $3
#echo $JOB
#eval $JOB