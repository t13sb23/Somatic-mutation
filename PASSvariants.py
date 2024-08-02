
import pandas as pd


df = pd.read_csv('/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling/step2_variantcalling.tsv.calling.step2.tsv',
                  sep='\t', skiprows=28, low_memory=False)
df.head()

df_pass = df[df['FILTER'].str.contains('PASS')]


df_pass.to_csv('/uoa/home/t13sb23/sharedscratch/my_project/SComatic/SComatic_results/newvariantcalling/step2_variantcalling.pass.tsv', sep='\t', index=False)