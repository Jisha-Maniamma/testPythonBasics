alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def Caesar_Cipher(direction,text,shift):
    if direction == "encode" :



if direction == "encode" or direction == "decode":
   Caesar_Cipher(direction,text,shift)

else:
    print(f"We couldnot help! you typed {direction} and not 'encode'/'decode'")






