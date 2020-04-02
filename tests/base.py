import unittest
import os

from .dummy_values import app_creds, base64_app_creds, alphabet, translation_alphabet

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.app_credentials = app_creds
        self.base64_app_creds = base64_app_creds
        self.setup_environment()
        #the import below is not ideal but it prevents the test variables
        #from being set when called in subsequent test files
        from drisy.core.credentials import get_credentials
        self.get_credentials = get_credentials


    def setup_environment(self):
        os.environ['DRS_ALPHABET'] = alphabet
        os.environ['DRS_TRANS_ALPHABET'] = translation_alphabet
        os.environ['DRS_APP_CRED'] = base64_app_creds
        os.environ['DRS_TRANS_VALUE'] = '221'
        os.environ['HOME'] = 'test_tmp'

    def tearDown(self):
        pass
