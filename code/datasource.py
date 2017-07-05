import random
import sys
import glob
import serial
from collections import deque
import datetime
from threading import Thread


def serial_path():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


class SerialReader(Thread):
    """A threaded class to read from serial devices.

    Bad => only read from the first device availlable.
    """

    def __init__(self):
        """Init."""
        Thread.__init__(self)
        self.data = deque([], 200)
        self.serial = serial.Serial(serial_path()[0])
        self.running = False

    def read_from_serial(self):
        """Read DHT22 data from serial."""
        self.running = True
        while self.running:
            data = self.serial.readline().decode()
            if "DATA" not in data:
                print("ERREUR : {}".format(data))
                continue

            try:
                _, hum, tem = data.split(" ")
                hum = float(hum)
                tem = float(tem)
            except Exception as e:
                print("ERREUR : ligne nulle {}".format(e))
            else:
                self.data.append([datetime.datetime.now(), hum, tem])

    def get_data(self):
        return list(zip(*self.data))

    def run(self):
        """Starts the thread => read from serial until interrupted."""
        self.read_from_serial()

    def stop(self):
        self.running = False
        self.serial.write_timeout = 0.001
        self.join()
        del self.serial



def fake_1_d():
    return [random.randint(0, 200) for _ in range(random.randint(10, 199))]



if __name__ == "__main__":
    sr = SerialReader()
    sr.start()
    import IPython; IPython.embed()
