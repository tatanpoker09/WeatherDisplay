import asyncio
from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label

from weather import getweather

Builder.load_string('''
<MyWidget>:
    orientation: 'vertical'
    RelativeLayout:
        Label:
            text: 'Mountain View'
            size_hint: None, None
            size: root.width * 0.8, root.height * 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.25}
            
        Image:
            source: 'resources/Sun.png'
            size_hint: None, None
            size: root.height * 0.7, root.height * 0.7
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            
        Label:
            id: temperature_label
            size_hint: None, None
            size: root.width * 0.5, root.height * 0.1
            pos_hint: {'center_x': 0.5, 'center_y': 0.15}
''')

class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)

        weather = asyncio.run(getweather('Mountain View'))
        self.ids.temperature_label.text = str(weather.current.temperature)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()
