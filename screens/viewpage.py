from kivymd.uix.screen import MDScreen
from assets.database.database import Database
from assets.data.user import UserData
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from components.listitemselectmode import ListItemSelectMode

db = Database()
class ViewPage(MDScreen):
    overlay_color = get_color_from_hex("#6042e4")
    diagnose = None
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def load_data(self):
        self.ids.selection_list.clear_widgets()
        user = UserData()
        self.diagnose = db.view_diagnose(user.user[0])
        ListItemSelectMode.host = self
        for i in  self.diagnose:
            self.ids.selection_list.add_widget(ListItemSelectMode(pk=i[0], result= i[2], text=i[4], secondary_text=i[1]))

        

    def unset_user(self):
        UserData.user = []
        UserData.diagnose = {}
    

    def set_selection_mode(self, instance_selection_list, mode):
        if mode:
            md_bg_color = self.overlay_color
            left_action_items = [
                [
                    "close",
                    lambda x: self.ids.selection_list.unselected_all(),
                ]
            ]
            right_action_items = [["trash-can", lambda x: [self.delete_items(), self.ids.selection_list.unselected_all()]]]
        else:
            md_bg_color = (0, 0, 1, 1)
            left_action_items = [
                [
                    "menu",
                    lambda x: self.ids.nav_drawer.set_state("open")
                 ]
                ]
            # right_action_items = [["magnify"], ["dots-vertical"]]
            right_action_items = []
            self.ids.toolbar.title = "Breast Cancer Diagnosing System"
        ListItemSelectMode.mode = mode

        Animation(md_bg_color=md_bg_color, d=0.2).start(self.ids.toolbar)
        self.ids.toolbar.left_action_items = left_action_items
        self.ids.toolbar.right_action_items = right_action_items

    def on_selected(self, instance_selection_list, instance_selection_item):
        self.ids.toolbar.title = str(
            len(instance_selection_list.get_selected_list_items())
        )

    def on_unselected(self, instance_selection_list, instance_selection_item):
        if instance_selection_list.get_selected_list_items():
            self.ids.toolbar.title = str(
                len(instance_selection_list.get_selected_list_items())
            )

    def delete_items(self):
        items = self.ids.selection_list.get_selected_list_items()
        # print(items)
        for item in items:
            pk = item.instance_item.pk
            db.delete_diagnose(pk)
            self.ids.selection_list.remove_widget(item)
            

    
