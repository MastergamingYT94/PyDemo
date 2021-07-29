from authlib.jose import JsonWebEncryption
from sjcl import SJCL


class Decrypt():
    def decrypt(self, token, key, type='AES'):
        if type == 'AES':
            data = SJCL.decrypt(self, token, key)
            return data.decode()
        else:
            jwe = JsonWebEncryption()
            data = jwe.deserialize_compact(token, key)
            return data['payload'].decode()


decrypt = Decrypt().decrypt
