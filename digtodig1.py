#Uni-polar-NRZ
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

    def unipolarNRZ(self):
        _gen = []
        x = []
        init_ = 0
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(0)
                _gen.append(0)
            else:
                _gen.append(1)
                _gen.append(1)
        print("Uni-polar-NRZ")
        print("---Graph---")

        plt.plot(x, _gen)
        plt.show()
data = str(input("enter your digital data : "))
d = DigitalToDigital(data)
d.unipolarNRZ()