import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay


'''this script calculates the delaunay mehs for a group of vertices. For the veritices connected to each, I compute
the distance, and calculate the average
GCG
11.30.23
'''
the_filename = 'fp_new_ves_nr'
d = pickle.load(open(the_filename,'rb')) #number of vesicles in LTP


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
        
        the_file = '../dis_ves_cc/fp/'+obj.name
        dis_cc = pickle.load(open(the_file,'rb')) #dis_cc[0i,0] dis cc for each vesicle
        print(np.shape(dis_cc))
        dt = np.sum(dis_cc) 
        prob = np.zeros((n))
        for i in range(n):
            prob[i] = prob[i] = (1 - dis_cc[i]/dt)/(n-1)
            #print(prob[i])
        if obj_name[:-5] in d:
           
            nr_ves_ltp = np.round(d[obj_name[:-5]],decimals =0)
            if (n<nr_ves_ltp):
                print(n, nr_ves_ltp,obj_name[:-5],'less_than_ltp')
                nr_ves_ltp = n
                
            nn = np.random.choice(n,int(nr_ves_ltp),replace=False, p = prob)
            

            vertices =[]
            for i in nn:
                vertices.append((obj.data.vertices[i].co[0],obj.data.vertices[i].co[1],obj.data.vertices[i].co[2]))

            edges = []
            mymesh = bpy.data.meshes.new(obj_name+'_ltp')
            myobject = bpy.data.objects.new(obj_name+'_ltp',mymesh)
            bpy.context.scene.objects.link(myobject)
            mymesh.from_pydata(vertices,edges,[])
            mymesh.update()
        else:
            print('ssvr is not in file')
