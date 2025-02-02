src contains two Python files. One which is meant for data collection from the NeuroSky kit and the other for transforming the data into a Pandas DataFrame, which in the case of the example code plots the brainwave data in a normalized fashion.

*seizure-detection.py does not contain the algorithms in place for detecting seizures (this is counter-intuitive but the naming scheme isn't perfect by nature of the time constraints present in a hackathon), such methods would either need to be added or approached within the .ipynb files*  


THe .ipynb files are meant to train the AI model for the simulation in silico modelling which shows the effect of temperature on seizure activity, along with establishing what is a seizure vs. what isn't, essentially detecting the seizure.
