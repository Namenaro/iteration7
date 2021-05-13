from utils import *
from deviceA import DeviceR, DeviceA
import matplotlib.pyplot as plt
from applyA import applyA_to_json



def visualise_device_no_inhibition(device, json_data, lead, threshold):
    num_plots = len(json_data.keys())
    if num_plots>10:
        num_plots=10
    fig, axs = plt.subplots(num_plots, sharey=True, sharex=True)
    fig.suptitle('device visualisation')
    i=0
    for patient_id in json_data.keys():
        ecg_json = json_data[patient_id]
        signal = get_lead_signal(ecg_json, lead)
        axs[i].plot(signal)

        center_coords, activation_levels, _ = apply_device_to_lead(signal, device, threshold)
        axs[i].scatter(center_coords, activation_levels, alpha=0.5, c='red')
        i=i+1
        if i == num_plots:
            break

    plt.show()

def visualise_device_lateral_inhibition(device, json_data, lead, threshold, lateral_inh_vicinity):

    num_plots = len(json_data.keys())
    if num_plots > 10:
        num_plots = 10
    fig, axs = plt.subplots(num_plots, sharey=True, sharex=True)
    fig.suptitle('device visualisation')
    i = 0
    for patient_id in json_data.keys():
        ecg_json = json_data[patient_id]
        signal = get_lead_signal(ecg_json, lead)
        axs[i].plot(signal)
        center_coords, activation_levels, activation_values = applyA_to_json \
            (ecg_json, lead, device, threshold, lateral_inh_vicinity)
        if len(center_coords)>0:
            axs[i].scatter(center_coords, activation_levels, alpha=0.5, c='red')
        i = i + 1
        if i == num_plots:
            break

    plt.show()