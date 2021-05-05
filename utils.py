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