import sys
from des import *
import pyowm
from pyowm.utils.config import get_default_config
from config import token_wthr

config_dict = get_default_config()
config_dict['language'] = 'ru'


class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.progressBar.value(0)
        self.ui.pushButton.clicked.connect(self.get_weather)
        self.ui.pushButton_2.clicked.connect(self.clear)


    def get_weather(self):
        owm = pyowm.OWM(token_wthr, config_dict)
        place = self.ui.lineEdit.text()
        mgr = owm.weather_manager()
        weather = mgr.weather_at_place(place).weather.temperature('celsius')["temp"]

        # for i


        if weather < 10:
            self.ui.plainTextEdit.appendPlainText(' Сейчас ' + str(weather) + ' градус(а/ов) и ппц как холодно!')

        elif weather < 20:
            self.ui.plainTextEdit.appendPlainText(' Сейчас ' + str(weather) + ' градус(а/ов) прохладно оденься теплее ')

        else:
            self.ui.plainTextEdit.appendPlainText(' Сейчас ' + str(weather) + ' градус(а/ов) нормально, одевай что хочешь')


    def clear(self):
        self.ui.plainTextEdit.clear()
        self.ui.lineEdit.clear()
        self.ui.progressBar.value(0)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())
