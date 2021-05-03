from numpy import linalg as LA

class DeviceA:
    def __init__(self, center, radius):
        self.center = center
        self.patch_len = len(center)
        self.radius = radius

    def get_level_and_value_of_activation(self, signal, point):
        if point<0 or point>len(signal)- self.patch_len -1:
            return None,None
        patch = signal[point:point+self.patch_len]
        value = self.center - patch
        dist = LA.norm(value)
        if dist > self.radius:
            return 0, None
        level = dist/self.radius
        return level, value









