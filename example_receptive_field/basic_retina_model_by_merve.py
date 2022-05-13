"""
Example network to learn how PyNN works
"""

import spynnaker8 as p
from pyNN.utility.plotting import Figure, Panel
import matplotlib.pyplot as plt


# (ms) duration of random stimulation
runtime = 5000
# (Hz) frequency of the random stimulation
rate = 100

params_photoreceptors = {}
params_horizontal_cells = {}
params_bipolar_cell = {}

p.setup( timestamp = 1.0 )

# cells first

# human eye - retinal receptive fields #

"""
Population method usage:
    1st param: neuron count
    2nd param: neuron type
    3rd param: neuron label
"""
photoreceptors   = [ p.Population( 1, p.IF_curr_exp(**params_photoreceptors), label = 'photoreceptors' )
                        for i in range(7) ] # 7 neurons for photoreceptors
horizontal_cells = [ p.Population( 1, p.IF_curr_exp(**params_horizontal_cells), label = 'horizontal_cells' )
                        for i in range(2) ] # 2 neurons for horizontal cells
bipolar_cell     = p.Population( 1, p.IF_curr_exp(**params_bipolar_cell), label = 'bipolar_cell' )

# stimuli will be the cause of whole simulation
visual_input     = [ p.Population( 1, p.SpikeSourcePoisson( rate = rate, duration = runtime ), label = 'visual_input' )
                        for i in range(7) ]
"""
Projection method usage here:
    1st param: source
    2nd param: target
    3rd param: connection type between neurons
    4th param: receptor type
    5th param: synapse type
"""

'''
Static variable definition for projections

All receptor's will be 'excitatory' here; so, no need to mention them.
'''
synchronous_static_synapse =  p.StaticSynapse( weight = 1, delay = 1 )

# start top to bottom, with the incoming 'visual input'
for i in range(7):
    p.Projection( visual_input[i], photoreceptors[i], p.OneToOneConnector(), synchronous_static_synapse )

# Photoreceptors
p.Projection( photoreceptors[0], horizontal_cells[0], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[1], horizontal_cells[0], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[2], horizontal_cells[0], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[3], horizontal_cells[0], p.OneToOneConnector(), synchronous_static_synapse )

p.Projection( photoreceptors[3], horizontal_cells[1], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[4], horizontal_cells[1], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[5], horizontal_cells[1], p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[6], horizontal_cells[1], p.OneToOneConnector(), synchronous_static_synapse )

# Two horizontal cells
p.Projection( horizontal_cells[0], bipolar_cell, p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( horizontal_cells[1], bipolar_cell, p.OneToOneConnector(), synchronous_static_synapse )

# Three of the photoreceptors
p.Projection( photoreceptors[2], bipolar_cell, p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[3], bipolar_cell, p.OneToOneConnector(), synchronous_static_synapse )
p.Projection( photoreceptors[4], bipolar_cell, p.OneToOneConnector(), synchronous_static_synapse )

"""
Record the Results
"""

bipolar_cell.record( ['v', 'spikes'] ) # first say, before running, you wanna record them

p.run( runtime )

v = bipolar_cell.get_data('v')
spikes = bipolar_cell.get_data('spikes')

Figure (
    Panel( spikes.segments[0].spiketrains, ylabel = "neuron ID", yticks = True, markerSize = 1, xlim = (0, runtime) ),

    Panel( v.segments[0].filter( name = 'v' )[0], ylabel = "Membrane potential (mW)", data_labels = [bipolar_cell.label], yticks = True, xlim = (0, runtime) ),

    title = "Retina and lateral geniculate nuclei",
    annotations = "Simulated with {}".format(p.name())
)
plt.show()

p.end()
