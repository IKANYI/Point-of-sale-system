from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class signinWindow(BoxLayout):
    pass

class signinApp(App):
    def build(self):
      return signinWindow()
  
if __name__ == '__main__':
    sa = signinApp()
    sa.run()