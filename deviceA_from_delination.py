import  numpy as np
from numpy import linalg as LA

def get_triplets(patient, component, lead_name='i'):
    return patient['Leads'][lead_name]['DelineationDoc'][component]

def get_lead_signal(ecg, lead_name):
    return ecg['Leads'][lead_name]['Signal']

def cut_patch(center_coord, patch_len, signal):
    start = center_coord - int(patch_len / 2)
    end = start + patch_len
    if start >= 0 and end < len(signal):
        return signal[start:end]
    return None

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

    for x in X:
        dist = LA.norm(center-x)

