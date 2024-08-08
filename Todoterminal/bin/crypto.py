import base64


def Rot13DecoderEncoder(data):
    new_data = list(data)
    ord_data = []
    ord_data_2 = []
    for x in new_data:
        ord_data.append(ord(x))
    for y in ord_data:
        if y <= 78 and y >= 65 :
            ord_data_2.append(y+13)
        elif y <= 90 and y > 78 :
            ord_data_2.append(y-13)
        elif y < 110 and y >= 97 :
            ord_data_2.append(y+13)
        elif y <= 122 and y >= 110:
            ord_data_2.append(y-13)
        else:
            ord_data_2.append(y)

    listToStr5 = ''.join([str(chr(element)) for element in ord_data_2])
    
    return(listToStr5)


def HexadecimalEncoder(data):
    sample_string = data
    sample_string_bytes = sample_string.encode("utf-8") 
    base16_bytes = base64.b16encode(sample_string_bytes) 
    base16_string = base16_bytes.decode("utf-8") 
    return(base16_string)

def HexadecimalDecoder(data):
    base16_string = data
    base16_bytes = base16_string.encode("utf-8") 
    sample_string_bytes = base64.b16decode(base16_bytes) 
    sample_string = sample_string_bytes.decode("utf-8") 
    return sample_string

def Base64Encoder(data):
  
    sample_string = data
    sample_string_bytes = sample_string.encode("ascii") 
    base64_bytes = base64.b64encode(sample_string_bytes) 
    base64_string = base64_bytes.decode("ascii") 
    return(base64_string)

def Base64Decoder(data):
      
    base64_string = data
    base64_bytes = base64_string.encode("ascii") 
    sample_string_bytes = base64.b64decode(base64_bytes) 
    sample_string = sample_string_bytes.decode("ascii") 
    return(sample_string)


def CryptoTask(data):
    data1 = Rot13DecoderEncoder(data)
    data2 = Base64Encoder(data1)
    result = HexadecimalEncoder(data2)
    return result

def DecryptoTask(data):
    hash1 = HexadecimalDecoder(data)
    hash2 = Base64Decoder(hash1)
    result = Rot13DecoderEncoder(hash2)
    return result             


