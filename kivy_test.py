import asyncio

from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from weather import getweather


def one_hour_in_seconds():
    return 3600


class MyWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(MyWidget, self).__init__(**kwargs)
        self.update_weather()  # Initial weather update
        Clock.schedule_interval(self.update_weather, one_hour_in_seconds())  # Schedule weather update every 1 hour

    def update_weather(self, dt=None):
        weather = asyncio.run(getweather('Mountain View'))
        self.ids.temperature_label.text = str(weather.current.temperature)


class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    Builder.load_file("mywidget.kv")
    MyApp().run()
