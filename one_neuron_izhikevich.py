import spynnaker8 as sim

# === Parameters ===============================================================

n_neurons = 1   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 10   # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

# Izhikevich neuron model
"""
Notes:
    * Interesting property about this neuron model: voltage_based_synapses = True
    * Initial voltage value = -70.0
"""
pop_exc = sim.Population( n_neurons, sim.Izhikevich(),
                          label = 'pop_exc' )

# == Instrument the network ====================================================

# Record all to observe.
"""
Note:
    Recordables of this neuron model are limited with voltage, spikes, and unit(mV/ms) of the population.
"""
pop_exc.record( "all" )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

# Data of recordables
data = pop_exc.get_data().segments[0]

spiketrains = data.spiketrains
voltage = data.filter( name = 'v' )[0]

from util.basic_visualizer import *
plot( spiketrains, voltage, plot_title="Izhikevich Neuron Model" )

# === Clean up and quit ========================================================

sim.end()
