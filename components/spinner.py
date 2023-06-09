# from kivy.animation import Animation
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.clock import Clock

class Spinner(Widget):
    progress_running = True
    angle = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_angle, 0.1)
        # self.animation = Animation(angle=360, duration=1)
        # self.animation.repeat = True

    def start(self):
        self.animation.start(self)

    def on_start(self):
        # Schedule the animation to update the angle
        Clock.schedule_interval(self.update_angle, 0.1)
    
    def update_angle(self, dt):
        if self.progress_running:
            # Update the angle
            self.angle += 10
            if self.angle >= 360:
                self.angle = 0

    def stop_progress(self):
        self.progress_running = False

