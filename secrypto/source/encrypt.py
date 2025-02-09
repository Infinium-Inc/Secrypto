from secrypto.source.key import Key
from random import shuffle, choice as select

def encrypt(string: str, key: Key | dict[str, list[str]]):
    if not string:
        return ''

    encryption = string

    str_order = ["a", "o", "b", "h"]
    shuffle(str_order)
    str_order = ''.join(str_order)

    for char in str_order:
        if char == 'a':
            encryption = ''.join(str(ord(a)) + select(['¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']) for a in encryption)
        elif char == 'o':
            encryption = ''.join(str(oct(ord(a))).replace('0o', '') + select(['9', 'A', 'B', 'C', 'D', 'E', 'F', 'G']) for a in encryption)
        elif char == 'b':
            encryption = ''.join(str(bin(ord(a))).replace('b', '') + select(['2', '3', '4', '5', '5', '6', '7', '8']) for a in encryption)
        elif char == 'h':
            encryption = ''.join(str(hex(ord(a))).replace('x', '') + select(['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']) for a in encryption)

    key = key.key if isinstance(key, Key) else key
    encryption = ''.join(select(key[a]) for a in encryption + str_order[::-1])

    return encryption