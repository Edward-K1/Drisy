from .base import BaseTest


class TestCredentials(BaseTest):

    def test_get_app_credentials(self):
        self.setup_environment()
        creds = self.get_credentials()
        self.assertEqual(creds, self.app_credentials)

