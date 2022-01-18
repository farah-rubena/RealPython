s = "foobar"

print(s[:] is s)

print(s[::-1][::-1] == s)

print(s[::-1][::-1] is s)

print(s[:] == s)
