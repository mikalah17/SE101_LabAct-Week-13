def add_unsigned_8bit(a, b):
    return (a + b) & 0xFF
 
print(format(4, "08b"), format(7, "08b"))     # the final position (4, 7) in binary
print(add_unsigned_8bit(250, 10))             # character at x = 250 moves right by 10
