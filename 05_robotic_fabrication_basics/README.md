# Module 2

In this **Robotic Fabrication Basics** sessions, you will learn about the basics of compas_fab.

## Installation

We will use the `afab19` environment and update it as follows:

    (base)  conda activate afab19
    (afab19) conda update compas compas_fab --yes
    (afab19) python -m compas_fab.rhino.install -v 6.0

## Verify installation

    (afab19) python
    >>> import compas_fab
    >>> compas_fab.__version__
    '0.10.0'
    >>> exit()

Some examples use Jupyter Notebooks, which needs to be installed **in the same environment**:

    (afab19) conda install jupyter rise pythreejs jupyter_contrib_nbextensions jupyter_nbextensions_configurator --yes

## Examples

### Session A: 

* **Slides**: [session 1](https://docs.google.com/presentation/d/1wE8Rpp_3Or0ItfSfTzsOB0B8ogb1tT9noUbGMIsG5wI/edit#slide=id.g7596e826ec_0_11)
* **Assignments**:

### Session B: 

* **Slides**:
* **Assignments**:
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
  * [Cartesian motion planning](examples/12_plan_cartesian_motion_ros_loader.py)
  * [Free space motion planning](examples/13_plan_motion_ros_loader.py)
  * Planning scene management:
    * [Add objects to the scene](examples/14_add_collision_mesh.py)
    * [Append nested objects to the scene](examples/15_append_collision_meshes.py)
    * [Remove objects from the scene](examples/16_remove_collision_mesh.py)
* [Grasshopper Playground](examples/17_robot_playground_ur5.ghx)

### Session C:

* **Slides**:  
* **Assignments**:
* **Jupyter Notebooks**:
  * [Path planning](Path%20planning.ipynb)
  * [Robotic Assembly](Robotic%20Assembly.ipynb)

---

* [Docker configuration to launch ROS & MoveIt](docker-ur5/)
* [Assembly Playground](examples/20_robot_assembly.ghx)
* Attaching gripper/tool:
  * [Attach tool to last link of the robot](examples/21_attach_tool.py)
  * [Plan cartesian motion with attached tool](examples/22_plan_cartesian_motion_with_attached_tool.py)
* Assembly elements (e.g. bricks):
  * [Add assembly element to planning scene](examples/23_create_element_and_add_to_planning_scene.py)
  * [Attach assembly element to gripper](examples/24_add_element_as_attached_collision_object.py)
* Pick and place examples:
  * [Pick and place](examples/25_pick_and_place.py)
  * [Pick and place Stack](examples/26_pick_and_place_stack.py)
