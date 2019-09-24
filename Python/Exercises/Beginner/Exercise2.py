'''
sys.version_info
A tuple containing the five components of the version number: major, minor, micro,
releaselevel, and serial.

All values except releaselevel are integers; the release
level is 'alpha', 'beta', 'candidate', or 'final'.

The sys.version_info value corresponding to the Python version 2.0 is
(2, 0, 0, 'final', 0).

The components can also be accessed by name, so sys.version_info[0] is equivalent to
sys.version_info.major and so on.
-----------------------------
sys.version
A string containing the version number of the Python
interpreter plus additional information on the build number and compiler
used. This string is displayed when the interactive interpreter is
started. Do not extract version information out of it, rather, use
version_info and the functions provided by the platform module.

'''
import sys
print('System Version')
print(sys.version)
print()
print('System Version Information')
print(sys.version_info)
print('Major version')      
print(sys.version_info[0])      
