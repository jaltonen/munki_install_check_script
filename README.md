munki_install_check_script
==========================
an installcheck_script for munki written in Python.
You supply a version number of your update and a path to the currently installed applications info.plist,
which is located inside the app bundle, /Application/SomeApp.app/Contents/Info.plist.  The CFBundleShortVersionString
seems to be pretty consistent across apps for supplying the version number.
if the version number you supplied for the update you are trying to install is greater than the version number in the 
applications info.plist, the script returns a 0 to munki and the update installs.  This solved issues that arose when an end user would install an update to an app outside of Managed Software Center before Managed Software Center had a chance to install it usually resulting in the update install failing and munki always thinking the update needs to be installed
