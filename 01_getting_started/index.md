# Getting started

### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
	(base) conda config --add channels conda-forge
	(base) conda create -n afab python=3.8 compas=0.15.6 --yes

Then continue with activating the environment and [setting it up for Rhino/GH]((https://compas-dev.github.io/main/gettingstarted/cad/rhino.html)):
	
	(base) conda activate afab
	(afab) python -m compas_rhino.install -v 6.0 -p compas compas_ghpython compas_rhino
    
To verify your installation, type the commands below:

	(afab) python
	>>> import compas_fab
	>>> compas_fab.__version__
	'0.15.6'
	>>> exit()

### 2. Setting up Jupyter and extensions

Install jupyter and extensions for the afab environment:

    (afab) conda install jupyter rise pythreejs jupyter_contrib_nbextensions jupyter_nbextensions_configurator --yes

To run the jupyter notebook, you simply have to type:

    (afab) jupyter notebook

in your command line.

<details>
<summary>Jupyter extensions activation</summary>
<br>
After installing, you can observe a new tab Nbextensions added to the menu (last entry under "Edit"), in which you can activate the extensions.
</details>

<details>
<summary>Jupyter workspace configuration</summary>
<br>
To configure the workspace, type

    (afab) jupyter notebook --generate-config

This writes a default configuration file into:

`%HOMEPATH%\.jupyter\jupyter_notebook_config.py` (on windows)

If you want jupyter to open in a different directory, then change the following line:

    c.NotebookApp.notebook_dir = 'YOUR_PREFERRED_PATH'
    
</details>

### 2. Installation of Dependencies

Create a workspace directory:

C:\Users\YOUR_USERNAME\workspace

Then open Github Desktop and clone the following repositories into you workspace folder:

* [afab_course](https://github.com/augmentedfabricationlab/afab_course)
* [assembly_information_model](https://github.com/augmentedfabricationlab/assembly_information_model)
* [climate_active_bricks](https://github.com/augmentedfabricationlab/climate_active_bricks)
* [ur_online_control](https://github.com/augmentedfabricationlab/ur_online_control)

And make the projects accessible from Rhino (change to the respective repository directory in the Anaconda prompt):

	(afab) invoke add-to-rhino
	
Make the assembly_information_model repository accessible for your environment 	
	
	(afab) pip install your_filepath_to_assembly_information_model 





	
    






