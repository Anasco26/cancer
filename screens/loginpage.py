from kivymd.uix.screen import MDScreen
from assets.database.database import Database
from assets.data.user import UserData

class LoginPage(MDScreen):
     
     def __init__(self, **kwargs):
         super().__init__(**kwargs)
         self.db = Database()

     def login(self):
          email = self.ids.text_field
          password = self.ids.password_field
          user = self.db.get_user(email.text)
          if user:
               if user[3] == password.text:
                    print(user[0])
                    self.manager.transition.direction = "left"
                    UserData.user = user
                    self.manager.current = "dashboard"
               else:
                    password.helper_text = "Wrong Password Entered"
                    password.error = True
                    return
          else:
               email.helper_text = "Wrong Email or Email Address doesn't exist"
               email.error = True
               return
