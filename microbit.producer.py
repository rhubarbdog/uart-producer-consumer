#
# Author Phil Hall
# copyleft July 2018

from microbit import *

BUSY=[Image("00000:00000:00900:00000:00000:"),
      Image.SQUARE_SMALL,
      Image.SQUARE,
      Image.SQUARE_SMALL]

MENU=("Horse","Cat","Rabbit","This is a sentence of considerable length",
      "mule")

menu=0
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


    display.show(BUSY[busy])

    rt=running_time()
    if rt<save_time or rt-save_time>200:
        busy=(busy+1)%len(BUSY)
        save_time=rt

#
# restore uart so USB works
uart.init(115200)

display.clear()
