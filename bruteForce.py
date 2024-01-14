from cryptBreak import cryptBreak
from BitVector import *
import sys

BLOCKSIZE = 16
numbytes = BLOCKSIZE // 8
PassPhrase = "Hopes and dreams of a million years"

def main():
    # Check if the input prompt is 3
    if len(sys.argv) != 3:
        sys.exit('''Needs two command-line arguments, one for '''
             '''the encrypted file and the other for the '''
             '''decrypted output file''')

    # Run through all the possible keys
    for key in range(2 ** 16):
        # Convert the key into bits
        for i in range(0,len(key) // numbytes):
            keyblock = key[i * numbytes:(i+1) * numbytes]
            key_bv ^= BitVector(textstring = keyblock)
        # Check it it is the correct key
        outputtext = cryptBreak(sys.argv[1], key_bv)
        if 'Farrari' in outputtext:
            print("Encryption Broken!")
            break
    
    print(f"Key: {key_bv}")
    print(f"Original Text:\n{outputtext}")

    FILEOUTPUT = open(sys.argv[2], 'w')
    FILEOUTPUT.write(outputtext)
    FILEOUTPUT.close()
