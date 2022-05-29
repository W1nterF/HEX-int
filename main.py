#====================IMPORTS====================
import sys
#====================FUNCTIONS====================

def toBytesArray(val):
    hexarray = bytearray.fromhex(val[2:])
    str_val = ''.join(format(x, '02x') for x in hexarray)
    print("Byte array format:", hexarray)
    length = len(hexarray)
    print("Number of bytes: ", length)
    
    return str_val

def to_little(val):
  little_endian = bytearray.fromhex(val[2:])
  little_endian.reverse()
  
  str_LE = ''.join(format(x, '02x') for x in little_endian)
  return str_LE

def to_big(value):
    bits = 16
    val = int(value, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

def from_le_to_hex(little_endian):
    print(f"From Little endian to HEX: {hex(little_endian)}")

def from_be_to_hex(big_endian):
    print(f"From Big endian to HEX: {hex(big_endian)}")

#====================MAIN====================
while True:
    value = str(input("Enter HEX number >> "))
    if value == "exit":
        sys.exit()
    bytesArray = toBytesArray(value)
    little_endian = to_little(value)
    big_endian = to_big(value)
    print(f"----------\nLittle endian HEX: {little_endian}")
    print(f"Little-endian: {int(little_endian, 16)}")
    print(f"Big-endian: {big_endian}")
    from_le_to_hex(int(little_endian,16))
    from_be_to_hex(big_endian)
    input("Press any key to continue...")
