alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def Caesar_Cipher(directions, texts, shifts):
    if directions == "encode":
        cipherText = ""
        for a in texts:
            # print(f"at location {alphabet.index(a)}  new location{int(int(alphabet.index(a)) + shift)}")
            # print(f" new charactpr for {a} -> {alphabet[alphabet.index(a) + shift]}")
            cipherText += alphabet[alphabet.index(a) + shifts]
        print(f"the encoded text is {cipherText}")
    else:
        decriptedText=""
        for a in texts:
            decriptedText += alphabet[alphabet.index(a) - shifts]
        print(f"the encoded text is {decriptedText}")

def Caesar_Cipher1(directions, texts, shifts):

        cipherText = ""
        for a in texts:
            # print(f"at location {alphabet.index(a)}  new location{int(int(alphabet.index(a)) + shift)}")
            # print(f" new charactpr for {a} -> {alphabet[alphabet.index(a) + shift]}")
            if directions == "decode":
                shifts*=-1
            cipherText += alphabet[alphabet.index(a) + shifts]
        print(f"the {directions} text is {cipherText}")




if direction == "encode" or direction == "decode":
    Caesar_Cipher1(direction, text, shift)

else:
    print(f"We couldnot help! you typed {direction} and not 'encode'/'decode'")
