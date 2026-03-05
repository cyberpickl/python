# Building a encoder - decoder that takes a message and shifts it ( user input variable) a certain number of times as specified to get the encoded message. 

choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
message= input ("Type your message: ").lower()
shift = int(input("Type the shift number: "))
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# encode function
def encode(message, shift):
    new_encoded_message = ""
    for letter in message: #if a letter in the list message is equal to an alphabet 
            position= alphabets.index(letter) #get its index
            new_position = (position + shift)% len(alphabets) #shift it forwar using the index  
            # incase the letter includes "z" shifting forward would go out of range to help with that we use modulo so that no matter how far out we go it gets adjusted
            new_encoded_message+= alphabets[new_position]  # get the alphabet at new index
    print("Encoded message:", new_encoded_message)

#decode function       
def decode(message,shift):
    original_decoded_message=" "
    for letter in message:
         for alphabet in alphabets:
            if letter == alphabet:
                position= alphabets.index(letter) 
                new_position = (position - shift) % len(alphabets)
                original_decoded_message+=alphabets[new_position]
    print("Decoded message:", original_decoded_message)



if choice == "encode":
    encode(message,shift)
elif choice == "decode":
    decode(message,shift)
else:
    print("Enter a valid option")