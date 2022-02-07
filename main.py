api_key = "40d1649f-0493-4b70-98ba-98533de7710b"

import os
import sys

import requests
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets

SCREEN_SIZE = [600, 450]
koord1 = 37.530887
koord2 = 55.703118
type = "map"


class Example(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.getImage()
        self.initUI()

    def getImage(self):
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={koord1},{koord2}&spn=0.002,0.002&l={type}"
        response = requests.get(map_request)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

    def initUI(self):
        desktop = QtWidgets.QApplication.desktop()

        self.setGeometry(desktop.width() // 2 - 300, desktop.height() // 2 - 225, 600, 450)
        self.setWindowTitle('Отображение карты')

        ## Изображение
        self.pixmap = QPixmap(self.map_file)
        self.image = QtWidgets.QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def closeEvent(self, event):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
