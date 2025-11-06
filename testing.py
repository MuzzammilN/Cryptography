
x = 104
binary = ""

def convert_to_binary():
    global x, binary
    while(x != 0):
        bit = x % 2
        binary += str(bit)
        x = x // 2

    while len(binary) < 8:
        binary += "0"

    binary = binary[::-1]



convert_to_binary()

print(binary)

