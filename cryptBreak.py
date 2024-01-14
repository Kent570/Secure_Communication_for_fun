from BitVector import *

BLOCKSIZE = 16
numbytes = BLOCKSIZE // 8

def cryptBreak(ciphertextFile, key_bv):
    PassPhrase = "Hopes and dreams of a million years"
    bv_iv = BitVector(bitlist = [0] * BLOCKSIZE)
    for i in range(0, len(PassPhrase) // numbytes):
        teststr = PassPhrase[i * numbytes: (i + 1) * numbytes]
        bv_iv ^= BitVector(textstring = textstr)
    
    FILE = open(ciphertextFile)
    encrypted_bv = BitVector(hexstring = FILE.read())

    msg_decrypted_bv = BitVector(size = 0)

    previous_decrypted_block = bv_iv
    for i in range(0, len(encrypted_bv) // BLOCKSIZE):
        bv = encrypted_bv[i * BLOCKSIZE: (i + 1) * BLOCKSIZE]
        temp = bv.deep_copy()
        bv ^= previous_decrypted_block
        previous_decrypted_block = temp
        bv ^= key_bv
        msg_decrypted_bv += bv

    return msg_decrypted_bv.get_text_from_bitvector()

