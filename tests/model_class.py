from blobmodel import Model, Blob
import numpy as np
import matplotlib.pyplot as plt

tmp = Model(Nx=100, Ny=50, Lx=10, Ly=10, dt=0.1, T=20, blob_shape='exp')

# blob = Blob(1, 'gauss', 1,1,1,1,1,5,5,0)

# x = np.linspace(0, 10, 100)
# y = np.linspace(0, 10, 50).reshape(-1, 1)
# t = np.linspace(0, 10, 10)

# xx, yy, tt = np.meshgrid(x, y, t)
# z = np.zeros(shape=(y.size, x.size, t.size))

# tmp = blob.discretize_blob(xx,yy,tt)
# print(tmp.shape)
# print(z.shape)
# plt.contourf(tmp[:,:,0])
# plt.show()


tmp.sample_blobs(num_blobs=100)

tmp.integrate()

#tmp.show_model(interval=100)