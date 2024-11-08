import spacy
import pandas as pd
from tqdm import tqdm 
import sys
import os 
import json

IN_PATH = sys.argv[1]
IN_COL = sys.argv[2]
OUT_PATH = sys.argv[3]
TRUNCATION = int(sys.argv[4])

#TODO: change number of rows 
df = pd.read_json(IN_PATH, orient="records", lines=True)
print(df.shape)

os.remove(IN_PATH)

#load spacy pipeline 
nlp = spacy.load("en_core_web_md", exclude=["parse", "tagger", "textcat"])

#get documents as list
df = df.dropna(subset=["potentialOutPath", IN_COL])

print(f"shape before removing long strings {df.shape}")
#we can't process strings over 1,000,000 characters in spacy... 
df = df[df[IN_COL].apply(len) < 1000000]
print(f"shape after removing long strings {df.shape}")

docs = df[IN_COL]

if TRUNCATION != 0: 
    docs = [doc[:TRUNCATION] for doc in docs]
    
outPaths = list(df["potentialOutPath"]) 
docs = nlp.pipe(docs)

print(f"processing file {IN_PATH}")
outNames = ["potentialOutPath", "ent", "start", "end", "type"]
#run NER!
with open(OUT_PATH, "w") as outFile: 
    for i, doc in tqdm(enumerate(docs)): 
        outStr = ""
        for ent in doc.ents: 
            outPath = outPaths[i]
            outList = [outPath, ent.text, ent.start_char, ent.end_char, ent.label_]
            outDict = dict(zip(outNames,outList))
            outFile.write(json.dumps(outDict) + "\n")
            '''
            outList = [str(item).replace("\t", "").replace("\n", "") for item in outList]
            outStr += "\t".join(outList) + "\n" 
            '''
        outFile.write(outStr) 
