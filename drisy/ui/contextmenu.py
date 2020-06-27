import wx


class ContextMenu(wx.Menu):
    def __init__(self, parent):
        super(ContextMenu, self).__init__()

        self.parent = parent

        openMItem = wx.MenuItem(self, wx.NewId(), "Open")

        tagMenu = wx.Menu()
        tagMenu.Append(wx.NewId(), "Add")
        tagMenu.Append(wx.NewId(), "Edit")

        filterMenu = wx.Menu()
        filterMenu.Append(wx.ID_ANY, "Owner")
        filterMenu.Append(wx.ID_ANY, "Type")
        filterMenu.Append(wx.ID_ANY, "Tag")

        self.Append(openMItem)
        self.AppendSeparator()
        self.Append(wx.ID_ANY, "Tags", tagMenu)
        self.AppendSeparator()
        self.Append(wx.ID_ANY, "Filter By", filterMenu)
