# Background
Florida Atlantic University hosted a BioTech Bridge Hackathon, in which the prompt was for "longevity". Essentially, solutions were meant to be innovative creations that would potentially solve problems or at least, develop a framework, for a longer, healthier life. My group decided to work with a NeuroSky device in order to read in EEG brainwave data in order to attempt seizure detection, which would then be proposed into a lab experiment with mice for administering a thermal shock on seizure induced mice once a seizure is detected. Our rationale was that this would be an improved, non-invasive solution for seizure intervention and could be marketed for consumer use once proper testing occurred.

# Overview of Files and Setup
## NeuroSky Interface

***Note:*** *This was all done on a Windows machine, if you utilize a different operating system, this may not work for you and certain tweaks should be considered.*

We used a NeuroSky Mindwave Mobile 2, though `mindwave.py` should theoretically work for other devices. If it does not, then experiment with other sources of code that can be found on GitHub, or experiment with the Python library *pymindwave2*, whose starting example code was used in `mindwave.py`.

Here's a link to the GitHub Repo [pymindwave2 GitHub Page](https://github.com/PrinceEGY/pymindwave2)

When using NeuroSky Mindwave Mobile 2, I installed some software that was developed and shipped through the NeuroSky store. As I developed on a Windows machine, I downloaded and installed *Windows Developer Tools*. **However**, truthfully, you theoretically only need ***ThinkGear Connector***. I was not able to install it by itself for some reason, so I opted for installing the entire toolkit.

Once you have at least ***ThinkGear Connector*** installed on your machine, connect your NeuroSky device to your machine either via a wired connection or a wireless connection through BlueTooth. 

In our case, we had a wireless device so we needed to turn on and pair the device to our machine. A pop-up may show prompting you for a passcode of some sort in order to pair with the device, this code should be on a user manual that came with your device. 

Once a connection has been made, you're ready to start ***ThinkGear Connector***. *You may lose connection to your NeuroSky device, in my experince this is fine, as ThinkGear Connector will be listening while `mindwave.py` makes a connection*

### File Overview
Once you have connected and paired your device and started ***ThinkGear Connector***, run `src\mindwave.py`.
This will create a `sessions` folder and a nested `User` folder whose name is dictated by the *user_name* argument in `mindwave.py#SessionConfig()`. Some data inside the `User` folder will populate once the script finishes. The main file you're concerned with is `data.csv`.

Running `src\eeg-data.py` will parse this csv using *Pandas* and populate a plot using *matplotlib* for the brainwave graph. Ensure that your path to the `data.csv` file is explicitly passed in the script. Running `eeg-data.py` may require it to be run in an interactive environment in order to visualize plots.  

This is about the groundwork that is supplied for interfacing with your NeuroSky device. Past this, it requires more programming in order to make use of this EEG data.

## Seizure Detection/Simulation
There are 2 .ipynb files: 
  `EEG_DATABASE.ipynb` takes an acquired database including EEG data that includes both people who have seizures and people who do not experience seizures. It then applies machine learning techniques that make use of a non-linear transform kernel to predict seizure activity. 
  A rough protocol considered during the development of the project which could potentially be used for future research when fully fleshed out:
    `SimulationsBioTech.ipynb` makes use of the *Brian2* library to simulate a network of LiF neurons that are spiking, with parameters that induce seizures. It tampers neuronal parameters with respect to what is affected by temperature as a simulation of applying thermal change to change brain wave activity.

# Rough Experimental Protocol
  The following is a proposed rough protocol that was developed during the time of this project:

![image](https://github.com/user-attachments/assets/5f1e0e2a-fd23-4264-9e2c-76eabc855ef4)
*Rough sketch and proposal courtesy of team member during Hackathon*
# Closing Thoughts
While rough in scope, with more time and resources than what was alloted during this Hackathon, a project could potentially be dedicated for this topic.

