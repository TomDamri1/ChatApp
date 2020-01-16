"""
HOW TO USE:
    use the function get_keys(initial_key,in_bits=False)
        initial key = the key u want to encrypt with.
        in bits ? if the key already in bits set it to True !!!

    the function returns a list
        0 index = the original key
        1...16 index all the keys by order.

    this function has been tested with this guide:
        http://page.math.tu-berlin.de/~kant/teaching/hess/krypto-ws2006/des.htm
        use this guide , the other one was wrong.

"""
from encryption.DES.des_tools.tables import PC2, PC1, ITERATION_TABLE, E, P, S_TABLES
from encryption.DES.des_tools.text_to_bits import text_to_bits


def permutate(item, table):
    """
    permutating the item with the table.
    :param item: the item to permutate
    :param table: the table to permutate with
    :return: a list with the permutation.
    """
    Ex = []
    Ex = [item[x - 1] for x in table]
    return Ex


def permutate_pc2(key):
    permutate_key = ""
    for i in PC2:
        permutate_key += key[i - 1]
    return permutate_key


def permutate_pc1(key):
    """
    seems to work for PC1
    :param key:
    :param pc:
    :return:
    """
    permutate_key = ""
    j = 0
    for i in PC1:
        permutate_key += key[i - 1]
        j += 1
    permutate_key = permutate_key[:29] + permutate_key[29::]
    return permutate_key


def break_and_left_shift_key(key, numberOfShifts=1):
    """
    takes the key (56 bits) and split it to  half , then using left shift for each side
    :param key: 56 bit key that we got from the function permutate
    :return:  the new key after breaking and shifting
    example:
    key = 1 2 3 4 5 6 7 8
    numberOfShifts = 1
    L = 1 2 3 4 => 2 3 4 1
    R = 5 6 7 8 => 6 7 8 5
    new key = R+L = 6 7 8 5 2 3 4 1
    """

    key_left = key[1:28] + key[0]
    key_right = key[29:] + key[28]
    if numberOfShifts != 1:
        key_left = key_left[1:] + key_left[0]
        key_right = key_right[1:] + key_right[0]

    return key_left + key_right

# make n bits shift left to keys according to ITERATION_TABLE
def iterator(key):
    this_key = key
    keys_1_to_16 = [this_key, ]
    for i in ITERATION_TABLE:
        this_key = break_and_left_shift_key(this_key, i)
        keys_1_to_16.append(this_key)

    return keys_1_to_16

"""
generate 16 keys for encrypt and decrypt
"""
def get_keys(inital_key, in_bits=False):
    if in_bits:
        key = inital_key
    else:
        key = text_to_bits(inital_key)
    permutate_key = permutate_pc1(key)
    keys_1_to_16 = iterator(permutate_key)
    final_keys_1_to_16 = []
    for i in keys_1_to_16:
        final_keys_1_to_16.append(permutate_pc2(i))
    return final_keys_1_to_16


def xor(L1, L2):
    return [str(int(a) ^ int(b)) for a, b in zip(L1, L2)]

"""
MAKE THE 4 STEPS:
1) Expansion E
2)XOR with round key
3)S-box substitution
4)Permutation
"""
def Step(R1, key):
    # Expansion E (increase num of bits from 32 to 48)
    R1 = permutate(R1, E)
    # make XOR operation between the bits of the input the the keys.
    R1 = xor(R1, list(key))
    R1 = sbox_substitution(R1)
    return permutate(R1, P)


"""
S-Box substitution
Eight substitution tables
6 bits of input to any box, 4 bits of output from any box.
"""


def sbox_substitution(word):
    result = ""
    j = 0
    k = 6
    for i in range(8):
        result += step_box_sub(word[j:k], i + 1)
        j = k
        k += 6
    return result


"""
take the first bit and the last bit together and them symbol the number of row at the s box table
take the four bits on the middle  together and them symbol the number of column at the s box table
take the number from the s-box that we get from the cuts of the row and the column (4 bits number)
"""
def step_box_sub(binList, tableNum):
    # Assemble the first number symbol the number of row at the s box table
    firstNum = [binList[0], binList[5]]
    firstNum = (int("".join(str(x) for x in firstNum), 2))
    # Assemble the second number symbol the number of column at the s box table
    secondNum = [binList[1], binList[2], binList[3], binList[4]]
    secondNum = (int("".join(str(x) for x in secondNum), 2))
    return bin(S_TABLES[tableNum][firstNum][secondNum])[2:].zfill(4)
