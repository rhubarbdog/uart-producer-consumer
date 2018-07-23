# uart-producer-consumer
uart producer consumer on raspberry pi and microbit.

You can connect 2 microbits or a raspberry pi and a microbit. Execute one as producer and one as consumer.  The electronics is easy, simply connect Tx to Rx and Rx to Tx. Remember to connect ground to ground.

The raspberry code is python 3. To get UART working on GPIO on the raspberry pi  had to edit /boot/cmdline.txt using the command `sudo nano /dev/cmdline.txt`. I deleteed the text `consol=serial0,115200`

The microbit consumer spins, pressing button b quits. The microbit producer pulsates. Pressing button a sends a message, button b quits. If you just power down and didn't quit microbit producer/consumer REPL over USB may cease to work, just flash and execute microbit.uart.flush.py on the offending microbit
