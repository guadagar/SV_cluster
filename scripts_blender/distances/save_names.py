import bpy
import numpy as np
import pickle
import cellblender as cb

az_names = []
selected_objects = bpy.context.selected_objects
for obj in selected_objects:
    bpy.context.scene.objects.active = obj
    az = []
    az.append(obj.mcell.regions.region_list.keys())
    flat_az = [item for sublist in az for item in sublist]
    #az_names.append(flat_az)
    az_names.append([i for i in flat_az if i[3]=='c']) 

the_filename ='name_az_fh_new_test'    
with open(the_filename, 'wb') as f:#
    pickle.dump(az_names, f)

    
    