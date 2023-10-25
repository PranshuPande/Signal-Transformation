#phase modulation
import numpy as np 
import matplotlib.pyplot as plt 

class GenSin:
    def __init__(self) -> None:
        pass

    def genSin(self, fq, t_sec):
        x = np.arange(0, t_sec, 0.001)
        y = np.sin(x*2*np.pi*fq)
        return x, y

class Analog2Analog:
    def __init__(self, signal_freq, signal_time) -> None:
        self.genSin = GenSin()
        self.signal_x, self.signal_y = self.genSin.genSin(fq = signal_freq, t_sec=signal_time)
        self.carrier_x, self.carrier_y = self.genSin.genSin(fq = 15, t_sec=signal_time)

    def PM(self):
        t = self.signal_x

        sig = self.signal_y

        fc = 10 
        k = 5
        phi = 2*np.pi*fc*t + k*sig
        sig_mod = np.sin(phi) 

        plt.title("---Phase Modulated Signal---")
        plt.plot(t, sig_mod)
        plt.plot(t, sig, c='r')

        plt.show()
        
a2a = Analog2Analog(signal_freq=1, signal_time=4)

a2a.PM()