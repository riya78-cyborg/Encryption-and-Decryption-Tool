import string
alphabets = string.ascii_lowercase

def encryption(plain_text, shift_key):
    cipher = ""
    for char in plain_text:
        pos = alphabets.index(char)
        new_pos = (pos+shift_key)%26
        cipher += alphabets[new_pos]
    print(f"Your encrypted text is: {cipher}")

def decryption(plain_text, shift_key):
    cipher = ""
    for char in plain_text:
        pos = alphabets.index(char)
        new_pos = (pos-shift_key)%26
        cipher += alphabets[new_pos]
    print(f"Your decrypted text is: {cipher}")


print("****CAESAR CIPHER ENCRYPTION METHOD****")
user_input = input("Enter 'e' for encryption, 'd' for decryption: ")
shift = int(input("Enter the shift key(from 0-26)"))
if user_input == 'e':
    text = input("Enter text to be encrypted: ")
    encryption(plain_text=text, shift_key=shift)
if user_input == 'd':
    text = input("Enter text to be decrypted: ")
    decryption(plain_text=text, shift_key=shift)