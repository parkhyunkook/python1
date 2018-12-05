import pandas as pd
dna="AGTCCGCGAATACAGGCTCGGT"
dna_as_series=pd.Series(list(dna),name="genes")
print(dna_as_series.head())

print(dna_as_series.unique())

