
choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
message= input ("Type your message: ").lower()
shift = int(input("Tyle the shift number: "))
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encode function
def encode(message, shift):
    new_encoded_message = ""
    for letter in message:
        for alphabet in alphabets:
            if letter == alphabet: #if a letter in the list message is equal to an alphabet 
                position= alphabets.index(letter) #get its index
                new_position = (position + shift) #shift it forwar using the index 
                new_encoded_message+= alphabets[new_position] # get the alphabet at new index
    print("Encoded message:", new_encoded_message)
                
def decode(message,shift):
    original_decoded_message=" "
    for letter in message:
         for alphabet in alphabets:
            if letter == alphabet:
                position= alphabets.index(letter)
                new_position = (position - shift)
                original_decoded_message+=alphabets[new_position]
    print("Decoded message:", original_decoded_message)



if choice == "encode":
    encode(message,shift)
elif choice == "decode":
    decode(message,shift)
else:
    print("Enter a vaid option")