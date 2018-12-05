import pandas as pd
alco2009=pd.read_csv("niaaa-report2009.csv",index_col="State")
alco=pd.read_csv("niaaa-report.csv",index_col=["State","Year"])

population=pd.read_csv("population.csv",index_col="State")

alco["Total"]=alco.Wine+alco.Spirits+alco.Beer

wine_state=alco2009["Wine"]>alco2009["Wine"].mean()
beer_state=alco2009["Beer"]>alco2009["Beer"].mean()

print(pd.crosstab(wine_state,beer_state))