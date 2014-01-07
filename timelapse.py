##!/usr/bin/env python
#
# timelapse.py by Goran Gustafsson 
# http://gorgusgfx.se
#
# 

import os
from time import localtime,strftime,sleep

# First declare some variables

folder=''
filename=''
period=20						# Time period between shots
path="/mnt/usb/timelapse/"				# Path to where the images will be stored


# Main loop
while(True):
	folder=strftime("%Y%m%d",localtime())		# Fix folder and pathnamns
	folder=path+folder
	filename=strftime("%H%M%S",localtime())

	if not os.path.exists(folder):			# Check if the folder exists,
	        os.makedirs(folder)			# If not, create it

	command="raspistill "
	command+=" -awb auto "				# automatic whitebalance
	command+=" -mm average "			# Meter mode average
	command+=" -ev 0 "				# ev=0
	command+=" -ex auto "
	command+=" -sh 11 "				# Sharpness
	command+=" -br 50"
	command+=" -co 0 "
	command+=" -sa 4 "
	command+=" -ifx none"				# no image effects
	command+=" -q 75"				# image quality
	command+=" -w 2592 "				# image width
	command+=" -h 1080 "				# image height
	command+=" -o " + str(folder) + "/" 
	command+=str(filename) + ".jpg"			# Output file

	os.system(command)				# Execute the command
        sleep(period)					# Wait for next iteration

