import numpy as np 
import matplotlib.pyplot as plt
from scipy.io import wavfile


class ToneGenerator:

	sr = 44100

	def __init__(self):
		self.freq = None
		self.length = None
		self.signal = None


	def render(self, length, freq, shape):
		self.length = length
		self.freq = freq
		self.shape = shape

		self.s = np.arange(0, self.length, 1.0/ToneGenerator.sr)
		x = np.pi * 2 * self.freq * self.s

		if(shape == "sin"):
			self.signal = np.sin(x)
		elif(shape == "triangle"):
			self.signal = np.abs((x / np.pi - 0.5) % 2 - 1) * 2 - 1
		elif(shape == "square"):
			self.signal = np.where(x / np.pi % 2 > 1, -1, 1)
		elif(shape == "sawtooth"):
			self.signal = -((x / np.pi) % 2) + 1
		else:
			self.signal = np.random.random(int(self.length * ToneGenerator.sr)) * 2.0 - 1.0 
		return self.signal

	def plot(self):
		plt.plot(self.s, self.signal)
		plt.show()

	@staticmethod
	def write_to_file(signal, name = "file.wav"):
		signal*= 32767
		signal = np.int16(signal)
		wavfile.write(name, ToneGenerator.sr, signal)

	def normalize(self, data):
		min_v = min(data)
		max_v = max(data)
		offset = min_v + max_v
		data = data + (offset/2)
		data = np.array([((x - min_v) / (max_v - min_v)) for x in data]) * 2.0 - 1
		return data * ((max_v / min_v) * -1)


if __name__ == "__main__":
	tone = ToneGenerator()
	#print(tone.render(3.0, 234, "sawtooth"))

	frequencies = [200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700]
	mellody = []
	for i in range(len(frequencies)):
		mellody += list(tone.render(0.5, frequencies[i], "sin"))
	ToneGenerator.write_to_file(np.array(mellody))
