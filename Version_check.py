#!/usr/bin/env python
import os
import plistlib
from distutils.version import LooseVersion

########################################################################
#
#  replace new_version with the version number that you are updating to
#  plist needs the path to the application in questions info.plist
#  if the new_version number is greater than the version number in the 
#  applications info.plist, the script return a 0 to munki and the update 
#  installs
#
########################################################################

new_version = "14.4.9"
plist = plistlib.readPlist('/Applications/Microsoft Office 2011/Microsoft Word.app/Contents/Info.plist')

########################################################################


current_version = plist['CFBundleShortVersionString']


# if a higher version or equal version is currently installed the following expression returns false
#   &#60;  replaces < less than in an xml file because < is a special xml character
install_update = LooseVersion(current_version) &#60; LooseVersion(new_version)
print install_update


if install_update == True:
#    print 'Im gonna install it'
    exit(0)
elif install_update == False:
#    print 'No go!'
    exit(1)