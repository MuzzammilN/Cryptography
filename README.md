# 🧮 Hex to Base64 Converter

A Python-based Hexadecimal to Base64 converter that demonstrates how to manually implement the Base64 encoding algorithm — without using built-in libraries.
This project converts a hexadecimal string into Base64 format by processing the data through binary transformations and 6-bit chunk encoding.

## 🚀 Features

✅ Converts hexadecimal strings to Base64
✅ Step-by-step encoding:

Hex → Binary

Binary → 6-bit groups

6-bit → Base64 characters
✅ Custom-built Base64 mapping (no external libraries)
✅ Includes error handling and binary padding
✅ Demonstrates encoding logic clearly for learning purposes

🧠 How It Works

Hexadecimal to Binary Conversion
Each hex character (0–F) is mapped to a 4-bit binary value using a predefined dictionary.

Binary Padding
If the binary string length isn’t a multiple of 6, zero bits are appended to make it divisible by 6.

6-bit Chunking
The padded binary string is split into chunks of 6 bits.

Bits to Number Conversion
Each 6-bit chunk is converted into a decimal number (0–63).

Base64 Mapping
Each decimal number is then mapped to a Base64 character using the standard Base64 table.

Output Generation
The Base64 characters are concatenated into the final encoded string.

#### 📜 Example Output
```python
Input:
hexString = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f"
print(HexToBase64.Encoder(hexString))
```
```python
Output:
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hybw==
```

### 🧩 Code Overview
Class: HexToBase64
Method	Description
HexadecimalToBinary(texts)	Converts a hex string into binary
Padding(binary)	Pads binary to make length divisible by 6
BinaryToSixBit(binary)	Splits binary into 6-bit chunks
BitsToNumber(bits)	Converts 6-bit binary to an integer (0–63)
Base64ToText(num)	Maps the integer to a Base64 character
Encoder(hexString)	Encodes the full hexadecimal string into Base64
# 🧱 Internal Mappings
## 🔢 Hexadecimal to Binary
"f" : "1111"
"e" : "1110"
"d" : "1101"
...
"0" : "0000"

## 🔡 Base64 Index Table
0: "A", 1: "B", ..., 25: "Z", 26: "a", ..., 51: "z", 52: "0", ..., 63: "/"

## 🛠️ Requirements

Python 3.7+

Works on Windows, macOS, and Linux

No external dependencies — it uses only built-in Python libraries.

🧪 Running the Program
Run in Terminal
python hex_to_base64.py

Example Output
Hex to Base64 Converter

Hex: A hexadecimal string is a sequence of characters...
Base64: is a binary-to-text encoding scheme...

SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hybw==

## 🧾 License

This project is open-source and available under the MIT License.
Feel free to modify, improve, and learn from it.

## 👨‍💻 Author

Muzzammil Naqvi
Information Technology Student @ York University
Passionate about software development, secure coding, and system design.
