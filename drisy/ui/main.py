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
from .const import view_docs_url, view_sheets_url, view_slides_url


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
        self.docTool = self.CreateToolBarTool('New Document', doc.Image,
                                              'New Google Document')
        self.toolbar.AddSeparator()
        self.sheetTool = self.CreateToolBarTool('New Spreadsheet', sheet.Image,
                                                "New Google Sheet")
        self.toolbar.AddSeparator()
        self.slideTool = self.CreateToolBarTool('New Presentation', slide.Image,
                                                "New Google Presentation")
        self.toolbar.AddSeparator()

        self.docTool.url = view_docs_url
        self.sheetTool.url = view_sheets_url
        self.slideTool.url = view_slides_url

        self.Bind(wx.EVT_TOOL, self.OnToolItemClick, self.docTool)
        self.Bind(wx.EVT_TOOL, self.OnToolItemClick, self.sheetTool)
        self.Bind(wx.EVT_TOOL, self.OnToolItemClick, self.slideTool)

        self.toolbar.Realize()

    def CreateToolBarTool(self, label, image, tooltip):
        return self.toolbar.AddTool(wx.ID_ANY, label,
                                    wx.Bitmap(rescale_image(image, 32, 32)),
                                    tooltip)

    def OnToolItemClick(self, event):
        import webbrowser as browser
        obj = event.GetEventObject().FindById(event.GetId())
        browser.open(obj.url)

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
