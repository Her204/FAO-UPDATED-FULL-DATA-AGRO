import pandas as pd, numpy as np
import os


path = "/mnt/d/data_ds/FAO-UPDATED-FULL-DATA-AGRO/data"
files = os.listdir(path)

names = pd.Series([file.split("2022_")[1].split("_")[0] for file in files])

names = names.replace("credit.csv","credit")

print(names)

names = names.unique()



for name in names:
    files_r = [pd.read_csv(path+"/"+file) for file in files if name in file]

    f = pd.concat(files_r)

    print(name)
    
    f.to_csv("data_2/"+name+".csv")
    
