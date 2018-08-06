#
# Author Phil Hall
# July 2018 - Public Domain

from microbit import *


DELAY=50

uart.init(baudrate=9600,bits=8,parity=None,tx=pin1,rx=pin0)

SPINNER=( Image("00900:00000:00500:00000:00000"),
          Image("00090:00000:00500:00000:00000"),
          Image("00000:00009:00500:00000:00000"),
          Image("00000:00000:00509:00000:00000"),
          Image("00000:00000:00500:00009:00000"),
          Image("00000:00000:00500:00000:00090"),
          Image("00000:00000:00500:00000:00900"),
          Image("00000:00000:00500:00000:09000"),
          Image("00000:00000:00500:90000:00000"),
          Image("00000:00000:90500:00000:00000"),
          Image("00000:90000:00500:00000:00000"),
          Image("09000:00000:00500:00000:00000") )

busy=0
save_time=running_time()
while True:

    message=None
    data=uart.read()

    if data is not None and data!=b'\x00':
        message=data
        while True:
            sleep(DELAY)
            data=uart.read()
            if data is None:
                break
            message+=data

        new=""
        for c in message:
            new+=chr(c)

        message=new


    if message=='Exit' or button_b.is_pressed():
        break
        
    if message is not None:
        display.scroll('"'+message+'"')


    rt=running_time()
    if rt<save_time or rt-save_time>=200:
        display.show(SPINNER[busy])
        busy=(busy+1)%len(SPINNER)
        save_time=rt

#
# restore uart so USB works
uart.init(115200)

display.clear()
