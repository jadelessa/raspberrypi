# UPDATE YOUR SOFTWARE AND OS

# The software on Raspbian will be periodically updated online,
# bringing with it bug fixes and security updates. Those don’t
# automatically sync with the Raspberry Pi, though, and you
# should regularly check to see if there are any updates for your
# system. This is handled entirely in the terminal again, much like
# the software installation.
# The update process consists of two parts: first you need to
# update the repositories; this is the list of available software
# and their versions kept on your system. You do that by first
# entering the command:

sudo apt-get update

# This will check online to see the state of the software
# repositories and report back to the Raspberry Pi, saving any
# changes. It will then determine what software can be and should
# be updated, but you then need to tell it to perform the update
# with this command:

sudo apt-get upgrade

# Every now and then, there may be a major update to the
# Raspbian operating system, bringing with it big changes
# like a new interface or browser, etc. It’s very rare, but when it
# happens, you can perform the upgrade with:

sudo apt dist-upgrade