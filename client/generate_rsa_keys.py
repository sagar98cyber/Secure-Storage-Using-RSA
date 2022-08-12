# Program : Generate rsa keys
# Description : Allow to generate rsa keys

import rsa
from store_rsa_keys_in_files import store_rsa_keys_in_files


def generate_rsa_keys() -> tuple:
    print(f'Keys are being generated')
    public_key: rsa.key.PublicKey
    private_key: rsa.key.PrivateKey

    (public_key, private_key) = rsa.newkeys(1024)

    return public_key, private_key

#(public_key, private_key) = generate_rsa_keys()

#store_rsa_keys_in_files(private_key, public_key)
