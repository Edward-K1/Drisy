import wx


class TopBarItem(wx.StaticBoxSizer):
    def __init__(self, parent, image, text, textFont):
        self.box = wx.StaticBox(parent, -1)
        super().__init__(self.box)

        self.panel = TopBarItemPanel(parent, image, text, textFont)
        self.Add(self.panel, 0, wx.ALL | wx.EXPAND, 0)


class TopBarItemPanel(wx.Panel):
    def __init__(self, parent, image, text, textFont):
        super().__init__(parent, size=(200, 40))

        self.image = wx.StaticBitmap(self, -1, wx.Bitmap(image), (10, 5))
        self.text = wx.StaticText(self, label=text, pos=(50, 5))
        self.text.Font = textFont
        self.initialBackColor = self.GetBackgroundColour()
        self.initialForeColor = self.GetForegroundColour()

        self.image.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseOver)
        self.text.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseOver)
        self.Bind(wx.EVT_ENTER_WINDOW, self.OnMouseOver)

        self.image.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        self.text.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)
        self.Bind(wx.EVT_LEAVE_WINDOW, self.OnMouseLeave)

    def OnMouseOver(self, event):
        self.SetBackgroundColour('#3e3e3e')
        self.text.SetForegroundColour('#ffffff')
        self.Refresh()
        event.Skip()

    def OnMouseLeave(self, event):
        self.SetBackgroundColour(self.initialBackColor)
        self.text.SetForegroundColour(self.initialForeColor)
        self.Refresh()
        event.Skip()
