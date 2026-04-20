# WARNING: This is an automatically generated file and will be overwritten
#          by CellBlender on the next model export.

import os
import shared
import mcell as m

from parameters import *

# ---- subsystem ----

MODEL_PATH = os.path.dirname(os.path.abspath(__file__))

const_conc = m.SurfaceClass(
    name = 'const_conc',
    type = m.SurfacePropertyType.CONCENTRATION_CLAMP,
    affected_complex_pattern = m.Complex('ves_out', orientation = m.Orientation.DOWN),
    concentration = 3.9e-8
)

surf = m.SurfaceClass(
    name = 'surf',
    type = m.SurfacePropertyType.REACTIVE
)

unnamed_reaction_rule_0 = m.ReactionRule(
    name = 'unnamed_reaction_rule_0',
    reactants = [ m.Complex('ves_in@IN', compartment_name = 'IN'), m.Complex('surf') ],
    products = [ m.Complex('ves_out@OUT', compartment_name = 'OUT') ],
    fwd_rate = f_rate
)

unnamed_reaction_rule_1 = m.ReactionRule(
    name = 'unnamed_reaction_rule_1',
    reactants = [ m.Complex('ves_out@OUT', compartment_name = 'OUT'), m.Complex('surf') ],
    products = [ m.Complex('ves_in@IN', compartment_name = 'IN') ],
    fwd_rate = f_rate
)

# ---- create subsystem object and add components ----

subsystem = m.Subsystem()
subsystem.add_surface_class(const_conc)
subsystem.add_surface_class(surf)
subsystem.add_reaction_rule(unnamed_reaction_rule_0)
subsystem.add_reaction_rule(unnamed_reaction_rule_1)

# load subsystem information from bngl file
subsystem.load_bngl_molecule_types_and_reaction_rules(os.path.join(MODEL_PATH, 'model.bngl'), shared.parameter_overrides)

# set additional information about species and molecule types that cannot be stored in BNGL,
# elementary molecule types are already in the subsystem after they were loaded from BNGL
def set_bngl_molecule_types_info(subsystem):
    ves_in = subsystem.find_elementary_molecule_type('ves_in')
    assert ves_in, "Elementary molecule type 'ves_in' was not found"
    ves_in.diffusion_constant_3d = 5e-10

    ves_out = subsystem.find_elementary_molecule_type('ves_out')
    assert ves_out, "Elementary molecule type 'ves_out' was not found"
    ves_out.diffusion_constant_3d = 1.95e-5

set_bngl_molecule_types_info(subsystem)
