import spynnaker8 as sim

"""
"""

# === Parameters ===============================================================

n_neurons = 5   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 100  # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

spikeArray = { 'spike_times': [ [0], [1], [13], [45], [93] ] } # in ms

# Presynaptic population - Input layer - Stimuli
pop_input = sim.Population( n_neurons,  sim.SpikeSourceArray, spikeArray,
# sim.SpikeSourcePoisson(), #(rate=1, duration=sim_time),
                            label = 'pop_input' )
# Postsynaptic population
"""
Notes:
    * Interesting property about this neuron model: voltage_based_synapses = True
    * Initial voltage value = -70.0
"""
pop_output = sim.Population( n_neurons, sim.Izhikevich(),
                             label = 'pop_output' )

sim.Projection( pop_input, pop_output, sim.OneToOneConnector(), sim.StaticSynapse( weight = 20.0, delay = 2 ) )

# == Instrument the network ====================================================

# Record all to observe.
"""
Note:
    Recordables of the Izhikevich neuron model are limited with voltage, spikes, and unit(mV/ms) of the population.
"""
pop_output.record( "all" )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

# Data of recordables
data = pop_output.get_data().segments[0]

spiketrains = data.spiketrains
voltage = data.filter( name = 'v' )[0]
# u = data.filter( name = 'u' )[0] # this one doesn't work for some reason

from util.basic_visualizer import *
plot( spiketrains, voltage, plot_title="Izhikevich SNN Model" )
color_plot( spiketrains, sim_time )

# === Clean up and quit ========================================================

sim.end()
