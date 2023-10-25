#Frequency Shifting key
#digital to analog
import numpy as np
import matplotlib.pyplot as plt

class Digital2Analog:
    def __init__(self, data) -> None:
        self.data = data 
        self.genCarr = GenCarrier()
    def FSK(self, baud_rate, fc, delta_f):
        _x = []
        _y = []

        _time = 1/baud_rate
        _st = 0
        for i in self.data:
            if( i == '1'):
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc+delta_f), t_sec=_time, st=_st)
            else:
                tmp_x, tmp_y = self.genCarr.genCarr(freq=(fc-delta_f), t_sec=_time, st=_st)

            _x.extend(tmp_x)
            _y.extend(tmp_y)
            _st += _time
        print("--Frequency Shifting Key--")
        print("---Graph---")
        plt.plot(_x, _y)
        plt.grid(which='both')
        plt.show()

class GenCarrier:
    def __init__(self) -> None:
        pass

    def genCarr(self, freq, t_sec, st=0, phi=0):
        x = np.arange(st, st+t_sec, 0.001)
        y = np.sin(x*freq*2*np.pi + phi)
        return x ,y 

data = str(input("Enter your digital data : "))
d2a = Digital2Analog(data)
d2a.FSK(baud_rate=2, fc=10, delta_f=3)