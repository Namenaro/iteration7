from numpy import linalg as LA

class DeviceA:
    def __init__(self, center, radius):
        self.center = center
        self.patch_len = len(center)
        self.radius = radius

    def get_level_and_value_of_activation(self, signal, center_point):
        start = center_point - int(self.patch_len / 2)
        end = start + self.patch_len
        if start <= 0 or end >= len(signal):
            return None,None
        patch = signal[start:end]
        value = self.center - patch
        dist = LA.norm(value)
        if dist > self.radius:
            return 0, None
        level = dist/self.radius
        return level, value


class DeviceA2:
    def __init__(self, bottom, top, center):
        self.top=top
        self.patch_len = len(top)
        self.bottom=bottom
        self.center = center

    def get_level_and_value_of_activation(self, signal, center_point):
        start = center_point - int(self.patch_len / 2)
        end = start + self.patch_len
        if start <= 0 or end >= len(signal):
            return None, None
        patch = signal[start:end]

        for i in range(self.patch_len):
            if patch[i]>=self.top[i] or patch[i]<=self.bottom[i]:
                return 0,None
        value = self.center - patch
        return 1, value




