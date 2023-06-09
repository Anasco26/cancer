from kivymd.uix.screen import MDScreen
from components.listitemwithcheckbox import ListItemWithCheckbox
from assets.data.symptoms import symptoms
from assets.data.user import UserData
from components.spinner import Spinner
from kivy.clock import Clock
# from kivy.animation import Animation
from kivy.uix.modalview import ModalView


class Dashboard(MDScreen):
    result = dict()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.spinner = Spinner(
            size_hint=(None, None), size=(80, 80), pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        self.modal_view = ModalView(size_hint=(1, 1), background_color=[0, 0, 0, 0.8])
    
    def on_start(self):
        self.ids.container.clear_widgets()
        for signs in symptoms:
            add_task = ListItemWithCheckbox(pk=signs['pk'],text=signs['symptom'], secondary_text=signs['description'], detail=signs['details'])
            self.ids.container.add_widget(add_task)
        # button = MDRectangleFlatButton(
        #     text = "Check Result", size_hint_x = .85, pos_hint = {"center_x": .5}
        # )
        # self.ids.container.add_widget(button)
        # button.bind(on_release=self.start_spinner)
        

    def start_spinner(self, instance):
        self.spinner.progress_running = True
        self.modal_view.add_widget(self.spinner)  # Add only the spinner to the modal view
        self.modal_view.open()  # Open the modal view
        Clock.schedule_once(lambda dt: self.transition_to_result(), 3)


    def transition_to_result(self):
        add_task = ListItemWithCheckbox()
        print("dashboard receive", len(add_task.diagnose))
        self.result = add_task.diagnose
        self.spinner.stop_progress()
        self.modal_view.remove_widget(self.spinner)
        self.modal_view.dismiss()
        self.manager.transition.direction = "up"
        self.manager.current = "result"

    def unset_user(self):
        UserData.user = []
        UserData.diagnose = {}
