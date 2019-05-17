This repository contains two simple files that will enable the LED, FAN, and Power/Reset buttons on the:
- Kintaro SNES case with Pine64 ROCK64 Board
- ROSHAMBO Super Famicom case for the Pine64 ROCK64 and ROCKPRO64 Boards

Here is information about the Kintaro SNES Case (Meant for a RPI, works for Rock64!): https://www.kintaro.co/products/super-kintaro-kuma-system
Here is information about the Roshambo Super Famicom case: https://www.cloudmedia.com/?product=roshambo-retro-gaming-case
Here is information about the Rock64: https://www.pine64.org/rock64/
Here is information about the RockPro64: https://www.pine64.org/rockpro64/

PRE-REQS

1) This script uses python, your Linux OS will need to have python installed. I have tested with python 2.7.

2) You will also need a copy of the R64-GPIO script installed. This is a python class that lets the kintaro-case.py program use the same pin commands as the Raspberry PI. Simply download the R64 folder from this repo and put it in the same folder that the kintaro-case.py will run. https://github.com/mrfixit2001/Rock64-R64.GPIO


INSTRUCTIONS HOW TO USE

First make sure you have read and met the two items listed under PRE-REQS.

The current folder structure in this repo is setup to be directly downloadable into RECALBOX (But you can use these with any Linux OS, keep reading)

MrFixIt's distrobutions of RECALBOX should already include these scripts out-of-the-box.
RECALBOX for the ROCK64 can be found here: https://github.com/mrfixit2001/recalbox_rock64/releases
RECALBOX for the ROCKPRO64 can be found here: https://github.com/mrfixit2001/recalbox_rockpro64/releases

If you are using recalbox and these scripts are not there (or you want to update them), just download and merge the two files into the folders they are already in and reboot!

These scripts can be used in any Linux OS, it does NOT need to be recalbox. There's a number of different ways to run a program when Linux boots up. This repo uses the file "S100kintaro" as an init.d bash script which runs at boot, but you don't need to use init.d, you can use systemd as well. 

If you want to use the included S100kintaro init.d script, put this in /etc/init.d and enable it to start when your ROCK64 is powered on. You will then need to update line 7 to point to the folder that you have choosen to put kintaro-case.py in. 

If you want to use systemd, just make a new service file in /etc/systemd/system, set it's Execstart to the location of where you've saved kintaro-case.py, and enable your new systemd service.

***Don't forget the R64-GPIO in the same folder as kintaro-case.py (or embed it in your python folder) - read the pre-reqs***
