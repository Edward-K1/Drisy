import wx


def rescale_image(image_path, width, height, quality=wx.IMAGE_QUALITY_HIGH):
    img = wx.Image(image_path)
    img = img.Scale(width, height, quality)
    return img
