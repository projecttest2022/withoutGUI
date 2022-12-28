import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import requests
import webbrowser

class MapsInterface(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Maps Interface')

        # Create the widgets
        self.label = QLabel('Enter a city name:')
        self.input_field = QLineEdit()
        self.button = QPushButton('Open in Maps')
        self.button.clicked.connect(self.open_maps)

        # Create a vertical layout and add the widgets to it
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.button)

        # Set the layout of the main widget
        self.setLayout(layout)

    def open_maps(self):
        # Open the Google Maps website
        webbrowser.open("https://www.google.com/maps")

        # Wait for 2 seconds to allow the user to see the website
        time.sleep(2)

        city = self.input_field.text()
        coordinates = self.get_coordinates(city)
        self.open_city_on_maps(city, coordinates)

    def get_coordinates(self, city):
        api_key = "AIzaSyC2SaoSKUBDXYMB4gjVX15u2mMiRywmTqo"
        endpoint = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {
            "address": city,
            "key": api_key
        }
        response = requests.get(endpoint, params=params)
        data = response.json()
        if data["status"] == "OK":
            lat = data["results"][0]["geometry"]["location"]["lat"]
            lng = data["results"][0]["geometry"]["location"]["lng"]
            return (lat, lng)
        else:
            return None

    def open_city_on_maps(self, city, coordinates):
        if coordinates:
            lat, lng = coordinates
            maps_url = f"https://www.google.com/maps?q={city}"
            webbrowser.open(maps_url)
        else:
            self.label.setText(f"Sorry, we were unable to find the coordinates of {city}.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MapsInterface()
    ex.show()
    sys.exit(app.exec_())
