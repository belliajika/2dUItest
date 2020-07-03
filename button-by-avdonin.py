import RPi.GPIO as GPIO
import dbus
import os
import signal
import subprocess


OMXPROC = None


def button_callback(channel):
    global OMXPROC
    print("Button was pushed!")
    if OMXPROC:
        print(OMXPROC)
        os.killpg(os.getpgid(OMXPROC.pid), signal.SIGTERM)
        OMXPROC = None
        print("Stop!")
        print('------')
    else:
       print(OMXPROC)
       OMXPROC = subprocess.Popen("omxplayer -o local musicmvd.wav",
                                  stdout=subprocess.PIPE,
                                  shell=True,
                                  preexec_fn=os.setsid)
       print("Start!")
       print('-------')
   
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, callback=button_callback, bouncetime=200)

message = input("Press Enter to quit\n\n")

GPIO.cleanup()
