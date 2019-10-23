import base64


def decode_base64(source_str):
    return base64.b64decode(source_str).decode('utf-8')
