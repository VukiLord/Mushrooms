

from kivy.app import App
#from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.graphics import Rectangle



class MyClass(GridLayout):
    first_name_text_input = ObjectProperty()
    
    def naming(self):
        mylabel = ObjectProperty()
        fname = self.first_name_text_input.text
        self.mylabel.text = fname
        
        print('Full Name: ', fname)
        self.first_name_text_input.text = ''
        

class FirstApp(App):
    def build(self):
        return MyClass()


if __name__ == '__main__':
    FirstApp().run()


