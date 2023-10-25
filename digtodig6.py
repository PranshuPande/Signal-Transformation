#Bi-polar AMI (Alternate Mark Inversion)
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
    def bipolarAMI(self):
        _gen = []
        x = []
        init_ = 0
        _curr = 1
        for i in self.data:
            x.append(init_)
            init_ += WIDTH
            x.append(init_)
            if(i == '0'):
                _gen.append(0)
                _gen.append(0)
            else:
                _gen.append(_curr)
                _gen.append(_curr)
                _curr = invert(_curr)
        
        print("--Bi-polar AMI (Alternate Mark Inversion)--")
        print("---Graph---")

        plt.plot(x, _gen)
        plt.show()

data = str(input("Enter your digital data : "))
d = DigitalToDigital(data)
d.bipolarAMI()