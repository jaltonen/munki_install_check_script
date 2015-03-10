<key>installcheck_script</key>
<string>#!/usr/bin/env python	
import os
import plistlib
from distutils.version import LooseVersion


#########################################################################################
#																						#
#  replace new_version with the version number that you are updating to					#
#  filename needs the path to the application in questions info.plist					#	
#  if the new_version number is greater than the version number in the 					#
#  applications info.plist, the script return a 0 to munki and the update 				#
#  installs.  If the info.plist file specified does not exist on the target system		#
#  we are assuming the software is not installed at all and assigning a					#
#  current_version number of 0.0.1 to approximate that condition, otherwise there		#
#  were errors thrown with a null value for current_version								#
#																						#
#########################################################################################

new_version = "11.2.1"
filename = "/Applications/DaVinci Resolve/DaVinci Resolve.app/Contents/Info.plist"

if os.path.exists(filename):
    plist = plistlib.readPlist(filename)
    current_version = plist['CFBundleShortVersionString']
else:
    current_version = "0.0.1"



# if a higher version or equal version is currently installed the following expression returns false
install_update = LooseVersion(current_version) &#60; LooseVersion(new_version)
#print install_update


if install_update == True:
#    print 'Im gonna install it'
    exit(0)
elif install_update == False:
#    print 'No go!'
    exit(1)
</string>