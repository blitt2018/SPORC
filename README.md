Welcome to the github repository for our analysis of the podcast ecosystem using SPoRC: the Structured Podcast Research Corpus! 

You can access our data [here](https://huggingface.co/datasets/blitt/SPoRC), our data processing pipeline [here](https://github.com/blitt2018/SPoRC_data), and our publication [here](https://arxiv.org/abs/2411.07892).

If you make use of our data analysis or processing pipeline, please cite: 

```
@misc{litterer2024mappingpodcastecosystemstructured,
      title={Mapping the Podcast Ecosystem with the Structured Podcast Research Corpus}, 
      author={Benjamin Litterer and David Jurgens and Dallas Card},
      year={2024},
      eprint={2411.07892},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.07892}, 
}
```


Our paper analyzes podcasts from the perspective of content, structure, and responsiveness. In doing so we describe the quantity and diversity of podcast topics, the social network of guests who occur on multiple podcasts, and the temporal trend and magnitude of content related to George Floyd in May-June of 2020. 

## Content: 
<p align="center">
  <img src="/figures/topicProjections.png?raw=true" width=80% height=80%>
</p>

To analyze podcast content, we run a topic model on the first 1,000 words of all episodes. We then project the topic vectors for each episode into a two-dimensional space using t-SNE. Our topic modelling code is found in [topicModelling](/topicModelling) and code to produce our figure can be in [contentNetwork](/contentNetwork). 


## Structure
<p align="center">
<img src="/figures/guestNetwork.png?raw=true" width=50% height=50%>
</p>

Our subsequent analysis considers the social network within the podcast ecosystem. To produce this network, we leverage inferred guest labels to identify instances where the same guest occurs on multiple podcasts -- avoiding common names that lead to high false positives. Code to produce this network is found in [hostGuestNetwork](/hostGuestNetwork), and code to infer host and guest labels is in our seperate [data repository](https://github.com/blitt2018/SPoRC_data).

## Responsiveness
<p align="center">
<img src="/figures/2panelFloydSummary.jpg?raw=true" width=75% height=75%>
</p>

The third study in our work investigates the temporal response of the podcast ecosystem to the murder of George Floyd. This analysis uses the six topics from our topic model that relate to racial justice, as well as the proportion of episodes mentioning George Floyd's name. Our code for this analysis can be found in [floydAnalysis](/floydAnalysis). 
