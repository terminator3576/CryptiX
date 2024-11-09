#primary padding function
def pad_message(message):
  if len(str(message)) >= 1024:
    return message
    
  #Convert the message to binary
  binary_message = ''.join(format(ord(c), '08b') for c in message)

  #Calculate the length of the original message in bits
  original_length = len(binary_message)

  #Calculate the number of padding bits required
  padding_length = 1024 - original_length - 64

  #Create the padding
  padding = '1' + '0' * padding_length

  #Convert the original length to a 64-bit binary string
  length_binary = format(original_length, '064b')

  #Concatenate the binary message, padding, and length
  padded_message = binary_message + padding + length_binary

  return padded_message
