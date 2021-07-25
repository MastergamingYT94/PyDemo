from Crypto.PublicKey import RSA
from authlib.jose import jwk, JsonWebEncryption
import json


class Encrypt():
    def encrypt(self, data):
        key = RSA.generate(2048)
        key = key.exportKey('PEM')
        key = jwk.dumps(key, kty='RSA')
        jwe = JsonWebEncryption()
        protected = {'alg': 'RSA-OAEP', 'enc': 'A256GCM'}
        payload = str(json.dumps(data)).encode()
        token = jwe.serialize_compact(protected, payload, key)
        return {'token': token.decode(), 'key': key}
