import spynnaker8 as sim

"""
A basic Spiking Neural Network(SNN) example constructed by using
SpikeSourcePoisson as stimuli in the input layer,
LIF neuron model (called as "cell type" in PyNN) in the post-synaptic population,
One-to-one connection in projection with
constant(fixed)-weighted StaticSynapse

Notes:
    * I can't run "IF_curr_alpha" neuron model with basic spinnaker environment:
            AttributeError: 'module' object has no attribute 'IF_curr_alpha'
    I can run it, however, with github version.
"""

# === Parameters ===============================================================

n_neurons = 5   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 100  # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

# Presynaptic population - Input layer - Stimuli
pop_input = sim.Population( n_neurons, sim.SpikeSourcePoisson( rate = 100, duration = sim_time ),
                            label = 'pop_input' )
# Postsynaptic population
pop_output = sim.Population( n_neurons, sim.IF_curr_alpha, {}, # Use default values of LIF neuron
                             label = 'pop_output' )

# Synapse value as weight = 5.0 nA, delay = 2 ms
static_synapse = sim.StaticSynapse( weight = 5.0, delay = 2 )

sim.Projection( pop_input,
                pop_output,
                sim.OneToOneConnector(),
                synapse_type = static_synapse,
                label = "LIF - alpha function Projection"
              )

# == Instrument the network ====================================================

# Record all to observe.
pop_output.record( "all" )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

from util.basic_visualizer import *
plot( [pop_output],
      "IF_curr_alpha Neuron Model Examination",
      "Simulated with {}".format( sim.name() ) )

# === Clean up and quit ========================================================

sim.end()
