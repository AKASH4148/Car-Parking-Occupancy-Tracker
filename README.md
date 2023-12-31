 ## Car Park Occupancy Detection System

This repository contains the code for a car park occupancy detection system. The system uses a camera to capture images of the car park and then processes the images to detect the presence of cars. The system can be used to monitor the occupancy of a car park and to provide information to drivers about the availability of parking spaces.

### Prerequisites

The system requires the following software to be installed:

* Python 3.6 or later
* OpenCV 4.2 or later
* NumPy 1.16 or later
* Pickle

### Installation

To install the system, clone the repository and then install the required dependencies:

```
git clone https://github.com/opencv/opencv.git
cd opencv
python3 -m pip install -r requirements.txt
```

### Usage

To use the system, first start the camera. Then, run the `main.py` script. The script will capture images of the car park and process them to detect the presence of cars. The script will then display the number of available parking spaces.

### Code Explanation

The `main.py` script is the main entry point to the system. The script first imports the necessary libraries. Then, it loads the list of car park spaces from the `carparkposi` file. The script then captures images of the car park and processes them to detect the presence of cars. The script then displays the number of available parking spaces.

The `spot_det.py` script is used to create the list of car park spaces. The script allows the user to click on the image of the car park to add or remove car park spaces. The script then saves the list of car park spaces to the `carparkposi` file.

### Conclusion

This car park occupancy detection system is a simple and effective way to monitor the occupancy of a car park. The system can be used to provide information to drivers about the availability of parking spaces.
