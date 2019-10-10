import os

from .utils import decode_base64

# special characters are tricky in .env files so we convert and read them
# as base64 strings instead
alphabet = ('' or decode_base64(os.getenv('DRS_ALPHABET')))
translated_alphabet = ('' or decode_base64(os.getenv('DRS_TRANS_ALPHABET')))
transposition_value = ('' or int(os.getenv('DRS_TRANS_VALUE')))

profile_path = os.getenv('HOME') or os.getenv('USERPROFILE')
user_credentials_path = os.path.join(profile_path, '.Drisy', 'chest')
app_credentials = ('' or os.getenv('DRS_APP_CRED'))

drive_scopes = (['https://www.googleapis.com/auth/drive.metadata.readonly']
                or os.getenv('DRS_DRIVE_SCOPES').split(','))
