def bin_to_dec(bits):
    """Convert a binary string such as '1101' to a decimal integer
    using the positional method: digit x 2^position."""
    total = 0
    # TODO: loop over the digits starting from the RIGHT (position 0)
    return total
 
def dec_to_bin(n):
    """Convert a non-negative integer to a binary string
    using repeated division by 2 (collect the remainders)."""
    if n == 0:
        return "0"
    bits = ""
    # TODO: while n > 0: take n % 2, add it to the FRONT of bits, then n = n // 2
    return bits
 
if __name__ == "__main__":
    for b in ["1101", "101101", "11111111", "10100101"]:
        print(b, bin_to_dec(b), int(b, 2))            # last two numbers must match
    for d in [13, 45, 200, 255]:
        print(d, dec_to_bin(d), bin(d)[2:], hex(d)[2:].upper())
