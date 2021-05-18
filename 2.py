from deviceA_from_delination import get_all_patches_by_delin
from get_dataset import *
from sklearn.decomposition import PCA
from sklearn import preprocessing
from sklearn.manifold import TSNE
from sklearn.cluster import AgglomerativeClustering
from scipy.stats import entropy
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch import nn
from scipy.ndimage import gaussian_filter1d

def split_y2_by_y1(Y1, Y2):
    result = []
    clusters1 = len(np.unique(Y1))
    for _ in range(clusters1):
        result.append([])
    for i in range(len(Y1)):
        result[Y1[i]].append(Y2[i])
    return result

def visualise_conditionality_of_clusters(Y1, Y2):
    n_bins = len(np.unique(Y2))
    y2_by_y1 = split_y2_by_y1(Y1, Y2)
    show_conditional_hists(y2_by_y1, n_bins)

def show_conditional_hists(y2_by_y1, n_bins):
    num_hists = len(y2_by_y1)
    fig, axs = plt.subplots(num_hists, sharey=True, sharex=True)
    fig.suptitle('conditional hists')
    for i in range(num_hists):
        axs[i].hist(y2_by_y1[i], bins=np.arange(n_bins+1)-0.5, histtype='bar')

    plt.show()

def getXY():
    comlex_name = "qrs"
    point_in_triplet = 1
    json_data = load_from_file(get_path_to_json_7_healthy())
    patch_len = 10
    lead1 = 'i'
    lead2 = 'ii'
    X = get_all_patches_by_delin(comlex_name, point_in_triplet, json_data, patch_len, lead1)
    Y = get_all_patches_by_delin(comlex_name, point_in_triplet, json_data, patch_len, lead2)
    return X, Y

def whitening(X):
    scaler = preprocessing.StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    return X_scaled, scaler.mean_, scaler.scale_

def dim_red(X):
    tsne = TSNE(n_components=2, random_state=0)
    projections = tsne.fit_transform(X)
    return projections

def cluster(X, n_clusters):
    clustering = AgglomerativeClustering(linkage='average', n_clusters=n_clusters)
    clustering.fit(X)
    return clustering.labels_

def downsample(X):
    m = nn.AvgPool1d(3, stride=2)
    y = m(torch.tensor([X])).numpy()
    return np.squeeze(y)

def downsample_gau(X):
    res = []
    for x in X:
        res.append(gaussian_filter1d(x, 3))
    return np.array(res)

X, Y = getXY()
X = downsample_gau(X)
X = downsample(X)
Y = downsample_gau(Y)
Y = downsample(Y)
X,_,_ = whitening(X)
Y,_,_ = whitening(Y)
X = dim_red(X)
Y = dim_red(Y)
Xc = cluster(X, 2)
Yc = cluster(Y, 5)

visualise_conditionality_of_clusters(Xc, Yc)


