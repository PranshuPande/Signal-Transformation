#analog to digital signal conversion
import numpy as np
import matplotlib.pyplot as plt
SAMPLE_FREQ = 2
class GenSin:
    def __init__(self):
        pass
    
    def generate(self, freq, amp, t_sec):
        x = np.linspace(0, t_sec, 10000)
        y = amp*np.sin(2*np.pi*freq*x)
        return (x, y)
class Utils:
    def __init__(self) -> None:
        pass
    def plot(x, y):
        plt.plot(x, y)
        plt.grid(True, which='both')
        plt.show()

    def plot_scatter(x, y, a, b):
        plt.plot(x, y)
        plt.grid(True, which='both')
        plt.scatter(a, b, c='r')
        plt.show()
generator = GenSin()

class AnalogToDigital:
    def __init__(self, x, y, data_freq) -> None:
        self.x=x
        self.y=y
        self.data_freq = data_freq

    def sample(self, sample_freq, levels):
        sample_rate = 1/sample_freq
        sampled_time = np.arange(0, 2, sample_rate)
        samples = np.sin(2*np.pi*self.data_freq*sampled_time)

        max_amp = max(samples)
        min_amp = min(samples)

        delta = (max_amp - min_amp) / levels

        data = ""
        for i in samples:
            _ctr = 0
            _amp = min_amp
            while not((i>=_amp) and (i<=(_amp+delta))):
                _amp += delta 
                _ctr += 1
            
            data += bin(_ctr)[2:]+" "

        print("YOUR ANALOG SIGNAL DATA IS : ---> ")
        print("---Converted Digital Signal---")
        print(data)
        Utils.plot_scatter(self.x, self.y, sampled_time, samples)

x, y = generator.generate(freq=2, amp=1, t_sec=2)

a2d = AnalogToDigital(x, y, data_freq=2)
a2d.sample(sample_freq=5, levels=4)