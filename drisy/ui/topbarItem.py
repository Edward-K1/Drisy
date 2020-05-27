import wx

class TopBarItem(wx.StaticBoxSizer):

    def __init__(self, parent, image, text, textFont):
        self.box = wx.StaticBox(parent, -1)
        super().__init__(self.box)
        
        self.image = wx.StaticBitmap(parent, -1, wx.Bitmap(image))
        self.text = wx.StaticText(parent, label=text)
        self.text.Font = textFont
        self.Add(self.image, 0, wx.ALL | wx.EXPAND, 5)
        self.Add(self.text, 0, wx.ALL | wx.EXPAND, 5)

        
