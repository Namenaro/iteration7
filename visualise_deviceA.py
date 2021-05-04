from deviceA_from_delination import get_lead_signal
from deviceA import DeviceA, DeviceA2
import matplotlib.pyplot as plt

def apply_device_to_lead(signal, device, threshold):
    center_coords = []
    activation_levels = []
    activation_values = []

    for center_coord in list(range(0, len(signal))):
        level, value = device.get_level_and_value_of_activation(signal, center_coord)
        if level is not None:
            if level>=threshold:
                center_coords.append(center_coord)
                activation_levels.append(level)
                activation_values.append(value)
    return center_coords, activation_levels, activation_values

def visualise_device_on_json_one_lead(device, json_data, lead, threshold):
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