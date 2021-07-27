import json
from authlib.jose import JsonWebEncryption


class Decrypt():
    def decrypt(self, token, key):
        jwe = JsonWebEncryption()
        data = jwe.deserialize_compact(token, key)
        return data['payload'].decode()


decrypt = Decrypt().decrypt
