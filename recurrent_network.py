import spynnaker8 as sim

"""
A recurrent Spiking Neural Network example constructed by using
SpikeSourceArray as stimuli,
IF_curr_exp as neuron model in hidden and output populations with
OneToOneConnector as connector in projection and a static synapse.
"""

# === Parameters ===============================================================

n_neurons = 2   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 100  # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

spikeArray = { 'spike_times': [ [0], [1] ] } # in ms

# Presynaptic population - Input layer - Stimuli
pop_input = sim.Population( n_neurons, sim.SpikeSourceArray, spikeArray,
                            label = 'pop_input' )
# Postsynaptic population - Hidden layer
pop_hidden = sim.Population( n_neurons, sim.IF_curr_exp, {},
                             label = 'pop_hidden' )

# Synapse values as weight = 5.0 nA, delay = 2 ms
synapse = sim.StaticSynapse( weight = 5.0, delay = 2 )

# Projection 1: Input layer to hidden layer projection
sim.Projection( pop_input, pop_hidden, sim.OneToOneConnector(), synapse )

# Projection 2: Hidden layer to hidden layer "recurrent" projection
sim.Projection( pop_hidden, pop_hidden, sim.OneToOneConnector(), synapse )

# === Instrument the network ===================================================

# Record voltage (v) and spikes of the population
pop_hidden.record( ['v', 'spikes'] )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

from util.basic_visualizer import *
plot( [pop_hidden],
      "Recurrent SNN",
      "Simulated with {}".format( sim.name() ) )

# === Clean up and quit ========================================================

sim.end()
