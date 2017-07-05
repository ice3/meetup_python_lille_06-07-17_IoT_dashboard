import dht22
import pyb

dht22.init(nc_pin=None, gnd_pin=None, vcc_pin=None, data_pin='C7')
while True:
    try:
        (hum, tem) = dht22.measure()
        print("DATA {} {}".format(hum, tem))
    except Exception as e:
        print("ohoh :(")
        print("{}".format(e))

    pyb.delay(3000)
