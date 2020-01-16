from des_algorithm.functions import get_keys, permutate, xor, Step
from des_tools.tables import PI_1, PI
from des_tools.text_to_bits import *

ENCRYPT = True
DECRYPT = False

"""
encrypt/decrypt 8 bytes string by des algorithm with 8 bytes given key.
"""
def des(text, key, encrypt=ENCRYPT):
	# convert the text to bits
	text = string_to_bit_array(text)
	# defined the keys order(
	if encrypt:
		func_range = range(1, 17)
	else:
		func_range = range(16, 0, -1)
	# Initial Permutation
	text = permutate(text, PI)
	# L and R swapped
	L = text[0:32]
	R = text[32:]
	# generate 16 keys
	keys = get_keys(key)
	"""                      
	MAKE THE 4 STEPS OF FUNCTION F:        
	1) Expansion E           
	2)XOR with round key     
	3)S-box substitution     
	4)Permutation
	---------------------------
	5)do xor on f function output and left side
	6)L and R swapped
	16 times with 16 different keys, for encrypt key order from 1 to 16, for decrypt from 16 to 1.         
	"""
	for i in func_range:
		# do function f on key and R
		f_out = Step(R, keys[i])
		# do xor on f function output and left side
		L = xor(f_out, L)
		# L and R swapped
		L, R = R, L

	# L and R swapped again at the end of the cipher, i.e., after round 16
	# followed by a final permutation
	text = R + L
	#  Final Permutation
	finalAns = permutate(text, PI_1)
	# cast finalAns from str array to int array
	finalAns = [int(num) for num in finalAns]
	# cast finalAns from bits to string
	finalAns = bit_array_to_string(finalAns)
	return finalAns
