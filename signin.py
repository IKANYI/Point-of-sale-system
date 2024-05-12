from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class signinWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        if uname == "" or passw =="":
            info.text="[color=#FF0000]username or password is required[/color]"

        else:
            if uname =="admin" and passw == "admin":
                info.text="[color=#00FF00]Logged In Successfully!!![/color]"
            else:
                 info.text="[color=#FF0000]Invalid username or password [/color]"
             
class signinApp(App):
    def build(self):
      return signinWindow()
  
if __name__ == '__main__':
    sa = signinApp()
    sa.run()