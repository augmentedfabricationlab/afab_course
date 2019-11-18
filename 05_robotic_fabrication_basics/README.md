# Robotic Fabrication Basics using COMPAS FAB

## Compas Fab Installation

Use the `afab19` environment and update it as follows:

    (base)  conda activate afab19
    (afab19) conda install compas=0.11 compas_fab=0.9 --yes
    (afab19) python -m compas_rhino.install
    (afab19) python -m compas_fab.rhino.install -v 6.0

### Installation Problems

If you run into problems, please remove and reinstall your `afab19` environment as follows:
    
    (base)  conda config --add channels conda-forge
    (base)  conda remove --name afab19 --all
    (base)  create -n urfab python=3.6 compas=0.11 compas_fab=0.9 matplotlib=3.0 --yes
    (base)  conda activate urfab

## Jupyter Notebooks Installation

Some examples will also use Jupyter Notebooks, which needs to be installed **in the same environment**:

    (afab19) conda install jupyter rise pythreejs jupyter_contrib_nbextensions jupyter_nbextensions_configurator --yes

## Verify Installation

    (afab19) python
    >>> import compas_fab
    >>> compas_fab.__version__
    '0.9.0'
    >>> exit()

## Examples

* **Slides**: [link](https://docs.google.com/presentation/d/1OIU3vCmwe3lkVWpI0JuJJ-GFoOq5HH8ulElPZNS_F2Y/edit?usp=sharing)
* **Assignments**: [link](assignments/README.md)

---

* [Docker configuration to launch ROS & MoveIt](docker-ur5/)
* [Open MoveIt! in your browser](http://localhost:8080/vnc.html?resize=scale&autoconnect=true) (once the UR5 docker compose has been started)
* Basic examples:
  * [Programatically define a robot](examples/01_define_model.py)
  * [Load robots from Github](examples/02_robot_from_github.py)
  * [Load robots from ROS](examples/03_robot_from_ros.py)
  * [Visualize robots in Rhino](examples/04_robot_artist_rhino.py)
  * [Visualize robots in Grasshopper](examples/05_robot_artist_grasshopper.ghx)
  * [Build your own robot](examples/06_build_your_own_robot.py)
* Basic ROS examples:
  * [Verify connection](examples/07_check_connection.py)
  * The cannonical example of ROS: chatter nodes
    * [Talker node](examples/08_ros_hello_world_talker.py)
    * [Listener node](examples/09_ros_hello_world_listener.py)
* Examples of ROS & MoveIt planning with UR5:
  * [Forward Kinematics](examples/10_forward_kinematics_ros_loader.py)
  * [Inverse Kinematics](examples/11_inverse_kinematics_ros_loader.py)
  * [Cartesian path planning](examples/12_plan_cartesian_motion_ros_loader.py)
  * [Free space path planning](examples/13_plan_motion_ros_loader.py)
  * Planning scene management:
    * [Add objects to the scene](examples/14_add_collision_mesh.py)
    * [Append nested objects to the scene](examples/15_append_collision_meshes.py)
    * [Remove objects from the scene](examples/16_remove_collision_mesh.py)
* [Grasshopper Playground](examples/17_robot_playground_ur5.ghx)
