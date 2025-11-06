import time

RED = "\033[3;31m"
GREEN = "\033[1;32m"
BLACK = "\033[0;30m"
RESET = "\033[0m"


print(f"\n{GREEN}Hex to Base64 Converter{RESET}")

time.sleep(0.5)


print(f"\n{GREEN}Hex:{RESET} A hexadecimal string is a sequence of characters, typically using the digits 0-9 and the letters A-F (or a-f), used to represent numerical values")
print(f"{GREEN}Base64:{RESET}  is a binary-to-text encoding scheme that represents binary data in an ASCII string format using a set of 64 characters.")

print("\nMore context on the implementation of this encoding: \n" \
      "Convert the Hexadecimal to Binary & convert the Binary into groups of 6bit chunks," \
      "match the 6bit chunks to base64 characters")

time.sleep(0.5)
print()
#----------------------------------------------------------------------------------------------------------------------#


#----------------------------------------------------------------------------------------------------------------------#
class HexToBase64:

    __private_base64 = {
        0: "A",  1: "B",  2: "C",  3: "D",  4: "E",  5: "F",  6: "G",  7: "H",
        8: "I",  9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
        16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
        24: "Y", 25: "Z", 26: "a", 27: "b", 28: "c", 29: "d", 30: "e", 31: "f",
        32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n",
        40: "o", 41: "p", 42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v",
        48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3",
        56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"
    }

    __private_hexadecimalConversion = {
        "0" : "0000", "5" : "0101", "a" : "1010", 
        "1" : "0001", "6" : "0110", "b" : "1011", 
        "2" : "0010", "7" : "0111", "c" : "1100",
        "3" : "0011", "8" : "1000", "d" : "1101", 
        "4" : "0100", "9" : "1001", "e" : "1110", 
        "f" : "1111"  
    }

    def HexadecimalToBinary(texts: str) -> str:
        try:
            return ''.join(HexToBase64.__private_hexadecimalConversion[char.lower()] for char in texts)
        except Exception as e:
            return f"an exception has an occured {e}"

    ## Adding padding if the remaining chunks do not have 6 bits
    def Padding(binary: str) -> str:
        try:
            while(len(binary) % 6):
                binary += "0"
            return binary
        except Exception as e:
            f"an exception has occurred {e}"

    def BinaryToSixBit(binary: str) -> list:
        try:
            if not all(bit in "01" for bit in binary):
                return "Error: binary string contains invalid bits"
            binary = HexToBase64.Padding(binary)
            chunks = []

            for i in range(0, len(binary), 6): ## iterates, 0 -> 6 -> 12 -> 18
                chunks.append(binary[i:i+6]) ## string slice from 0 -> 6
            return chunks
        
        except Exception as e:
            return f"an exception has occurred {e}"
          
    def BitsToNumber(bits: str) -> int:
        try:
            if not all(bit in "01" for bit in bits):
                return "Error: binary string contains invalid bits"
            return sum(int(bit) * pow(2, len(bits)-i-1) for i, bit in enumerate(bits))
            
        except Exception as e:
            return f"an exception has occurred {e}"
        
    def Base64ToText(num: int) -> str:
        if num <= 63 and num >= 0:
            return HexToBase64.__private_base64[num]
        else:
            return "Value is not contained in base64"
        
    def Encoder(hexString: str) -> str:
        try:
            binary = HexToBase64.HexadecimalToBinary(hexString)
            sixBit = HexToBase64.BinaryToSixBit(binary)
            numberOutput = [HexToBase64.BitsToNumber(bits) for bits in sixBit]
            return ''.join(HexToBase64.Base64ToText(int(num)) for num in numberOutput)
        
        except Exception as e:
            return f"an exception occured {e}"


#----------------------------------------------------------------------------------------------------------------------#

hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f"

print(f"{HexToBase64.Encoder(hexString)} \n")
