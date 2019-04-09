"""
    string to send has such binary format:
    bytes 1-4   (4):    destination address     [0:32]
    bytes 5-8   (4):    sender address          [32:64]
    bytes 9-16  (8):    auto number             [64:128]
    bytes 19-23 (5):    five digits for price  without dot 999.00   [128:168]
    bytes 24-25 (2):    duration in minutes (max65536)              [168:184]
    byte 26    (1):     device                  [184:192]
    byte 27     (1):    tariff                  [192:200]
    bytes 28-            limit time                       [200:]
"""

import socket
import settings
import re


def destination_from_string(bin_text):
    return addr_to_decimal(bin_text[:32])

def sender_from_string(bin_text):
    return addr_to_decimal(bin_text[32:64])

def number_from_string(bin_text):
    return bin_to_text(bin_text[64:128])

def number_to_bin(text):
    result = text_to_bin(text)
    return result +'0'*(64-len(result))

def price_to_bin(price):
    price = str(price) + '00'       # change later
    result = text_to_bin(price)
    return '0'*(40-len(result)) + result

def price_from_string(bin_text):
    result = bin_to_text(bin_text[128:168])
    return result[:-2]+'.'+result[-2:]

def duration_to_bin(text):
    result = text_to_bin(text)
    return '0'*(16-len(result))+result

def duration_from_string(bin_text):
    result = bin_to_text(bin_text[168:184])
    return int(result)



def text_to_bin(text):
    text = str(text)
    result=''
    if len(text)==1:
        result = bin(ord(text))[2:]
    else:
        for char in text:
            result+=text_to_bin(char)
    return  '0'*(8-len(result)) + result

def bin_to_text(bin_str):
    if len(bin_str)>8:
        return chr(int('0b' + bin_str[:8], 2)) + bin_to_text(bin_str[8:])
    else:
        return chr(int('0b' + bin_str, 2))

def to_bit(number):
    """ returns binary representatation of a decimal number
    in octet format """
    if number in range (256):
        binary = bin(number)[2::]
        return '0'*(8-len(binary)) + binary
    return '-1'

def to_decimal(binary):
    """ returns decimal representation of the string binary  with 0 and 1 only
    and not longer than 8 symbols"""
    if len(re.findall('[0-1]+', binary)[0] )< 9:
        return int('0b'+binary, 2)
    return -1

def addr_to_bin(address):
    """returns binary representation of an IP-address from string address"""
    bin_address = ''
    if re.findall('\d', address)[0].isdigit():
        octet = address.split('.')
        for oct in octet:
            bin_address+=to_bit(int(oct))
    return bin_address

def addr_to_decimal(bin_address):
    """returns decimal representation of binary 32 long bin_address"""
    if len(bin_address) == 32:
        if re.match('[0-1]+', bin_address):
            return (str(to_decimal(bin_address[0:8])) + '.'
                    + str(to_decimal(bin_address[8:16])) + '.'
                    + str(to_decimal(bin_address[16:24])) + '.'
                    + str(to_decimal(bin_address[24:32])))
    return '-1'


def send_packet(auto_number, price, duration, tariff=1, flag='0',
                destination=settings.HOST_ADDRESS,
                port=settings.PORT,
                device=settings.DEVICE_NUMBER):
    text=''
    text+=addr_to_bin('127.0.0.5')  # destination address

    text+=addr_to_bin('127.0.0.3')  # sender address

    text+=number_to_bin(auto_number)

    text+=price_to_bin(price)

    text+=duration_to_bin(str(duration))

    text+=text_to_bin(tariff)
    text+=text_to_bin(device)

    print('parsed info:')
    print(destination_from_string(text))
    print(sender_from_string(text))
    print(number_from_string(text))
    print(price_from_string(text))
    print(duration_from_string(text))


    return text
#     sock = socket.socket()



if __name__=='__main__':

    numbers = ['AE3456AH', '123A', 'dfr123', 'DFR123',
               '127.0.0.1', '{asd: 1278; number:245}']

    price = [15, 30, 45]

    duration = [75, 127]

    for number in numbers:
        binary = text_to_bin(number)
        parsed = bin_to_text(binary)
        # print('number: {} -- length of the string: {} -- parsed: {}'.format(number , len(binary), parsed))


    print('---')

    text = send_packet(numbers[0], price[2], duration[1])

    print(destination_from_string(text))
    print(sender_from_string(text))
    print(number_from_string(text))
    print(price_from_string(text))
    print(duration_from_string(text))

