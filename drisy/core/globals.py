import os

from .utils import decode_base64

# use base64 strings to store special characters in .env variables
alphabet = ('' or decode_base64(os.getenv('DRS_ALPHABET')))
translated_alphabet = ('' or decode_base64(os.getenv('DRS_TRANS_ALPHABET')))
transposition_value = ('' or int(os.getenv('DRS_TRANS_VALUE')))

profile_path = os.getenv('HOME') or os.getenv('USERPROFILE')
user_credentials_path = os.path.join(profile_path, '.Drisy', 'chest')
app_credentials = ('' or os.getenv('DRS_APP_CRED'))

db_path = os.path.join(profile_path, '.Drisy', 'index')

drive_scopes = (['https://www.googleapis.com/auth/drive.metadata.readonly']
                or os.getenv('DRS_DRIVE_SCOPES').split(','))
