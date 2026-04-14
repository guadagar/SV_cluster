import bpy
import numpy as np
import pickle
from scipy.spatial import Delaunay, Voronoi,ConvexHull
import re

'''This script generates the voronoi cells for each SV cluster. The closed voronoi cells are considered, the intersection with the convex-hull (intersected with the mito & the axon) is performed. The meshes are also triangulated to calculate the volumes. This script requieres the convex hull for each SV cluster.
GCG
12.13.23
'''

objs = []
for i in bpy.context.selected_objects:
    objs.append(i)

bpy.ops.object.select_all(action = 'TOGGLE')

for obj in objs:
    n = len(obj.data.vertices)
    points = np.zeros((n,3))
    obj_name = obj.name

    for i in range(0,n):
        points[i,0] = obj.data.vertices[i].co[0]
        points[i,1] = obj.data.vertices[i].co[1]
        points[i,2] = obj.data.vertices[i].co[2]
    
    verts = []
    
    for i in range(n):
        verts.append((points[i,0],points[i,1],points[i,2]))

    #calculate voronoi cells of the vertices
    v = Voronoi(verts)
    vol_vor = np.zeros((len(v.point_region)))
    n_vor = 0
    f = open(obj.name +'.txt','w') # In this file I write the volume of all the voronoi cells (without intersections)

    for i, reg_num in enumerate(v.point_region):
        indices = v.regions[reg_num] #vertices of the region reg_num
        ve = v.vertices[indices]
        ve_vor = []
      
        for s in ve:
            ve_vor.append((s[0],s[1],s[2])) #the points forming one given voronoi vol

        if -1 in indices: # some regions can be opened
            gr_zero = np.where(np.array(indices) >= 0)
            continue
        else:
            n_vor =+ 1
        #    hull = ConvexHull(v.vertices[indices]) #for the region, reg_num, compute convex hull of the vornoi cell
            vol_vor[i] = ConvexHull(ve).volume

            f.write(str(i))
            f.write('\t')
            f.write(str(vol_vor[i]))
            f.write('\n')

            mymesh = bpy.data.meshes.new(obj_name +str('_vor_')+str(i))
            myobject = bpy.data.objects.new(obj_name +str('_vor_')+str(i),mymesh)
            mymesh.from_pydata(ve_vor,[],[])
            mymesh.update()
            bpy.context.scene.objects.link(myobject)

            #convex-hull vertices
            bpy.context.scene.objects.active = myobject
            myobject.select = True
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.convex_hull()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()

            #boolean vornoi cell with convex-hull vertices
            #bpy.context.scene.objects.active = myobject
            #myobject.select = True
            bpy.ops.object.modifier_add(type='BOOLEAN')
            bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[obj_name +str('_vert_hull')]
            bpy.context.object.modifiers["Boolean"].solver = 'CARVE'
            bpy.ops.object.modifier_apply(apply_as = 'DATA', modifier = 'Boolean')

            #triangulate the meshe to calculate vol
            bpy.context.scene.objects.active = myobject
            myobject.select = True
            bpy.ops.object.editmode_toggle()
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.mesh.quads_convert_to_tris(quad_method='BEAUTY',ngon_method='BEAUTY')
            bpy.ops.mesh.select_all(action='TOGGLE')
            bpy.ops.object.editmode_toggle()

    #Comment these lines if you want to generate the voronoi cells (as objects in Blender), if not they will be       deleted after each volume is computed

    #select all the voronoi volumes
    objetos = bpy.context.scene.objects
    my_pat = re.compile('.*_vor_')
    my_objetos = [obj for obj in objetos if my_pat.match(obj.name)!=None]
    for i in my_objetos:
        i.select=  True

    #compute & save the values
    bpy.ops.mcell.gen_meshalyzer_report()
    bpy.ops.object.select_all(action='TOGGLE')
    text_ref = bpy.data.texts['mesh_analysis.txt']
    destination = './' + obj_name +'_vor_vol.txt'
    with open(destination, 'w') as outfile:
        outfile.write(text_ref.as_string())
    foo = bpy.data.texts['mesh_analysis.txt']
    bpy.data.texts.remove(foo)

    #compute & delete the objects
    for i in my_objetos:
        i.select=  True
    bpy.ops.object.delete(use_global=False)
   
    f.close()
