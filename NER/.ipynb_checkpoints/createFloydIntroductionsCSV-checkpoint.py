import pandas as pd
import os
from tqdm import tqdm
from multiprocessing import Pool
import numpy as np

OUT_STEM = "/shared/3/projects/benlitterer/podcastData/NER/tempFloydIntroductions/floydIntroductions"

df = pd.read_csv("/shared/3/projects/benlitterer/podcastData/processed/floydMonth/floydMonthEnSHORT.csv") 

df["potentialOutPathFull"] = "/shared/3/projects/benlitterer/podcastData/prosodyMerged/floydMonth" + df["potentialOutPath"] 
df["exists"] = df["potentialOutPathFull"].apply(lambda x: os.path.exists(x)) 
df = df[df["exists"] == True]

dfList = np.array_split(df, 12)

def outputDataFile(i): 
    currDf = dfList[i]
    OUT_PATH = f"{OUT_STEM}{i}.tsv"
    with open(OUT_PATH, "w") as outFile: 
        for path in tqdm(currDf["potentialOutPathFull"]): 
            with open(path) as currFile: 
                fullText =  "".join([row.split(",")[4] for row in currFile.readlines()])
                firstBit = " ".join(fullText.split()[:500]).replace("\t", "").replace("\n", "") 
                outFile.write(f"{path}\t{firstBit}\n")

pool = Pool(processes=12)
pool.map(outputDataFile, list(range(12)))