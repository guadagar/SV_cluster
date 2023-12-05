import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay

'''this script calculates the delaunay mehs for a group of vertices. For the veritices connected to each, I compute
the distance, and calculate the average
GCG
11.30.22
'''

if bpy.context.selected_objects != []:
    for obj in bpy.context.selected_objects:
        #print(obj.name)
        n = len(obj.data.vertices)
        verts = np.zeros((n,3))
        obj_name = obj.name

        for i in range(0,n):
            verts[i,0] = obj.data.vertices[i].co[0]
            verts[i,1] = obj.data.vertices[i].co[1]
            verts[i,2] = obj.data.vertices[i].co[2]

        #euclidean distance
        def dist(x1,y1,z1,x2,y2,z2):
            d = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            return d

        cm_verts = np.zeros((3,1))
        cm_verts[0] = np.mean(verts[:,0])
        cm_verts[1] = np.mean(verts[:,1])
        cm_verts[2] = np.mean(verts[:,2])

        dis_i_cm = np.zeros(n)
        for i in range(0,n):
            dis_i_cm[i] = np.sqrt((verts[i,0] - cm_verts[0])**2 + (verts[i,1] - cm_verts[1])**2 + (verts[i,2]- cm_verts[2])**2)

        dma = np.zeros((n,n))

        for i in range(0,n):
            for j in range(0,n):
                dma[i,j] = dist(verts[i,0],verts[i,1],verts[i,2],verts[j,0],verts[j,1],verts[j,2])

        min_dist = np.zeros((n))
        for i in range(0,n):
            min_dist[i] = np.min((dma[i,np.nonzero(dma[i,:])]))
        
        dis = np.zeros((n,2)) # dis cm & NN dis
        dis[:,0] = dis_i_cm[:]
        dis[:,1] = min_dist[:]        

        the_filename = obj_name+str('_dis_cm')
        with open(the_filename, 'wb') as f:#
            pickle.dump(dis, f)

