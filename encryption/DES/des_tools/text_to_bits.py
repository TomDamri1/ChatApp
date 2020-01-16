"""
CONTAINS ALL THE TEXT TO BITS AND BITS TO TEXT FUNCTIONS
"""

import binascii


def nsplit(s):  # Split a list into sublist of size 8
	return [s[k:k + 8] for k in range(0, len(s), 8)]


def bit_array_to_string(array):  # Recreate the string from the bit array
	res = ''.join([chr(int(y, 2)) for y in [''.join([str(x) for x in _bytes]) for _bytes in nsplit(array)]])
	return res


def string_to_bit_array(text):  # Convert a string into a list of bits
	array = list()
	for char in text:
		binval = binvalue(char, 8)  # Get the char value on one byte
		array.extend([int(x) for x in list(binval)])  # Add the bits to the final list
	return array


def binvalue(val, bitsize):  # Return the binary value as a string of the given size
	binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
	if len(binval) > bitsize:
		raise ("binary value larger than the expected size")
	while len(binval) < bitsize:
		binval = "0" + binval  # Add as many 0 as needed to get the wanted size
	return binval


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
	bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
	return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-16', errors='surrogatepass'):
	n = int(bits, 2)
	return int2bytes(n).decode(encoding, errors)


def int2bytes(i):
	hex_string = '%x' % i
	n = len(hex_string)
	return binascii.unhexlify(hex_string.zfill(n + (n & 1)))
