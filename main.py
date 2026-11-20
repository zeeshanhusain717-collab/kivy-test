from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class TestApp(App):
    def build(self):
        self.count = 0
        root = BoxLayout(orientation="vertical", padding=40, spacing=30)
        self.label = Label(text="Test chal raha hai. Button dabayein.",
                           font_size="22sp")
        self.button = Button(text="Dabaiye (0)", size_hint_y=None, height=120,
                             background_color=(0.2, 0.7, 0.3, 1))
        self.button.bind(on_release=self.on_press)
        root.add_widget(self.label)
        root.add_widget(self.button)
        return root

    def on_press(self, *args):
        self.count += 1
        self.button.text = f"Dabaiye ({self.count})"
        self.label.text = f"Button {self.count} baar dabaya gaya"


if __name__ == "__main__":
    TestApp().run()
