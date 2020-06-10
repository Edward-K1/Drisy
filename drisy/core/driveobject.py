class DriveObject:
    def __init__(self, dict_data):
        for key in dict_data:
            setattr(self, key, dict_data[key])