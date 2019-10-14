import os.path
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

from .credentials import get_credentials, save_credentials
from .data import drive_scopes, user_credentials_path


def get_auth_credentials():
    """Gets a user's google drive oauth credentials
    
    Returns:
        Object -- Google's Authorization Credentials object
    """
    creds = get_credentials()

    if not os.path.exists(user_credentials_path):
        flow = InstalledAppFlow.from_client_config(creds, drive_scopes)
        creds = flow.run_local_server(
            port=0,
            success_message=
            'Drisy authorised successfully. You can close this Tab.')
        save_credentials(creds.__dict__)

    else:
        creds = Credentials.from_authorized_user_info(creds)

    return creds
