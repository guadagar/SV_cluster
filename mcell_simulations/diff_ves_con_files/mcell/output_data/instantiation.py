# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- instantiation ----

# ---- release sites ----

# ---- surface classes assignment ----

axon_cc.surface_class = const_conc
cloud_membrane.surface_class = surf
# ---- compartments assignment ----

di_ves_i = m.ReleaseSite(
    name = 'di_ves_i',
    complex = m.Complex('ves_in'),
    region = cloud,
    number_to_release = 600
)

di_ves_o = m.ReleaseSite(
    name = 'di_ves_o',
    complex = m.Complex('ves_out'),
    region = axon - cloud,
    number_to_release = 10
)

# ---- create instantiation object and add components ----

instantiation = m.Instantiation()
instantiation.add_geometry_object(cloud)
instantiation.add_geometry_object(axon)
instantiation.add_geometry_object(mito)
instantiation.add_release_site(di_ves_i)
instantiation.add_release_site(di_ves_o)

# load seed species information from bngl file
instantiation.load_bngl_compartments_and_seed_species(os.path.join(MODEL_PATH, 'model.bngl'), None, shared.parameter_overrides)

