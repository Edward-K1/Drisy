import wx


class DriveItemListCtrl(wx.ListCtrl):
    def __init__(self, parent, imageList, imageMapIndex, columns, columnSizes):
        super().__init__(parent, -1, style=wx.LC_REPORT)
        self.imageList = imageList
        self.SetImageList(self.imageList, wx.IMAGE_LIST_SMALL)
        self.imageIndex = imageMapIndex
        self.columns = columns
        self.colsizes = columnSizes

        for count, colName in enumerate(columns):
            self.InsertColumn(count, colName, width=columnSizes[count])

    def InsertDriveObjects(self, objectList):
        for count, drive_object in enumerate(objectList):
            image_index = self.imageIndex[drive_object.mimegroup]
            item_index = self.InsertItem(count, drive_object.filename,
                                         image_index)
            self.SetItem(item_index, 1, drive_object.mimegroup)
            self.SetItem(item_index, 2, drive_object.username)
