import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#全道绘图_垂向 work well
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

#全道绘图_剖面
def trace_show_all_surf(z):
	fig = plt.figure()
	Z = np.array(z)
	plt.imshow(z, cmap='bwr')
	plt.show()
	
#单道绘图 work well 
def trace_show_single(z, i):
    fig = plt.figure()
    xax = np.arange(0, len(z[0]), 1)
    plt.plot(z[i], color = 'black')
    ax = plt.gca()
    ax.fill_between(xax, z[i], facecolor="black")
    # ax.view_init(90,90)
    plt.show()


#并行绘图_subplot方式 waiting pass
def trace_show_all_sub(z, tt, ifshow):
    fig = plt.figure()
    if tt > len(z):
        tt = len(z)
    print("trace in fig.")
    print(tt)
    for i in range(tt):
        j = i + 1
        plt.subplot(tt, 1, j)
        ax = plt.gca()
        plt.plot(z[i], color = 'lightgray')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.spines['left'].set_color('none')
        ax.spines['bottom'].set_color('none')
        plt.xticks([])
        plt.yticks([])
    plt.grid()
    if ifshow == 0:
        plt.show()
    else:
        plt.savefig(ifshow)
        plt.close()

#并行绘图_axes 方式 work well
def trace_show_all_axes(z, tt, ifshow):
	if tt > len(z):
		tt = len(z)
	print("trace in fig.")
	print(tt)
	fig = plt.figure()
	xax = np.arange(0, len(z[0]), 1)
	for i in range(tt):
		j = i + 1
		l = 1/tt
		axsize = [0, 1-i*l, 1, l]
		a = plt.axes(axsize)
		plt.plot(xax, z[i], linewidth = '1', color = 'gray')
		ax = plt.gca()
		ax.fill_between(xax, z[i], facecolor="black")
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.spines['left'].set_color('none')
		ax.spines['bottom'].set_color('none')
		plt.xticks([])
		plt.yticks([])
	plt.grid()
	if ifshow == 0:
		plt.show()
	else:
		plt.savefig(ifshow)
		plt.close()
	return fig

