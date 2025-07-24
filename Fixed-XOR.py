


hexidecimalConversion = {
        "0" : "0000", "5" : "0101", "a" : "1010", 
        "1" : "0001", "6" : "0110", "b" : "1011", 
        "2" : "0010", "7" : "0111", "c" : "1100",
        "3" : "0011", "8" : "1000", "d" : "1101", 
        "4" : "0100", "9" : "1001", "e" : "1110", 
        "f" : "1111"  
    }


first = "1010"
second = "1001"
print(f"XOR, short for 'exclusive or,' is a logical operation that outputs true if and only if one of its inputs is true, but not both")

def XOROperation(firstCompare: str, secondCompare: str) -> str:
    return "0" if firstCompare == secondCompare else "1"

def HexidecimalToBinary(texts: str) -> str:
    try:
        return ''.join(hexidecimalConversion[char.lower()] for char in texts)
    except Exception as e:
        return f"an exception has an occured {e}"
    


def BitsToFourBit(binary: str) -> list:
    try:
        if not all(bit in "01" for bit in binary):
            return "Error: binary string contains invalid bits"
        
        chunks = []
        for i in range(0, len(binary), 4): ## iterates, 0 -> 6 -> 12 -> 18
            chunks.append(binary[i:i+4]) ## string slice from 0 -> 6
        return chunks
    
    except Exception as e:
        return f"an exception has an occured {e}"
    

cryptographyOne = "1c0111001f010100061a024b53535009181c"
cryptographyTwo = "686974207468652062756c6c277320657965"
        
binary = ''.join(XOROperation(first, second) for first, second in zip(HexidecimalToBinary(cryptographyOne), HexidecimalToBinary(cryptographyTwo)))

FourBit = BitsToFourBit(binary)

output = ''.join(hexidecimalConversion[bit] for bit in enumerate(FourBit))

binaryToHex = {v: k for k, v in hexidecimalConversion.items()}

print(FourBit)