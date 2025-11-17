import sys 
import requests
import os
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QPushButton 
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon 

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label = QLabel("Enter the city's name", self)
        self.city_input = QLineEdit(self) 
        self.get_weather_button = QPushButton("Get weather", self)
        self.temperature_label = QLabel(self) 
        self.emoji_label = QLabel(self) 
        self.description_label = QLabel(self)     
        self.initUI() 

    def initUI(self):
        icon_path = os.path.join(os.path.dirname(__file__), "weather_icon.jpg")
        if os.path.exists(icon_path): 
            self.setWindowIcon(QIcon(icon_path))
        else:
            print("Icon not found:", icon_path) 

        self.setGeometry(700, 250, 600, 600)
        self.setWindowTitle("Weather Forecast")   
        
        vbox = QVBoxLayout() 
        vbox.addWidget(self.city_label) 
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label) 

        self.setLayout(vbox) 

        self.city_label.setAlignment(Qt.AlignCenter) 
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter) 

        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label") 

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: Calibri;
            }           
            QLabel#city_label{
                font-size: 40px;         
            } 
            QLineEdit#city_input{
                font-size: 35px;               
            }
            QPushButton#get_weather_button{
                font-size: 40px;              
            }
            QLabel#temperature_label{
                font-size: 80px;               
            }
            QLabel#emoji_label{
                font-size: 120px; 
                font-family: Segoe UI emoji;             
            }
            QLabel#description_label{
                font-size: 45px;             
            }
        """)

        self.get_weather_button.clicked.connect(self.get_weather)
        

    def get_weather(self):
        api_key = "b71032d6891760314da7ced637ba90c4"
        city_name = self.city_input.text() 
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}" 
        
        try:
            response = requests.get(url) 
            response.raise_for_status() 
            data = response.json()

            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            match response.status_code:
                case 400:
                    self.display_error("Bad request \nplease check your input")  
                case 401:
                    self.display_error("Unauthorized \nInvalid API key")   
                case 403:
                    self.display_error("It is forbidden \nAccess is denied")    
                case 404:
                    self.display_error("Not found\nCity not found")  
                case 500:
                    self.display_error("Internal server error \nplease try again later")   
                case 502:
                    self.display_error("Bad gateway \nInvalid response from the server")   
                case 503:
                    self.display_error("Service is unavailable \nServer is down") 
                case 504:
                    self.display_error("Gateway timeout \nNo response from the server")  
                case _:
                    self.display_error(f"HTTP error has occured\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection error:\nPlease check your internet")

        except requests.exceptions.Timeout:
            self.display_error("Time out error:\nthe request timed out") 

        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects:\ncheck the URL") 

        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error:\n{req_error}") 
    
    def display_error(self, message): 
        self.temperature_label.setText(message)
        self.temperature_label.setStyleSheet("font-size: 40px;") 
        self.emoji_label.clear() 
        self.description_label.clear() 

    def display_weather(self, data):
        self.temperature_label.setStyleSheet("font-size: 80px;") 
        ktemp = data['main']['temp']  
        ctemp = ktemp - 273.15 
        self.temperature_label.setText(f"{ctemp:.1f}°C")
        wdescription = data["weather"][0]['description'] 
        wid = data['weather'][0]['id']
        self.description_label.setText(wdescription)
        self.emoji_label.setText(self.get_emoji(wid)) 
        
    @staticmethod
    def get_emoji(wid):
        
        if 200 <= wid <= 232:
            return "⛈️"
        elif 300 <= wid <= 321:
            return "🌦️"
        elif 500 <= wid <= 531:
            return "🌧️" 
        elif 600 <= wid <= 622:
            return "❄️"
        elif 701 <= wid <= 741:
            return "🌫️"
        elif wid == 762:
            return "🌋"
        elif wid == 771:
            return "💨"
        elif wid == 781:
            return "🌪️"
        elif wid == 800:
            return "☀️"
        elif 801 <= wid <= 804:
            return "☁️"
        else:
            return ""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show() 
    sys.exit(app.exec_()) 