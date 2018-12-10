from scipy.stats import pearsonr
import pandas as pd
gspc=pd.read_csv("^GSPC.csv",index_col="Date")
print(gspc["Close"].mean())
print(gspc["Close"].std())
print(pearsonr(gspc["Close"],gspc["Volume"]))