
from BitVector import *
import sys

BLOCKSIZE = 16
numbytes = BLOCKSIZE // 8
PassPhrase = "Hopes and dreams of a million years"

def main():
    if len(sys.argv) != 3:
        sys.exit('''Needs two command-line arguments, one for '''
             '''the encrypted file and the other for the '''
             '''decrypted output file''')

    key = None                                                          
    if sys.version_info[0] == 3:                                                #(L)
        key = input("\nEnter key: ")                                            #(M)
    else:                                                               
        key = raw_input("\nEnter key: ")                                        #(N)
    key = key.strip()

    key_bv = BitVector(bitlist = [0]*BLOCKSIZE)                                 #(P)
    for i in range(0, len(key) // numbytes):                                     #(Q)
        keyblock = key[i * numbytes: (i + 1) * numbytes]                               #(R)
        key_bv ^= BitVector(textstring = keyblock)
    
    decryptText = cryptBreak(sys.argv[1], key_bv)

    FILEOUT = open(sys.argv[2], 'w')
    FILEOUT.write(decryptText)
    FILEOUT.close()


def cryptBreak(ciphertextFile, key_bv):
    
    bv_iv = BitVector(bitlist = [0] * BLOCKSIZE)
    for i in range(0, len(PassPhrase) // numbytes):
        teststr = PassPhrase[i * numbytes: (i + 1) * numbytes]
        bv_iv ^= BitVector(textstring = textstr)
    
    FILEIN = open(ciphertextFile, 'r')
    encrypted_bv = BitVector(hexstring = FILEIN.read())
    FILEIN.close()

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

if __name__ == "__main__":
    main()