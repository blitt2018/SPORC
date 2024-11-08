import pandas as pd
import spacy
import numpy as np
from collections import Counter
import csv
from multiprocessing import Pool 
import sys

IN_PATH = sys.argv[1]
IN_COL = sys.argv[2]
OUT_STEM = sys.argv[3]
N_SPLITS = int(sys.argv[4])
SEP = str(sys.argv[5])

print(SEP)

if SEP == "json":
    print(f"reading file {IN_PATH}") 
    df = pd.read_json(IN_PATH, orient="records", lines=True)
else:  
    #may need to change the sep and column names for different input files
    #FOR Introductions: df = pd.read_csv(IN_PATH, sep="\t", names=["potentialOutPath", "first500"])
    #FOR podcast despcriptions
    df = pd.read_csv(IN_PATH, sep=",") 

                  
print(df.columns)
print(df.shape)

sub_df = df[['potentialOutPath', IN_COL]]

#we use 160 because that's how many cores we have 
indexList = np.array_split(np.array(list(range(0, len(sub_df)))), N_SPLITS)
zippedIndices = list(zip(list(range(0, N_SPLITS)), indexList))

#last file will be missing one row 
def writeFrame(tup):
    i, indices = tup
    outDf = sub_df.iloc[indices, :]
    print(f"writing file split {i}")
    outDf.to_json(OUT_STEM + str(i), orient="records", lines=True)

with Pool(12) as p: 
    p.map(writeFrame, zippedIndices)
