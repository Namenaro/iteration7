from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score

import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np

def make_cluster_analisys(patches):
    n_clusters=12
    clusterer = KMeans(n_clusters=n_clusters)
    labels = clusterer.fit_predict(patches)
    best_cluster_index = make_silhouette(patches, labels, n_clusters)
    ideal = clusterer.cluster_centers_[best_cluster_index]
    plt.plot(ideal)
    plt.show()


def make_silhouette(patches, labels, n_clusters):
    silhouette_avg = silhouette_score(patches, labels)
    print("The average silhouette_score is :" + str(silhouette_avg))

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(patches, labels)
    y_lower =10
    cluster_silhu_means = []
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to
        # cluster i, and sort them
        ith_cluster_silhouette_values = \
            sample_silhouette_values[labels == i]
        cluster_silhu_means.append(ith_cluster_silhouette_values.mean())
        ith_cluster_silhouette_values.sort()
        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        color = cm.nipy_spectral(float(i) / n_clusters)
        plt.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster numbers at the middle
        plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10  # 10 for the 0 samples
        # The vertical line for average silhouette score of all the values
        plt.axvline(x=silhouette_avg, color="red", linestyle="--")
    print("clusters silh means max:")
    print (max(cluster_silhu_means))
    best_i = cluster_silhu_means.index(max(cluster_silhu_means))
    print("best cluster is " + str(best_i))
    plt.show()
    return best_i

