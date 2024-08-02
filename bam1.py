#!/opt/software/uoa/spack-sw/linux-rhel8-x86_64/gcc-12.1.0/python-3.9.12-u2o5ndnqcbr26nc573ubjrvv7o5n5wts/bin/python

import pysam
import pandas as pd
import sys

metadata = pd.read_csv("/uoa/home/t13sb23/sharedscratch/my_project/Randolph_singlecell_metadata-Sristi.tsv", sep="\t")
metadata.head()

bamfile = sys.argv[1]
outdir = sys.argv[2]
chromosome = sys.argv[3]
#bamfile = "/uoa/scratch/shared/Morgan_Lab/tcell_ageing_meta_analysis_2023/data/randolph_2021/bam/SRR13194369.bam"
inbam = pysam.AlignmentFile(bamfile, "rb")

excel_sheet = "/uoa/home/t13sb23/sharedscratch/my_project/sra_metadata_with_batchid.csv"
df = pd.read_csv(excel_sheet)
df.head()

filename_column = df.columns[0]
batch_id_column = df.columns[-1]

bam_name = bamfile.split('/')[-1].split('.')[0]
matching_row = df[df[filename_column] == bam_name]

if not matching_row.empty:
    batch_id = matching_row[batch_id_column].values[0]
    print(f"Batch ID for {bam_name}: {batch_id}")

else:
    print(f"No matching batch ID found for {bam_name}")
    batch_id = None



cell_types = ["CD4_T", "CD8_T", "NK", "B", "monocytes", "highly_infected", "infected_monocytes", "NK_high_response", "neutrophils", "DC"]


outputbam = {}
for cell_type in cell_types:
   outputbam[cell_type] = {}
   chrom_str = "chr20"
   outputbam[cell_type][chrom_str] = pysam.AlignmentFile(f"{outdir}/{bam_name}_{cell_type}_{chrom_str}.bam", "wb", template=inbam)

count = 0
for x in (inbam.fetch("chr20")): 

    #print (x.query_sequence)
    count += 1
    try:

     cellbarcode = x.get_tag("CB")
     cb_id = batch_id + "_" + cellbarcode
     cb_id = cb_id.rstrip("-1")
     x.set_tag("CB", cb_id)
     if metadata['CellID'].isin([cb_id]).any():

        celltype = metadata.loc[metadata['CellID'] == cb_id, 'celltype'].values[0]
        if celltype == "CD4_T" :
            chrom_str = "chr20"
            outputbam["CD4_T"][chrom_str].write(x)
        elif celltype == "CD8_T":
           chrom_str = "chr20"
           outputbam["CD8_T"][chrom_str].write(x)
        elif celltype == "NK":
           chrom_str = "chr20"
           outputbam["NK"][chrom_str].write(x)
        elif celltype == "B":
           chrom_str = "chr20"
           outputbam["B"][chrom_str].write(x)
        elif celltype == "monocytes":
           chrom_str = "chr20"
           outputbam["monocytes"][chrom_str].write(x)
        elif celltype == "highly_infected":
           chrom_str = "chr20"
           outputbam["highly_infected"][chrom_str].write(x)
        elif celltype == "infected_monocytes":
           chrom_str = "chr20"
           outputbam["infected_monocytes"][chrom_str].write(x)
        elif celltype == "NK_high_response":
           chrom_str = "chr20"
           outputbam["NK_high_response"][chrom_str].write(x)
        elif celltype == "neutrophils":
           chrom_str = "chr20"
           outputbam["neutrophils"][chrom_str].write(x)
        elif celltype == "DC":
           chrom_str = "chr20"
           outputbam["DC"][chrom_str].write(x)

    except KeyError :
     #print(f"Read {x.query_name} does not have a CB tag")
        continue

for cell_type, chrom_bams in outputbam.items():
   for chrom, bam in chrom_bams.items():
   
       bam.close()
inbam.close()


import os
os.listdir(os.getcwd())




