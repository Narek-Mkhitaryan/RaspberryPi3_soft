# Sensor Integrations: BME280 & LTR390
This repository provides integration for two widely used environmental sensors: BME280 and LTR390. These sensors can be used to measure environmental parameters such as temperature, humidity, pressure, and UV light intensity.

## BME280
The BME280 is a highly accurate sensor from Bosch that combines a temperature, humidity, and pressure sensor in a single compact device. It's perfect for a variety of applications, including weather stations, climate monitoring, and IoT projects. The sensor communicates with microcontrollers over I2C or SPI interfaces and provides high-resolution data that can be used for environmental sensing in embedded systems.

### Key Features:

Temperature: ±1°C
Humidity: ±3% RH
Pressure: ±1 hPa

Low power consumption
I2C & SPI interface
Datasheet: BME280 Datasheet
*******************************************************************************
## LTR390
The LTR390 is a precision UV light sensor from LITE-ON, designed to measure ultraviolet (UV) light intensity in the 200–400nm range. This sensor is especially useful in applications like UV index monitoring, outdoor environmental monitoring, and wearable health devices. The LTR390 is capable of high-speed measurements with low power consumption, making it ideal for portable devices.

### Key Features:

Measures UV light intensity (200–400nm)
High accuracy and low power consumption
I2C interface for easy integration
Wide dynamic range
Datasheet: LTR390 Datasheet

********************************************************************************

# Which file for what:

*** bme280Sensor.py  --> *** code in python which read information from sensor bme280
*** ltr390Sensor.py --> *** Code in python which read infotmation from sensor ltr390
*** main.py -->***  main file wich run the porgrame and return results

*** reuarement.tet --> *** .txt file wich contain all needed librarys


********************************************************************************
[!TIP]
How to run the code:


Step 1: Creat virtual environment

    python3 -m venv [name_of_your_environment]

Step 2: Enter in environment

    source [name_of_your_environement]/bin/activate

Step 3: Install all needed lybrarys 

    pip install -r requirements.txt

Step 4: Run the Programm 
 
    python3 main.py

Step 5: Deactivate environement 

    deactivate
