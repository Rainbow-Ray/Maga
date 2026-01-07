import random
import numpy as np
import sklearn
from matplotlib import pyplot as plt
import matplotlib
from scipy.cluster.hierarchy import dendrogram
matplotlib.use('TkAgg')

def plot_dendrogram(model, **kwargs):
    # Create linkage matrix and then plot the dendrogram

    # create the counts of samples under each node
    counts = np.zeros(model.children_.shape[0])
    n_samples = len(model.labels_)
    for i, merge in enumerate(model.children_):
        current_count = 0
        for child_idx in merge:
            if child_idx < n_samples:
                current_count += 1  # leaf node
            else:
                current_count += counts[child_idx - n_samples]
        counts[i] = current_count

    linkage_matrix = np.column_stack(
        [model.children_, model.distances_, counts]
    ).astype(float)

    # Plot the corresponding dendrogram
    dendrogram(linkage_matrix, **kwargs)


data = [9, 2, 0, 3, 7, 6, 3, 5]
# for i in range(10):
#     data.append(random.randint(0, 10))

data = np.reshape(data, (-1, 1))
print(data)

n_samples = len(data)

agg = sklearn.cluster.AgglomerativeClustering(n_clusters=2, linkage="ward", compute_distances=True)
model = agg.fit(data)

print(model.n_leaves_)
print(model.children_)

print(model.distances_)
ch = model.children_


quuery = []
def get_both(q):
    r = q.pop()
    print(f"{r}")
    if r < n_samples:
        print("Конец")
        return q
    elif r >= n_samples:

        l = ch[r - n_samples][0]
        r = ch[r - n_samples][1]
        q.append(l)
        q.append(r)
        get_both(q)


for i in ch:
    l = i[0]
    r = i[1]
    quuery.append(r)
    quuery.append(l)

while len(quuery) > 0:
    get_both(quuery)


plot_dendrogram(model, truncate_mode="level", p=3)
plt.xlabel("Number of points in node (or index of point if no parenthesis).")
plt.show()
