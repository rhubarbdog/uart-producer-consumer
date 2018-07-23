#
# Author Phil Hall
# CopyLeft July 2018

from microbit import *

DELAY=50

uart.init(baudrate=9600,bits=8,parity=None,tx=pin1,rx=pin0)

clock=0
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
        
    if message==None:
        display.show(Image.ALL_CLOCKS[clock])
    else:
        display.scroll('"'+message+'"')
        clk=0

    rt=running_time()
    if rt<save_time or rt-save_time>=200:
        clock=(clock+1)%len(Image.ALL_CLOCKS)
        save_time=rt

#
# restore uart so USB works
uart.init(115200)

display.clear()
