alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from art import logo
print(logo)

def caesar(direction,text,shift):
  message=""
  if direction=="decode":
    shift*=-1
  for char in text:
    if char in alphabet:
      position=alphabet.index(char)
      newPosition=position+shift
      message+=alphabet[newPosition]
    else:
      message+=char
  print(f"The {direction}ed text is {message}")


continuation=True
while continuation:
  direction = input("Type 'encode' to encrypt,   type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift=shift%26
  caesar(direction,text,shift)    
  user=input("Type 'yes'/'no' if you want to continue or not\n")
  if user=="no":
    continuation=False
    print("GoodBye")

