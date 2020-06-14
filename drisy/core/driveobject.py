from .mimetypes import supported_mimetypes

class DriveObject:
    def __init__(self, dict_data):
        for key in dict_data:
            setattr(self, key, dict_data[key])
        self.mimegroup = self.assign_mimegroup(self.mimetype)

    def assign_mimegroup(self, mimetype_str):
        mimegroup = 'Unknown'
        for group in supported_mimetypes:
            if mimetype_str in supported_mimetypes[group]:
                mimegroup = group.title()
        return mimegroup