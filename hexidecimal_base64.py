import time

RED = "\033[3;31m"
GREEN = "\033[1;32m"
RESET = "\033[0m"


print(f"{GREEN}Hex to Base64 Converter{RESET}")

time.sleep(1)


print(f"\n{GREEN}Hex:{RESET} A hexadecimal string is a sequence of characters, typically using the digits 0-9 and the letters A-F (or a-f), used to represent numerical values")
print(f"{GREEN}Base64:{RESET}  is a binary-to-text encoding scheme that represents binary data in an ASCII string format using a set of 64 characters.")

print("\nMore context on the implementation of this encoding: \n" \
      "Convert the Hexidecimal to Binary & convert the Binary into groups of 6bit chunks," \
      "match the 6bit chunks to base64 characters")
#----------------------------------------------------------------------------------------------------------------------#
hexidecimalConversion = {
    #     8421
    "0" : "0000",
    "1" : "0001", #1
    "2" : "0010", #2
    "3" : "0011", #3
    "4" : "0100", #4
    "5" : "0101", #5
    "6" : "0110", #6
    "7" : "0111", #7
    "8" : "1000", #8
    "9" : "1001", #9
    "a" : "1010", #10
    "b" : "1011", #11
    "c" : "1100", #12
    "d" : "1101", #13
    "e" : "1110", #14
    "f" : "1111", #15
}

#----------------------------------------------------------------------------------------------------------------------#
def HexidecimalToBinary(text) -> str:
    output = ""
    for char in text.lower():
        try:
            output += hexidecimalConversion[char]
        except Exception as e:
            print(f"An unexpecteded error occured {e}")
    return output

## Adding padding if the remaining chunks do not have 6 bits
def Padding(binary) -> str:
    while(len(binary) % 6):
        binary += "0"
    return binary


def BinaryToSixBit(binary) -> list:
    binary = Padding(binary)

    chunks = []
    stringChunks = ""
         
    for char in binary:
        stringChunks += char
        if len(stringChunks) == 6:
            chunks.append(stringChunks)
            stringChunks = ""

    return chunks    
    
#----------------------------------------------------------------------------------------------------------------------#

cryptography = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f"

binary = HexidecimalToBinary(cryptography)
sixBit = BinaryToSixBit(binary)

print(sixBit)