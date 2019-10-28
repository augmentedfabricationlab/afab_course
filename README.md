# AFAB Seminar

*Basics of Robotic Fabrication*

## Description

The Master-level course will introduce computational methods for architecture engineering, fabrication & construction, incentivising computational literacy. Students learn the theoretical background and basic implementation details of fundamental data structures and algorithms, and to solve real-world problems using the COMPAS and COMPAS_fab framework, and other open-source libraries.

## Learning objectives

* understand the scope and relevance of computational methods for architecture and engineering research and practice,
* the theoretical background of fundamental data structures, 
* the basic principles of algorithmic design; 
* implement basic versions of prevalent algorithms related to architectural geometry and robotic assembly; and
* use common CAD tools as interfaces to self-implemented solutions.

## Overview

This course will consist of a few lectures, several tutorials and project-based exercises.

The topics will include:

* Intro Python programming
* Intro COMPAS open-source framework (https://compas-dev.github.io/) 
* Intro to geometry processing, data structures, topology, numerical computation
* Domain-specific case studies (i.e., on architectural geometry, robotic assembly)

## Schedule

Week | Date | Title | Description | Links
---- | ---- | ---- | ----- | -----------
1 | Oct 29 | Introduction | Course overview, COMPAS intro, UR10 intro | .
2 | Nov 6 | Introduction | Python basics | .



# Dependencies

* Windows 10
* Rhino 6 / Grasshopper
* [Anaconda Python](https://www.anaconda.com/distribution/?gclid=CjwKCAjwo9rtBRAdEiwA_WXcFoyH8v3m-gVC55J6YzR0HpgB8R-PwM-FClIIR1bIPYZXsBtbPRfJ8xoC6HsQAvD_BwE)
* [COMPAS](https://compas-dev.github.io/)
* [COMPAS_fab](https://gramaziokohler.github.io/compas_fab/latest/)

## Jupyter and extensions

If you have Anaconda installed, then jupyter is already installed. If not, then install jupyter with pip.

To run the jupyter notebook, you simply have to type:

    jupyter notebook

in your command line.

### Configure workspace

To configure the workspace, type

    jupyter notebook --generate-config

This writes a default configuration file into:

`%HOMEPATH%\.jupyter\jupyter_notebook_config.py` (on windows)

or

`~/.jupyter/jupyter_notebook_config.py` (on mac)

If you want jupyter to open in a different directory, then change the following line:

    c.NotebookApp.notebook_dir = 'YOUR_PREFERRED_PATH'

### Download nbextensions

To install nbextensions, execute the commands below in Anaconda Prompt (run as Administrator):

    conda install -c conda-forge jupyter_contrib_nbextensions
    conda install -c conda-forge jupyter_nbextensions_configurator
    conda install -c conda-forge rise

After installing, restart the Jupyter notebook, and you can observe a new tab Nbextensions added to the menu, last entry under "Edit".
Install the following extensions:

1. Split Cells Notebook - Enable split cells in Jupyter notebooks

2. [RISE](https://rise.readthedocs.io/en/stable/installation.html#) - allows you to instantly turn your Jupyter Notebooks into a slideshow

### Python Dependencies

Three JS

    conda install -c conda-forge pythreejs
    
    
