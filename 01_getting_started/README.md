# Getting started

[Slides](https://docs.google.com/presentation/d/1XW2h3WrHfVG4USUCjJp5Sgxk5VMwEWn4va1VxWz6eRc/edit?usp=sharing)

### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
	(base) conda config --add channels conda-forge
	(base) conda create -n afab python=3.8 compas=0.15.6 --yes

Then continue with activating the environment and [setting it up for Rhino/GH]((https://compas-dev.github.io/main/gettingstarted/cad/rhino.html)):
	
	(base) conda activate afab
	(afab) python -m compas_rhino.install -v 6.0 -p compas compas_ghpython compas_rhino
    
To verify your installation, type the commands below:

	(afab) python
	>>> import compas
	>>> compas.__version__
	'0.15.6'
	>>> exit()


### 2. Installation of Dependencies

Create a workspace directory:

C:\Users\YOUR_USERNAME\workspace

Then open Github Desktop and clone the following repositories into you workspace folder:

* [afab_course](https://github.com/augmentedfabricationlab/afab_course)
* [assembly_information_model](https://github.com/augmentedfabricationlab/assembly_information_model)
* [participative_fabrication](https://github.com/augmentedfabricationlab/participative_fabrication)
* [ur_online_control](https://github.com/augmentedfabricationlab/ur_online_control)

And make all the projects accessible from Rhino (change to the respective repository directory in the Anaconda prompt):

	(afab) cd your_filepath_to_repository
	(afab) invoke add-to-rhino
	
If this is not working, try it manually:
* Start Rhino and the Rhino Python Editor by typing EditPythonScript in the command line.
* -> *Tools* -> *Options* and press the Button: *Add to search path* according to browse the folder *Assembly Information Model*
* Select the *src* folder C:\Users\Name\Workspace\projects\assembly_information_model\src
* Redo the same with the folder for the *UR Online Control* C:\Users\Name\Workspace\projects\ur_online_control\src
* Restart Rhino and Grasshopper
	
<details>
<summary>Problems?</summary>

* If invoke is not recognized as command, first install it via pip:
	
		(afab) pip install invoke
	

* You have to change to the respective repository directory in the Anaconda prompt to execute the invoke command:
	
		(afab) cd your_filepath_to_repository
		(afab) invoke add-to-rhino

        
	
</details>
	
Make the assembly_information_model repository accessible for your environment 	
	
	(afab) pip install your_filepath_to_assembly_information_model 
	


	
    






