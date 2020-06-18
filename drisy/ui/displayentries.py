import wx

from collections import OrderedDict, defaultdict
from inspect import getsourcefile
from .assets.icon import (doc, sheet, slide, unknown, image, archive, folder,
                          audio, video, pdf, executable, code)
from .utils import rescale_image
from .ItemListCtrl import DriveItemListCtrl
from drisy.core.drive import DriveManager


def CreateItemList(parentWindow):
    imgList = wx.ImageList(32, 32)
    imageMap = OrderedDict({
        "Unknown": unknown.Image,
        "Document": doc.Image,
        "Spreadsheet": sheet.Image,
        "Presentation": slide.Image,
        "Folder": folder.Image,
        "Archive": archive.Image,
        "Pdf": pdf.Image,
        "Code": code.Image,
        "Image": image.Image,
        "Executable": executable.Image,
        "Audio": audio.Image,
        "Video": video.Image,
    })
    for img in imageMap:
        imgList.Add(wx.Bitmap(rescale_image(imageMap[img], 32, 32)))
    imageMapIndex = defaultdict(lambda: 0)
    for count, key in enumerate(imageMap.keys()):
        imageMapIndex[key] = count

    dman = DriveManager()
    driveObjects = dman.get_drive_objects()
    colNames = ("Filename", "Type", "Owner")
    colSizes = (500, 100, 200)
    itemDisplay = DriveItemListCtrl(parentWindow.panel, imgList, imageMapIndex,
                                    colNames, colSizes)
    itemDisplay.InsertDriveObjects(driveObjects)

    parentWindow.baseBox.Add(itemDisplay,
                             proportion=5,
                             flag=wx.ALL | wx.EXPAND,
                             border=15)
