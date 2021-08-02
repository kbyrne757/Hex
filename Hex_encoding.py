#python version 3.9.5
#Hex Encoding/Decoding

def intro():
    decision = input("Would you like to encode or decode Base64? (encode/decode) ")
    decision = decision.upper()

    if (decision == 'ENCODE'):
        encoding()

    
    elif (decision == 'DECODE'):
        decoding()

    else:
        print("Invalid Input")

def encoding():
        #hex encoding
        userInput = input("Enter string to convert to hex: ")
        userInput = userInput.encode('utf-8')
        hexOutput = userInput.hex()
        print (hexOutput)

def decoding():
        #hex decoding
        userInput2 = input("Enter string to convert from hex: ")
        byte_array = bytearray.fromhex(userInput2)
        hexDecode= byte_array.decode()
        print (hexDecode)


intro()
