....
    w = ButtonList(id_button=str(id_resume))
    # w.bind(on_release=lambda x: self.show_detail(x.id_button))    
    # w.fbind('on_release', self.show_detail)
    w.bind(on_release=self.show_detail)
    self.listing.add_widget(w)
...

def show_detail(self, item):
    self.save_selection(item.id_button)
    sm.transition = SlideTransition()
    sm.current = "item_detail"
    sm.transition.direction = "left"
...

class ButtonList(BoxLayout, Button):

    def __init__(self, **kwargs):
        super().__init__()
        with self.canvas.before:
            Color(0, 0, 0.7, 1, mode='rgba') if self.state == 'normal' else Color(0, 0, 1, 1, mode='rgba')
            self.rect = RoundedRectangle(size=self.size, pos=self.pos, radius=[(10, 10), (10, 10), (10, 10), (10, 10)])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.id_button = kwargs['id_button']
        ...
