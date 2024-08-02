#!/bin/bash

INDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/basecellcounts
OUTDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/BaseCellCountsMerged
OUTFILE=${OUTDIR}/merged_BaseCellCounts.AllCellTypes.tsv


sbatch Step3_SComatic_jobsubmit.sh $INDIR $OUTFILE










