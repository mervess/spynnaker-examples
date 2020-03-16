# An Introduction to Spiking Neural Networks (SNNs)

![Introduction to Spikes](https://images.unsplash.com/photo-1552154357-aaba12e68e64?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1050&q=80)
*Photo by [Scott Webb](https://unsplash.com/@scottwebb) on [Unsplash](https://unsplash.com/).*

This repository contains introductory level SNN examples that I built to understand more about the neuron models and the main network types by using _sPyNNaker_ (_PyNN_ for _SpiNNaker_).

---

## Setup
### Software
#### Necessary Python Packages
* [sPyNNaker8](https://github.com/SpiNNakerManchester/sPyNNaker8)*
* matplotlib (2.2.3)
* PyNN (0.9.3)**
* numpy (1.16.0)

Along with Python 2.7.

#### Included Files and Their Usage

```
spynnaker-examples/
├── compare_voltages.py
├── empty_snn_pattern.py
├── izhikevich_snn.py
├── one_neuron_if_curr_exp.py
├── one_neuron_izhikevich.py
├── recurrent_network.py
├── scripts
│   ├── install_spynnaker.sh
│   └── uninstall_spynnaker.sh
├── snn_if_cond_exp.py
├── snn_if_curr_alpha.py
├── snn_if_curr_exp.py
└── util
    ├── basic_visualizer.py
    └── __init__.py
```

Each python file could be run separately except *basic_visualizer.py* and *empty_snn_pattern.py*. 

Folder _util_ includes utility library *basic_visualizer* which contains plotting functions.

Folder _scripts_* includes bash scripts to install and uninstall pip based _sPyNNaker_ packages.

*empty_snn_pattern.py* is a pattern python file which is reproducible by filling the sections. I built this as a template for my codes.

<p align="center">
  <img src="compare_voltages.png" alt="Voltage Comparisons" height="750">
</p>

<p align="center">
  <i>Comparisons of neuron models in sPyNNaker8 with default values, reference <a href="https://github.com/mervess/spynnaker-examples/blob/master/compare_voltages.py">compare_voltages.py</a>.</i>
</p>

---

### Hardware
SpiNNaker neuromorphic hardware resource is used in this project. Please refer to [SpiNNaker project page](http://apt.cs.manchester.ac.uk/projects/SpiNNaker/) regarding its setup and usage.

**Notes**

*There is also a python package of _sPyNNaker_ available on pip. However, the GitHub repository of the _sPyNNaker_ is more comprehensive and up-to-date than the pip version. If you'd lke to install _sPyNNaker_ via pip, you may refer to my scripts in the _scripts_ folder.

**You can run these examples on a different neuromorphic hardware resource or a simulator as well. Please see [PyNN documentation](http://neuralensemble.org/PyNN/) for alternatives.

