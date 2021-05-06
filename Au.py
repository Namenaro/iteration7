from utils import *
from deviceA import *
from u import *
from applyA import applyA_to_json


def make_u_from_A(json_data, A, u, threshold, lateral_inh_vicinity):
    lead="i"
    result_dxs = []
    result_patches = []
    patients_ids = []
    num_A_points=0
    for patient_id in json_data.keys():
        json_node = json_data[patient_id]
        center_coords, _, _ = applyA_to_json \
            (json_node, lead, A, threshold, lateral_inh_vicinity)
        num_A_points=num_A_points+len(center_coords)
        for current_x in center_coords:
            dxs, patches = u.do(json_node, current_x)
            patients_ids = patients_ids + [patient_id] * len(dxs)
            result_dxs = result_dxs + dxs
            result_patches = result_patches + patches
    print("A triggered times: " + str(num_A_points))
    return result_patches, result_dxs, patients_ids

def make_u_from_A_by_example(json_data, A, u, threshold, lateral_inh_vicinity):
    lead = "i"
    result_dxs = []
    result_patches = []
    patients_ids = []
    num_A_points = 0
    for patient_id in json_data.keys():
        json_node = json_data[patient_id]
        center_coords, _, _ = applyA_to_json \
            (json_node, lead, A, threshold, lateral_inh_vicinity)
        num_A_points = num_A_points + len(center_coords)
        for current_x in center_coords:
            dx, patch = u.do(json_node, current_x)
            if dx is not None:
                patients_ids.append(patient_id)
                result_dxs.append(dx)
                result_patches.append(patch)
    print("A triggered times: " + str(num_A_points))
    return result_patches, result_dxs, patients_ids
