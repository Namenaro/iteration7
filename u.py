from utils import *

class U_slider:
    def __init__(self, du, lead, d_left, d_right, patch_len):
        self.du=du
        self.lead=lead
        self.d_left = d_left
        self.d_right = d_right
        self.patch_len = patch_len

    def do(self, json_node, current_x):
        dxs=[]
        patches = []

        signal = get_lead_signal(json_node, self.lead)
        for dx in range(-self.d_left, self.d_right):
            center_point = current_x+dx+self.du
            patch = cut_patch(center_point, self.patch_len, signal)
            if patch is not None:
                dxs.append(dx)
                patches.append(patch)
        return dxs, patches
