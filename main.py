from deviceA_from_delination import make_deviceA2_from_json, make_deviceA_from_json
from visualise_deviceA import *
from get_dataset import *

def make_initial_deviceA():
    json_data = load_from_file(get_path_to_json_7_healthy())
    complex_name = "qrs"
    point_in_triplet=1
    lead = "i"
    patch_len = 5
    deviceA = make_deviceA2_from_json(complex_name, point_in_triplet, json_data, patch_len, lead)
    return deviceA

def visualise_device_raw(device):
    lead = "i"
    threshold =0.7
    json_data = load_from_file(get_path_to_200())
    visualise_device_no_inhibition(device, json_data, lead, threshold)

def visualise_device_lat_inh(device):
    lead = "i"
    threshold = 0.7
    lateral_inh_vicinity = 15
    json_data = load_from_file(get_path_to_200())
    visualise_device_lateral_inhibition(device, json_data, lead, threshold, lateral_inh_vicinity)

deviceA = make_initial_deviceA()
visualise_device_raw(deviceA)
visualise_device_lat_inh(deviceA)