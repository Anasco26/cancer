from kivymd.uix.screen import MDScreen
from kivy.properties import ListProperty, StringProperty
from kivymd.uix.label import MDLabel
from assets.database.database import Database
from assets.data.user import UserData
from datetime import datetime
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout

class Result(MDScreen):
    test_result = StringProperty('')
    diagnose = {}
    comment = StringProperty()
    diagnose_date = StringProperty()
    result_key = StringProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.test_result = ""
        self.comment = ""
        self.result_key = ""
        
        
    def on_start(self):
        container = self.ids.container
        container.clear_widgets()
        self.diagnose_date = str(datetime.now().strftime('%A %d %B %Y'))
        item = UserData()
        self.diagnose = item.diagnose
        UserData.diagnose = {}
        n = len(self.diagnose)
        keys = []
        explanation = []
        title = []
        if n == 0:
            self.comment = "Please select at least one symptom for the system to properly diagnose your condition."
        elif n < 4: 
            self.comment = "Nothing much to worry about, however if you noticed any additional changes. Please see a doctor"
        elif n < 6: 
            self.comment = "Please see a doctor. These might be an early signs of breast cancer"
        else:
            self.comment = "Please see a doctor immediately. These are serious signs of a breast cancer"

        for k, r in self.diagnose.items():
            title.append(r['symptom'])
            explanation.append(r['detail'])
            keys.append(k)

        # print("result=",self.title)
        for i in keys:
            self.result_key += str(i)

        self.test_result = ", ".join(title) + "."

        self.examine(explanation, container)
        
    def examine(self, explanation, container):
        
        for ex in explanation:
            lb = MDLabel(text = ex, size_hint_y= None, halign= "justify", font_style="Caption")
            lb.bind(texture_size=lambda instance, size: setattr(instance, 'size', size))
            container.add_widget(lb)
        
           
        # print('this works',self.test_result)

    def save_result(self):
        user = UserData()
        user_id = user.user[0]
        db = Database()
        db.save_diagnose(self.test_result, self.result_key, self.comment, self.diagnose_date, user_id)
        self.open_dialog()

    def open_dialog(self):
        self.dialog = MDDialog(
            title="SAVE DIAGNOSES",
            text = 'Diagnoses saved successfuly',
            buttons=[
                MDFlatButton(
                    text="OK",
                    theme_text_color="Custom",
                    on_release=self.dismiss_dialog
                    # text_color=self.theme_cls.primary_color,
                    ),
                ],
        )
        self.dialog.open()
    def dismiss_dialog(self, *args):
        # if self.dialog:
        self.dialog.dismiss()

    def save_data(self, *args):
        text = self.dialog.content.children[0].text
        self.save_result()
        print(f"Entered text: {text}")
        self.dialog.dismiss()

