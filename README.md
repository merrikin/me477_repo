# Merrikin_ME477_Repo
This is a repository by Christian Merrikin, a student of Saint Martin's School of Engineering. Spring semester, 2020.
## Background:
### Course Description
ME477 is a course in embedded computing utilizing C code on the MyRio platform. In case you have not 
heard, there was a COVID-19 epidemic that shut down many aspects of civilized life in the U.S., 
including all in-person academic activities. Therefore, because it was not feasible to continue
the ACTUAL ME477 coursework, the second half of the course focused on an introduction to the 
ROS system.
### Course Details
This course was taught by Dr. Rico Picone. Much of his teaching material can be found on his [webpage](http://ricopic.one/courses/robotics_mini_course).
Written on an Ubuntu virtual computer the ROS packages enclosed in this repository are written with Python.
### Purpose
The purpose of this repository is to demonstrate the understanding of the basic ROS structure and functionality. It is the 
final project for the ME477 course.
## ROS Packages:
There are three ROS packages included in this repository. The details for **merrikin_actions**, **merrikin_services**, and **merrikin_topics** are listed below.
### Requirements
To best run these ROS packages utilize a computer with the Ubuntu_18.04.4_LTE operating system installed. The ROS program is largely interfaced with through the Bash shell terminal. 
> #### Operating System: [Ubuntu 18.04 LTS](https://ubuntu.com/download/desktop)
> #### ROS Version: [Melodic](http://wiki.ros.org/melodic)
> #### Python Version: [2.7.17](https://www.python.org/downloads/release/python-2717/)
### Installation and Configuration
To run the packages in this repository first [clone](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository), [download](https://superuser.com/questions/1309683/how-do-i-download-my-whole-repository-from-gitlab) or [fork](https://help.github.com/en/enterprise/2.13/user/articles/fork-a-repo) the repository so that you have the file system locally on your operating platform. 

Once you have the files locally, assuming you are running a form of Ubuntu, open up a new Terminal to the repository file and perform the following checks:

#### &nbsp;&nbsp;&nbsp; Python:
&nbsp;&nbsp;&nbsp;Make sure you are running Python version 2.7.17 or newer. To determine what Python version you are running submit the &nbsp;&nbsp;&nbsp;following to your terminal: 

&nbsp;&nbsp;&nbsp; `python --version`

&nbsp;&nbsp;&nbsp;Ensure the following Python packages are available on your platform. You can 'pip' them and if they already exist, no harm, no &nbsp;&nbsp;&nbsp;foul.

&nbsp;&nbsp;&nbsp; `pip insall empy` 

&nbsp;&nbsp;&nbsp; `pip insall pyyaml` 

&nbsp;&nbsp;&nbsp; `pip insall catkin_pkg` 

&nbsp;&nbsp;&nbsp; `sudo apt install rosbash` 

#### &nbsp;&nbsp;&nbsp;ROS:
&nbsp;&nbsp;&nbsp;It is very important to remember to source the _setup.bash_ file associated with the repository's packages. To do 
this, ensure &nbsp;&nbsp;&nbsp;you are still in the repository's main directory and submit the following command to the Terminal:

&nbsp;&nbsp;&nbsp; `source devel/setup.bash`

&nbsp;&nbsp;&nbsp;You will need to do this for each new terminal window you open to prevent frustrating sourcing errors. If you are pretty sure &nbsp;&nbsp;&nbsp;you have your system setup right but you're unable to run or launch packages, go back to the repository's main directory and &nbsp;&nbsp;&nbsp;run that little piece of magic. It could save you an hour or hair-pulling. 

&nbsp;&nbsp;&nbsp;Once you have the repository sourced you should be able to run the enclosed packages. Descriptions of the packages can be &nbsp;&nbsp;&nbsp;found further down. In case you've forgotten how, here is how to run an ROS package.
- Navigate to the repository's main directory: _me477_repo_ 
   - Source the setup.bash file as described above 
   - Open a new terminal window (__Ctrl+Alt+T__) 
     - Submit: `roscore` 
     - This is your ROS brain, so to speak. It coordinates all ROS functions that are subsequently deployed
   - In the first terminal, or another if you wish (having ensured that you did your sourcing, last reminder) you can begin to run or launch packages. 
     - To run a package use the following syntax: `rosrun <package_name> <program_name> [args]` \
       &nbsp;&nbsp;&nbsp;Example: `rosrun merrikin_topics topic_subscriber.py`
     - To launch a set of packages use the following syntax: `roslaunch <package_name> <launch_file_name> [args]` \
       &nbsp;&nbsp;&nbsp;Example: `roslaunch merrikin_services services.launch`
 - End a program with __Ctrl+C__
       
### Packages Included in this Repository

#### &nbsp;&nbsp;&nbsp; merrikin_actions
Files:
&nbsp;&nbsp;&nbsp; [fancy_action_client.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_actions/src/fancy_action_client.py)
&nbsp;&nbsp;&nbsp; [fancy_action_server.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_actions/src/fancy_action_server.py)

Function:
&nbsp;&nbsp;&nbsp;This package demonstrates the usefulness of being able to do minor computational or otherwise administrative tasks with a single node. A ROS node with an action provides feedback to its subscribers for the duration of the action. 

Inputs:
&nbsp;&nbsp;&nbsp;Action servers require action files that define the action to be completed. The [action](https://github.com/merrikin/me477_repo/tree/master/merrikin_actions/action) files are located in the package directory, above src/ and include a `<name>.action` file. 

Outputs:
&nbsp;&nbsp;&nbsp;In the case of merrikin_actions, the action server completes an action and outputs it to the client.

#### &nbsp;&nbsp;&nbsp; merrikin_services
Files:
&nbsp;&nbsp;&nbsp; [service_client.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_services/src/service_client.py)
&nbsp;&nbsp;&nbsp; [service_serrver.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_services/src/service_server.py)

Function:
&nbsp;&nbsp;&nbsp;This package demonstrates how to complete a service utilizing a ROS node. A service differs from an action because the subscribed client must wait for the end result of the requested service.  

Inputs:
&nbsp;&nbsp;&nbsp;In the case of merrikin_services, the client supplies the server with a string of words and the server utilizes its service module, [WordCount.srv](https://github.com/merrikin/me477_repo/blob/master/merrikin_services/srv/WordCount.srv) to count the words. To enter a string of words for the server to count add them as the argument after the `rosrun` or `roslaunch` command.

Outputs:
&nbsp;&nbsp;&nbsp;Once the server has completed its task, counting the words, it sends back an integer corresponding to the count and the client prints it to the display.

#### &nbsp;&nbsp;&nbsp; merrikin_topics
Files:
&nbsp;&nbsp;&nbsp; [doubler.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_topics/src/doubler.py)
&nbsp;&nbsp;&nbsp; [message_publisher.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_topics/src/message_publisher.py)
&nbsp;&nbsp;&nbsp; [message_subscriber.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_topics/src/message_subscriber.py)
&nbsp;&nbsp;&nbsp; [topic_publisher.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_topics/src/topic_publisher.py)
&nbsp;&nbsp;&nbsp; [topic_subscriber.py](https://github.com/merrikin/me477_repo/blob/master/merrikin_topics/src/topic_subscriber.py)

Function:
&nbsp;&nbsp;&nbsp;The purpose of this package is to demonstrate the connection between publishers and subscribers through topics and subscriptions.

Inputs:
&nbsp;&nbsp;&nbsp;When merrikin_topics is launched a publisher and subscriber begin. There are no input arguments.

Outputs:
&nbsp;&nbsp;&nbsp;Once the publisher and subscriber are running the user will see a counter printing to the terminal window.
