import wx
import wx.adv

from .assets.icon import DrisyIcon


class DrisyTray(wx.adv.TaskBarIcon):
    def __init__(self, frame):
        super(DrisyTray, self).__init__()
        self.frame = frame

        self.SetIcon(DrisyIcon.GetIcon(), 'Drisy')
        self.PopupMenu = self.CreatePopupMenu()

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(wx.ID_EXIT, "Exit")
        return menu
