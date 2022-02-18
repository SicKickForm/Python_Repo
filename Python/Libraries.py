# Modules
# Python has built-in standard modules, importable modules and external modules
# Install external module A from PyPI (Python package index) using
# pip install A command on your device terminal
# You can create modules by saving a file with .py format
# You can call modules using import command
# Use import module as A command to rename module to A
# Use from module import A command to call only A from module
# When using from method don't refer to module other functions and variables
# Use module.A command to use A from module
# Use dir() function to get all methods and variables in a module

# Built-in modules
import platform
import datetime as Date
import math
# Platform module methods
# print(platform.__builtins__)
print(platform.__cached__)
print(platform.__file__)
print(platform.__name__)
print(platform.__version__)
platform.__doc__
platform.__loader__
platform.__package__
platform.__spec__
print(platform.release())
print(platform.processor())
print(platform.sys)
print(platform.system())
print(platform.uname())
print(platform.version())
print(platform.win32_edition())
print(platform.win32_is_iot())
print(platform.win32_ver())
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.java_ver())
print(platform.mac_ver())
print(platform.python_branch())
print(platform.python_build())
print(platform.python_compiler())
print(platform.python_implementation())
print(platform.python_revision())
print(platform.python_version())
print(platform.python_version_tuple())
platform.architecture()
platform.uname_result
platform.freedesktop_os_release
platform.system_alias

# Datetime module methods
# Use datetime() constructor command Create time objects
# You can create time objects up to micro seconds
print(Date.date(2003, 1, 17))
print(Date.time(19, 37))
print(Date.datetime(2003, 1, 17, 19, 37))
print(Date.datetime.now())
print(Date.datetime.now().year)
print(Date.datetime.now().month)
print(Date.datetime.now().day)
print(Date.datetime.now().weekday())
print(Date.datetime.now().hour)
print(Date.datetime.now().minute)
print(Date.datetime.now().second)
print(Date.datetime.now().microsecond)
# Use strftime command to format date objects into readable strings
# strftime methods
# Date and time methods
print(Date.datetime.now().strftime('%c'))
print(Date.datetime.now().strftime('%x'))
print(Date.datetime.now().strftime('%X'))
# Year methods
print(Date.datetime.now().strftime('%C'))
print(Date.datetime.now().strftime('%G'))
print(Date.datetime.now().strftime('%Y'))
print(Date.datetime.now().strftime('%y'))
# Month methods
print(Date.datetime.now().strftime('%B'))
print(Date.datetime.now().strftime('%b'))
print(Date.datetime.now().strftime('%m'))
# Week methods
print(Date.datetime.now().strftime('%U'))
print(Date.datetime.now().strftime('%W'))
print(Date.datetime.now().strftime('%V'))
# Day methods
print(Date.datetime.now().strftime('%A'))
print(Date.datetime.now().strftime('%a'))
print(Date.datetime.now().strftime('%j'))
print(Date.datetime.now().strftime('%d'))
print(Date.datetime.now().strftime('%w'))
print(Date.datetime.now().strftime('%u'))
# Hour methods
print(Date.datetime.now().strftime('%H'))
print(Date.datetime.now().strftime('%I'))
print(Date.datetime.now().strftime('%p'))
# Minute method
print(Date.datetime.now().strftime('%M'))
# Second method
print(Date.datetime.now().strftime('%S'))
# Micro second method
print(Date.datetime.now().strftime('%f'))
print(Date.datetime.now().strftime('%%'))
