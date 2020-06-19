import os
import random
import base64


class Config:
    def __init__(self):
        alphb64 = ('ICEiIyQlJicoKSorLC0uLzAxMjM0NTY3ODk6Ozw9Pj',
                   '9AQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVpbXF1eX2BhY',
                   'mNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ent8fX4=')

        alphabet_length = len(
            base64.b64decode(''.join(alphb64)).decode('utf-8'))
        char_range = [chr(x) for x in range(255, 30000)]
        random.shuffle(char_range)
        trans_alph_chars = char_range[:alphabet_length]

        self.alphabet = ''.join(alphb64)
        self.transposition_value = random.randrange(133, 1000, 7)
        self.alphabet_translation = base64.b64encode(
            bytes(''.join(trans_alph_chars), 'utf-8')).decode('utf-8')

    def setup_environment(self):
        os.environ['DRS_ALPHABET'] = self.alphabet
        os.environ['DRS_TRANS_ALPHABET'] = self.alphabet_translation
        os.environ['DRS_TRANS_VALUE'] = f'{self.transposition_value}'

    def write(self):
        self.setup_environment()
        with open('credo.json', 'r') as cred_file:
            credentials = cred_file.read()

        from drisy.core.credentials import transpose
        transposed_creds = transpose(str(credentials))
        self.app_credentials = base64.b64encode(transposed_creds).decode('utf-8')

        env_values = [
            f'export DRS_ALPHABET="{self.alphabet}"',
            f'export DRS_TRANS_ALPHABET="{self.alphabet_translation}"',
            f'export DRS_APP_CRED="{self.app_credentials}"',
            f'export DRS_TRANS_VALUE={self.transposition_value}',
            f'DRS_DRIVE_SCOPES=', ""
        ]

        self.template = "\n".join(env_values)

        with open('.env.config', 'wt') as config_file:
            config_file.write(self.template)
