munki_install_check_script
==========================
replace new_version with the version number that you are updating to
plist needs the path to the application in questions info.plist
if the new_version number is greater than the version number in the 
applications info.plist, the script return a 0 to munki and the update 
installs
