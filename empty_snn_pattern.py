import spynnaker8 as sim

"""

"""

# === Parameters ===============================================================

n_neurons = ?   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = ? # simulate the network with 1.0 ms time steps
sim_time = ?  # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

# Presynaptic population - Input layer - Stimuli
pop_input = sim.Population( n_neurons, ... , label = 'pop_input' )
# Postsynaptic population
pop_output = sim.Population( n_neurons, ..., label = 'pop_output' )

sim.Projection( pop_input,
                pop_output,
                connector = ?,
                synapse_type = ?,
                receptor_type = ?,
                space = ?,
                label = "? Projection"
              )

# == Instrument the network ====================================================

# Record all to observe.
pop_output.record( "all" )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

from util.basic_visualizer import *
plot( [pop_output] )

# === Clean up and quit ========================================================

sim.end()
