from kivymd.uix.list import TwoLineAvatarListItem
from assets.data.symptoms import symptoms
from assets.data.user import UserData

class ListItemSelectMode(TwoLineAvatarListItem):
    host = None
    mode = False
    def __init__(self, pk=None, result = None, **kwargs):
        super().__init__(**kwargs)
        self.pk = pk
        self.result = result

    def preview(self):
        if not self.mode:
            for pk in self.result:
                for s in symptoms:
                    if int(s['pk']) == int(pk):
                        result = {"symptom": s['symptom'], "description": s['description'], "detail": s["details"]}
                        UserData.diagnose[pk] = result
                        break
            self.host.manager.transition.direction = "up"
            self.host.manager.current = "result"

        
