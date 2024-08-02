#!/bin/bash


INDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/BaseCellCountsMerged
INFILE=${INDIR}/merged_BaseCellCounts.AllCellTypes.tsv
REF=/uoa/scratch/shared/Morgan_Lab/common_resources/hg38/chroms/chr20.fa.gz
OUTDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling
OUTFILE=${OUTDIR}/step1_variantcalling.tsv




  sbatch Step4.1_SComatic_jobsubmit.sh $INFILE $OUTFILE $REF

