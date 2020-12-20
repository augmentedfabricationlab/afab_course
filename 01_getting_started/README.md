# Getting started

[Slides](https://docs.google.com/presentation/d/1XW2h3WrHfVG4USUCjJp5Sgxk5VMwEWn4va1VxWz6eRc/edit?usp=sharing)

### 1. Setting up the Anaconda environment with COMPAS

Execute the commands below in Anaconda Prompt:
	
    (base) conda config --add channels conda-forge

#### Windows
    (base) conda create -n afab python=3.8 compas_fab=0.13 --yes
    (base) conda activate afab

#### Mac
    (base) conda create -n afab python=3.8 compas_fab=0.13 python.app --yes
    (base) conda activate afab
    

### Verify Installation

    (afab) pip show compas_fab
###
    Name: compas-fab
    Version: 0.13.1
    Summary: Robotic fabrication package for the COMPAS Framework
    ...

### Install on Rhino

    (afab) python -m compas_rhino.install

NOTE: This installs to Rhino 6.0, use `-v 5.0` if needed.


### 2. Installation of Dependencies

    (afab) conda install git

#### Assembly Information Model
    
    (afab) python -m pip install git+https://github.com/augmentedfabricationlab/assembly_information_model@master#egg=assembly_information_model
    (afab) python -m compas_rhino.install -p assembly_information_model

#### UR Fabrication Control
    
    (afab) python -m pip install git+https://github.com/augmentedfabricationlab/ur_fabrication_control@master#egg=ur_fabrication_control
    (afab) python -m compas_rhino.install -p ur_fabrication_control


### 3. Cloning the Course Repository

Create a workspace directory:

C:\Users\YOUR_USERNAME\workspace

Then open Github Desktop and clone the following repositories into you workspace folder:

* [afab_course](https://github.com/augmentedfabricationlab/afab_course)
	


	
    






