# This file contains hooks to override default MCell4 model
# code behavior for models generated from CellBlender
import sys
import os
import shared
import mcell as m

#def custom_argparse_and_parameters():
     # When uncommented, this function is called to parse
    # custom commandline arguments.
    # It is executed before any of the automatically generated
    # parameter values are set so one can override the parameter
    # values here as well.
    # To override parameter values, add or overwrite an item in dictionary
    # shared.parameter_overrides, e.g. shared.parameter_overrides['SEED'] = 10

#    if len(sys.argv) != 5 or sys.argv[1] != '-seed':
#        sys.exit("Expected following arguments: -seed N name_cloud nr_ves")

    # overwrite value of seed defined in module parameters
#    shared.parameter_overrides['SEED'] = int(sys.argv[2])

    # and remember selected variant,
    # cannot use parameter_overrides because its values must be always floats
#    global name_cloud,nr_ves_in
#    name_cloud = sys.argv[3]
#    nr_ves_in = sys.argv[4]


#def custom_config(model):
    # When uncommented, this function is called to set custom
    # model configuration.
    # It is executed after basic parameter setup is done and
    # before any components are added to the model.

def custom_init_and_run(model):
    import parameters as parameters
    # When uncommented, this function is called after all the model
    # components defined in CellBlender were added to the model.
    # It allows to add additional model components before initialization
    # is done and then to customize how simulation is ran.
    # The module parameters must be imported locally otherwise
    # changes to shared.parameter_overrides done elsewhere won't be applied.
    # initialize the model
    #ves = model.find_elementary_molecule_type('ves_in')
    #assert ves
    #ves.diffusion_constant_3d =  5e-6
    model.initialize()

    for i in range(parameters.ITERATIONS):
        ves = model.find_elementary_molecule_type('ves_in')
     #   assert ves
      #  ves.diffusion_constant_3d =  5e-6
    #    if i == 10:
        #    ves = model.find_elementary_molecule_type('ves_in')
        #    assert ves
        #    ves.diffusion_constant_3d =  5e-6
       # ves = model.find_elementary_molecule_type('ves_in')
        #assert ves
        #print("Ves_in: ",ves.diffusion_constant_3d,i)
            #.set_diffusion_constants(ves_in, 5e-6)
            #ves_in.diffusion_constant_3d = 5e-10
        # run only one iteration
        model.run_iterations(1)
    model.end_simulation()
