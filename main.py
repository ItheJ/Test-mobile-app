from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Application(App):

    def click(self, instance):
        self.i += 1
        if self.i > 1:
            self.lbl.text = f"Твою маму сбил камаз {self.i} раза! Хочешь ещё?"
        else:
        
            self.lbl.text = f"Твою маму сбил камаз {self.i} раз! Хочешь ещё?"

    def click2(self, instance):
        self.i = 0

        self.lbl.text = f"Ты спас маму от камаза!"
    
    def build(self):

        all_widgets = GridLayout(cols=1)
        self.i = 0
        
        btn = Button(text="Нажми на меня, если твою маму сбил камаз", font_size=10, background_color="blue", on_press=self.click)
        btn2 = Button(text="Нажми на меня, чтобы обнулить условие", font_size=20, background_color="blue", on_press=self.click2)

        self.lbl = Label(text="       Выбери!", font_size = 20)

        all_widgets.add_widget(btn)
        all_widgets.add_widget(btn2)
        all_widgets.add_widget(self.lbl)

        return all_widgets

if __name__ == "__main__":

    Application().run()
