boot = """# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import pyb
pyb.main('main.py') # main script to run after this one
pyb.usb_mode('CDC+MSC') # act as a serial and a storage device
#pyb.usb_mode('CDC+HID') # act as a serial device and a mouse
"""

f = open("boot.py", "w")
f.write(boot)
f.close()


print("\n".join(open("boot.py", "r").readlines()))