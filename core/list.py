from googleapiclient.discovery import build

from .auth import get_auth_credentials


class ListDrive:
    """Lists the contents of a User's Google Drive
    """
    def __init__(self, page_size=100):
        self._credentials = get_auth_credentials()
        self.page_size = page_size
        self.file_attributes = "id, name, mimeType, starred,\
                                webViewLink, iconLink, viewedByMe,\
                                createdTime, modifiedTime, modifiedByMe,\
                                owners, shared, ownedByMe"

    def list_files(self):
        """return a list of all files objects in  a user's drive
        """
        service = build('drive', 'v3', credentials=self._credentials)
        drive_items = []
        token = None

        while True:
            # network exceptions occuring here have to be handled by the caller
            results = self.get_files(service, token)
            drive_items.extend(results.get('files', []))
            token = results.get('nextPageToken', None)

            if not token:
                break

        return drive_items

    def get_files(self, drive_service, token):
        """fetch files for a given drive service
        """
        results = drive_service.files().list(
            pageSize=self.page_size,
            pageToken=token,
            fields=f'nextPageToken, files({self.file_attributes})').execute()

        return results
