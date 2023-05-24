import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QPushButton, QLineEdit
import datetime
from dateutil.relativedelta import relativedelta
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow(object):
    indexProduc=0
    categoriaProduc='Todos los productos'
    def setupUi(self, MainWindow , cursor, id, LogIn):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(958, 794)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_83 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_83.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_83.setSpacing(0)
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.Navbar_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Navbar_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.Navbar_Frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Navbar_Frame.setStyleSheet("background-color: #F4F4F4;")
        self.Navbar_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navbar_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navbar_Frame.setObjectName("Navbar_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Navbar_Frame)
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_Info_actual = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_Info_actual.setMinimumSize(QtCore.QSize(0, 0))
        self.label_Info_actual.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_Info_actual.setText("")
        self.label_Info_actual.setWordWrap(True)
        self.label_Info_actual.setObjectName("label_Info_actual")
        self.horizontalLayout_2.addWidget(self.label_Info_actual)
        self.label_3 = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_3.setMinimumSize(QtCore.QSize(70, 70))
        self.label_3.setStyleSheet("image: url(:/menu/logonegro.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.Navbar_Frame)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 87 18pt;\n"
"color: rgb(0, 0, 0);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.Navbar_Frame)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/menuiconBLACK.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/menu/menuIcon.png);\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout_83.addWidget(self.Navbar_Frame, 0, 0, 1, 1)
        self.Frame_Inferior = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Inferior.setMinimumSize(QtCore.QSize(0, 0))
        self.Frame_Inferior.setStyleSheet("background-color: #231f20;")
        self.Frame_Inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Inferior.setObjectName("Frame_Inferior")
        self.gridLayout = QtWidgets.QGridLayout(self.Frame_Inferior)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.Frame_Inferior)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame)
        self.stackedWidget.setMinimumSize(QtCore.QSize(300, 70))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Catalogo_2 = QtWidgets.QWidget()
        self.Catalogo_2.setObjectName("Catalogo_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Catalogo_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.Catalogo_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.NavSecundaria = QtWidgets.QFrame(self.frame_3)
        self.NavSecundaria.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"")
        self.NavSecundaria.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.NavSecundaria.setFrameShadow(QtWidgets.QFrame.Raised)
        self.NavSecundaria.setObjectName("NavSecundaria")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.NavSecundaria)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_10.addWidget(self.NavSecundaria, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.Catalogo_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Foto = QtWidgets.QFrame(self.frame_5)
        self.Foto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Foto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Foto.setObjectName("Foto")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Foto)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_6 = QtWidgets.QFrame(self.Foto)
        self.frame_6.setStyleSheet("")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_27.setMinimumSize(QtCore.QSize(50, 60))
        self.pushButton_27.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 25pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 25pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_12.addWidget(self.pushButton_27, 0, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.frame_11 = QtWidgets.QFrame(self.Foto)
        self.frame_11.setStyleSheet("")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setMinimumSize(QtCore.QSize(300, 300))
        self.label_6.setStyleSheet("\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:90%;\n"
"    border: .5px solid #e6b31e;")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_13.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_11)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_13.addWidget(self.label_7, 3, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_22.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_22.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setReadOnly(False)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_13.addWidget(self.lineEdit_22, 2, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.frame_11)
        self.lineEdit_24.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_24.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setReadOnly(False)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_13.addWidget(self.lineEdit_24, 4, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_13.addWidget(self.label_8, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_13.addItem(spacerItem2, 5, 0, 1, 1)
        self.horizontalLayout_3.addWidget(self.frame_11)
        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.Foto)
        self.Info = QtWidgets.QFrame(self.frame_5)
        self.Info.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Info.setObjectName("Info")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Info)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.frame_12 = QtWidgets.QFrame(self.Info)
        self.frame_12.setStyleSheet("")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_12)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_13 = QtWidgets.QLabel(self.frame_12)
        self.label_13.setText("")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_18.addWidget(self.label_13, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_12)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_18.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_12)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_18.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.frame_12)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_18.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_12)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_18.addWidget(self.label_11, 1, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_12)
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout_18.addWidget(self.plainTextEdit, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_18.addItem(spacerItem3, 7, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.frame_12)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout_18.addWidget(self.label_15, 6, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.Info)
        self.frame_13.setStyleSheet("")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_13)
        self.pushButton_11.setMinimumSize(QtCore.QSize(50, 60))
        self.pushButton_11.setMaximumSize(QtCore.QSize(50, 60))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 25pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 25pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_19.addWidget(self.pushButton_11, 0, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.frame_13)
        self.horizontalLayout_4.setStretch(0, 8)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout.addWidget(self.Info)
        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 5)
        self.gridLayout_20.addWidget(self.frame_5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)
        self.stackedWidget.addWidget(self.Catalogo_2)
        self.InfoPersona_2 = QtWidgets.QWidget()
        self.InfoPersona_2.setObjectName("InfoPersona_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.InfoPersona_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_128 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_128.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_128.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_128.setObjectName("label_128")
        self.gridLayout_4.addWidget(self.label_128, 2, 1, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_15.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_15.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_4.addWidget(self.lineEdit_15, 5, 2, 1, 1)
        self.label_131 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_131.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_131.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_131.setObjectName("label_131")
        self.gridLayout_4.addWidget(self.label_131, 5, 1, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_14.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_14.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_4.addWidget(self.lineEdit_14, 4, 2, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_13.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_4.addWidget(self.lineEdit_13, 2, 2, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_10.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_4.addWidget(self.lineEdit_10, 3, 2, 1, 1)
        self.label_130 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_130.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_130.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_130.setObjectName("label_130")
        self.gridLayout_4.addWidget(self.label_130, 3, 1, 1, 1)
        self.label_132 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_132.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_132.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_132.setObjectName("label_132")
        self.gridLayout_4.addWidget(self.label_132, 1, 1, 1, 1)
        self.label_133 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_133.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_133.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_133.setObjectName("label_133")
        self.gridLayout_4.addWidget(self.label_133, 6, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_11.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_4.addWidget(self.lineEdit_11, 1, 2, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_129.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_129.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_129.setObjectName("label_129")
        self.gridLayout_4.addWidget(self.label_129, 4, 1, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_12.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout_4.addWidget(self.lineEdit_12, 0, 2, 1, 1)
        self.label_134 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_134.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_134.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_134.setObjectName("label_134")
        self.gridLayout_4.addWidget(self.label_134, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 0, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(150, 0, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 0, 3, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.InfoPersona_2)
        self.label_127.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_127.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_127.setObjectName("label_127")
        self.gridLayout_4.addWidget(self.label_127, 0, 1, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_16.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_16.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_4.addWidget(self.lineEdit_16, 6, 2, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.InfoPersona_2)
        self.lineEdit_17.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_17.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_4.addWidget(self.lineEdit_17, 7, 2, 1, 1)
        self.stackedWidget.addWidget(self.InfoPersona_2)
        self.Membresia_2 = QtWidgets.QWidget()
        self.Membresia_2.setObjectName("Membresia_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Membresia_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_7 = QtWidgets.QFrame(self.Membresia_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem6 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem6, 2, 4, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem7, 3, 4, 1, 1)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_32.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_32.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_32.setReadOnly(True)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_14.addWidget(self.lineEdit_32, 0, 2, 1, 2)
        self.label_149 = QtWidgets.QLabel(self.frame_7)
        self.label_149.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_149.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_149.setObjectName("label_149")
        self.gridLayout_14.addWidget(self.label_149, 1, 0, 1, 3)
        self.label_150 = QtWidgets.QLabel(self.frame_7)
        self.label_150.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_150.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_150.setObjectName("label_150")
        self.gridLayout_14.addWidget(self.label_150, 2, 0, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_33.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_33.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_33.setText("")
        self.lineEdit_33.setReadOnly(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_14.addWidget(self.lineEdit_33, 2, 1, 1, 3)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_34.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_34.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_34.setText("")
        self.lineEdit_34.setReadOnly(True)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_14.addWidget(self.lineEdit_34, 1, 3, 1, 1)
        self.label_151 = QtWidgets.QLabel(self.frame_7)
        self.label_151.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_151.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_151.setObjectName("label_151")
        self.gridLayout_14.addWidget(self.label_151, 0, 0, 1, 2)
        self.label_163 = QtWidgets.QLabel(self.frame_7)
        self.label_163.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_163.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_163.setObjectName("label_163")
        self.gridLayout_14.addWidget(self.label_163, 4, 0, 1, 1)
        self.label_152 = QtWidgets.QLabel(self.frame_7)
        self.label_152.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_152.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_152.setObjectName("label_152")
        self.gridLayout_14.addWidget(self.label_152, 3, 0, 1, 1)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_35.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_35.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_35.setText("")
        self.lineEdit_35.setReadOnly(True)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_14.addWidget(self.lineEdit_35, 3, 1, 1, 3)
        self.lineEdit_45 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_45.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_45.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_45.setText("")
        self.lineEdit_45.setReadOnly(True)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.gridLayout_14.addWidget(self.lineEdit_45, 4, 1, 1, 3)
        spacerItem8 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem8, 4, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem9, 0, 4, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(180, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_14.addItem(spacerItem10, 1, 4, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.Membresia_2)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.label_164 = QtWidgets.QLabel(self.frame_8)
        self.label_164.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_164.setAlignment(QtCore.Qt.AlignCenter)
        self.label_164.setObjectName("label_164")
        self.gridLayout_15.addWidget(self.label_164, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_15.addItem(spacerItem11, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_8)
        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 3)
        self.stackedWidget.addWidget(self.Membresia_2)
        self.Reusmen_2 = QtWidgets.QWidget()
        self.Reusmen_2.setObjectName("Reusmen_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Reusmen_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_9 = QtWidgets.QFrame(self.Reusmen_2)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem12 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem13, 0, 0, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.frame_9)
        self.label_165.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_165.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_165.setObjectName("label_165")
        self.gridLayout_16.addWidget(self.label_165, 1, 1, 1, 1)
        self.lineEdit_46 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_46.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_46.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_46.setReadOnly(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout_16.addWidget(self.lineEdit_46, 1, 2, 1, 1)
        self.lineEdit_47 = QtWidgets.QLineEdit(self.frame_9)
        self.lineEdit_47.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_47.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_47.setReadOnly(True)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.gridLayout_16.addWidget(self.lineEdit_47, 0, 2, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.frame_9)
        self.label_166.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_166.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_166.setObjectName("label_166")
        self.gridLayout_16.addWidget(self.label_166, 0, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem14, 0, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem15, 1, 3, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_10 = QtWidgets.QFrame(self.Reusmen_2)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.TablaEmpleados_5 = QtWidgets.QTableWidget(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_5.setFont(font)
        self.TablaEmpleados_5.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #77838d;\n"
"    border: .5px solid #034aa6;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(202, 202, 202);\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #343434;\n"
"    border:  .3px solid #034aa6;\n"
"    background-color: whitesmoke;\n"
"}\n"
"")
        self.TablaEmpleados_5.setDragEnabled(False)
        self.TablaEmpleados_5.setObjectName("TablaEmpleados_5")
        self.TablaEmpleados_5.setColumnCount(4)
        self.TablaEmpleados_5.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_5.setHorizontalHeaderItem(3, item)
        self.TablaEmpleados_5.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_5.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_5.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_5.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_5.verticalHeader().setVisible(False)
        self.TablaEmpleados_5.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_17.addWidget(self.TablaEmpleados_5, 1, 0, 1, 1)
        self.label_167 = QtWidgets.QLabel(self.frame_10)
        self.label_167.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_167.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_167.setObjectName("label_167")
        self.gridLayout_17.addWidget(self.label_167, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_168 = QtWidgets.QLabel(self.frame_10)
        self.label_168.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_168.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_168.setObjectName("label_168")
        self.gridLayout_17.addWidget(self.label_168, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.TablaEmpleados_6 = QtWidgets.QTableWidget(self.frame_10)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_6.setFont(font)
        self.TablaEmpleados_6.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #77838d;\n"
"    border: .5px solid #034aa6;\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"\n"
"}\n"
"QTableWidget{\n"
"background-color: rgb(202, 202, 202);\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #343434;\n"
"    border:  .3px solid #034aa6;\n"
"    background-color: whitesmoke;\n"
"}\n"
"")
        self.TablaEmpleados_6.setDragEnabled(False)
        self.TablaEmpleados_6.setObjectName("TablaEmpleados_6")
        self.TablaEmpleados_6.setColumnCount(4)
        self.TablaEmpleados_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_6.setHorizontalHeaderItem(3, item)
        self.TablaEmpleados_6.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_6.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_6.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_6.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_6.verticalHeader().setVisible(False)
        self.TablaEmpleados_6.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_17.addWidget(self.TablaEmpleados_6, 3, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 2)
        self.stackedWidget.addWidget(self.Reusmen_2)
        self.ActualizarInfo = QtWidgets.QWidget()
        self.ActualizarInfo.setObjectName("ActualizarInfo")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.ActualizarInfo)
        self.gridLayout_2.setContentsMargins(-1, -1, -1, 50)
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem16 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 1, 0, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.ActualizarInfo)
        self.lineEdit_18.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_18.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_18.setReadOnly(False)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_2.addWidget(self.lineEdit_18, 1, 2, 1, 1)
        self.lineEdit_20 = QtWidgets.QLineEdit(self.ActualizarInfo)
        self.lineEdit_20.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_20.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_20.setReadOnly(False)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.gridLayout_2.addWidget(self.lineEdit_20, 2, 2, 1, 1)
        self.label_136 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_136.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_136.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_136.setObjectName("label_136")
        self.gridLayout_2.addWidget(self.label_136, 1, 1, 1, 1)
        self.label_135 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_135.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_135.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_135.setObjectName("label_135")
        self.gridLayout_2.addWidget(self.label_135, 2, 1, 1, 1)
        self.label_170 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_170.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_170.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_170.setObjectName("label_170")
        self.gridLayout_2.addWidget(self.label_170, 0, 1, 1, 2, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_138 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_138.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_138.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_138.setObjectName("label_138")
        self.gridLayout_2.addWidget(self.label_138, 4, 1, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.ActualizarInfo)
        self.lineEdit_21.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_21.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_21.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_2.addWidget(self.lineEdit_21, 4, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.ActualizarInfo)
        self.pushButton_5.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/ojo.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_5.setText("")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 4, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 4, 4, 1, 1)
        self.BuscarBotonActualizar_4 = QtWidgets.QPushButton(self.ActualizarInfo)
        self.BuscarBotonActualizar_4.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_4.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"\n"
"")
        self.BuscarBotonActualizar_4.setObjectName("BuscarBotonActualizar_4")
        self.gridLayout_2.addWidget(self.BuscarBotonActualizar_4, 7, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.ActualizarInfo)
        self.lineEdit_19.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_19.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_19.setReadOnly(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.gridLayout_2.addWidget(self.lineEdit_19, 5, 2, 1, 1)
        self.label_137 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_137.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_137.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_137.setObjectName("label_137")
        self.gridLayout_2.addWidget(self.label_137, 5, 1, 1, 1)
        self.label_171 = QtWidgets.QLabel(self.ActualizarInfo)
        self.label_171.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_171.setAlignment(QtCore.Qt.AlignCenter)
        self.label_171.setObjectName("label_171")
        self.gridLayout_2.addWidget(self.label_171, 6, 1, 1, 3)
        self.stackedWidget.addWidget(self.ActualizarInfo)
        self.Menu_2 = QtWidgets.QWidget()
        self.Menu_2.setObjectName("Menu_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.Menu_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_7.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_5.addWidget(self.pushButton_7, 1, 2, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem18, 7, 0, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_5.addWidget(self.pushButton_13, 7, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem19, 10, 0, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_15.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_5.addWidget(self.pushButton_15, 10, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem20, 4, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_5.addWidget(self.pushButton_16, 4, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem21, 10, 3, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(149, 117, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem22, 1, 0, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem23, 4, 0, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem24, 1, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_14.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (4).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_14.setIcon(icon2)
        self.pushButton_14.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_5.addWidget(self.pushButton_14, 7, 2, 1, 1)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem25, 7, 3, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_17.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_17.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_17.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (3).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_17.setIcon(icon3)
        self.pushButton_17.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_5.addWidget(self.pushButton_17, 10, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_9.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_6.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/MenuCliente/MenuCliente (2).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon4)
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_5.addWidget(self.pushButton_6, 4, 2, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_23.setMinimumSize(QtCore.QSize(400, 70))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:10px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_5.addWidget(self.pushButton_23, 8, 1, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem26, 8, 0, 1, 1)
        self.pushButton_24 = QtWidgets.QPushButton(self.Menu_2)
        self.pushButton_24.setMinimumSize(QtCore.QSize(110, 120))
        self.pushButton_24.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_24.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/MenuCliente/ActualizarInfo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_24.setIcon(icon5)
        self.pushButton_24.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_24.setObjectName("pushButton_24")
        self.gridLayout_5.addWidget(self.pushButton_24, 8, 2, 1, 1)
        self.stackedWidget.addWidget(self.Menu_2)
        self.gridLayout_6.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.Frame_Inferior)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setMaximumSize(QtCore.QSize(0, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setHorizontalSpacing(5)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_19.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_19.setText("")
        self.pushButton_19.setIcon(icon4)
        self.pushButton_19.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_19.setObjectName("pushButton_19")
        self.gridLayout_7.addWidget(self.pushButton_19, 3, 1, 1, 2)
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_22.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_22.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_22.setText("")
        self.pushButton_22.setIcon(icon1)
        self.pushButton_22.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout_7.addWidget(self.pushButton_22, 2, 1, 1, 1)
        self.pushButton_20 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_20.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_20.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_20.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_20.setText("")
        self.pushButton_20.setIcon(icon2)
        self.pushButton_20.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_20.setObjectName("pushButton_20")
        self.gridLayout_7.addWidget(self.pushButton_20, 4, 1, 1, 2)
        self.pushButton_21 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_21.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_21.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_21.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_21.setText("")
        self.pushButton_21.setIcon(icon3)
        self.pushButton_21.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_21.setObjectName("pushButton_21")
        self.gridLayout_7.addWidget(self.pushButton_21, 6, 1, 1, 2)
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_26.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_26.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_26.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_26.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/menu/logouthover.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_26.setIcon(icon6)
        self.pushButton_26.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_26.setObjectName("pushButton_26")
        self.gridLayout_7.addWidget(self.pushButton_26, 7, 1, 1, 1)
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_25.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_25.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setIcon(icon5)
        self.pushButton_25.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_25.setObjectName("pushButton_25")
        self.gridLayout_7.addWidget(self.pushButton_25, 5, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_18.setMinimumSize(QtCore.QSize(110, 100))
        self.pushButton_18.setMaximumSize(QtCore.QSize(110, 120))
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 14pt \"Bahnschrift SemiBold\";\n"
"    color: whitesmoke;\n"
"    border-radius:40px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_18.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/menu/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_18.setIcon(icon7)
        self.pushButton_18.setIconSize(QtCore.QSize(50, 50))
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_7.addWidget(self.pushButton_18, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout_83.addWidget(self.Frame_Inferior, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        """
        Aqui inician los botenes hacia las funciones
        """
        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # Botones del menu 
        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_16.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_15.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))
        
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_14.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))

        self.pushButton_23.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ActualizarInfo))
        self.pushButton_24.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ActualizarInfo))
       
        
        #menu de navegacion
        self.pushButton.clicked.connect(lambda: self.desplegarMenu())
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Menu_2))
        
        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.InfoPersona_2))
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Membresia_2))
        self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Catalogo_2))
        self.pushButton_21.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.Reusmen_2))
        self.pushButton_25.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ActualizarInfo))
        self.pushButton_26.clicked.connect(lambda: self.cerrarSesion(MainWindow, cursor, LogIn))
        
        #Fecha de hoy
        fechaActual = datetime.datetime.now()
        fecha=datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
        #informacion personal
        sql = "select * from cliente where cast(id_cliente as varchar)='{}' """.format(id)
        cursor.execute(sql)
        row=cursor.fetchall()
        for rows in row:
                #informacion personal
                self.lineEdit_12.setText(str(rows[0]))
                self.lineEdit_11.setText(str(rows[1]))
                self.lineEdit_13.setText(str(rows[2]))
                self.lineEdit_10.setText(str(rows[3]))
                self.lineEdit_14.setText(str(rows[4]))
                self.lineEdit_15.setText(str(rows[5]))
                self.lineEdit_16.setText(str(rows[6]))
                self.lineEdit_17.setText(str(rows[11]))
                        #Informacion membresia
                self.lineEdit_32.setText(str(rows[0]))
                self.lineEdit_34.setText(str(rows[1]))
                self.lineEdit_33.setText(str(rows[12]))
                self.lineEdit_35.setText(str(rows[8]))  
                self.lineEdit_45.setText(str(rows[9])) 
                password=str(rows[10])
                venci = str(rows[9])
                #Seguimiento info
                self.lineEdit_47.setText(str(rows[0]))  
                self.lineEdit_46.setText(str(rows[1])) 
        #Informacion membresia
        ano = venci[:4]
        mes = venci[5:7]
        dia = venci[8:11]
        venc = datetime.datetime(int(ano), int(mes), int(dia))
        venci =datetime.datetime.strftime(venc, '%d/%m/%Y')
        today = datetime.datetime.today()
        if today >= venc:
                resta = today - venc
                msg ="Tu membresia vencio hace "+str(resta.days)+" dias el dia "+str(venci)
                self.label_164.setText(msg)
        else:
                resta = venc - today
                msg ="Tu membresia vencera en "+str(resta.days)+" dias el dia "+str(venci)
                self.label_164.setText(msg)
        self.lineEdit_21.setText(password)
        #Actualizar informacion
        self.BuscarBotonActualizar_4.clicked.connect(lambda: self.actualizarInfo(cursor, id, password))
        self.pushButton_5.clicked.connect(lambda: self.passwordHide(self.lineEdit_21))
        #Seguimiento 
        self.seguimientoAct(cursor, id)
        self.pushButton_17.clicked.connect(lambda: self.seguimientoAct(cursor, id))
        self.pushButton_15.clicked.connect(lambda: self.seguimientoAct(cursor, id))
        self.pushButton_21.clicked.connect(lambda: self.seguimientoAct(cursor, id))
        
        #Catalogo de productos:
        self.pushButton_13.clicked.connect(lambda: self.IniciarCatalogo(cursor))
        self.pushButton_14.clicked.connect(lambda: self.IniciarCatalogo(cursor))
        self.pushButton_20.clicked.connect(lambda: self.IniciarCatalogo(cursor))
        self.pushButton_11.clicked.connect(lambda:self.siguienteProducto(cursor))
        self.pushButton_27.clicked.connect(lambda:self.anteriorProducto(cursor))
        

            
    #funcion para el menu de navegacion
    def desplegarMenu(self):
        
        if True:
            width = self.frame_2.width()
            normal = 0
            if width==0:
                extender = 150
            else:
                extender = normal
            
            self.animacion = QtCore.QPropertyAnimation(self.frame_2, b'minimumWidth') 
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width) 
            self.animacion.setEndValue(extender) 
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart) 
            self.animacion.start()
    
    def actualizarInfo(self, cursor, id, password):
        peso=self.lineEdit_18.text()
        altura=self.lineEdit_20.text()
        passw=self.lineEdit_21.text()

        fechaActual = datetime.datetime.now()
        fecha=datetime.datetime.strftime(fechaActual, '%d/%m/%Y')

        alt=float(altura)
        pes=float(peso) 
        IMC = pes / (alt**2)
            
        if IMC<18.5:
                IMCS= str(self.truncate(IMC,2))+" Bajo peso"
        elif (IMC<=24.9) and (IMC>=18.5):
                IMCS= str(self.truncate(IMC,2))+" Peso saludable"
        elif (IMC<=29.9) and (IMC>=25):
                IMCS= str(self.truncate(IMC,2))+" Sobrepeso"  
        elif (IMC>30):
                IMCS= str(self.truncate(IMC,2))+" Obesidad" 
        self.lineEdit_19.setText(IMCS)
        if len(peso)==0:
            self.msgError("Falta de informacion", "Debes ingresar tu peso actual")
        elif len(altura)==0:
            self.msgError("Falta de informacion", "Debes ingresar tu altura actual para continuar")
        elif len(passw)==0:
            SQL=""" update cliente set peso_act='{}', altura='{}', IMC='{}' where id_cliente='{}' """.format(peso, altura, IMCS, id)
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                print(ex)  
            SQL=""" insert into actualizaciones (ID_cliente, Fecha_Vencimiento, peso_act, altura, IMC) values ('{}','{}','{}','{}','{}'); """.format(id,str(fecha),peso,altura,IMCS)
            cursor.execute(SQL)     
            cursor.connection.commit()

            self.lineEdit_18.clear()
            self.lineEdit_20.clear()
        else:
                SQL=""" update cliente set peso_act='{}', altura='{}', IMC='{}', contraseña='{}' where id_cliente='{}' """.format(peso, altura, IMCS, passw, id)
                try:
                        cursor.execute(SQL)     
                        cursor.connection.commit()
                except Exception as ex:
                        print(ex)  
                SQL=""" insert into actualizaciones (ID_cliente, Fecha_Vencimiento, peso_act, altura, IMC) values ('{}','{}','{}','{}','{}'); """.format(id,str(fecha),peso,altura,IMCS)
                cursor.execute(SQL)     
                cursor.connection.commit()

                self.lineEdit_18.clear()
                self.lineEdit_20.clear()

    def seguimientoAct(self, cursor, id):
        SQL="""select * from visita where cast(ID as varchar)='{}' """.format(id)
        cursor.execute(SQL)
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
                self.TablaEmpleados_5.setRowCount(tablerow + 1)
                self.TablaEmpleados_5.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                self.TablaEmpleados_5.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                self.TablaEmpleados_5.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                self.TablaEmpleados_5.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                tablerow+=1
        SQL="""select * from actualizaciones where cast(ID_cliente as varchar)='{}' """.format(id)
        cursor.execute(SQL)
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
                self.TablaEmpleados_6.setRowCount(tablerow + 1)
                self.TablaEmpleados_6.setItem(tablerow,0,QTableWidgetItem(str(rows[1])))
                self.TablaEmpleados_6.setItem(tablerow,1,QTableWidgetItem(str(rows[2])))
                self.TablaEmpleados_6.setItem(tablerow,2,QTableWidgetItem(str(rows[3])))
                self.TablaEmpleados_6.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                tablerow+=1    
                
    def IniciarCatalogo(self,cursor):
        sql="SELECT * FROM inventario ORDER BY codigo asc LIMIT 1;"
        cursor.execute(sql)
        row=cursor.fetchall()
        if (len(row)) == 0:
            self.msgError("No hay productos disponibles :(")
        else:
            for rows in row:
                codigo = (rows[0])
                nombre = (rows[1])
                cantidad= (rows[2])
                categoria =(rows[5])
                precio = (rows[6])
                descripcion=(rows[8])
                direccionfoto =(rows[9])
        
        foto=QPixmap(direccionfoto)
        self.label_6.setPixmap(foto)
        self.lineEdit_22.setText(str(codigo))
        self.lineEdit_24.setText(nombre)
        self.label_10.setText("Precio: "+precio)
        self.plainTextEdit.insertPlainText(descripcion)
        self.label_14.setText(categoria)
        if(cantidad==0):
            self.label_15.setText("No disponible :( ")
        elif(cantidad>0 and cantidad<=10):
            self.label_15.setText("¡Quedan pocas unidades!")
        else:
            self.label_15.setText(" ¡Aun disponible!")
    
    def siguienteProducto(self,cursor):
        self.plainTextEdit.clear()
        cursor.execute("select *from inventario")
        row=cursor.fetchall()
        cantidad = len(row)
        if(self.indexProduc+1)!=cantidad:
            self.indexProduc+=1
        codigo = (row[self.indexProduc][0])
        nombre = (row[self.indexProduc][1])
        cantidad= (row[self.indexProduc][2])
        categoria =(row[self.indexProduc][5])
        precio = (row[self.indexProduc][6])
        descripcion=(row[self.indexProduc][8])
        direccionfoto =(row[self.indexProduc][9])
        foto=QPixmap(direccionfoto)
        self.label_6.setPixmap(foto)
        self.lineEdit_22.setText(str(codigo))
        self.lineEdit_24.setText(nombre)
        self.label_10.setText("Precio: "+precio)
        self.plainTextEdit.insertPlainText(descripcion)
        self.label_14.setText(categoria)
        if(cantidad==0):
            self.label_15.setText("No disponible :( ")
        elif(cantidad>0 and cantidad<=10):
            self.label_15.setText("¡Quedan pocas unidades!")
        else:
            self.label_15.setText(" ¡Aun disponible!")
        
    
    def anteriorProducto(self,cursor):
        self.plainTextEdit.clear()
        cursor.execute("select *from inventario")
        row=cursor.fetchall()
        if (self.indexProduc) != 0:
            self.indexProduc-=1
        codigo = (row[self.indexProduc][0])
        nombre = (row[self.indexProduc][1])
        cantidad= (row[self.indexProduc][2])
        categoria =(row[self.indexProduc][5])
        precio = (row[self.indexProduc][6])
        descripcion=(row[self.indexProduc][8])
        direccionfoto =(row[self.indexProduc][9])
        foto=QPixmap(direccionfoto)
        self.label_6.setPixmap(foto)
        self.lineEdit_22.setText(str(codigo))
        self.lineEdit_24.setText(nombre)
        self.label_10.setText("Precio: "+precio)
        self.plainTextEdit.insertPlainText(descripcion)
        self.label_14.setText(categoria)
        if(cantidad==0):
            self.label_15.setText("No disponible :( ")
        elif(cantidad>0 and cantidad<=10):
            self.label_15.setText("¡Quedan pocas unidades!")
        else:
            self.label_15.setText(" ¡Aun disponible!")
        
    
    def passwordHide(self, passw):
        if passw.echoMode() == QLineEdit.Password:
            passw.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            passw.setEchoMode(QtWidgets.QLineEdit.Password)

    def cerrarSesion(self, MainWindow, cursor, Login):
        MainWindow.close()
        Login.show()

    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
    
    def truncate(self, number: float, max_decimals: int) -> float:
        int_part, dec_part = str(number).split(".")
        return float(".".join((int_part, dec_part[:max_decimals])))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Clientes Teflon Academy"))
        self.label_4.setText(_translate("MainWindow", "  Bienvenido "))
        self.pushButton_27.setText(_translate("MainWindow", "<"))
        self.label_7.setText(_translate("MainWindow", "Nombre del producto:"))
        self.label_8.setText(_translate("MainWindow", "Codigo del producto:"))
        self.label_12.setText(_translate("MainWindow", "Categoria:"))
        self.label_10.setText(_translate("MainWindow", "Precio:"))
        self.label_14.setText(_translate("MainWindow", "Suplemento"))
        self.label_11.setText(_translate("MainWindow", "Información del producto:"))
        self.label_15.setText(_translate("MainWindow", "Disponible!"))
        self.pushButton_11.setText(_translate("MainWindow", ">"))
        self.label_128.setText(_translate("MainWindow", "Teléfono"))
        self.label_131.setText(_translate("MainWindow", "Peso actual:"))
        self.label_130.setText(_translate("MainWindow", "Correo electronico:"))
        self.label_132.setText(_translate("MainWindow", "Nombre:"))
        self.label_133.setText(_translate("MainWindow", "Altura:"))
        self.label_129.setText(_translate("MainWindow", "Edad:"))
        self.label_134.setText(_translate("MainWindow", "IMC:"))
        self.label_127.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_149.setText(_translate("MainWindow", "Nombre:"))
        self.label_150.setText(_translate("MainWindow", "Fecha de ingreso:"))
        self.label_151.setText(_translate("MainWindow", "ID de cliente:"))
        self.label_163.setText(_translate("MainWindow", "Fecha de vencimiento:"))
        self.label_152.setText(_translate("MainWindow", "Membresia actual:"))
        self.label_164.setText(_translate("MainWindow", "Tu membresía vence en: "))
        self.label_165.setText(_translate("MainWindow", "Nombre:"))
        self.label_166.setText(_translate("MainWindow", "ID de cliente:"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nombre"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.TablaEmpleados_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Hora"))
        self.label_167.setText(_translate("MainWindow", "Seguimiento de visitas"))
        self.label_168.setText(_translate("MainWindow", "Seguimiento de avances"))
        item = self.TablaEmpleados_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Fecha"))
        item = self.TablaEmpleados_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso"))
        item = self.TablaEmpleados_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Altura"))
        item = self.TablaEmpleados_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IMC"))
        self.label_136.setText(_translate("MainWindow", "Peso actual:"))
        self.label_135.setText(_translate("MainWindow", "Altura:"))
        self.label_170.setText(_translate("MainWindow", "Actualiza tu informacion"))
        self.label_138.setText(_translate("MainWindow", "Contraseña:"))
        self.BuscarBotonActualizar_4.setText(_translate("MainWindow", "Actualizar"))
        self.label_137.setText(_translate("MainWindow", "Tu nuevo IMC:"))
        self.label_171.setText(_translate("MainWindow", "Si no deseas actualizar tu contraseña deja la actual\n"
" o deja el espacio en blanco :)"))
        self.pushButton_13.setText(_translate("MainWindow", "Ver catálogo de productos"))
        self.pushButton_15.setText(_translate("MainWindow", "Ver resumen personal"))
        self.pushButton_16.setText(_translate("MainWindow", "Ver plan de membresía"))
        self.pushButton_9.setText(_translate("MainWindow", "Ver información personal"))
        self.pushButton_23.setText(_translate("MainWindow", "Actualizar informacion"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

