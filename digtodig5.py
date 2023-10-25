#Bi-phase Differential Manchester
#digital to digital
import numpy as np
import matplotlib.pyplot as plt
WIDTH = 10
def invert(x):
    if x==1: 
        return -1
    return 1
class DigitalToDigital:
    def __init__(self, data):
        self.data = data
    def biphaseDifferentialManchester(self):
        _gen = []
        x_axis = []
        _init = 0
        _curr = 1
        for i in self.data:
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)

            if i == '0':
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
            else:
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
                _gen.append(_curr)
                _gen.append(_curr)
        print("--Bi-phase Differential Manchester--")
        print("---Graph---")
        plt.plot(x_axis, _gen)
        plt.show()

data = str(input("Enter your digital data : "))
d = DigitalToDigital(data)
d.biphaseDifferentialManchester()