# Program : Encrypt files
# Description : Allow to decrypt file encrypted with the RSA key

import rsa


def encrypt(data: bytes, public_key: rsa.key.PublicKey):

    return rsa.encrypt(data, public_key)

