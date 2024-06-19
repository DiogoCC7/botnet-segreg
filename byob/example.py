import marshal, zlib, base64

print(marshal.loads(zlib.decompress(base64.b64decode(b'eJwrtWZgYCgtyskvSM3TUM8oKSmw0tcvTi0qSy2ysjQwMNJPzslMzSsp1i8uSUxPLSrWLw2x0CuoVNfUK0pNTNHQBACiIRT0'))))