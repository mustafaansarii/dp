
a = 13
b = 9

print(bin(a)[2:],  bin(b)[2:])
print(f"a = {a}, b = {b}")
print(f"a&b = {a & b}")

# The result is 00001101
print(f"a|b = {a | b}")

# The result is 00001100
print(f"a^b = {a ^ b}")

# The result is 11111111111111111111111111111010
# (assuming 32-bit unsigned int)
print(f"~a = {~a}")
a = ~a

# The result is 00010010
print(f"b<<1 = {b << 1}")

# The result is 00000100
print(f"b>>1 = {b >> 1}")