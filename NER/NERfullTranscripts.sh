BASE_PATH=/home/blitt/projects/podcasts/analysis/NER
DATASET_PATH=/shared/3/projects/benlitterer/podcastData/processed/mayJune/mayJuneMetaTranscripts.jsonl
NER_COL="transcript"
TEMP_STEM=/shared/3/projects/benlitterer/podcastData/NER/transcriptSplits/tempSplit
TEMP_PATH=/shared/3/projects/benlitterer/podcastData/NER/transcriptSplits/
OUT_PATH=/shared/3/projects/benlitterer/podcastData/NER/transcripts/mayJuneNEs.jsonl

#split up the files
python3 $BASE_PATH/splitForNER.py $DATASET_PATH $NER_COL $TEMP_STEM 20 "json"

#run NER on each file
ls $TEMP_PATH | parallel python3 $BASE_PATH/NER.py $TEMP_PATH/{} $NER_COL $TEMP_PATH/{.}NEs{\#}.jsonl 0

#merge output files back into one csv!
cat $TEMP_PATH/* > $OUT_PATH

#clean up after ourselves!
rm $TEMP_PATH/* 
