from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.garden.navigationdrawer import NavigationDrawer

Builder.load_string('''
<Menu>:
    NavigationDrawer:
        id: nav
        # left menu(navigationdrawer)
        anim_type: 'slide_above_anim'
        BoxLayout:
            orientation: 'vertical'
            canvas:
                Color:
                    rgba: (1,1,1,1)
                Rectangle:
                    pos: self.pos
                    size: self.size
            Label:
                text: "Menu"
                #black color
                color: 0,0,0,1
            Button:
                text:"First"
                on_release: root.change_text(self)
            Button:
                text:"Second"
                on_release: root.change_text(self)
            Button:
                text:"Third"
                on_release: root.change_text(self)
        # Initial screen
        BoxLayout:
            orientation: 'vertical'
            canvas:
                # white color
                Color:
                    rgb: (1,1,1)
            ActionBar:
                ActionView:
                    ActionPrevious:
                        app_icon: 'icon.png'
                        title:'Initial'
                        on_release: nav.toggle_state()
            Label:
                id: screen
                text: "Hello, world!"
    
''')

class Menu(BoxLayout):
    def change_text(self, obj):
        if self.ids.screen.text == "Hello, world!":
            self.ids.screen.text = "Hello, planet!"
        elif self.ids.screen.text == "Hello, planet!":
            self.ids.screen.text = "Hello, earth!"
        else:
            self.ids.screen.text = "Hello, world!"

class Example(App):
    def build(self):
        return Menu()

Example().run()
