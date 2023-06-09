from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from assets.database.database import Database
from kivymd.uix.textfield import MDTextField
from kivy.properties import StringProperty



db = Database()
class RegistrationPage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def open_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.size_hint = (None, None)
        date_dialog.size = (200, 400)
        date_dialog.pos_hint = {"center_x": .5, "center_y": .5}
        date_dialog.open()

        def on_save(instance, value, date_range):
            self.ids.dob.text = str(value.strftime('%d/%m/%Y'))
            date_dialog.dismiss()

        date_dialog.bind(on_save=on_save)

    def show_date_picker(self):
        date_dialog = MDDatePicker(
            size = (300, 200),
            pos_hint = {"center_x": .5, "center_y": .5}

        )
        date_dialog.bind(on_save=self.on_save)
        # print(date_dialog)
        date_dialog.open()

    def on_save(self, instance, value, date_range):
        date = value.strftime('%d/%m/%Y')
        self.ids.dob.text = str(date)

    def check_errors(self):
        parent = self.ids.form 
        
        for child in parent.children:
            if isinstance(child, MDTextField):
                if not child.text:
                    child.error = True
                if child.error:
                    return True

    def format_phone_number(self, instance):
        text = instance.text.replace(" ", "")  # Remove spaces from the input text

        if len(text) > 0 and text[0] != "+":
            text = "+234" + text[1:]  # Prepend "+234" if the input doesn't start with "+"

        if len(text) > 4 and text[4] != " ":
            text = text[:4] + " " + text[4:]  # Insert a space after the country code

        if len(text) > 8 and text[8] != " ":
            text = text[:8] + " " + text[8:]  # Insert a space after the first group of digits

        instance.text = text

    
    def min_text_input(self, instance, value):
        text = instance.text

        if len(text) < value:
            instance.error = True
        else:
            instance.error = False
            # instance.helper_text = ""

    def filter_text_input(self, instance):
        text = instance.text
        filtered_text = ''.join(c for c in text if c.isalpha() or c.isspace())
        instance.text = filtered_text

    def register(self):
        fullname = self.ids.full_name
        email = self.ids.email
        password = self.ids.password
        dob = self.ids.dob
        phone = self.ids.phone

        # print(email.text, db.get_user(email.text))

        if db.get_user(email.text):
            email.helper_text = "Email already exists!"
            email.error = True
            return
        
        if self.check_errors(): 
            return
        
        else:
            db.register_user(fullname.text, email.text, password.text, phone.text, dob.text)
            self.manager.transition.direction = "left"
            self.manager.current = "Login"
