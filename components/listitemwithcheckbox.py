from kivymd.uix.list import TwoLineAvatarIconListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from assets.data.user import UserData


class ListItemWithCheckbox(TwoLineAvatarIconListItem):
    
    diagnose = dict()
    dialog = None
        
    def __init__(self, pk=None, detail=None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
        self.detail = detail

        # self.theme_cls.theme_style = "Light"
        # self.theme_cls.primary_palette = "Indigo"
        # self.theme_cls.font_size = "10sp"  # Adjust font size
        # self.theme_cls.icon_font_size = "24sp"  # Adjust icon size
        # self.theme_cls.secondary_text_font_style = "Caption"  # Adjust secondary text style
        # self.theme_cls.secondary_text_padding = "8dp"  # Adjust padding between lines
        
    def mark(self, check, the_list_item):
        if check.active == True:
            result = {"symptom": the_list_item.text, "description": the_list_item.secondary_text, "detail": self.detail}
            self.diagnose[self.pk] = result
            UserData.diagnose[self.pk] = result
            
        else:
            del(self.diagnose[self.pk])
        # print(sorted(self.diagnose.values())['symptom'])
        print(len(self.diagnose))
    
    def show_detail_dialog(self, item):
        #Create and open the dialog box with the details
        self.dialog = MDDialog(
            title=item.text,
            text = item.secondary_text,
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