#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
import time
SHUNT_OHMS = 0.05


def read():
    ina = INA219(SHUNT_OHMS)
    ina.configure(ina.RANGE_16V)

    print("Bus Voltage: %.3f V" % ina.voltage())
    try:
        print("Bus Current: %.3f mA" % ina.current())
        print("Power: %.3f mW" % ina.power())
        print("Shunt voltage: %.3f mV" % ina.shunt_voltage())
        print()
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)


if __name__ == "__main__":
    try:
        while True:
            read()
            time.sleep(0.5)
    except KeyboardInterrupt:
        print('Ctrl+C pressed')