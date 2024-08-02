
import pandas as pd


df = pd.read_csv("/uoa/home/t13sb23/sharedscratch/my_project/SComatic/visualization/Tcell_mutation_withdonors.tsv", sep="\t")

# DataFrame to only include NI (mock infection) samples
ni_samples = df[df["infection_status"] == "NI"]

# filtered DataFrame to a new TSV file
ni_samples.to_csv("ni_samples.tsv", sep="\t", index=False)