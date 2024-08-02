#! /bin/bash

INDIR="/uoa/scratch/shared/Morgan_Lab/tcell_ageing_meta_analysis_2023/data/randolph_2021/bam"
OUTDIR="/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newcelltypesbam"


echo "Current working directory: $PWD"
echo "Input directory: $INDIR"
echo "Output directory: $OUTDIR"


for x in $(find $INDIR -type f -name "*.bam" | grep -v ".bam.bai$");
do
    echo "Found BAM file: $x"
	fname=$(echo $x | rev | cut -d "/" -f 1 | rev | cut -d "." -f 1-2)
	echo "Filename without extension: $fname"
	
	
	    sbatch run_bam1.sh "$x" "$OUTDIR" "chr20"
	
	
done
