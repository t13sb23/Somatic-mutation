#!/opt/software/uoa/spack-sw/linux-rhel8-x86_64/gcc-12.1.0/python-3.9.12-u2o5ndnqcbr26nc573ubjrvv7o5n5wts/bin/python

import pandas as pd
import numpy as np
import os

nmut_per_cell = {}
ncell_per_mut = {}

infiles = os.listdir("/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newsinglecell")
sample_meta = "/uoa/home/t13sb23/sharedscratch/my_project/sra_metadata_with_batchid.csv"
sample_meta_df = pd.read_table(sample_meta, sep=",")

sc_meta = "/uoa/home/t13sb23/sharedscratch/my_project/Randolph_singlecell_metadata-Sristi.tsv"
sc_meta_df = pd.read_table(sc_meta, sep="\t")

donor_meta = "/uoa/home/t13sb23/sharedscratch/my_project/SComatic/visualization/donor_metadata_with_batchid.csv"
donor_meta_df = pd.read_table(donor_meta, sep=",")


for infile in infiles:
     if infile.endswith(".tsv"):

         indf = pd.read_table(os.path.join("/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newsinglecell", infile), sep="\t")
         
         # update cellbarcode to include batch info
         sampname = infile.split("_")[0]
        

         indf["mutation"] = indf["#CHROM"] + "_" + indf["Start"].astype(str) + "_" + indf["End"].astype(str) + "_" + indf["REF"] + "_" + indf["ALT_expected"]
         indf["CellBarcode"] = [ cbx for cbx in indf["CB"]]

         mutations = indf["mutation"].unique()
         nmuts = len(mutations)

         cellbarcode = indf["CellBarcode"].unique()
         ncells = len(cellbarcode)

         mut_mat = np.zeros(shape=(nmuts, ncells))

         for mut in range(nmuts):
             xmut = mutations[mut] # name of mutation
             allele = xmut.split("_")[-1] # mutant/alt allele
             xdf = indf.loc[(indf["mutation"] == xmut) & (indf["Base_observed"] == allele), ["CB", "Base_observed"]] # subset of genotyped CBs

             if xdf.shape[0] > 0:
                 # find CBs that have mutation
                 idxCB = np.isin(cellbarcode,  xdf["CB"])
                 mut_mat[mut, idxCB] = 1.0

         

         # loop over each Indiv ID - compute cells_carrying_mut for each
         unique_donors = sc_meta_df.loc[sc_meta_df.CellID.isin(cellbarcode), "sample_condition"].unique()
         for donor in unique_donors:
             donor_cells = sc_meta_df.loc[(sc_meta_df.CellID.isin(cellbarcode)) & (sc_meta_df.sample_condition.isin([donor])), "CellID"]
             donor_index = np.isin(indf["CellBarcode"].unique(), donor_cells)

             cells_carrying_mut = mut_mat[:, donor_index].sum(axis=1)
             muts_per_cell = mut_mat[:, donor_index].sum(axis=0)

             sample_name = "_".join(infile.split("_")[0:3]).rstrip("chr20.single") + "_" + donor # + donor ID
             nmut_per_cell[sample_name] = muts_per_cell.mean()
             ncell_per_mut[sample_name] = cells_carrying_mut.mean()

     final_df = pd.DataFrame({"Sample": list(nmut_per_cell.keys()),
                              "CellType": ["_".join(x.split("_")[1:3]) for x in nmut_per_cell.keys()],
                              "indiv_ID": [x.split("_")[-2] for x in nmut_per_cell.keys()],
                              "condition": [x.split("_")[-1] for x in nmut_per_cell.keys()],
                            "No. of mutation per cell": list(nmut_per_cell.values()), 
                            "No. of cells per mutation": [ncell_per_mut[s] for s in nmut_per_cell.keys()]})
     #cd8_df = pd.DataFrame({"Sample": list(nmut_per_cell.keys()), 
      #                      "CD8_No. of mutation per cell": [nmut_per_cell[s.replace("CD4", "CD8")] for s in nmut_per_cell.keys()], 
      #                      "CD8_No. of cells per mutation": [ncell_per_mut[s.replace("CD4", "CD8")] for s in nmut_per_cell.keys()]})

     #final_df = pd.merge(cd4_df, cd8_df, on="Sample")

# merge with donor meta-data
final_merge = pd.merge(final_df, donor_meta_df, on='indiv_ID')

final_merge.to_csv('Tcell_mutation_withdonors.tsv', sep="\t", index=False)







