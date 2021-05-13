from deviceA_from_delination import make_deviceA2_from_json, make_deviceA_from_json
from visualise_deviceA import *
from get_dataset import *
from Au import make_u_from_A_by_example, make_u_from_A
from u import U_slider, U_by_example
from u_result_cluster_analisys import make_cluster_analisys
from deviceA import DeviceB

def make_initial_deviceA():
    json_data = load_from_file(get_path_to_json_7_healthy())
    patient_num = 1

    json_data = {k: json_data[k] for k in list(json_data.keys())[0:patient_num]}


    complex_name = "qrs"
    point_in_triplet=1
    lead = "i"
    patch_len = 5
    deviceA = make_deviceA2_from_json(complex_name, point_in_triplet, json_data, patch_len, lead)
    return deviceA

def visualise_device_raw(device):
    lead = "i"
    threshold =0.7
    json_data = load_from_file(get_path_to_json_7_healthy())
    visualise_device_no_inhibition(device, json_data, lead, threshold)

def visualise_device_lat_inh(device):
    lead = "i"
    threshold = 0.7
    lateral_inh_vicinity = 15
    json_data = load_from_file(get_path_to_200())
    visualise_device_lateral_inhibition(device, json_data, lead, threshold, lateral_inh_vicinity)

def make_u_slider_from_A(A):
    u = U_slider(du=20,lead="i",d_left=5,d_right=5,patch_len=15)
    threshold = 0.7
    lateral_inh_vicinity = 15
    json_data = load_from_file(get_path_to_json_7_healthy())
    result_patches, result_dxs, patients_ids = make_u_from_A(json_data, A, u, threshold, lateral_inh_vicinity)
    print ("Au resulted in " + str(len(result_patches)))
    return result_patches, result_dxs, patients_ids

def make_u_by_exmaple_from_A(A):
    A_lead = "i"
    threshold = 0.7
    lateral_inh_vicinity = 15
    json_data = load_from_file(get_path_to_json_7_healthy())

    patient_num=0
    point_num = 0
    u_lead = "i"
    json_node = json_data[list(json_data.keys())[patient_num]]
    center_coords, _, _ = applyA_to_json(json_node, A_lead, A, threshold, lateral_inh_vicinity)
    if len(center_coords) == 0:
        print ("Au (by example) is empty")
        return None, None, None
    u = U_by_example(du=30, lead=u_lead, d_left=10, d_right=11, patch_len=15)
    u.init_example(json_node,  center_coords[point_num])
    result_patches, result_dxs, patients_ids = make_u_from_A_by_example(json_data, A, u, threshold, lateral_inh_vicinity)
    print("Au (by example) resulted in " + str(len(result_patches)))
    return result_patches, result_dxs, patients_ids

A = make_initial_deviceA()
A.show()
print ("gap A=" + str(A.get_mean_gap()))
#visualise_device_raw(deviceA)
#visualise_device_lat_inh(deviceA)
#result_patches, result_dxs, patients_ids = make_u_slider_from_A(deviceA)
#make_cluster_analisys(result_patches)

result_patches, result_dxs, patients_ids = make_u_by_exmaple_from_A(A)
#make_cluster_analisys(result_patches)

B = DeviceB(result_patches)
result_patches, result_dxs, patients_ids = make_u_by_exmaple_from_A(B)
print ("gap B=" + str(B.get_mean_gap()))
B.show()

