This repository contains two simple files that will enable the LED and buttons on the Kintaro SNES case for the Pine64 ROCK64 Board

Here is information about the Kintaro SNES Case (Meant for a RPI): https://www.kintaro.co/products/super-kintaro-kuma-system

Here is information about the Rock64: https://www.pine64.org/?page_id=7147

PRE-REQS

1) This script uses python, your Linux OS will need to have python installed. I have tested with python 2.7.

2) You will also need a copy of the R64-GPIO script installed. This is a python class that lets the kintaro-case.py program use the same pin commands as the Raspberry PI. Simply download the R64 folder from this repo and put it in the same folder that the kintaro-case.py will run. https://github.com/mrfixit2001/Rock64-R64.GPIO


INSTRUCTIONS HOW TO USE

First make sure you have read and met the two items listed under PRE-REQS.

The current folder structure in this repo is setup to be directly downable into RECALBOX. If you are using recalbox, just download and merge the two files into the folders they are already in and reboot!

With a slight modification, these scripts can be used in any Linux OS, however, it does NOT need to be recalbox. The file "S100kintaro" needs to run at boot, so put that bash script somewhere that it will run when your ROCK64 is powered on. You will then need to update line 7 to point to the folder that you have choosen to put kintaro-case.py in. (Don't forget the R64-GPIO in that folder! - read the pre-reqs)
