import os
import sys

import wx
import concurrent.futures
import threading

from .assets.icon import (DrisyIcon, doc, sheet, slide, unknown, image,
                          archive, folder, audio, video, pdf, executable, code)
from .systray import DrisyTray
from .utils import rescale_image
from .displayentries import CreateItemList


class MainFrame(wx.Frame):
    def __init__(self, parent, title='Drisy'):
        super(MainFrame, self).__init__(parent, title=title)

        self.SetIcon(DrisyIcon.GetIcon())
        self.tbIcon = DrisyTray(self)
        self.panel = wx.Panel(self)
        self.tbIcon.Bind(wx.EVT_MENU, self.ExitApp, id=wx.ID_EXIT)

        self.SetBaseSizer()
        self.CreateTopBar()
        self.CreateMainMenu()

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
            executor.map(CreateItemList(self))  # not proper usage of threading

        self.Size = (800, 600)

    def CreateMainMenu(self):
        self.menu = wx.MenuBar()

        fileMenu = wx.Menu()
        fileItem = fileMenu.Append(wx.ID_EXIT, "&Quit", "Close Drisy")
        self.menu.Append(fileMenu, "&File")

        viewMenu = wx.Menu()
        toolsMenu = wx.Menu()
        settingsMenu = wx.Menu()
        aboutMenu = wx.Menu()

        self.menu.Append(viewMenu, "&View")
        self.menu.Append(toolsMenu, "&Tools")
        self.menu.Append(settingsMenu, "&Settings")
        self.menu.Append(aboutMenu, "&About")

        self.SetMenuBar(self.menu)

    def CreateTopBar(self):
        self.toolbar = self.CreateToolBar(style=wx.TB_HORZ_TEXT)
        self.toolbar.AddSeparator()
        docTool = self.toolbar.AddTool(
            wx.ID_ANY, 'New Document',
            wx.Bitmap(rescale_image(doc.Image, 32, 32)), "New Google Document")
        self.toolbar.AddSeparator()
        sheetTool = self.toolbar.AddTool(
            wx.ID_ANY, 'New Spreadsheet',
            wx.Bitmap(rescale_image(sheet.Image, 32, 32)), "New Google Sheet")
        self.toolbar.AddSeparator()
        slideTool = self.toolbar.AddTool(
            wx.ID_ANY, 'New Presentation',
            wx.Bitmap(rescale_image(slide.Image, 32, 32)),
            "New Google Presentation")
        self.toolbar.AddSeparator()

        self.toolbar.Realize()

    def SetBaseSizer(self):
        self.baseBox = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.baseBox)

    def ExitApp(self, event):
        self.tbIcon.RemoveIcon()
        self.tbIcon.Destroy()
        sys.exit()


class DrisyApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None, title='Drisy 0.1')
        self.frame.Show()
        return True


if __name__ == '__main__':
    app = DrisyApp()
    app.MainLoop()
