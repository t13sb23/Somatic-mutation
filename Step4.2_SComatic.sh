#!/bin/bash

INDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling
INFILE=${INDIR}/step1_variantcalling.tsv.calling.step1.tsv
EDITING=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/RNAediting/AllEditingSites.hg38.txt
PON=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/PoNs/PoN.scRNAseq.hg38.tsv
OUTDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling
OUTFILE=${OUTDIR}/step2_variantcalling.tsv


sbatch Step4.2_SComatic_jobsubmit.sh $INFILE $OUTFILE $EDITING $PON