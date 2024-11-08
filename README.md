Welcome to the github repository for our analysis of the podcast ecosystem using SPoRC: the Structured Podcast Research Corpus! 

You can access our data [here](https://huggingface.co/datasets/blitt/SPoRC), our data processing pipeline [here](https://github.com/blitt2018/SPoRC_data), and our publication [here](FILL_IN).

Our paper analyzes podcasts from the perspective of content, structure, and responsiveness. In doing so we describe the quantity and diversity of podcast topics, the social network of guests who occur on multiple podcasts, and the temporal trend and magnitude of content related to George Floyd in May-June of 2020. 

## Content: 
![Projection of podcast topics colored by category](/figures/topicProjections.png?raw=true)

To analyze podcast content, we run a topic model on the first 1,000 words of all episodes. We then project the topic vectors for each episode into a two-dimensional space using t-SNE. Our topic modelling code is found in [topicModelling](/topicModelling) and code to produce our figure can be in [contentNetwork](/contentNetwork). 


## Structure
<img src="/figures/guestNetwork.png?raw=true" width=35% height=35%>

Our subsequent analysis considers the social network within the podcast ecosystem. To produce this network, we leverage inferred guest labels to identify instances where the same guest occurs on multiple podcasts -- avoiding common names that lead to high false positives. Code to produce this network is found in [hostGuestNetwork](/hostGuestNetwork), and code to infer host and guest labels is in our seperate [data repository](https://github.com/blitt2018/SPoRC_data).

## Responsiveness
<img src="/figures/2panelFloydSummary.jpg?raw=true" width=75% height=75%>

The third study in our work investigates the temporal response of the podcast ecosystem to the murder of George Floyd. This analysis uses the six topics from our topic model that relate to racial justice, as well as the proportion of episodes mentioning George Floyd's name. Our code for this analysis can be found in [floydAnalysis](/floydAnalysis). 
