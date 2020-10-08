from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.core.text import LabelBase
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.graphics.vertex_instructions import RoundedRectangle

Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '580')

LabelBase.register(name="SinkinSans",
                   fn_regular="police\SinkinSans-400Regular.otf",
                   fn_bold="police\SinkinSans-700Bold.otf")

LabelBase.register(name="SourceSansPro",
                   fn_regular="police\SourceSansPro-Regular.otf",
                   fn_bold="police\SourceSansPro-Bold.otf")


class PublicHelp(Screen):
    pass


class PublicLanding(Screen):
    pass


class PublicSearch(Screen):
    pass


class PublicResult(Screen):
    pass


class Result(Screen):
    pass


class Help(Screen):
    pass


class Login(Screen):
    pass


class Account(Screen):
    pass


class Search(Screen):
    pass


class Landing(Screen):
    pass


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        return kv

    def on_start(self):
        advertise_list = self.root.ids['result'].ids['advertise_list']
        for i in range(10):
            w = Button(text="Advertise here ! dmiqh dhfiodms id os qhiod q id ")
            advertise_list.add_widget(w)

        advertise_public_list = self.root.ids['public_result'].ids['advertise_list']
        for i in range(10):
            x = Button(text="Advertise here !")
            advertise_public_list.add_widget(x)


app = MyMainApp()
app.run()
