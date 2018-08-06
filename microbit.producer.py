#
# Author Phil Hall
# July 2018 - Public Domain

from microbit import *

MENU=("Horse","Cat","Rabbit","This is a sentence.","Mule")

menu=0

PULSATE=( Image("00000:00000:00900:00000:00000:"),
          Image.SQUARE_SMALL,
          Image.SQUARE,
          Image.SQUARE_SMALL )
busy=0

uart.init(baudrate=9600,bits=8,parity=None,tx=pin1,rx=pin0)

save_time=running_time()
while True:

    if button_a.is_pressed():

        while button_a.is_pressed():
            pass

        message=MENU[menu]
        menu=(menu+1)%len(MENU)

        display.scroll('"'+message+'"')
        
        uart.write(message)

    if button_b.is_pressed():
        break


    rt=running_time()
    if rt<save_time or rt-save_time>200:
        display.show(PULSATE[busy])
        busy=(busy+1)%len(PULSATE)
        save_time=rt

#
# restore uart so USB works
uart.init(115200)

display.clear()
