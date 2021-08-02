#python version 3.9.5
#Hex Encoding/Decoding


userInput = input("Enter string to convert to hex: ")
userInput = userInput.encode('utf-8')
hexOutput = userInput.hex()

print (hexOutput)
