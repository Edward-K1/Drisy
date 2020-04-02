from dotenv import load_dotenv

from drisy.ui.main import DrisyApp

load_dotenv()
app = DrisyApp()
app.MainLoop()
