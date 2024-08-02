
#!/bin/bash


INDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newcelltypesbam
REF=/uoa/scratch/shared/Morgan_Lab/common_resources/hg38/chroms/chr20.fa.gz
OUTDIR=/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/basecellcounts

##loop through BAM files
for bam in $(find "$INDIR" -type f -name "*.bam"); 
do
  cell_type=$(basename $bam | awk -F'.' '{print $(NF-1)}')

  temp=$OUTDIR/temp_${cell_type}
  mkdir -p $temp

  
  sbatch Step2_SComatic_jobsubmit.sh $bam $temp $REF $OUTDIR
done  
