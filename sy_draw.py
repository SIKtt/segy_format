import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def trace_show_all(z):
	fig = plt.figure()
	ax = fig.add_subplot(111, projection='3d')
	X = np.arange(0, len(z), 1)
	Y = np.arange(0, len(z[0]), 1)
	X1, Y1 = np.meshgrid(X, Y)
	Z = np.array(z)
	ax.plot_surface(X1, Y1, Z, cmap='bwr')
	ax.view_init(90,90)
	plt.show()

def trace_show_single(z, i):
	fig = plt.figure()
	plt.plot(z[i])
	ax.view_init(90,90)
	plt.show()