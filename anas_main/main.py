import sys
from custome_errors import *
sys.excepthook=my_excepthook
import wx
import settings,gui,guiTools
settings.language.init_translation()
class main(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,title=settings.app.name + _(" version ") + str(settings.app.version))
        panel=wx.Panel(self)
        sizer=wx.BoxSizer()
        self.settings=wx.Button(panel,-1,_("settings"))
        self.Bind(wx.EVT_BUTTON,lambda event:settings.settings(self).Show(),self.settings)
        sizer.Add(self.settings)
        panel.SetSizer(sizer)
        self.Bind(wx.EVT_CLOSE,self.CloseEvent)
        mb=wx.MenuBar()
        help=wx.Menu()
        cus=wx.Menu()
        telegram=cus.Append(-1,"telegram")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/mesteranasm"),telegram)
        telegramChannel=cus.Append(-1,_("telegram channel"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://t.me/tprogrammers"),telegramChannel)
        github=cus.Append(-1,"github")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://Github.com/mesteranas"),github)
        x=cus.Append(-1,"X")
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://x.com/mesteranasm"),x)
        email=cus.Append(-1,_("email"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.sendEmail("anasformohammed@gmail.com",settings.settings_handler.appName,"hello"),email)
        help.AppendSubMenu(cus,_("contect us"))
        projetGithub=help.Append(-1,_("visit project on github"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://github.com/mesteranas/{}_gui_wx".format(settings.settings_handler.appName)),projetGithub)
        donate=help.Append(-1,_("donate"))
        self.Bind(wx.EVT_MENU,lambda event:guiTools.OpenLink(self,"https://www.paypal.me/AMohammed231"),donate)
        about=help.Append(-1,_("about"))
        self.Bind(wx.EVT_MENU,lambda event:wx.MessageBox(_("{} version: {} description: {} developer: {}").format(settings.app.name,settings.app.version,settings.app.description,settings.app.creater),_("about")),about)
        mb.Append(help,_("help"))
        self.SetMenuBar(mb)
    def CloseEvent(self,event):
        if settings.settings_handler.get("g","exitdialog")=="True":
            guiTools.ExitDialog(self).Show()
        else:
            wx.Exit()
app=wx.App()
w=main()
w.Show()
app.MainLoop()