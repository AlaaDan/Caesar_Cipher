alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)
mode = True


def ceasar(direction, text, shift):
  if direction  == "encode":
    cipher_code = ""
    position = 0
    for char in text:
      if char in alphabet:
        position = alphabet.index(char)
      
        if position > 20 and position+shift > 25:
          new_position= shift-1
          cipher_code+=alphabet[new_position]
        else:
          new_position = (position + shift)
          cipher_code+=alphabet[new_position]
      else:
        cipher_code+=char
    print(f'The encoded text is: {cipher_code}')
  
  elif direction == "decode":
    cipher_code = ""
    position = 0
    for char in text:
      if char in alphabet:
        position = alphabet.index(char)
        if position > 20 and position+shift > 25:
          new_position= position-shift
          cipher_code+=alphabet[new_position]
        else:
          new_position = (position - shift)
          cipher_code+=alphabet[new_position]
      else:
        cipher_code+= char
    
    print(f'The decoded text is: {cipher_code}')
    
on = True
while on:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if shift > 26:
    shift = shift%26
  
  ceasar(direction, text, shift)
  repeat = input("If you want to go again, Type: 'yes'. Otherwise Type: 'no'.").lower()
  if repeat != "no" or repeat != "yes":
    on = False
    print("Wrong input. The program is now offline")
  elif repeat == "no":
    on = False
    print("Thanks for using the Caesar Cipher.")
    
  
 

