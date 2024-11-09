import numpy as np
import string
import sys

sys.set_int_max_str_digits(100000000)

values = []
weights = []

def generate_password(text, length=40):
    ln = len(text)
    np.random.seed(int(text[ln-7:ln]))
    """Generates a random password of specified length using numpy."""
    characters = np.array(list(string.ascii_letters + string.digits + string.punctuation))
    password = ''.join(np.random.choice(characters, size=length))
    return password


def calculate_weights(binary):
    n = len(binary)
    local_weights = [0] * n  # Initialize the weights list with zeros

    for i in range(n):
        if binary[i] == '1':
            weight = 1
            if i > 0 and binary[i-1] == '1':
                weight += 1
            if i < n - 1 and binary[i+1] == '1':
                weight += 1
            local_weights[i] = weight
    return local_weights

def text_to_binary(text):
    for char in text:
        binary = format(ord(char), '08b')
        values.append(binary)
        weight = calculate_weights(binary)
        weights.append(weight)
    return values

def rearrange_bits_based_on_weights(values, weights):
    rearranged = []
    for binary, weight in zip(values, weights):
        # Create and sort tuples of (bit, weight) in one step
        sorted_bits = ''.join(bit for bit, _ in sorted(zip(binary, weight), key=lambda x: (-x[1], x[0])))
        rearranged.append(sorted_bits)
    return rearranged

def xor_binaries(original, rearranged):
    xor_result = []
    for orig, rearr in zip(original, rearranged):
        # XOR each bit and convert result back to binary string
        xor_bin = ''.join('1' if o != r else '0' for o, r in zip(orig, rearr))
        xor_result.append(xor_bin)
    return xor_result

def combine_results(values, rearranged, xor_result):
    combined = []
    for orig, rearr, xor in zip(values, rearranged, xor_result):
        combined_bin = orig + rearr + xor
        combined.append(combined_bin)
    return combined

def rotate(lst, steps='1000'):
    if not lst:
        return lst  # Return empty list as is
    steps = int(steps)
    steps = steps % len(lst)  # Handle cases where steps > len(lst)
    return lst[-steps:] + lst[:-steps]



def deterministic_shuffle(lst):
    lst = unlist(lst)
    nlst = []
    for i in lst:
        nlst.append(i)
    # Create a copy of the list to avoid modifying the original
    shuffled_lst = nlst[:]
    n = len(shuffled_lst)
    # Fisher-Yates shuffle with seeded randomness
    for i in range(n-1, 0, -1):
        j = np.random.randint(0, i+1)  # Generate a random index from 0 to i (inclusive)
        shuffled_lst[i], shuffled_lst[j] = shuffled_lst[j], shuffled_lst[i]

    return shuffled_lst


def jumble(binary_list, security):
    security = security
    counter = 0
    while counter != int(security):
        binary_list = deterministic_shuffle(binary_list)
        binary_list = rotate(binary_list)
        counter += 1
    return binary_list
        

def pad(binary_list):
    list = []
    for value in binary_list:
        count_of_ones = value.count('1')
        if count_of_ones % 2 == 0:
            value = value + '0'
        else:
            value = value + '1'

        count_no_two = value.count('10')
        if count_no_two % 2 == 0:
            value = value + '0'
        else:
            value = value + '1'

        count_no_three = value.count('01')
        if count_no_three % 2 == 0:
            value = value + '0'
        else:
            value = value + '1'
        list.append(value)

    return list

def unlist(binary_str):
    return ''.join(map(str, binary_str))

def shuffle(message):
    choice = np.random.randint(1,1000000000000)
    message = int(message) + choice
    return message

def seed(ntext, password):
    seed = zip(ntext)
    nseed = 0
    for ch in seed:
        my_character = ch[0]
        my_string = str(my_character)
        nseed += ord(my_string)

    nseed2 = 0
    for ch in password:
        my_string = str(ch)
        nseed2 += ord(my_string)
    np.random.seed(nseed + nseed2)

def inverse(message):
    choice = np.random.randint(1,1010101010101)
    if choice % 2 == 0:
        return message[::-1]
    else:
        return message


def hash_text(text, security):
    text = text_to_binary(text)
    ntext = unlist(text)
    password = generate_password(ntext, 40)
    seed(ntext, password)
    rearranged = rearrange_bits_based_on_weights(text, weights)
    xor_result = xor_binaries(values, rearranged)
    combined = combine_results(values, rearranged, xor_result)
    final = jumble(combined, security)
    final = rotate(final)
    final = rotate(final)
    final = pad(final)
    final = unlist(final)
    swap = inverse(final)
    return swap

def mainA(message, security):
    # Calculate hash values
    result = hash_text(str(message), security)
    return result