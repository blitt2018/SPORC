import pandas as pd

#import the file containing the transcripts 
df = pd.read_json("/shared/3/projects/benlitterer/podcastData/processed/mayJune/mayJuneDataRoles.jsonl", orient="records", lines=True)

#get the first 1000 words of each pod 
leanDf = df[["transcript", "potentialOutPath", "podDescription"]]

#drop missing values, need to create seperate dfs for this 
transDf = leanDf.dropna(subset=["transcript"])
descDf = leanDf.dropna(subset=["podDescription"])

#using split should remove tab and newline characters 
transDf["transcriptStarts"] = transDf["transcript"].apply(lambda x: " ".join(x.split()[:1000]))
descDf["podDescription"] = descDf["podDescription"].apply(lambda x: " ".join(x.split()))

#dummy column
transDf["tag"] = 1
descDf["tag"] = 1


#need to output to seperate text files, mallet will then import these 
transDf[["potentialOutPath", "tag", "transcriptStarts"]].to_csv("/shared/3/projects/benlitterer/podcastData/topicModelling/transcriptStarts.txt", sep="\t", index=False, header=False)
descDf[["potentialOutPath", "tag", "podDescription"]].to_csv("/shared/3/projects/benlitterer/podcastData/topicModelling/podDescriptions.txt", sep="\t", index=False, header=False)