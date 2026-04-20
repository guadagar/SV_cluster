# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *
from subsystem import *
from geometry import *
MODEL_PATH = os.path.dirname(os.path.abspath(__file__))


# ---- observables ----

# ---- declaration of rxn rules defined in BNGL and used in counts ----

cterm_count_ves_in_species_cloud = m.CountTerm(
    species_pattern = m.Complex('ves_in'),
    region = cloud
)

count_ves_in_cloud = m.Count(
    name = 'ves_in_cloud',
    expression = cterm_count_ves_in_species_cloud,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/ves_in_cloud.dat'
)

cterm_count_ves_out_species_axon = m.CountTerm(
    species_pattern = m.Complex('ves_out'),
    region = axon
)

count_ves_out_axon = m.Count(
    name = 'ves_out_axon',
    expression = cterm_count_ves_out_species_axon,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/ves_out_axon.dat'
)

cterm_count_ves_out_species_cloud = m.CountTerm(
    species_pattern = m.Complex('ves_out'),
    region = cloud
)

count_ves_out_cloud = m.Count(
    name = 'ves_out_cloud',
    expression = cterm_count_ves_out_species_cloud,
    file_name = './react_data/seed_' + str(SEED).zfill(5) + '/ves_out_cloud.dat'
)

# ---- create observables object and add components ----

observables = m.Observables()
observables.add_count(count_ves_in_cloud)
observables.add_count(count_ves_out_axon)
observables.add_count(count_ves_out_cloud)
