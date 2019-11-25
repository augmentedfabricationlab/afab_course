# Getting started

### Dependencies

* Windows 10 Professional
* Rhino 6 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Github Desktop](https://desktop.github.com/)

### 1. Setting up the Anaconda environment with COMPAS and COMPAS_fab

Add conda-forge to the list of channels where conda looks for packages.

	(base) conda config --add channels conda-forge

Execute the commands below in Anaconda Prompt to install compas and compas_fab:

	(base) conda create -n afab19 python=3.6 compas=0.11 compas_fab=0.10 --yes
    
Alternatively: If you run into problems with the PIL library, run instead:

	(base) conda create -n afab19 python=3.6 compas=0.11 compas_fab=0.10 matplotlib=3.0 --yes

Then continue with activating the environment:

    	(base) conda activate afab19
	
For simply updating your environment, you can also call the following command:
	
	(afab19) conda update compas compas_fab --yes
    
For more info about COMPAS follow this [link](https://compas-dev.github.io/).

For more info about COMPAS_fab follow this [link](https://gramaziokohler.github.io/compas_fab/latest/).

### 2. Setting up the Rhino/Grasshopper Environment

see also this [link](https://compas-dev.github.io/main/gettingstarted/cad/rhino.html)

Installing COMPAS for Rhino is very simple. Just type the following on Anaconda prompt:
    
    (afab19) python -m compas_rhino.install
    (afab19) python -m compas_fab.rhino.install -v 6.0

### 3. Setting up jupyter and extensions

Install jupyter and extensions for the afab19 environment:

    (afab19) conda install jupyter rise pythreejs jupyter_contrib_nbextensions jupyter_nbextensions_configurator --yes

To run the jupyter notebook, you simply have to type:

    (afab19) jupyter notebook

in your command line.

#### Jupyter extensions activation

After installing, you can observe a new tab Nbextensions added to the menu (last entry under "Edit"), in which you can activate the extensions.

#### Jupyter workspace configuration

To configure the workspace, type

    (afab19) jupyter notebook --generate-config

This writes a default configuration file into:

`%HOMEPATH%\.jupyter\jupyter_notebook_config.py` (on windows)

or

`~/.jupyter/jupyter_notebook_config.py` (on mac)

If you want jupyter to open in a different directory, then change the following line:

    c.NotebookApp.notebook_dir = 'YOUR_PREFERRED_PATH'



	
    






