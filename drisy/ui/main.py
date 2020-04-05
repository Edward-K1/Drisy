import os
import sys

import wx

from inspect import getsourcefile
from .assets.icon import DrisyIcon
from .systray import DrisyTray

class MainFrame(wx.Frame):
    def __init__(self, parent, title='Drisy'):
        super(MainFrame, self).__init__(parent, title=title)

        self.SetIcon(DrisyIcon.GetIcon())
        self.tbIcon = DrisyTray(self)
        self.panel = wx.Panel(self)
        self.tbIcon.Bind(wx.EVT_MENU, self.ExitApp, id=wx.ID_EXIT)

        self.SetBaseSizer()
        self.CreateMainMenu()


    def CreateMainMenu(self):
        self.menu = wx.MenuBar()

        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT,"&Quit","Close Drisy")
        self.menu.Append(fileMenu, "&File")

        viewMenu = wx.Menu()
        self.menu.Append(viewMenu,"&View")

        toolsMenu = wx.Menu()
        self.menu.Append(toolsMenu,"&Tools")

        settingsMenu = wx.Menu()
        self.menu.Append(settingsMenu, "&Settings")

        aboutMenu = wx.Menu()
        self.menu.Append(aboutMenu, "&About")

        self.SetMenuBar(self.menu)

    def SetBaseSizer(self):
        self.baseBox = wx.BoxSizer(wx.VERTICAL)
        self.baseBoxPnl = wx.Panel(self.panel)
        self.baseBoxPnl.SetBackgroundColour('#ffffff')
        self.baseBox.Add(self.baseBoxPnl, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        self.panel.SetSizer(self.baseBox)


    def ExitApp(self, event):
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        sys.exit()


class DrisyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title='Drisy 1.0')
        self.frame.Show()
        return True


def get_base_dir():
    file_path = os.path.abspath(getsourcefile(lambda: 0))
    base_dir = os.path.dirname(file_path)
    return base_dir


if __name__ == '__main__':
    app = DrisyApp()
    app.MainLoop()
