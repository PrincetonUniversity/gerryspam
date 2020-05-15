import pandas as pd
import numpy as np
from rich import print

dat = pd.read_csv('/Users/hopecj/projects/gerryspam/OR/dat/OR data/Oregon Data - State House.csv',
                  header=1)
dat["id"] = dat.index
dat
dat_long = pd.wide_to_long(dat, ["D", "R", "O"], i="id", j="year")

# data from Eric McGhee helpful paper: https://escholarship.org/uc/item/27n2n1tg#main
df = pd.read_stata('/Users/hopecj/projects/gerryspam/OR/dat/CA data/cjpp1197_supplementary_1/CA House 1-to-1 2011.final.dta')
print(df.head)
print(df.columns)
print(df.shape)