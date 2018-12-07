import pandas as pd
a=pd.read_csv("lynx.csv")
a["Year"]=lynx.Year/10
a["Year"]=a["Year"].round()*10
sum_a=a.groupby("Year").sum()
result=sum_lynx.sort_values("huneted",ascending= False)
print(result)