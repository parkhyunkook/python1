import pandas as pd
alco2009=pd.read_csv("niaaa-report2009.csv",index_col="State")
population=pd.read_csv("population.csv",index_col="State")


df=pd.merge(alco2009.reset_index(),population.reset_index()).set_index("State")


print(alco2009.max())
print(alco2009.min(axis=1))

alco=pd.read_csv("niaaa-report.csv",index_col=["State","Year"])



