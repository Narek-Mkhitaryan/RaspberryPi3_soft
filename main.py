from bme280Sensor import BME280Sensor
from ltr390Sensor import LTR390Sensor


bme = BME280Sensor()

ltr = LTR390Sensor()
print(bme.get_data())
print(ltr.read_uv_and_light())


