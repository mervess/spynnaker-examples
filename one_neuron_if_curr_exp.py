import spynnaker8 as sim

# === Parameters ===============================================================

n_neurons = 1   # number of neurons in each population for the Spiking Neural Network in this example
timestamp = 1.0 # simulate the network with 1.0 ms time steps
sim_time = 50   # total simulation time

# === Configure the simulator ==================================================

sim.setup( timestamp )

# === Build the network ========================================================

cell_params = {'tau_refrac':2.0,'v_thresh':-50.0,'tau_syn_E':2.0, 'tau_syn_I':2.0}

# Leaky Integrate and Fire neuron
pop_exc = sim.Population( n_neurons, sim.IF_curr_alpha(), # for some reason alpha can't be run with the basic setup
                          label = 'pop_exc' )

# == Instrument the network ====================================================

# Record all to observe.
# Note: For PyNN's IF_curr_exp recordables are limited with voltage and spikes of the population.
pop_exc.record( "all" )

# === Run the simulation =======================================================

sim.run( sim_time )

# === Plot the results =========================================================

# Data of recordables
data = pop_exc.get_data().segments[0]

spiketrains = data.spiketrains
voltage = data.filter( name = 'v' )

# Libraries necessary for plotting
from pyNN.utility.plotting import Figure, Panel
import matplotlib.pyplot as plt

def plotBlackAndWhite():
    Figure(
        Panel( spiketrains,
               ylabel = "Neuron ID",
               yticks = True
        ),
        Panel( voltage[0],
               xlabel = "Time (ms)", ylabel = "Membrane potential (mV)",
               data_labels = [pop_exc.label],
               xticks = True, yticks = True
        ),
        title = "Recurrent Spiking Neural Network",
        annotations = "Simulated with {}".format(sim.name())
    )#.save("recurrent_snn.png")
    plt.legend( loc = "lower right" )
    plt.show()

def plotColourful():
    import numpy as np

    for spiketrain in spiketrains:
        y = np.ones_like(spiketrain) * spiketrain.annotations['source_index']
        plt.plot(spiketrain, y, '.')

    plt.ylabel("Neuron ID")
    plt.xlabel("Time (ms)")
    plt.setp( plt.gca().get_xticklabels(), visible = True )
    plt.xlim(0, sim_time)
    plt.show()


plotBlackAndWhite()

# === Clean up and quit ========================================================

sim.end()
