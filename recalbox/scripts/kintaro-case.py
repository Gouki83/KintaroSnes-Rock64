#!/usr/bin/python -u
# Author: Mrfixit2001 - Enables LED and Monitors for the buttons on the Kintaro SNES Case

import time
import os
import R64.GPIO as GPIO
# NOTE: the R64GPIO package doesn't support "add_event_detect", so we can't use callbacks

# Initialize
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
PCB = 10
RESET = 3
POWER = 5
LED = 7

# Tell the script if this is running on a ROCK64 or ROCKPRO64
GPIO.setrock("ROCK64")

# Setup 
GPIO.setup(PCB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RESET, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(POWER, GPIO.IN)
GPIO.setup(LED, GPIO.OUT)
IGNORE_PWR_OFF = False
if(GPIO.input(POWER) == "0"):
	# System was started with power switch off
	IGNORE_PWR_OFF = True

# Turn on LED
GPIO.output(LED, GPIO.HIGH)

# Monitor for Inputs
while True:
	if(GPIO.input(PCB) == "0"):
		if(GPIO.input(RESET) == "0"):
			print("Rebooting...")
			GPIO.output(LED, GPIO.LOW)
			time.sleep(0.2)
			GPIO.output(LED, GPIO.HIGH)
			os.system("reboot")
			break
		if(GPIO.input(POWER) == "1" and IGNORE_PWR_OFF == True):
			IGNORE_PWR_OFF = False
		if(GPIO.input(POWER) == "0" and IGNORE_PWR_OFF == False):
			if(''.join(filter(lambda c: c in string.printable, subprocess.check_output("cat /sys/firmware/devicetree/base/rockchip-suspend/status", shell=True).strip())).lower() == "okay"):
				print("Suspending...")
				GPIO.output(LED, GPIO.LOW)
				os.system("ifconfig eth0 down")
				os.system("echo mem > /sys/power/state")
				time.sleep(1)
				os.system("ifconfig eth0 up")
				GPIO.output(LED, GPIO.HIGH)
			else:
				print("Shutting down...")
				BLINK = True
				os.system("shutdown -h now")
				break
	else:
		break
	time.sleep(0.3)

GPIO.cleanup()
