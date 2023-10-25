#Amplitude Shifting key
#digital to analog
import numpy as np
import matplotlib.pyplot as plt

class Digital2Analog:
    def __init__(self, data) -> None:
        self.data = data 
        self.genCarr = GenCarrier()
    
    def ASK(self, baud_rate):

        carrier_time = len(self.data)/baud_rate
        _x, _y = self.genCarr.genCarr(freq=4, t_sec=carrier_time)
        
        _init = 0

        to_chg = int(len(_y)/(carrier_time*baud_rate))

        for i in self.data:
            if(i=='0'):
                for i in range(to_chg):
                    try:
                        _y[_init] = 0
                        _init += 1
                    except:
                        break
            else:
                _init += to_chg
        print("--Amplitude Shifting Key--")
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
d2a.ASK(baud_rate=2)