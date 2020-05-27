import wx

from .utils import rescale_image
from .assets.icon import doc, sheet, slide
from .topbarItem import TopBarItem


def topbar(parent):
    docsImg = rescale_image(doc.Image, 32, 32)
    sheetsImg = rescale_image(sheet.Image, 32, 32)
    slidesImg = rescale_image(slide.Image, 32, 32)

    fxGridSizer = wx.FlexGridSizer(1, 6, 10, 10)
    font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
    font.SetPointSize(12)

    docItem = TopBarItem(parent, docsImg, "New Document", font)
    sheetItem = TopBarItem(parent, sheetsImg, "New Sheet", font)
    slideItem = TopBarItem(parent, slidesImg, "New Presentation", font)

    fxGridSizer.AddMany([(docItem), (sheetItem), (slideItem)])

    return fxGridSizer
