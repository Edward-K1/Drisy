import os
import random
import base64


class Config:
    def __init__(self):
        alphb64 = ('ICEiIyQlJicoKSorLC0uLzAxMjM0NTY3ODk6Ozw9Pj',
                   '9AQUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVpbXF1eX2BhY',
                   'mNkZWZnaGlqa2xtbm9wcXJzdHV2d3h5ent8fX4=')

        self.alphabet_text = base64.b64decode(''.join(alphb64)).decode('utf-8')
        alphabet_length = len(self.alphabet_text)
        char_range = [chr(x) for x in range(255, 30000)]
        random.shuffle(char_range)
        trans_alphabet_chars = char_range[:alphabet_length]
        self.translation_text = ''.join(trans_alphabet_chars)

        self.alphabet = ''.join(alphb64)
        self.transposition_value = random.randrange(133, 1000, 7)
        self.alphabet_translation = base64.b64encode(
            bytes(self.translation_text, 'utf-8')).decode('utf-8')

    def write(self):
        with open('credo.json', 'r') as cred_file:
            credentials = cred_file.read()

        translator = credentials.maketrans(self.alphabet_text,
                                           self.translation_text)
        translated_creds = credentials.translate(translator)
        encoded_creds = base64.b64encode(bytes(translated_creds,
                                               'utf-8')).decode('utf-8')

        self.app_credentials = encoded_creds

        profile_path = os.getenv('HOME') or os.getenv('USERPROFILE')
        drisy_path = os.path.join(profile_path,'.Drisy')
        if not os.path.exists(drisy_path):
            os.makedirs(drisy_path)

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


if __name__ == "__main__":
    cfg = Config()
    cfg.write()
    