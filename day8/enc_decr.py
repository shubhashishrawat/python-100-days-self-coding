alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
taken=input('type  "encode" to encrypt, type "decode"  to decrypt')
text=input("enter a word that you want to encrypt").lower()
shift=int(input("from how many you want to shift"))

def encode(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position=alphabet.index(letter)
        new_position=position + shift_amount
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"the encode text is {cipher_text}")
encode(plain_text=text, shift_amount=shift)


