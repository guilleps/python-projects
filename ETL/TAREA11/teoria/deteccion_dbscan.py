import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("TAREA11/data/mall_customers.csv")

x = data.loc[:, ['Annual Income (k$)','Spending Score (1-100)']].values

from sklearn.cluster import DBSCAN

dbscan = DBSCAN(eps = 8, min_samples = 4).fit(x)
labels = dbscan.labels_
plt.scatter(x[:, 0], x[:,1], c = labels, cmap= "plasma")
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()