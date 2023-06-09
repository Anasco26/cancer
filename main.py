from kivymd.app import MDApp
from kivy.core.window import Window
from screens.myscrens import MyScreens
from kivy.properties import StringProperty 


# Window.size = [310, 580]

class CancerApp(MDApp):
    title ="Breast Cancer"
    icon = "assets/images/brand.png"
    latoBlack = StringProperty("assets/fonts/Lato/Lato-Black.ttf")
    latoRegular = StringProperty("assets/fonts/Lato/Lato-Regular.ttf")
    latoBold = StringProperty("assets/fonts/Lato/Lato-Bold.ttf")
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        self.load_all_kv_files('screens')
        self.load_all_kv_files('components')
        return MyScreens()
    

if __name__ == '__main__':
    CancerApp().run()