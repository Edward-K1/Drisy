import os

from ast import literal_eval
from google_auth_oauthlib.flow import InstalledAppFlow

from .utils import decode_base64
from .globals import (alphabet, translated_alphabet, transposition_value,
                   profile_path, user_credentials_path, app_credentials)


def save_credentials(credentials_dict):
    """saves user credentials returned after authorization
    
    Arguments:
        credentials_dict {dict} -- Dictionary representation 
        of the fields contained in google's credentials object
    """
    field_mappings = {
        'token': 'token',
        'refresh_token': '_refresh_token',
        'token_uri': '_token_uri',
        'client_id': '_client_id',
        'client_secret': '_client_secret'
    }
    credentials = {
        field: credentials_dict[value]
        for (field, value) in field_mappings.items()
    }

    with open(user_credentials_path, 'wb') as cred_file:
        cred_file.write(transpose(str(credentials)))


def get_credentials():
    """returns the user's saved authorization credentials.
       if not found, it returns Drisy's
    
    Raises:
        Exception: no App or User credentials found
    
    Returns:
        dict -- dictionary representation of authorization credentials
    """
    credentials = credentials_from_base64_str(app_credentials)

    if os.path.exists(user_credentials_path):
        credentials = credentials_from_path(user_credentials_path)

    if not credentials:
        raise Exception('No Credentials Found!')
    return credentials


def transpose(source_str):
    """translates the source string according to Drisy's alphabet. Changes
       the equivalent byte values according to the transposition value
    
    Arguments:
        source_str {string} -- the string to transpose
    
    Returns:
        bytes -- a transposed array of bytes
    """

    translated_str = translate(source_str)
    transposed_array = [
        hex(ord(char) * transposition_value) for char in translated_str
    ]
    transposed_bytes = bytes('\\'.join(transposed_array), 'utf-8')

    return transposed_bytes


def get_original_string(source_bytes):
    """translates `source_bytes` to their original string
    
    Arguments:
        source_bytes {bytes} -- the encoded bytes representing user credentials
    
    Returns:
        string -- the original credentials object string
    """

    hex_byte_strings = source_bytes.decode('utf-8').split('\\')

    encoded_str = ''.join(
        chr(int(hex_val, 16) // transposition_value)
        for hex_val in hex_byte_strings)
    original_str = translate(encoded_str,
                             order=(translated_alphabet, alphabet))
    return original_str


def translate(source_str, order=(alphabet, translated_alphabet)):
    """translates a given string from one alphabet to another (left to right)
    
    Arguments:
        source_str {string} -- the string to be translated
    
    Keyword Arguments:
        order {tuple} -- the order in which to translate the given string
         (default: {(alphabet, translated_alphabet)})
    
    Returns:
        string -- the translated string
    """
    translator = source_str.maketrans(order[0], order[1])
    return source_str.translate(translator)


def credentials_from_path(path):
    """reads credentials from given path
    
    Arguments:
        path {str} -- the system path from which to read credentials
    
    Returns:
        dict -- dictionary representation of the stored credentials
    """

    credentials = None

    with open(path, mode='rb') as cred_path:
        cred_bytes = cred_path.read()
        credentials = literal_eval(get_original_string(cred_bytes))
    return credentials


def credentials_from_base64_str(b64str):
    """decodes the base64 representation of app credentials
    
    Arguments:
        b64str {str} -- the base64 credentials string to be decoded
    
    Returns:
        dict -- the dictionary representation of the app credentials
    """
    decoded_str = decode_base64(b64str)
    translated = translate(decoded_str, order=(translated_alphabet, alphabet))
    return literal_eval(translated)
