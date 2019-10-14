import spynnaker8 as sim

"""
Compare voltage values of SpiNNaker-supported PyNN neuron models
"""

# === Parameters ===============================================================

n_neurons = 3   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 100  # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

# Presynaptic population - Input layer - Stimuli
pop_input = sim.Population( n_neurons, sim.SpikeSourcePoisson( rate = 100, duration = sim_time ),
                            label = 'pop_input' )
# Synapse value as weight = 5.0 nA, delay = 1 ms
static_synapse = sim.StaticSynapse( weight = 5.0, delay = 1 )

# I - IF_cond_exp Population
pop_cond_exp = sim.Population( n_neurons, sim.IF_cond_exp, {}, label = 'if_cond_exp' )
sim.Projection( pop_input, pop_cond_exp, sim.OneToOneConnector(), synapse_type = static_synapse )

# II - IF_curr_exp Population
pop_curr_exp = sim.Population( n_neurons, sim.IF_curr_exp, {}, label = 'if_curr_exp' )
sim.Projection( pop_input, pop_curr_exp, sim.OneToOneConnector(), synapse_type = static_synapse )

# III - IF_curr_alpha Population
pop_curr_alpha = sim.Population( n_neurons, sim.IF_curr_alpha, {}, label = 'if_curr_alpha' )
sim.Projection( pop_input, pop_curr_alpha, sim.OneToOneConnector(), synapse_type = static_synapse )

# IV - Izhikevich Population
pop_izhikevich = sim.Population( n_neurons, sim.Izhikevich, {}, label = 'izhikevich' )
sim.Projection( pop_input, pop_izhikevich, sim.OneToOneConnector(), synapse_type = static_synapse )

# == Instrument the network ====================================================

# Record voltage values of each population.
pop_cond_exp.record( 'v' )
pop_curr_exp.record( 'v' )
pop_curr_alpha.record( 'v' )
pop_izhikevich.record( 'v' )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

from util.basic_visualizer import *
plot( [ pop_cond_exp, pop_curr_exp, pop_curr_alpha, pop_izhikevich ],
      "Voltage Value Comparison of SpiNNaker-Supported PyNN Neuron Models",
      "Simulated with {}".format( sim.name() ) )

# === Clean up and quit ========================================================

sim.end()
