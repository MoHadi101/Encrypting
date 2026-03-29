import random
import string


chars = " " + string.punctuation + string.ascii_letters + string.digits

chars = list(chars) # convert string to list
# random.shuffle(chars) # shuffle the list
key = chars.copy() # create a copy of the list to use as the key

random.shuffle(key) # shuffle the key list

# print(f"chars: {chars}")
# print(key)

# encryption
plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter) # find the index of the letter in the chars list
    cipher_text += key[index] # add the corresponding letter from the key list to the cipher text

print(f"Oringinal text: {plain_text}")
print(f"encrypted text: {cipher_text}")


# decryption
cipher_text = input("Enter the text to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter) # find the index of the letter in the key list
    plain_text += chars[index] # add the corresponding letter from the chars list to the plain text
print(f"ecrypted text: {cipher_text}")
print(f"Oringinal text: {plain_text}")
