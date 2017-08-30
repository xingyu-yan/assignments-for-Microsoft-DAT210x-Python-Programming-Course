import pandas as pd
import numpy as np
from scipy import misc
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt

# Look pretty...
# matplotlib.style.use('ggplot')
plt.style.use('ggplot')


# %%
# TODO: Start by creating a regular old, plain, "vanilla"
# python list. You can call it 'samples'.
#
# .. your code here .. 
samples = []
samples_colors = []
# %%
# TODO: Write a for-loop that iterates over the images in the
# Module4/Datasets/ALOI/32/ folder, appending each of them to
# your list. Each .PNG image should first be loaded into a
# temporary NDArray, just as shown in the Feature
# Representation reading.
#
# Optional: Resample the image down by a factor of two if you
# have a slower computer. You can also convert the image from
# 0-255  to  0.0-1.0  if you'd like, but that will have no
# effect on the algorithm's results.
#
# .. your code here .. 
for i in np.arange(0, 356, 5):
    img = misc.imread('Datasets/ALOI/32/32_r' + str(i) +'.png')
    samples.append((img).reshape(-1))
    samples_colors.append('b')

#
# TODO: Once you're done answering the first three questions,
# right before you converted your list to a dataframe, add in
# additional code which also appends to your list the images
# in the Module4/Datasets/ALOI/32_i directory. Re-run your
# assignment and answer the final question below.
#
# .. your code here .. 
for i in np.arange(110, 221, 10):
    img = misc.imread('Datasets/ALOI/32i/32_i' + str(i) +'.png')
    samples.append((img).reshape(-1)) 
    samples_colors.append('r')

#%%
# TODO: Convert the list to a dataframe
#
# .. your code here .. 
df = pd.DataFrame(samples)


#%%
# TODO: Implement Isomap here. Reduce the dataframe df down
# to three components, using K=6 for your neighborhood size
#
# .. your code here .. 
from sklearn import manifold
iso = manifold.Isomap(n_neighbors=6, n_components=3)
iso.fit(df)
#Isomap(eigen_solver='auto', max_iter=None, n_components=3, n_neighbors=4,
#    neighbors_algorithm='auto', path_method='auto', tol=0)

manifold_3D = iso.transform(df)

#%%
# TODO: Create a 2D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker. Graph the first two
# isomap components
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_title('2D Components from Isomap of vanilla')
ax.set_xlabel('X')
ax.set_ylabel('Y')
#ax.scatter(manifold_3D[:,0], manifold_3D[:,1], c='red', marker='.', alpha=0.75)
ax.scatter(manifold_3D[:,0], manifold_3D[:,1], c=samples_colors, marker='.', alpha=0.75)

#
# TODO: Create a 3D Scatter plot to graph your manifold. You
# can use either 'o' or '.' as your marker:
#
# .. your code here .. 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title('3D Components from Isomap of "vanilla"')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.scatter(manifold_3D[:,0], manifold_3D[:,1], manifold_3D[:,2], c=samples_colors, marker='.', alpha=0.75)

plt.show()
