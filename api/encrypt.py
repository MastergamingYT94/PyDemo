from Crypto.PublicKey import RSA
from authlib.jose import jwk, JsonWebEncryption
from sjcl import SJCL
import secrets
import json


class Encrypt():
    def encrypt(self, data, type='AES', Key=None, dump=True):
        """
        Encrypt data using RSA , AES

        param: type= type of key used in encryption: 'AES' or 'RSA'
        param: key= use your own key for RSA encryption
        param: dump= dumps the data if neccessary
        """

        if dump == True:
            payload = str(json.dumps(data)).encode()
        else:
            payload = str(data).encode()

        if type == 'RSA':
            key = RSA.generate(2048)
            key = key.exportKey('PEM')
            key = jwk.dumps(key, kty='RSA')

            if Key:
                key = Key

            protected = {'alg': 'RSA-OAEP', 'enc': 'A256GCM'}
            jwe = JsonWebEncryption()
            token = jwe.serialize_compact(protected, payload, key)
            token = token.decode()
        else:
            key = secrets.token_urlsafe(32)
            token = SJCL().encrypt(payload, key, "ccm", 1000, 32)
            token['salt'] = str(token['salt']).replace(
                "b'", "").replace("'", "")
            token['ct'] = str(token['ct']).replace("b'", "").replace("'", "")
            token['iv'] = str(token['iv']).replace("b'", "").replace("'", "")
            dic = {}
            dic['iv'] = token['iv']
            dic['v'] = token['v']
            dic['iter'] = token['iter']
            dic['ks'] = token['ks']
            dic['ts'] = token['ts']
            dic['mode'] = token['mode']
            dic['adata'] = token['adata']
            dic['cipher'] = token['cipher']
            dic['salt'] = token['salt']
            dic['ct'] = token['ct']
            token = dic
        return {'token': token, 'key': key}


encrypt = Encrypt().encrypt
