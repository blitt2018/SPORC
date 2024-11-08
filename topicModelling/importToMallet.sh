BASE_PATH="/shared/3/projects/benlitterer/podcastData/topicModelling" 

#import transcript starts and pod descriptions into mallet format 
/shared/0/resources/mallet/mallet-2.0.8/bin/mallet import-file --input $BASE_PATH/transcriptStarts.txt --keep-sequence --remove-stopwords TRUE --output $BASE_PATH/transcriptStarts.mallet
/shared/0/resources/mallet/mallet-2.0.8/bin/mallet import-file --input $BASE_PATH/podDescriptions.txt --keep-sequence --remove-stopwords TRUE --output $BASE_PATH/podDescriptions.mallet

