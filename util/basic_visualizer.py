# -*- coding: utf-8 -*-

from pyNN.utility.plotting import Figure, Panel
import matplotlib.pyplot as plt


def plot( populations, plot_title=None, annotations=None ):
    if populations != []:
        panels = []

        for variable in ( 'v', 'u', 'gsyn_exc', 'gsyn_inh', 's', 'w' ):
            for population in populations:
                data_segment = population.get_data().segments[0]
                data = None

                if variable != 's' and data_segment.filter( name=variable ) != []:
                    data = data_segment.filter( name=variable )[0]
                elif variable == 's' and data_segment.spiketrains != []:
                    data = data_segment.spiketrains

                if data is not None:
                    panels.append(
                        Panel( data,
                               ylabel=get_y_label( variable ),
                               yticks=True,
                               data_labels=[population.label]
                        ),
                    )

        panels[-1].options.update( xticks=True, xlabel="Time (ms)" )

        Figure( *panels,
                title=plot_title if plot_title != None else "",
                annotations=annotations if annotations != None else ""
        )
        plt.show()
    else:
        print( "No population, no plot!" )


def get_y_label( variable ):
    if variable == 'v':
        return "Membrane potential (mV)"
    elif variable == 'u':
        return "u (mV/ms)"
    elif variable == 'gsyn_exc':
        return u"Synaptic conductance - excitatory (µS)"
    elif variable == 'gsyn_inh':
        return u"Synaptic conductance - inhibitory (µS)"
    elif variable == 's':
        return "Neuron ID"
    elif variable == 'w':
        return "w (nA)"
    else:
        return ""


def color_plot( spiketrains, sim_time ):
    # plt.figure()
    # plt.yticks=True
    # plt.xticks=True

    import numpy as np

    for spiketrain in spiketrains:
        y = np.ones_like(spiketrain) * spiketrain.annotations['source_index']
        plt.plot(spiketrain, y, '.')

    plt.ylabel("Neuron ID")
    plt.xlabel("Time (ms)")
    plt.setp( plt.gca().get_xticklabels(), visible = True )
    plt.xlim(0, sim_time)
    plt.show()

    """
    Continue to this with voltage data from:
    http://neuralensemble.org/docs/PyNN/examples/stochastic_synapses.html
    http://neuralensemble.org/docs/PyNN/data_handling.html?highlight=plot_spiketrains
    http://neuralensemble.org/docs/PyNN/examples/simple_STDP.html?highlight=annotations
    """
