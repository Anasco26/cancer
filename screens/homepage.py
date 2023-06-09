from kivymd.uix.screen import MDScreen
from assets.data.doctors import doctors
from kivymd.uix.card import MDCard
from kivymd.uix.imagelist import MDSmartTile


class HomePage(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # print("homepage at init")
        # self.on_pre_enter()

    def on_pre_enter(self):
        print("homepage")
        for doctor in doctors:
            card = MDCard(
                orientation="vertical",
                size_hint=(None, None),
                size=("280dp", "320dp"),
                pos_hint={"center_x": 0.5, "center_y": 0.5},
            )
            tile = MDSmartTile(
                source=doctor["avatar_url"],
            )
            card.add_widget(tile)
            # self.ids.doctors.add_widget(card)
        