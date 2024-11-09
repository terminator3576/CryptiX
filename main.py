from hash import main

def get_public_key():
  public_key = []
  # Read key.txt and populate public_key list
  with open('key.txt', 'r') as file:
      for line in file:
          number = int(line.strip())  # Convert each line to an integer
          public_key.append(number)
  return public_key

with open('input.txt', 'r') as file:
        message = file.read()


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


try:
    x = main(str(message), get_public_key(), security)
    print('The hashed answer is: ', hex(x))
except Exception as e:
    print(f"An error occured: {e}")