from authlib.jose import JsonWebEncryption


class Decrypt:
    def decrypt(token, key):
        jwe = JsonWebEncryption()
        data = jwe.deserialize_compact(token, key)
        return data
