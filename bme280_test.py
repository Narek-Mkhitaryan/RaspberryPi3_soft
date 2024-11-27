import time
import smbus2
import bme280
import board
import adafruit_ltr39



class SensorReader:
    def __init__(self):
        # Initialize I2C for both sensors
        self.i2c = board.I2C()  # Default I2C bus

        # Initialize LTR390 UV and ambient light sensor
        self.ltr = adafruit_ltr390.LTR390(self.i2c)

        # Initialize BME280 environmental sensor
        self.bus = smbus2.SMBus(1)  # I2C bus 1 (use appropriate bus for your device)
        self.address = 0x76  # BME280 default I2C address
        self.calibration_param = bme280.load_calibration_params(self.bus, self.address)

    def read_uv_and_light(self):
        """Reads UV and ambient light values from the LTR390 sensor."""
        uv = self.ltr.uvs  # Get the UV light intensity from the sensor
        light = self.ltr.light  # Get the ambient light intensity from the sensor
        print(f"UV: {uv}\t\tAmbient Light: {light}")

    def read_bme280(self):
        """Reads temperature, pressure, and humidity from the BME280 sensor."""
        data = bme280.sample(self.bus, self.address, self.calibration_param)
        temperature = data.temperature
        pressure = data.pressure
        humidity = data.humidity

        print(f"Temperature: {temperature:.2f} °C")
        print(f"Pressure: {pressure:.2f} hPa")
        print(f"Humidity: {humidity:.2f} %")
        print("*************************")

def main():
    # Create an instance of the SensorReader class
    sensor_reader = SensorReader()

    # Read and print UV and ambient light data
    sensor_reader.read_uv_and_light()

    # Read and print BME280 data (temperature, pressure, humidity)
    sensor_reader.read_bme280()

0
