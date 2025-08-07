# main.py
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import pytesseract
from PIL import Image
import io
import requests

class TesseractApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn = Button(text="Rozpoznaj tekst z obrazu")
        btn.bind(on_press=self.recognize_text)
        layout.add_widget(btn)
        return layout

    def recognize_text(self, instance):
        url = "https://i.imgur.com/3X6Q3xq.png"  # Przykładowy obraz
        response = requests.get(url)
        img = Image.open(io.BytesIO(response.content))
        text = pytesseract.image_to_string(img)
        print("Rozpoznany tekst:", text)

if __name__ == "__main__":
    TesseractApp().run()
