# %%
import pandas as pd
import os

# %%
df = pd.read_feather("/shared/3/projects/benlitterer/podcastData/processed/mayJune/mayJuneDataRoles.feather")
df.head() 


# %%
#pd.read_csv(df.loc[0, "fullPotentialOutPath"])
DIARIZE_STEM = "/shared/3/projects/benlitterer/podcastData/diarizationMerged"
prosDf = pd.read_json(DIARIZE_STEM + df.loc[600, "potentialOutPath"], orient="records", lines=True)

FRAC_CUTOFF = .1
#get their speaking time 
prosDf = prosDf[prosDf["speakers"].apply(len) > 0]
prosDf["wDuration"] = prosDf["end"] - prosDf["start"]
prosDf["firstSpeaker"] = prosDf["speakers"].apply(lambda x: x[0])

#aggregate speaking duration to speaker level 
prosDf = prosDf[["firstSpeaker", "wDuration"]].groupby("firstSpeaker").agg(sum)

#get speaking fraction 
prosDf["speakingFraction"] = prosDf["wDuration"] / sum(prosDf["wDuration"])
prosDf = prosDf[prosDf["speakingFraction"] >= FRAC_CUTOFF] 
prosDf

# %%
#check if for business, discussion of race is more localized to podcasts with a single speaker or just a host 
#if we only predict a host name, it's likely that there's no guest, since it would be weird to introduce oneself and not another 
N_SAMP=60000
sampDf = df[df["category1"] == "business"].sample(N_SAMP, random_state=23)

#to store speaker counts in 
spCountList = []

DIARIZE_STEM = "/shared/3/projects/benlitterer/podcastData/diarizationMerged"
#we need to loop through our data and quickly get speaker counts 
for potPath in sampDf["potentialOutPath"]:  
    if os.path.exists(DIARIZE_STEM + potPath): 
        prosDf = pd.read_json(DIARIZE_STEM + potPath, orient="records", lines=True)
    
        FRAC_CUTOFF = .1
        #get their speaking time 
        prosDf = prosDf[prosDf["speakers"].apply(len) > 0]
        prosDf["wDuration"] = prosDf["end"] - prosDf["start"]
        prosDf["firstSpeaker"] = prosDf["speakers"].apply(lambda x: x[0])

        #aggregate speaking duration to speaker level 
        prosDf = prosDf[["firstSpeaker", "wDuration"]].groupby("firstSpeaker").agg("sum")

        #get speaking fraction 
        prosDf["speakingFraction"] = prosDf["wDuration"] / sum(prosDf["wDuration"])
        prosDf = prosDf[prosDf["speakingFraction"] >= FRAC_CUTOFF] 
        
        nSpeakers = len(prosDf)
        spCountList.append(nSpeakers)

    else: 
        spCountList.append(None)

sampDf["speakerCount"] = spCountList

# %%
sampDf = sampDf.dropna(subset=["speakerCount"])

#write this to a file so that it's easy to work with 
sampDf.to_json("/shared/3/projects/benlitterer/podcastData/network/businessSpNum/60000samp.jsonl", orient="records", lines=True)

# %%
#check whether it is typically the host or the guest that mentions racial justice 
#I have a hypothesis that guests were brought on to discuss this topic 


