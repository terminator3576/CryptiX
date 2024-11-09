from hash import main

def get_public_key():
  '''Get the public key from key.txt'''
  public_key = []
  with open('key.txt', 'r') as file:
      for line in file:
          number = int(line.strip())  
          public_key.append(number)
  return public_key

with open('input.txt', 'r') as file:
        message = file.read()

#security level input
while True:
    security = input("Enter a security level: ")
    if security == '':
        print("Please enter a valid security level.")
    else:
        try:
            int(security)
            break
        except ValueError:
            print("Please enter a valid security level")

#process message
try:
    x = main(str(message), get_public_key(), security)
    print('The hashed answer is: ', hex(x))
except Exception as e:
    print(f"An error occured: {e}")
