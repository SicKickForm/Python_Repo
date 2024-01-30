# Casting frozenset
Members = frozenset({'SicKickForm', 'Dia', 'Siren'})
print(Members)
print(type(Members))
del Members

# ------------------------------------------------------------------------------- #

# Casting specified amount of bytes
# bytes have binary numeric values and are created in hexa-deximal format
# bytes are immutable
Empty_Bytes = bytes(5)
print(Empty_Bytes)
print(type(Empty_Bytes))
Data_Bytes = bytes(b'\x57\x6f\x72\x6c\x64')
print(Data_Bytes)
del Empty_Bytes, Data_Bytes

# ------------------------------------------------------------------------------- #

# bytearray
# Casting specified amount of bytes in a bytearray
# Bytearrays are mutable
# You can use list methods on bytearrays
Mutable_Bytearray = bytearray(3)
print(Mutable_Bytearray)
print(type(Mutable_Bytearray))
Data_Bytearray = bytearray(b'\x57\x6f\x72\x6c\x64')
Data_Bytearray[0] = 255
print(Data_Bytearray)
print(Data_Bytearray[0:2])
del Data_Bytearray, Mutable_Bytearray

# ------------------------------------------------------------------------------- #

# Casting memoryview
# Use memoryview to access internal data of an objct that supports buffer protocol
# bytes and bytearray are two python objects that supoort buffer protocol
# Memoryview makes a reference to the data rather than copying the data itself
Data_Bytes = b'abcdefgh'
print(type(Data_Bytes))
print(Data_Bytes)
Data_Memoryview = memoryview(Data_Bytes)
print(type(Data_Memoryview))
print(Data_Memoryview)
# Memoryview methods
print(Data_Memoryview.tobytes())
print(Data_Memoryview.tolist())
print(Data_Memoryview.toreadonly())
print(Data_Memoryview.hex())
del Data_Memoryview, Data_Bytes

# ------------------------------------------------------------------------------- #

# Variables scope
# Variables created without indentation are global
# Variables created with indentation are local
# global and local variables with same name are different
# You can use global command to create or change global variables in local
Date = 2022
print(Date)


def Func():
    global Date
    Date = '2/9/2022'
    print(Date)


Func()

# ------------------------------------------------------------------------------- #
