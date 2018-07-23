#
# Author Phil Hall
# CopyLeft July 2018

import posix
import termios
import time

DELAY=0.1

def main():
    Raise=False
    try:
        fd=posix.open("/dev/serial0", posix.O_RDWR |\
                      posix.O_NOCTTY | posix.O_NDELAY)
    except:
        Raise=True

    if Raise:
        raise Exception("UART busy."
                        " Try /dev/serial1, /dev/ttyS0,"
                        " /dev/ttyAMA0.")

    options=termios.tcgetattr(fd)
    options[0]=termios.IGNPAR
    options[1]=0
    options[2]=termios.B9600 |\
               termios.CS8 |\
               termios.CLOCAL |\
               termios.CREAD
    options[3]=0
    
    termios.tcflush(fd,termios.TCIFLUSH)
    termios.tcsetattr(fd,termios.TCSANOW,options)

    while  True:
        message="Consumer :"
        print(message,end="\r"+message)

        data=None
        message=None
 
        while data is None:
            try:
                data=bytearray(posix.read(fd,128))
            except:
                data=None
                time.sleep(DELAY)
                continue
            
            if message is not None and data is None:
                break
            
            if message is None:
                message=data
            else:
                message+=data
                
            time.sleep(DELAY)

        new=""
        for i in message:
            new+=chr(i)

        message=new
            
        print('"'+message+'"')

    posix.close(fd)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass

    
