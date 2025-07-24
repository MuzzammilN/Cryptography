# Cryptography

This Repository is dedicated towards the implementation of Cryptographic Encoding & Cryptography Algorithms respectively. 

---

## Algorithms & Encoding Schemes Currently Implemented 

### 1. Fixed XOR Encoding

- This encoding algorithm performs a bitwise XOR on two hexadecimal strings by converting them to binary, applying XOR on each bit, splitting the result into 4-bit chunks, and attempting to map them back to hex.
- It includes functions for hex-to-binary conversion, XOR logic, and chunking binary strings.

### 2. Hexadecimal to Base64 Encoding

- This encoding algorithm converts a hexadecimal string to a Base64-encoded string.
- It includes functions to convert hex to binary, pad binary to 6-bit chunks, convert chunks to decimal, and map those to Base64 characters using a custom dictionary.

---
