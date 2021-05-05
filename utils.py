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