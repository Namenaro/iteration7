from deviceA import DeviceA, DeviceA2
import copy

from utils import *

import  numpy as np
from numpy import linalg as LA



def get_all_patches_by_delin(comlex_name, point_in_triplet, json_data, patch_len, lead):
    X=[]
    for patient_id in json_data.keys():
        ecg_json = json_data[patient_id]
        triplets = get_triplets(ecg_json, comlex_name, lead)
        signal = get_lead_signal(ecg_json, lead)
        for triplet in triplets:
            center_coord = triplet[point_in_triplet]
            x = cut_patch(center_coord, patch_len, signal)
            if x is not None:
                X.append(x)
    print ("Found " + str(len(X))+" points")
    return np.array(X)

def get_center_and_radius_of_X(X):
    center = np.mean(X, axis=0)
    radius = None
    for x in X:
        dist = LA.norm(center-x)
        if radius is None:
            radius = dist
        else:
            if dist>radius:
                radius=dist
    return center, radius

def get_center_top_bottom_of_X(X):
    center = np.mean(X, axis=0)
    top = copy.deepcopy(X[0])
    bottom=copy.deepcopy(X[0])
    for i in range(len(top)):
        for x in X:
            if x[i]<bottom[i]:
                bottom[i] = x[i]
            if x[i]>top[i]:
                top[i]=x[i]
    return center, top, bottom

def make_deviceA_from_json(comlex_name, point_in_triplet, json_data, patch_len, lead):
    X = get_all_patches_by_delin(comlex_name, point_in_triplet, json_data, patch_len, lead)
    center, radius = get_center_and_radius_of_X(X)
    deviceA = DeviceA(center, radius)
    return deviceA

def make_deviceA2_from_json(comlex_name, point_in_triplet, json_data, patch_len, lead):
    X = get_all_patches_by_delin(comlex_name, point_in_triplet, json_data, patch_len, lead)
    center, top, bottom = get_center_top_bottom_of_X(X)
    deviceA2 = DeviceA2(bottom, top, center)
    return deviceA2