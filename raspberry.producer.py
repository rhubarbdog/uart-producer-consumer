#
# Author Phil Hall
# CopyLeft July 2018

import posix
import termios

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

    while True:
        try:
            message=input("Producer :")
        except EOFError:
            print("")
            break

        binmess=bytearray(len(message))
        for i in range(len(message)):
            binmess[i]=ord(message[i])
            
        posix.write(fd,binmess)

    posix.close(fd)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    
