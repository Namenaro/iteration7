from numpy import linalg as LA
import numpy as np
import copy
import matplotlib.pyplot as plt

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


class DeviceB:
    def __init__(self, patches):
        self.patch_len = len(patches[0])
        self.center = np.mean(patches, axis=0)
        self.top = copy.deepcopy(patches[0])
        self.bottom = copy.deepcopy(patches[0])
        for i in range(len(self.top)):
            for x in patches:
                if x[i] < self.bottom[i]:
                    self.bottom[i] = x[i]
                if x[i] > self.top[i]:
                    self.top[i] = x[i]

    def get_level_and_value_of_activation(self, signal, center_point):
        start = center_point - int(self.patch_len / 2)
        end = start + self.patch_len
        if start <= 0 or end >= len(signal):
            return None, None
        patch = signal[start:end]

        for i in range(self.patch_len):
            if patch[i] >= self.top[i] or patch[i]<=self.bottom[i]:
                return 0,None
        value = self.center - patch
        return 1, value

    def show(self):
        plt.plot(self.center)
        plt.plot(self.top)
        plt.plot(self.bottom)
        plt.show()