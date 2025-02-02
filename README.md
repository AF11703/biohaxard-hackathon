src contains two Python files. One which is meant for data collection from the NeuroSky kit and the other for transforming the data into a Pandas DataFrame, which in the case of the example code plots the brainwave data in a normalized fashion.

*seizure-detection.py does not contain the algorithms in place for detecting seizures (this is counter-intuitive but the naming scheme isn't perfect by nature of the time constraints present in a hackathon), such methods would either need to be added or approached within the .ipynb files*  


There are 2 .ipynb files: 
  EEG-Database takes an acquired database including EEG data that includes both people who have seizures and people who do not experience seizures. It then applies machine learning techniques that make use of a non-linear transform kernel to predict seizure activity. 
A rough protocol considered during the development of the project which could potentially be used for future research when fully fleshed out:
  SimulationBioTech makes use of the Brian2 library to simulate a network of LiF neurons that are spiking, with parameters that induce seizures. It tampers neuronal parameters with respect to what is affected by temperature as a simulation of applying thermal change to change brain wave activity.
  
  The following is a proposed rough protocol that was developed during the time of this project:
![image](https://github.com/user-attachments/assets/5f1e0e2a-fd23-4264-9e2c-76eabc855ef4)

