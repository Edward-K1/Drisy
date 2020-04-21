import wx


def TopBarItem(parent, image, text, textFont):
    box = wx.StaticBox(parent, -1)
    sizer = wx.StaticBoxSizer(box)
    bmp = wx.StaticBitmap(
        parent,
        -1,
        wx.Bitmap(image),
    )
    txt = wx.StaticText(parent, label=text)
    txt.Font = textFont
    sizer.Add(bmp, 0, wx.ALL | wx.EXPAND, 5)
    sizer.Add(txt, 0, wx.ALL | wx.EXPAND, 5)
    return sizer
