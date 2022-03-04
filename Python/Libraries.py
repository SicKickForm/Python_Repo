# Modules
# Python has built-in standard modules, importable modules and external modules
# Install external module A from PyPI (Python package index) using
# py -m pip --install A command on terminal
# Use py -m pip --h for more commands
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
import json
import re

# Platform module methods
# Platform module includes Your device's specs information
print(platform.__builtins__)
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
# Datetime module includes various methods to show date and time
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

# Math module methods
# Math module includes various arithmetical subjects and operators
print(math.e)
print(math.inf)
print(math.nan)
print(math.pi)
print(math.tau)
# Any
print(math.tan(90))
print(math.tanh(90))
print(math.atan(90))
print(math.atan2(1, 1))
print(math.sinh(60))
print(math.asinh(60))
print(math.cosh(30))
print(math.erf(5))
print(math.erfc(5))
print(math.fmod(11, 6))
print(math.exp(5))
print(math.expm1(5))
print(math.frexp(5))
print(math.ldexp(1.25, 2))
print(math.ceil(4.4))
print(math.trunc(5.4))
print(math.floor(5.6))
print(math.comb(5, 4))
print(math.perm(5, 4))
print(math.factorial(5))
print(math.pow(5 ** (1 / 2), 2))
print(math.sqrt(25))
print(math.gcd(15, 25))
print(math.remainder(5, 4))
print(math.copysign(-5, 2))
print(math.fabs(-5))
print(math.isclose(1.25, 1.251))
print(math.isfinite(0))
print(math.isinf(1))
print(math.isnan(1))
# W
print(math.gamma(5))
print(math.lgamma(5))
print(math.isqrt(26))
print(math.log(1))
print(math.log10(100000))
print(math.log1p(0))
print(math.log2(1))
# W - (1 , 0)
print(math.acosh(1))
# [-1 , +1]
print(math.acos(-1))
print(math.asin(1))
print(math.cos(0))
print(math.sin(0))
# (-1 , +1)
print(math.atanh(0.5))
# Angle
print(math.degrees(math.pi))
print(math.radians(90))
# Coordinated point
print(math.dist((3, 4), (0, 0)))
print(math.hypot(3, 4))
# Array
print(math.fsum((1, 2, 2)))
print(math.prod([5]))

# Json module methods
# Json module includes various methods to store and exchange Json (Java
# Script object notation) data
# converting json type data into a python dictionary
Json_Type_Info = '{"Name" : "SicKickForm", "Age" : 18}'
Python_Dict_Info = json.loads(Json_Type_Info)
# When You convert from Python to Json objects change to Json equivalent
# Python    JSON
# dict 	 =  Object
# list 	 =  Array
# tuple  =  Array
# str 	 =  String
# int 	 =  Number
# float  =  Number
# True   =  true
# False  =  false
# None   =  null
Json_Type_Info2 = json.dumps(Python_Dict_Info)
x = {
    "Name": "SicKickForm",
    "Age": 18,
    "Sensitive": False,
    "Friends": ("Dia", "akaTeen"),
    "Interests": None,
    "Languages": [
        {"Name": "Python", "Level": "Inter mediate"},
        {"Name": "Java", "Level": "Basic"}
    ]
}
print(json.dumps(x))
# Use the indent parameter to specify numbers of indents to output
# Use the separators parameter to set a separator
# Default separator is (", ",": ")
# Use sort-keys command to specify is the keys should be ordered or not
print(json.dumps(x, indent=1, separators=(', ', ': ',), sort_keys=True))
# load() function is to read Json data from a file and convert to Python dict
# dump() function is to read Python file and convert to Json file

# RegEx module methods
# Use RegEx to check if a string contains the specified search pattern
Info = 'SicKickForm of human kind is a nickname for a 18 years old boy'
print(re.search('SicKickForm', Info))
print(re.search('SicKickForm', Info).span())
print(re.search('SicKickForm', Info).string)
print(re.search('SicKickForm', Info).group())
print(re.findall('f', Info))
print(re.split('i', Info, 3))
print(re.sub('i', '/', Info, 3))
# RegEx meta characters
# Lower case charcaters in the domain
print(re.findall('[a-h]', Info))
print(re.findall('[abc]', Info))
print(re.findall('[12345]', Info))
# Single digits in the domain
print(re.findall('[6-9]', Info))
# Double digits in the domain
print(re.findall('[1-5][5-8]', Info))
# Lower and upper case charcaters in the domain
print(re.findall('[a-hA-L]', Info))
# Except given characters
print(re.findall('[^abc]', Info))
# Any character in the blank spot
print(re.findall('o.', Info))
# Zero or more characters in the blank sport
print(re.findall('i.*F', Info))
# One or more characters in the blank sport
print(re.findall('i.+F', Info))
# Zero or one characters in the blank sport
print(re.findall('i.?F', Info))
# Specified amount of  characters in the blank sport
print(re.findall('i.{2}F', Info))
# Starting with
print(bool(re.search('^S', Info)))
# Ending with
print(bool(re.search('y$', Info)))
# Either or
print(re.findall('boy|girl', Info))
# Special charcaters
# Start of string
print(bool(re.search('\ASicK', Info)))
# Start or end of a word
print(bool(re.search(r'\bSicK', Info)))
print(bool(re.search(r'Form\b', Info)))
# Middle of a word
print(bool(re.search(r'\BKick', Info)))
# End of a word
print(bool(re.search('boy\Z', Info)))
# Digits of String
print(re.findall('\d', Info))
# String without digits
print((re.findall('\D', Info)))
# Spaces of string
print(re.findall('\s', Info))
# String without spaces
print(re.findall('\S', Info))
# Letters digits underscores of string
print(re.findall('\w', Info))
# String without letters digits underscores
print(re.findall('\W', Info))
