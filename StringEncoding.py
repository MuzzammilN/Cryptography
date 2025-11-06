class String:
    

    def __NumberArray(self, String: str) -> list:
        array = [ord(char) for char in String]
        return array

    def __bits(self, array: list, length: int) -> list: 
        bitsList = []
        bits = ""
        for num in array:
            while(num != 0):
                bit = num % 2
                bits += str(bit)
                num = num // 2

            while(len(bits) < length):
                bits += "0"
            
            bits = bits[::-1]
   
            bitsList.append(bits)
            bits = ""
        return bitsList

    def binary(self, string: str) -> str:
        numArray = self.__NumberArray(string)
        binaryList = self.__bits(numArray, 8)

        return ' '.join(binaryList)
    

    def octal(self, string: str) -> str:
        numsArray = self.__NumberArray(string)
        array = self.__bits(numsArray, 8)

        octalArray = []
        for bits in array:
            newbit = "0"
            newbit += bits
            arr = [newbit[:3], newbit[3:6], newbit[6:9]]
            octalValue = 0
            for bitString in arr:
                number = 0
                bitString = bitString[::-1]
                for index in range(len(bitString)):
                    bit = int(bitString[index])
                    number += bit * pow(2, index)
                
                octalValue = octalValue * 10 + number
            octalArray.append(octalValue)                  
        return ' '.join(str(char) for char in octalArray)
  
      
    ## 001 101 000
    def hexidecimal():
        print()

    def base58():
        print()
    
    def base64():
        print()




