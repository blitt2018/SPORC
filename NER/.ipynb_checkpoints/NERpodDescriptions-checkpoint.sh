BASE_PATH=/home/blitt/projects/podcasts/analysis/hostIdentification/NER
DATASET_PATH=/shared/3/projects/benlitterer/podcastData/processed/floydMonth/floydMonthEnSHORT.csv
NER_COL="podDescription"
TEMP_STEM=/shared/3/projects/benlitterer/podcastData/NER/descriptionSplits/tempSplit
TEMP_PATH=/shared/3/projects/benlitterer/podcastData/NER/descriptionSplits
OUT_PATH=/shared/3/projects/benlitterer/podcastData/NER/podDescriptions/floydMonthNEs.csv

#split up the files
python3 $BASE_PATH/splitForNER.py $DATASET_PATH $NER_COL $TEMP_STEM 20

#run NER on each file
ls $TEMP_PATH | parallel python3 NER.py $TEMP_PATH/{} $NER_COL $TEMP_PATH/{.}NEs{\#}.tsv 0

#merge output files back into one csv!
cat $TEMP_PATH/* > $OUT_PATH

#clean up after ourselves!
rm $TEMP_PATH/* 