from utils import *



def applyA_to_json(json_node, lead, A, threshold, lateral_inh_vicinity):
    signal = get_lead_signal(json_node, lead)
    center_coords, activation_levels, activation_values = apply_device_to_lead(signal, A, threshold)
    if len(center_coords)> 0:
        return make_lateral_inhibition(center_coords, activation_levels, activation_values, lateral_inh_vicinity)
    return [], [], []

def make_lateral_inhibition(center_coords, activation_levels, activation_values, lateral_inh_vicinity):

    clouds = find_clouds(center_coords, lateral_inh_vicinity)
    indexes = clouds_to_points(clouds, activation_levels)

    center_coords_ = []
    activation_levels_ = []
    activation_values_ = []

    for i in indexes:
        center_coords_.append(center_coords[i])
        activation_levels_.append(activation_levels[i])
        activation_values_.append(activation_values[i])

    return center_coords_, activation_levels_, activation_values_

def find_clouds(centers, lateral_inh_vicinity):
    clouds = []
    clouds.append([0])
    for i in range(1, len(centers)):
        if abs(centers[i]-centers[i-1]) < lateral_inh_vicinity:
            clouds[-1].append(i)
        else:
            clouds.append([i])
    return clouds

def clouds_to_points(clouds_of_indexes, levels_of_activations):
    indexes = []
    for cloud in clouds_of_indexes:
        indexes.append(cloud_to_point(cloud,levels_of_activations))
    return indexes

def cloud_to_point(cloud, levels_of_activations):
    s=0
    for index in cloud:
        s=s+index*levels_of_activations[index]
    m = int(s/len(cloud))
    return m




