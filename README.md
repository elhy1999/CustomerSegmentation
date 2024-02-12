# Welcome to `CustomerSegmentation`!

This repository is a first attempt at understanding the applicability of data in the world of e-commerce and sales. 
Customer segmentation is not a novel concept in marketing analysis.
The segregation of customers makes the assumption that customers within each segment not only have similar spending habits, but also respond similarly to marketing strategies.
Thus, by segregating the consumer base, businesses can devise marketing strategies to cater to customers from specific segments by understanding their wants and/or needs.

The dataset I used for this mini project can be found from [this website on Kaggle](https://www.kaggle.com/datasets/yasserh/customer-segmentation-dataset).
It consists of online retail transactions data from Dec 2010 to Dec 2011.

As for the analysis done, you can find the data exploration and feature engineering steps under the `EDA.ipynb` notebook within the `notebooks/` directory.
I have taken ideas from marketing analysis found online which suggested three key features to describe each consumer's spending habits:

1. Recency: When was the last time the customer bought a product?
2. Frequency: How often does the customer purchase something?
3. Marketing value: How much $ has the customer spent?

After engineering the features, we segment the customers using a simple K-Means clustering model. You can find the code under the `kmeans.ipynb` notebook. 
![customer_clusters](https://github.com/elhy1999/CustomerSegmentation/blob/main/assets/clusters.png)

Lastly, some basic inference is conducted to describe the spending habits of customers from each segment/cluster within the `inference.ipynb` notebook.

Future steps could be taken to:

1. Understand the items bought by customers of specific segments to find out what they shop for in the store, perhaps by processing the text found within the `Descriptions` column describing the item bought.
2. Find out if spending habits are universal (i.e. if clusters of customers from different countries look similar to one another). If we find that customers from different regions of origins behave differently, then perhaps adjusting marketing strategies towards each region could be one way to go.
