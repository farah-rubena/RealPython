# create a bytes object consisting of five null (0x00) bytes. All of the following will work except one. Select the one that doesn't work
#
#
print(bytes(0, 0, 0, 0, 0))
print(bytes("\x00\x00\x00\x00\x00", "utf-8"))
print(bytes([0] * 5))
print(bytes(5))
