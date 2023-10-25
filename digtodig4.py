#Bi-phase Manchester
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
    def biphaseManchester(self):
        _gen = []
        x_axis = []
        _init = 0
        for i in self.data:
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)
            x_axis.append(_init)
            _init += (WIDTH//2)
            x_axis.append(_init)

            if i == '0':
                _gen.append(-1)
                _gen.append(-1)
                _gen.append(1)
                _gen.append(1)
            else:
                _gen.append(1)
                _gen.append(1)
                _gen.append(-1)
                _gen.append(-1)

        print("--Bi-phase Manchester--)")
        print("---Graph---")
        plt.plot(x_axis, _gen)
        plt.show()
data = str(input("enter your digital data : "))
d = DigitalToDigital(data)
d.biphaseManchester()