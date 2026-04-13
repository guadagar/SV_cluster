
import numpy as np
from scipy.spatial import Voronoi,ConvexHull,Delaunay,voronoi_plot_2d
import matplotlib.pyplot as plt
import matplotlib as mpl

'''
This script generates fig 5 panel a
GCG
'''

params = {'axes.labelsize': 8,
           'axes.titlesize': 8,
          'legend.fontsize': 8,
           'xtick.labelsize': 8,
           'ytick.labelsize': 8,
            'figure.figsize': (0.9,0.9)}

mpl.rcParams.update(params)

#seed = 1234
#np.random.seed(seed)
#rng = np.random.default_rng()
#points = rng.random((100, 2))


#points = np.array([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0,8],[0, 9],
 #                  [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [1,8],[1, 9],
  #                 [2, 0], [2, 1], [2, 2],[2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [2,8],[2, 9],
   #                [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [3, 8], [3, 9],
    #               [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [4, 8], [4, 9],
    #                [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [5,8],[5, 9],
    #               [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [6,8],[6, 9],
    #               [7, 0], [7, 1], [7, 2],[7, 3], [7, 4], [7, 5], [7, 6], [7, 7], [7,8],[7, 9],
    #              [8, 0], [8, 1], [8, 2], [8, 3], [8, 4], [8, 5], [8, 6], [8, 7], [8, 8], [8, 9],
    #              [9, 0], [9, 1], [9, 2], [9, 3], [9, 4], [9, 5], [9, 6], [9, 7], [9, 8], [9, 9]])
points = np.zeros((100,2))

points[0:30,0] = np.random.normal(2,1,30)
points[0:30,1] = np.random.normal(2,1,30)

points[30:60,0] = np.random.normal(2,1,30)
points[30:60,1] = np.random.normal(7,1,30)

points[60:,0] = np.random.normal(8,1,40)
points[60:,1] = np.random.normal(8,1,40)

n = len(points)
print(n)
v = Voronoi(points)
vol_vor = np.zeros((len(v.point_region)))

ve = v.vertices
#pts = v.points #input valuess
p_reg = v.point_region


fig, ax = plt.subplots(figsize=(1.1,1.1))
fig.subplots_adjust(right=0.99, left = 0.01, bottom =0.01, top = 0.98)

voronoi_plot_2d(v, ax =ax,line_colors='red', show_vertices=False, point_size = 1)
#plt.scatter(points[:,0],points[:,1],marker ='.',s = 10)
plt.plot(points[:,0], points[:,1], 'o',color='limegreen', markersize=1)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.xaxis.set_ticks([])
ax.yaxis.set_ticks([])

#plt.savefig('../../../../../figures/v2/figures/new/final/final_final/another_final/uniform.png',dpi =600)

plt.show()
