# Merrikin_ME477_Repo
This is a repository by Christian Merrikin, a student of Saint Martin's School of Engineering. Spring semester, 2020.
## Background:
### Course Description
ME477 is a course in embeded computing utilizing C code on the MyRio platform. In case you have not 
heard, there was a COVID-19 epidemic that shut down many aspects of civilized life in the U.S., 
including all in-person acedemic activities. Therefore, because it was not feasible to continue
the ACTUAL ME477 coursework, the second half of the course focussed on an introduction to the 
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
> #### Python:
>> Make sure you are running Python version 2.7.17 or newer. To determine what Python version you are running submit the following to your terminal:
>>>>> `python --version`

>> Ensure the following Python packages are available on your platform. You can 'pip' them and if they already exist, no harm, no foul.

>>>>> `pip insall empy` \
>>>>> `pip insall pyyaml` \
>>>>> `pip insall catkin_pkg` \
>>>>> `sudo apt install rosbash` (not Python specific, but helpful none the less)

> #### ROS:
>> It is very important to remember to source the _setup.bash_ file associated with the repository's packages. To do this, ensure you are still in the repository's main directory and submit the following command to the Terminal:
>>>>> `source devel/setup.bash`

>> You will need to do this for each new terminal window you open to prevent frustrating sourcing errors. If you are pretty sure you have your system setup right but you're unable to run or launch packages, go back to the repository's main directory and run that little piece of magic. It could save you an hour or hair-pulling. 

>> Once you have the repository sourced you should be able to run the enclosed packages. Descriptions of the packages can be found further down.  In case you've forgotten how, here is how to run an ROS package.
- Navigate to the repository's main directory: _me477_repo_ 
   - Source the setup.bash file as described above 
   - Open a new terminal window (__Ctrl+Alt+T__) 
     - Submit: `roscore` 
     - This is your ROS brain, so to speak. It coordinates all ROS functions that are subsequently deployed
   - In the first terminal, or another if you wish (having ensured that you did your sourcing, last reminder) you can begin to run or launch packages. 
     - To run a package use the following syntax: `rosrun <package_name> <program_name> [args]` \
       >Example: `rosrun merrikin_topics topic_subscriber.py`
     - To launch a set of packages use the following syntax: `roslaunch <package_name> <launch_file_name> [args]` \
       >Example: `roslaunch merrikin_services serrvices.launch`
       
### Packages Included in this Repository
