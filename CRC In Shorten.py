def xor(a,b):
    result =""
    for bit_a,bit_b in zip(a,b):
        result+= '1' if bit_a != bit_b else '0'
    return result
def crc(data,poly):
    pad_data = data + '0'*(len(poly)-1)
    remainder = pad_data[:len(poly)]
    for i in range(len(data)):
        if remainder[0] == '1':
            remainder = xor(remainder,poly)
        else:
            remainder = xor(remainder,'0'*len(poly))
        if len(poly)+i<len(pad_data):
            remainder+=pad_data[len(poly)+i]
        remainder=remainder[1:]
    return remainder
data = input("Enter Data:")
poly = input("Enter Polynomial:")
redata= input("Enter received data:")
crc_value = crc(data,poly)
print(f"CRC is:{crc_value}")
data_with_crc = data+crc_value
print(f"Data with CRC: {data_with_crc}")
if(redata==data_with_crc):
    print("No Error")
else:
    print("Error found")
