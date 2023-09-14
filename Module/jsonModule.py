import json 

# Json module methods
# JSON is an object similar to dictionaries containing plain data
# Json module has methods to convert Json (JavaScript object notation) to dict
print("loads")
Json_Type_Info = '{"Name" : "SicKickForm", "Age" : 18}'
Python_Dict_Info = json.loads(Json_Type_Info)
# When You convert from Python to Json objects change to Json equivalent
# Python |   JSON
# dict 	 |  Object
# list 	 |  Array
# tuple  |  Array
# str 	 |  String
# int 	 |  Number
# float  |  Number
# True   |  true
# False  |  false
# None   |  null
print("dumps")
Json_Type_Info2 = json.dumps(Python_Dict_Info)
Info = {
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
print(json.dumps(Info))
# Use the indent parameter to specify numbers of indents to output
# Use the separators parameter to set a separator
# Default separator is (", " , ": ")
# Use sort-keys command to specify is the keys should be ordered or not
print(json.dumps(Info, indent=1, separators=('. ' , ' = '), sort_keys=True))
# load() function is to read Json data from a file and convert to Python dict
print("load")
# dump() function is to read Python file and convert to Json file
print("dump")

