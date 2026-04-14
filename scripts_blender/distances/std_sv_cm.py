import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay

'''this script calculates the standard deviation from the SVs to the center of the cluster. 
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

        sdt_dis_i = np.zeros(n)
        for i in range(0,n):
            sdt_dis_i[i] = (verts[i,0] - cm_verts[0])**2 + (verts[i,1] - cm_verts[1])**2 + (verts[i,2]- cm_verts[2])**2

        std_dis = np.sqrt(np.sum(sdt_dis_i[:])/n)

        cm_co_verts = []
        for i in range(n):
            cm_co_verts.append((cm_verts[0],cm_verts[1],cm_verts[2]))

        #creates an object with the cm
        cm_name = obj_name + str('_cm')
        mymesh = bpy.data.meshes.new(cm_name)
        myobject = bpy.data.objects.new(cm_name,mymesh)
        bpy.context.scene.objects.link(myobject)
        mymesh.from_pydata(cm_co_verts,[],[])
        mymesh.update()

        the_filename = './sd_dis/FH' + obj_name
        with open(the_filename, 'wb') as f:#
            pickle.dump(std_dis, f)
