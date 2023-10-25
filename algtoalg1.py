#amplitude modulation
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

    def AM(self):
        plt.subplot(1, 3, 1)
        plt.plot(self.carrier_x, self.carrier_y)

        for i in range(len(self.signal_x)):
            self.carrier_y[i] *= self.signal_y[i]
        
        plt.title("--Signal Wave--")
        plt.subplot(1, 3, 2)
        plt.plot(self.signal_x, self.signal_y)
        plt.title("--Carrier Wave--")
        plt.subplot(1, 3, 3)
        plt.plot(self.carrier_x, self.carrier_y)
        plt.title("---Amplitude Modulation---")
        print("--Signal after Modulation--")
        plt.show()

a2a = Analog2Analog(signal_freq=1, signal_time=4)

a2a.AM()