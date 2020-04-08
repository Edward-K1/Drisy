import wx
import wx.adv

from .assets.icon import DrisyIcon
from .utils import rescale_image


class DrisyTray(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        super(DrisyTray, self).__init__()
        self.frame = frame

        self.SetIcon(DrisyIcon.GetIcon(), 'Drisy')
        self.PopupMenu = self.CreatePopupMenu()

    def CreatePopupMenu(self):
        docsImg = rescale_image(r"drisy/ui/assets/icons/doc.png", 16, 16)
        sheetsImg = rescale_image(r"drisy/ui/assets/icons/sheet.png", 16, 16)
        slidesImg = rescale_image(r"drisy/ui/assets/icons/slide.png", 16, 16)

        menu = wx.Menu()
        menu.Append(wx.ID_ANY, "About")
        menu.Append(wx.ID_ANY, "Show Interface")
        menu.AppendSeparator()

        # Begin: Create Menu
        createMenu = wx.Menu()
        createDocItem = wx.MenuItem(createMenu, wx.ID_ANY, "Doc")
        createDocItem.SetBitmap(wx.Bitmap(docsImg))
        createMenu.Append(createDocItem)

        createSheetItem = wx.MenuItem(createMenu, wx.ID_ANY, "Sheet")
        createSheetItem.SetBitmap(wx.Bitmap(sheetsImg))
        createMenu.Append(createSheetItem)

        createSlideItem = wx.MenuItem(createMenu, wx.ID_ANY, "Presentation")
        createSlideItem.SetBitmap(wx.Bitmap(slidesImg))
        createMenu.Append(createSlideItem)
        menu.Append(wx.ID_ANY, "Create", createMenu)
        # End: Create Menu
        # Begin: View Menu
        viewMenu = wx.Menu()
        viewDocsItem = wx.MenuItem(viewMenu, wx.ID_ANY, "Docs")
        viewDocsItem.SetBitmap(wx.Bitmap(docsImg))
        viewMenu.Append(viewDocsItem)

        viewSheetsItem = wx.MenuItem(viewMenu, wx.ID_ANY, "Sheets")
        viewSheetsItem.SetBitmap(wx.Bitmap(sheetsImg))
        viewMenu.Append(viewSheetsItem)

        viewSlidesItem = wx.MenuItem(viewMenu, wx.ID_ANY, "Presentations")
        viewSlidesItem.SetBitmap(wx.Bitmap(slidesImg))
        viewMenu.Append(viewSlidesItem)
        menu.Append(wx.ID_ANY, "View", viewMenu)
        # End: View Menu
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit")
        return menu
