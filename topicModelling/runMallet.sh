BASE_PATH="/shared/3/projects/benlitterer/podcastData/topicModelling" 

#topic model descriptions, then beginnings of transcripts 
#/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/podDescriptions.mallet \
#      --num-topics 100 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/100/descriptions/topic-state.gz --output-doc-topics $BASE_PATH/100/descriptions/doc_topics.txt --output-topic-keys $BASE_PATH/100/descriptions/topic_keys.txt

#/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/transcriptStarts.mallet \
#      --num-topics 100 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/100/transcripts/topic-state.gz --output-doc-topics $BASE_PATH/100/transcripts/doc_topics.txt --output-topic-keys $BASE_PATH/100/transcripts/topic_keys.txt

#/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/podDescriptions.mallet \
#      --num-topics 40 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/40/descriptions/topic-state.gz --output-doc-topics $BASE_PATH/40/descriptions/doc_topics.txt --output-topic-keys $BASE_PATH/40/descriptions/topic_keys.txt

#/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/transcriptStarts.mallet \
#      --num-topics 40 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/40/transcripts/topic-state.gz --output-doc-topics $BASE_PATH/40/transcripts/doc_topics.txt --output-topic-keys $BASE_PATH/40/transcripts/topic_keys.txt

/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/podDescriptions.mallet \
      --num-topics 200 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/200/descriptions/topic-state.gz --output-doc-topics $BASE_PATH/200/descriptions/doc_topics.txt --output-topic-keys $BASE_PATH/200/descriptions/topic_keys.txt

/shared/0/resources/mallet/mallet-2.0.8/bin/mallet train-topics --input $BASE_PATH/transcriptStarts.mallet \
      --num-topics 200 --num-threads 50 --optimize-interval 10 --output-state $BASE_PATH/200/transcripts/topic-state.gz --output-doc-topics $BASE_PATH/200/transcripts/doc_topics.txt --output-topic-keys $BASE_PATH/200/transcripts/topic_keys.txt