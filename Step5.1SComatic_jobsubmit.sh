#!/bin/bash

INDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling
INFILE=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling/step2_variantcalling.pass.tsv
REF=/uoa/scratch/shared/Morgan_Lab/common_resources/hg38/chroms/chr20.fa.gz
META=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_scripts/Sristi_Metadata.tsv
OUTDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newsinglecell


for bam in $(ls -d /uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newcelltypesbam/*CD[48]_T*.bam); do
  cell_type=$(basename $bam | awk -F'.' '{print $(NF-1)}')
  OUTFILE=$OUTDIR/${cell_type}.single_cell_genotype.tsv
  tmp_dir=${OUTDIR}/tmp_${cell_type}
  mkdir -p $tmp_dir




  sbatch Step5.1SComatic.sh "$bam" "$INFILE" "$REF" "$META" "$OUTFILE" "$tmp_dir"
done