#Polar RZ (Returning to Zero)
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
    def polarRZ(self):
        _gen = []
        x = []
        init_ = 0
        for i in self.data:
            x.append(init_)
            init_ += WIDTH//2
            x.append(init_)
            x.append(init_)
            init_ += WIDTH//2
            x.append(init_)
            if(i == '0'):
                _gen.append(-1)
                _gen.append(-1)
            else:
                _gen.append(1)
                _gen.append(1)
            _gen.append(0)
            _gen.append(0)
        
        print("--Polar RZ (Returning to Zero)--")
        print("---Graph---")

        plt.plot(x, _gen)
        plt.show()

data = str(input("Enter your digital data : "))
d = DigitalToDigital(data)
d.polarRZ()