import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)

del df["Luminosity"]
del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"]

print(df.shape)

df.drop(['Unnamed: 0'],axis=1,inplace=True)
df.drop(['Unnamed: 6'],axis=1,inplace=True)

df.to_csv('final.csv') 
print(df.shape)