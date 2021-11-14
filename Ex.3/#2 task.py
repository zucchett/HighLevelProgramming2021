import struct
t = 123456
packed_string = struct.pack("HH", *t)
unpacked_float = struct.unpack("f", packed_string)[0]
print(unpacked_float)