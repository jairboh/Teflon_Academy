import cv2
import datetime
from dateutil.relativedelta import relativedelta
from os import getcwd, makedirs
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, pyqtSignal, QFile
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QPushButton, QLineEdit
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuEmpleados(object):
    def setupUi(self, MenuEmpleados,cursor, id, LogIn):
        MenuEmpleados.setObjectName("MenuEmpleados")
        MenuEmpleados.resize(1138, 836)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MenuEmpleados.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MenuEmpleados)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_26 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_26.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_26.setSpacing(0)
        self.gridLayout_26.setObjectName("gridLayout_26")
        self.Navbar_Frame = QtWidgets.QFrame(self.centralwidget)
        self.Navbar_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.Navbar_Frame.setMaximumSize(QtCore.QSize(16777215, 80))
        self.Navbar_Frame.setStyleSheet("background-color: #343434;")
        self.Navbar_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Navbar_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Navbar_Frame.setObjectName("Navbar_Frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Navbar_Frame)
        self.horizontalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.Navbar_Frame)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 70))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/menuIcon.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/menu/menuicon2.png);\n"
"}\n"
"")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.label_Info_actual = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_Info_actual.setMinimumSize(QtCore.QSize(0, 0))
        self.label_Info_actual.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_Info_actual.setText("")
        self.label_Info_actual.setWordWrap(True)
        self.label_Info_actual.setObjectName("label_Info_actual")
        self.horizontalLayout_2.addWidget(self.label_Info_actual)
        spacerItem = QtWidgets.QSpacerItem(386, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_3.setMinimumSize(QtCore.QSize(70, 70))
        self.label_3.setStyleSheet("image: url(:/logos/logo.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(385, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.Navbar_Frame)
        self.label_4.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.gridLayout_26.addWidget(self.Navbar_Frame, 0, 0, 1, 1)
        self.Frame_Inferior = QtWidgets.QFrame(self.centralwidget)
        self.Frame_Inferior.setStyleSheet("background-color: #231f20;")
        self.Frame_Inferior.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Frame_Inferior.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Frame_Inferior.setObjectName("Frame_Inferior")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Frame_Inferior)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Menu_Lateral_Frame = QtWidgets.QFrame(self.Frame_Inferior)
        self.Menu_Lateral_Frame.setMinimumSize(QtCore.QSize(0, 0))
        self.Menu_Lateral_Frame.setMaximumSize(QtCore.QSize(0, 16777215))
        self.Menu_Lateral_Frame.setStyleSheet("background-color: #343434;")
        self.Menu_Lateral_Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Menu_Lateral_Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Menu_Lateral_Frame.setObjectName("Menu_Lateral_Frame")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.Menu_Lateral_Frame)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.frame_57 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_57.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_57.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/menu/home2.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/home.png);\n"
"}\n"
"\n"
"")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.frame_57)
        self.verticalLayout_34.setSpacing(20)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_57)
        self.pushButton_36.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_36.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_36.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_36.setStyleSheet("")
        self.pushButton_36.setText("")
        self.pushButton_36.setObjectName("pushButton_36")
        self.verticalLayout_34.addWidget(self.pushButton_36)
        self.verticalLayout_17.addWidget(self.frame_57)
        self.frame_56 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_56.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_56.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/menu/reloj.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    \n"
"    image: url(:/menu/relojhover.png);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.frame_56)
        self.verticalLayout_33.setSpacing(20)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_35.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_35.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setStyleSheet("")
        self.pushButton_35.setText("")
        self.pushButton_35.setObjectName("pushButton_35")
        self.verticalLayout_33.addWidget(self.pushButton_35)
        self.verticalLayout_17.addWidget(self.frame_56)
        self.frame_54 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_54.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_54.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/venta.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/PuntoVentaHover.png);\n"
"}\n"
"\n"
"")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_54)
        self.verticalLayout_31.setSpacing(20)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.pushButton_33 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_33.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_33.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_33.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_33.setStyleSheet("")
        self.pushButton_33.setText("")
        self.pushButton_33.setObjectName("pushButton_33")
        self.verticalLayout_31.addWidget(self.pushButton_33)
        self.verticalLayout_17.addWidget(self.frame_54)
        self.frame_51 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_51.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_51.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/entrenador.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/EntrenadoresHover.png);\n"
"}\n"
"\n"
"")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_51)
        self.verticalLayout_26.setContentsMargins(-1, -1, -1, 9)
        self.verticalLayout_26.setSpacing(20)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.pushButton_30 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_30.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_30.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_30.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_30.setStyleSheet("")
        self.pushButton_30.setText("")
        self.pushButton_30.setObjectName("pushButton_30")
        self.verticalLayout_26.addWidget(self.pushButton_30)
        self.verticalLayout_17.addWidget(self.frame_51)
        self.frame_36 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_36.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_36.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/clientes.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/ClientesHover.png);\n"
"}\n"
"")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_36)
        self.verticalLayout_21.setSpacing(20)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_36)
        self.pushButton_24.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_24.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_24.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_24.setStyleSheet("")
        self.pushButton_24.setText("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.verticalLayout_21.addWidget(self.pushButton_24)
        self.verticalLayout_17.addWidget(self.frame_36)
        self.frame_53 = QtWidgets.QFrame(self.Menu_Lateral_Frame)
        self.frame_53.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_53.setStyleSheet("QLabel{\n"
"    font: 87 8pt \"Arial Black\";\n"
"    \n"
"color: rgb(226, 176, 30);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/logout.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/logouthover.png);\n"
"}\n"
"\n"
"")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_53)
        self.verticalLayout_30.setSpacing(20)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_32.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_32.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_32.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_32.setStyleSheet("")
        self.pushButton_32.setText("")
        self.pushButton_32.setObjectName("pushButton_32")
        self.verticalLayout_30.addWidget(self.pushButton_32)
        self.verticalLayout_17.addWidget(self.frame_53)
        self.label_131 = QtWidgets.QLabel(self.Menu_Lateral_Frame)
        self.label_131.setMinimumSize(QtCore.QSize(0, 0))
        self.label_131.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_131.setStyleSheet("QLabel{\n"
"    font: 87 6pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: rgb(226, 176, 30);\n"
"    font: 87 10pt \"Arial Black\";\n"
"    border-radius: 15px;\n"
"}")
        self.label_131.setAlignment(QtCore.Qt.AlignCenter)
        self.label_131.setWordWrap(True)
        self.label_131.setObjectName("label_131")
        self.verticalLayout_17.addWidget(self.label_131)
        self.horizontalLayout.addWidget(self.Menu_Lateral_Frame)
        self.frame_4 = QtWidgets.QFrame(self.Frame_Inferior)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_4)
        self.stackedWidget.setObjectName("stackedWidget")
        self.MenuPrincipal = QtWidgets.QWidget()
        self.MenuPrincipal.setObjectName("MenuPrincipal")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.MenuPrincipal)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.MenuPrincipal)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_123 = QtWidgets.QLabel(self.frame_5)
        self.label_123.setMinimumSize(QtCore.QSize(100, 100))
        self.label_123.setStyleSheet("image: url(:/menu/adorno.png);")
        self.label_123.setText("")
        self.label_123.setObjectName("label_123")
        self.horizontalLayout_4.addWidget(self.label_123)
        self.label_Bienvenida = QtWidgets.QLabel(self.frame_5)
        self.label_Bienvenida.setStyleSheet("font: 87 32pt \"Helvetica Black\";\n"
"    color: whitesmoke;")
        self.label_Bienvenida.setObjectName("label_Bienvenida")
        self.horizontalLayout_4.addWidget(self.label_Bienvenida)
        spacerItem2 = QtWidgets.QSpacerItem(715, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(self.frame_5)
        self.label.setMinimumSize(QtCore.QSize(100, 100))
        self.label.setStyleSheet("image: url(:/logos/logo.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.MenuPrincipal)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_7 = QtWidgets.QFrame(self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(15)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_33 = QtWidgets.QFrame(self.frame_7)
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_33)
        self.verticalLayout_4.setContentsMargins(0, 50, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_34 = QtWidgets.QFrame(self.frame_33)
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_34)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setSpacing(15)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.frame_3 = QtWidgets.QFrame(self.frame_34)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setStyleSheet("font: 87 32pt \"Helvetica Black\";\n"
"color: whitesmoke;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setStyleSheet("\n"
"font: 87 20pt \"Helvetica Black\";\n"
"color: whitesmoke;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.frame_37 = QtWidgets.QFrame(self.frame_2)
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_37)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_37)
        self.pushButton_22.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_22.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_22.setStyleSheet("QPushButton{\n"
"    border: 0px;    \n"
"    image: url(:/menu/reloj.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/relojhover.png);\n"
"}")
        self.pushButton_22.setText("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.verticalLayout_19.addWidget(self.pushButton_22, 0, QtCore.Qt.AlignHCenter)
        self.label_13 = QtWidgets.QLabel(self.frame_37)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_19.addWidget(self.label_13, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.frame_37, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_38 = QtWidgets.QFrame(self.frame_2)
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_38)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_38)
        self.pushButton_25.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_25.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_25.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/menu/venta.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/PuntoVentaHover.png);\n"
"}")
        self.pushButton_25.setText("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.verticalLayout_22.addWidget(self.pushButton_25, 0, QtCore.Qt.AlignHCenter)
        self.label_15 = QtWidgets.QLabel(self.frame_38)
        self.label_15.setWordWrap(False)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_22.addWidget(self.label_15, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_15.addWidget(self.frame_38, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.frame_40 = QtWidgets.QFrame(self.frame_3)
        self.frame_40.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_40.setStyleSheet("font: 87 20pt \"Helvetica Black\";\n"
"color: whitesmoke;")
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_40)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.frame_42 = QtWidgets.QFrame(self.frame_40)
        self.frame_42.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_42.setStyleSheet("")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_42)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_42)
        self.pushButton_27.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_27.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_27.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/entrenador.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/EntrenadoresHover.png);\n"
"}")
        self.pushButton_27.setText("")
        self.pushButton_27.setObjectName("pushButton_27")
        self.verticalLayout_24.addWidget(self.pushButton_27, 0, QtCore.Qt.AlignHCenter)
        self.label_137 = QtWidgets.QLabel(self.frame_42)
        self.label_137.setWordWrap(True)
        self.label_137.setObjectName("label_137")
        self.verticalLayout_24.addWidget(self.label_137, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_18.addWidget(self.frame_42, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_41 = QtWidgets.QFrame(self.frame_40)
        self.frame_41.setMinimumSize(QtCore.QSize(300, 0))
        self.frame_41.setStyleSheet("")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_41)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_41)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    \n"
"    image: url(:/menu/clientes.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"    image: url(:/menu/ClientesHover.png);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_25.addWidget(self.pushButton_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.label_135 = QtWidgets.QLabel(self.frame_41)
        self.label_135.setWordWrap(True)
        self.label_135.setObjectName("label_135")
        self.verticalLayout_25.addWidget(self.label_135)
        self.verticalLayout_25.setStretch(0, 20)
        self.verticalLayout_25.setStretch(1, 20)
        self.horizontalLayout_18.addWidget(self.frame_41, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_5.addWidget(self.frame_40)
        self.horizontalLayout_16.addWidget(self.frame_3)
        self.verticalLayout_4.addWidget(self.frame_34)
        self.horizontalLayout_5.addWidget(self.frame_33)
        self.verticalLayout_3.addWidget(self.frame_7)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.MenuPrincipal)
        self.MenuPuntoVenta = QtWidgets.QWidget()
        self.MenuPuntoVenta.setObjectName("MenuPuntoVenta")
        self.gridLayout_27 = QtWidgets.QGridLayout(self.MenuPuntoVenta)
        self.gridLayout_27.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_27.setSpacing(0)
        self.gridLayout_27.setObjectName("gridLayout_27")
        self.frame_24 = QtWidgets.QFrame(self.MenuPuntoVenta)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_25 = QtWidgets.QFrame(self.frame_24)
        self.frame_25.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_25)
        self.horizontalLayout_12.setContentsMargins(0, 0, 20, 0)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_125 = QtWidgets.QLabel(self.frame_25)
        self.label_125.setMinimumSize(QtCore.QSize(100, 100))
        self.label_125.setStyleSheet("image: url(:/menu/adorno.png);")
        self.label_125.setText("")
        self.label_125.setObjectName("label_125")
        self.horizontalLayout_12.addWidget(self.label_125)
        self.label_Bienvenida_2 = QtWidgets.QLabel(self.frame_25)
        self.label_Bienvenida_2.setStyleSheet("font: 87 28pt \"Helvetica Black\";\n"
"    color: whitesmoke;")
        self.label_Bienvenida_2.setObjectName("label_Bienvenida_2")
        self.horizontalLayout_12.addWidget(self.label_Bienvenida_2, 0, QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(715, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem3)
        self.label_126 = QtWidgets.QLabel(self.frame_25)
        self.label_126.setMinimumSize(QtCore.QSize(100, 100))
        self.label_126.setStyleSheet("image: url(:/logos/logo.png);")
        self.label_126.setText("")
        self.label_126.setObjectName("label_126")
        self.horizontalLayout_12.addWidget(self.label_126)
        self.verticalLayout.addWidget(self.frame_25)
        self.frame_26 = QtWidgets.QFrame(self.frame_24)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_26)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_27 = QtWidgets.QFrame(self.frame_26)
        self.frame_27.setStyleSheet("\n"
"\n"
"font: 87 20pt \"Helvetica Black\";\n"
"color: whitesmoke;")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_27)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.frame_28 = QtWidgets.QFrame(self.frame_27)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_28)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_11.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_11.setStyleSheet("QPushButton{\n"
"    border: 0px;    \n"
"    image: url(:/menu/ventaIcon.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_11.setText("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayout_15.addWidget(self.pushButton_11, 0, QtCore.Qt.AlignVCenter)
        self.label_127 = QtWidgets.QLabel(self.frame_28)
        self.label_127.setWordWrap(True)
        self.label_127.setObjectName("label_127")
        self.verticalLayout_15.addWidget(self.label_127, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_13.addWidget(self.frame_28, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_29 = QtWidgets.QFrame(self.frame_27)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_12.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_12.setStyleSheet("QPushButton{\n"
"    border: 0px;    \n"
"    image: url(:/menu/InventarioIcon.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_12.setText("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.verticalLayout_16.addWidget(self.pushButton_12)
        self.label_128 = QtWidgets.QLabel(self.frame_29)
        self.label_128.setWordWrap(True)
        self.label_128.setObjectName("label_128")
        self.verticalLayout_16.addWidget(self.label_128, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_13.addWidget(self.frame_29, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_14.addWidget(self.frame_27)
        self.frame_30 = QtWidgets.QFrame(self.frame_26)
        self.frame_30.setStyleSheet("font: 87 20pt \"Helvetica Black\";\n"
"color: whitesmoke;")
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_30)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.frame_32 = QtWidgets.QFrame(self.frame_30)
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_32)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_32)
        self.pushButton_14.setMinimumSize(QtCore.QSize(120, 150))
        self.pushButton_14.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_14.setStyleSheet("QPushButton{\n"
"    border: 0px;    \n"
"    image: url(:/menu/ReporteIcon.png);\n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_14.setText("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.verticalLayout_18.addWidget(self.pushButton_14, 0, QtCore.Qt.AlignHCenter)
        self.label_130 = QtWidgets.QLabel(self.frame_32)
        self.label_130.setWordWrap(True)
        self.label_130.setObjectName("label_130")
        self.verticalLayout_18.addWidget(self.label_130, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_14.addWidget(self.frame_32, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_14.addWidget(self.frame_30, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout.addWidget(self.frame_26)
        self.gridLayout_27.addWidget(self.frame_24, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.MenuPuntoVenta)
        self.PuntoVenta = QtWidgets.QWidget()
        self.PuntoVenta.setObjectName("PuntoVenta")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.PuntoVenta)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_13 = QtWidgets.QFrame(self.PuntoVenta)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_12 = QtWidgets.QFrame(self.frame_13)
        self.frame_12.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.frame_15 = QtWidgets.QFrame(self.frame_12)
        self.frame_15.setStyleSheet("")
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.label_70 = QtWidgets.QLabel(self.frame_15)
        self.label_70.setObjectName("label_70")
        self.gridLayout_18.addWidget(self.label_70, 0, 0, 1, 1)
        self.label_86 = QtWidgets.QLabel(self.frame_15)
        self.label_86.setObjectName("label_86")
        self.gridLayout_18.addWidget(self.label_86, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit_4.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_18.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.frame_15)
        self.lineEdit.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_18.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.horizontalLayout_9.addWidget(self.frame_15)
        self.frame_16 = QtWidgets.QFrame(self.frame_12)
        self.frame_16.setStyleSheet("font: 87 12pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_16)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.radioButton = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_11.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_11.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_11.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_16)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_11.addWidget(self.radioButton_4)
        self.horizontalLayout_9.addWidget(self.frame_16)
        self.frame_17 = QtWidgets.QFrame(self.frame_12)
        self.frame_17.setStyleSheet("")
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_82 = QtWidgets.QLabel(self.frame_17)
        self.label_82.setObjectName("label_82")
        self.gridLayout_11.addWidget(self.label_82, 1, 0, 1, 2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_3.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_11.addWidget(self.lineEdit_3, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_17)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_2.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_11.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        self.label_73 = QtWidgets.QLabel(self.frame_17)
        self.label_73.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_73.setObjectName("label_73")
        self.gridLayout_11.addWidget(self.label_73, 0, 0, 1, 2)
        self.horizontalLayout_9.addWidget(self.frame_17)
        self.verticalLayout_10.addWidget(self.frame_12)
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_14)
        self.gridLayout_21.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_21.setSpacing(0)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.frame_14)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.Puntodeventas = QtWidgets.QWidget()
        self.Puntodeventas.setObjectName("Puntodeventas")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Puntodeventas)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.Puntodeventas)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_20 = QtWidgets.QFrame(self.frame_18)
        self.frame_20.setStyleSheet("\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_20)
        self.gridLayout_22.setVerticalSpacing(10)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.label_106 = QtWidgets.QLabel(self.frame_20)
        self.label_106.setAlignment(QtCore.Qt.AlignCenter)
        self.label_106.setObjectName("label_106")
        self.gridLayout_22.addWidget(self.label_106, 0, 0, 1, 3)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_8.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_22.addWidget(self.lineEdit_8, 3, 2, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_9.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout_22.addWidget(self.lineEdit_9, 5, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_6.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_22.addWidget(self.lineEdit_6, 4, 2, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.frame_20)
        self.label_120.setObjectName("label_120")
        self.gridLayout_22.addWidget(self.label_120, 5, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_20)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_5.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_22.addWidget(self.lineEdit_5, 1, 2, 1, 1)
        self.label_116 = QtWidgets.QLabel(self.frame_20)
        self.label_116.setObjectName("label_116")
        self.gridLayout_22.addWidget(self.label_116, 4, 0, 1, 2)
        self.label_115 = QtWidgets.QLabel(self.frame_20)
        self.label_115.setObjectName("label_115")
        self.gridLayout_22.addWidget(self.label_115, 3, 0, 1, 2)
        self.label_112 = QtWidgets.QLabel(self.frame_20)
        self.label_112.setObjectName("label_112")
        self.gridLayout_22.addWidget(self.label_112, 1, 0, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_22.addItem(spacerItem4, 3, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_20)
        self.pushButton_7.setMinimumSize(QtCore.QSize(120, 50))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_22.addWidget(self.pushButton_7, 2, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_10.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_18)
        self.frame_21.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_21)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.label_119 = QtWidgets.QLabel(self.frame_21)
        self.label_119.setObjectName("label_119")
        self.gridLayout_23.addWidget(self.label_119, 1, 0, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.frame_21)
        self.label_122.setObjectName("label_122")
        self.gridLayout_23.addWidget(self.label_122, 4, 0, 1, 1)
        self.label_121 = QtWidgets.QLabel(self.frame_21)
        self.label_121.setObjectName("label_121")
        self.gridLayout_23.addWidget(self.label_121, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_23.addWidget(self.pushButton_8, 6, 1, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_21)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_11.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_23.addWidget(self.lineEdit_11, 4, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_21)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_7.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_23.addWidget(self.lineEdit_7, 1, 1, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_21)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_10.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout_23.addWidget(self.lineEdit_10, 2, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_23.addItem(spacerItem5, 4, 2, 1, 1)
        self.horizontalLayout_10.addWidget(self.frame_21)
        self.verticalLayout_12.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.Puntodeventas)
        self.frame_19.setStyleSheet("")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.frame_22 = QtWidgets.QFrame(self.frame_19)
        self.frame_22.setStyleSheet("")
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.frame_22)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_22)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QHeaderView::section{\n"
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
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_24.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.frame_22)
        self.frame_23 = QtWidgets.QFrame(self.frame_19)
        self.frame_23.setStyleSheet("\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_113 = QtWidgets.QLabel(self.frame_23)
        self.label_113.setAlignment(QtCore.Qt.AlignCenter)
        self.label_113.setObjectName("label_113")
        self.verticalLayout_13.addWidget(self.label_113)
        self.label_114 = QtWidgets.QLabel(self.frame_23)
        self.label_114.setObjectName("label_114")
        self.verticalLayout_13.addWidget(self.label_114)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_23)
        self.lineEdit_12.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_12.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_12.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout_13.addWidget(self.lineEdit_12)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_13.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_23)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_10.setObjectName("pushButton_10")
        self.verticalLayout_13.addWidget(self.pushButton_10)
        self.horizontalLayout_11.addWidget(self.frame_23)
        self.horizontalLayout_11.setStretch(0, 8)
        self.verticalLayout_12.addWidget(self.frame_19)
        self.stackedWidget_2.addWidget(self.Puntodeventas)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_44 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_44.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_44.setSpacing(0)
        self.gridLayout_44.setObjectName("gridLayout_44")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.page_2)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_4.setFont(font)
        self.tabWidget_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_4.setMouseTracking(False)
        self.tabWidget_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_4.setStyleSheet("QTabWidget::pane {\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"  font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"  color: whitesmoke;\n"
"  background-color: #343434;\n"
"  border: 1px solid #cacaca; \n"
"  padding: 20px;\n"
"    width: 160px;\n"
"    height: 50px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: #e6b31e; \n"
"border: 1px solid rgb(161, 161, 161);\n"
"  margin-bottom: -1px; \n"
"}\n"
"\n"
"")
        self.tabWidget_4.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_4.setUsesScrollButtons(False)
        self.tabWidget_4.setDocumentMode(False)
        self.tabWidget_4.setTabsClosable(False)
        self.tabWidget_4.setMovable(True)
        self.tabWidget_4.setTabBarAutoHide(False)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_20 = QtWidgets.QWidget()
        self.tab_20.setObjectName("tab_20")
        self.gridLayout_37 = QtWidgets.QGridLayout(self.tab_20)
        self.gridLayout_37.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_37.setSpacing(0)
        self.gridLayout_37.setObjectName("gridLayout_37")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_20)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 87, 87))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_34 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_34.setObjectName("gridLayout_34")
        self.scrollArea_14 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_14.setStyleSheet("border-radius: 5px;")
        self.scrollArea_14.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_14.setWidgetResizable(True)
        self.scrollArea_14.setObjectName("scrollArea_14")
        self.scrollAreaWidgetContents_14 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_14.setGeometry(QtCore.QRect(0, 0, 1083, 528))
        self.scrollAreaWidgetContents_14.setObjectName("scrollAreaWidgetContents_14")
        self.gridLayout_35 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_14)
        self.gridLayout_35.setObjectName("gridLayout_35")
        self.label_67 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_67.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_67.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_67.setObjectName("label_67")
        self.gridLayout_35.addWidget(self.label_67, 1, 1, 1, 1)
        self.lineEdit_21 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.lineEdit_21.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.gridLayout_35.addWidget(self.lineEdit_21, 1, 2, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_37.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_37.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_35.addWidget(self.label_37, 2, 1, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.lineEdit_22.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.gridLayout_35.addWidget(self.lineEdit_22, 2, 2, 1, 1)
        self.label_60 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_60.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_60.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_60.setObjectName("label_60")
        self.gridLayout_35.addWidget(self.label_60, 4, 1, 1, 1)
        self.label_163 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_163.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_163.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_163.setObjectName("label_163")
        self.gridLayout_35.addWidget(self.label_163, 0, 1, 1, 1)
        self.lineEdit_31 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.lineEdit_31.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.gridLayout_35.addWidget(self.lineEdit_31, 3, 2, 1, 1)
        self.NombreRegistrar_12 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.NombreRegistrar_12.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_12.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_12.setStyleSheet("font: 63 18pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_12.setObjectName("NombreRegistrar_12")
        self.gridLayout_35.addWidget(self.NombreRegistrar_12, 0, 2, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.lineEdit_24.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.gridLayout_35.addWidget(self.lineEdit_24, 5, 2, 1, 1)
        self.label_164 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_164.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_164.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_164.setObjectName("label_164")
        self.gridLayout_35.addWidget(self.label_164, 5, 1, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_26.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_26.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_26.setObjectName("label_26")
        self.gridLayout_35.addWidget(self.label_26, 6, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_14)
        self.dateEdit.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_35.addWidget(self.dateEdit, 6, 2, 1, 1)
        self.label_129 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_129.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_129.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_129.setObjectName("label_129")
        self.gridLayout_35.addWidget(self.label_129, 7, 0, 1, 2)
        self.label_171 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_171.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_171.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_171.setObjectName("label_171")
        self.gridLayout_35.addWidget(self.label_171, 3, 0, 1, 2)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_14)
        self.lineEdit_14.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_35.addWidget(self.lineEdit_14, 7, 2, 1, 1)
        self.GuardarRegistrarPaciente_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_14)
        self.GuardarRegistrarPaciente_5.setMinimumSize(QtCore.QSize(250, 80))
        self.GuardarRegistrarPaciente_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GuardarRegistrarPaciente_5.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.GuardarRegistrarPaciente_5.setObjectName("GuardarRegistrarPaciente_5")
        self.gridLayout_35.addWidget(self.GuardarRegistrarPaciente_5, 10, 3, 1, 1)
        self.label_156 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_156.setText("")
        self.label_156.setAlignment(QtCore.Qt.AlignCenter)
        self.label_156.setObjectName("label_156")
        self.gridLayout_35.addWidget(self.label_156, 8, 2, 1, 1)
        self.label_155 = QtWidgets.QLabel(self.scrollAreaWidgetContents_14)
        self.label_155.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_155.setObjectName("label_155")
        self.gridLayout_35.addWidget(self.label_155, 8, 0, 1, 2)
        self.pushButton_13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_14)
        self.pushButton_13.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  18pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 18pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_35.addWidget(self.pushButton_13, 9, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents_14)
        self.comboBox.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_35.addWidget(self.comboBox, 4, 2, 1, 1)
        self.scrollArea_14.setWidget(self.scrollAreaWidgetContents_14)
        self.gridLayout_34.addWidget(self.scrollArea_14, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_37.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_20, "")
        self.tab_21 = QtWidgets.QWidget()
        self.tab_21.setObjectName("tab_21")
        self.gridLayout_39 = QtWidgets.QGridLayout(self.tab_21)
        self.gridLayout_39.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_39.setSpacing(0)
        self.gridLayout_39.setObjectName("gridLayout_39")
        self.scrollArea_15 = QtWidgets.QScrollArea(self.tab_21)
        self.scrollArea_15.setStyleSheet("border-radius: 5px;")
        self.scrollArea_15.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_15.setWidgetResizable(True)
        self.scrollArea_15.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_15.setObjectName("scrollArea_15")
        self.scrollAreaWidgetContents_15 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_15.setGeometry(QtCore.QRect(0, 0, 1094, 464))
        self.scrollAreaWidgetContents_15.setObjectName("scrollAreaWidgetContents_15")
        self.gridLayout_36 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_15)
        self.gridLayout_36.setObjectName("gridLayout_36")
        self.scrollArea_11 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_15)
        self.scrollArea_11.setWidgetResizable(True)
        self.scrollArea_11.setObjectName("scrollArea_11")
        self.scrollAreaWidgetContents_11 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_11.setGeometry(QtCore.QRect(0, 0, 1076, 446))
        self.scrollAreaWidgetContents_11.setObjectName("scrollAreaWidgetContents_11")
        self.gridLayout_38 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_11)
        self.gridLayout_38.setObjectName("gridLayout_38")
        self.scrollArea_18 = QtWidgets.QScrollArea(self.scrollAreaWidgetContents_11)
        self.scrollArea_18.setStyleSheet("border-radius: 5px;")
        self.scrollArea_18.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_18.setWidgetResizable(True)
        self.scrollArea_18.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_18.setObjectName("scrollArea_18")
        self.scrollAreaWidgetContents_18 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_18.setGeometry(QtCore.QRect(0, 0, 1041, 775))
        self.scrollAreaWidgetContents_18.setObjectName("scrollAreaWidgetContents_18")
        self.gridLayout_40 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_18)
        self.gridLayout_40.setContentsMargins(0, 0, 0, 50)
        self.gridLayout_40.setHorizontalSpacing(20)
        self.gridLayout_40.setVerticalSpacing(15)
        self.gridLayout_40.setObjectName("gridLayout_40")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_28.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.gridLayout_40.addWidget(self.lineEdit_28, 11, 2, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_25.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.gridLayout_40.addWidget(self.lineEdit_25, 7, 2, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_14.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_40.addWidget(self.label_14, 7, 0, 1, 1)
        self.label_133 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_133.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_133.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_133.setObjectName("label_133")
        self.gridLayout_40.addWidget(self.label_133, 14, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_15.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_40.addWidget(self.lineEdit_15, 14, 2, 1, 1)
        self.label_69 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_69.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_69.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_69.setObjectName("label_69")
        self.gridLayout_40.addWidget(self.label_69, 10, 0, 1, 1)
        self.label_162 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_162.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_162.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_162.setObjectName("label_162")
        self.gridLayout_40.addWidget(self.label_162, 11, 0, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_18)
        self.pushButton_16.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  18pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 18pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}")
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_40.addWidget(self.pushButton_16, 16, 2, 1, 1)
        self.label_59 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_59.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_59.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_59.setObjectName("label_59")
        self.gridLayout_40.addWidget(self.label_59, 8, 0, 1, 1)
        self.label_167 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_167.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_167.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_167.setObjectName("label_167")
        self.gridLayout_40.addWidget(self.label_167, 12, 0, 1, 1)
        self.lineEdit_29 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_29.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.gridLayout_40.addWidget(self.lineEdit_29, 12, 2, 1, 1)
        self.lineEdit_26 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_26.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.gridLayout_40.addWidget(self.lineEdit_26, 8, 2, 1, 1)
        self.label_166 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_166.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_166.setObjectName("label_166")
        self.gridLayout_40.addWidget(self.label_166, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_30 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.lineEdit_30.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.gridLayout_40.addWidget(self.lineEdit_30, 9, 2, 1, 1)
        self.BuscarBotonActualizar_9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_18)
        self.BuscarBotonActualizar_9.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_9.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_9.setObjectName("BuscarBotonActualizar_9")
        self.gridLayout_40.addWidget(self.BuscarBotonActualizar_9, 0, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.BuscarPor_13 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_18)
        self.BuscarPor_13.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarPor_13.setObjectName("BuscarPor_13")
        self.BuscarPor_13.addItem("")
        self.BuscarPor_13.addItem("")
        self.gridLayout_40.addWidget(self.BuscarPor_13, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.NombreActualizarPaciente_11 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.NombreActualizarPaciente_11.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_11.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_11.setObjectName("NombreActualizarPaciente_11")
        self.gridLayout_40.addWidget(self.NombreActualizarPaciente_11, 3, 2, 1, 1)
        self.label_165 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_165.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_165.setObjectName("label_165")
        self.gridLayout_40.addWidget(self.label_165, 2, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ID_BuscarActualizarPaciente_6 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_18)
        self.ID_BuscarActualizarPaciente_6.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarActualizarPaciente_6.setMaximumSize(QtCore.QSize(600, 16777215))
        self.ID_BuscarActualizarPaciente_6.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.ID_BuscarActualizarPaciente_6.setObjectName("ID_BuscarActualizarPaciente_6")
        self.gridLayout_40.addWidget(self.ID_BuscarActualizarPaciente_6, 0, 2, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.ActualizarBotonPaciente_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_18)
        self.ActualizarBotonPaciente_6.setMinimumSize(QtCore.QSize(130, 70))
        self.ActualizarBotonPaciente_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActualizarBotonPaciente_6.setStyleSheet("QPushButton{\n"
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
"")
        self.ActualizarBotonPaciente_6.setObjectName("ActualizarBotonPaciente_6")
        self.gridLayout_40.addWidget(self.ActualizarBotonPaciente_6, 17, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_170 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_170.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_170.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_170.setObjectName("label_170")
        self.gridLayout_40.addWidget(self.label_170, 9, 0, 1, 1)
        self.label_158 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_158.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_158.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_158.setObjectName("label_158")
        self.gridLayout_40.addWidget(self.label_158, 15, 0, 1, 1)
        self.label_157 = QtWidgets.QLabel(self.scrollAreaWidgetContents_18)
        self.label_157.setText("")
        self.label_157.setAlignment(QtCore.Qt.AlignCenter)
        self.label_157.setObjectName("label_157")
        self.gridLayout_40.addWidget(self.label_157, 15, 2, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_18)
        self.comboBox_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_40.addWidget(self.comboBox_2, 10, 2, 1, 1)
        self.scrollArea_18.setWidget(self.scrollAreaWidgetContents_18)
        self.gridLayout_38.addWidget(self.scrollArea_18, 0, 0, 1, 1)
        self.scrollArea_11.setWidget(self.scrollAreaWidgetContents_11)
        self.gridLayout_36.addWidget(self.scrollArea_11, 0, 0, 1, 1)
        self.scrollArea_15.setWidget(self.scrollAreaWidgetContents_15)
        self.gridLayout_39.addWidget(self.scrollArea_15, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_21, "")
        self.tab_23 = QtWidgets.QWidget()
        self.tab_23.setObjectName("tab_23")
        self.gridLayout_42 = QtWidgets.QGridLayout(self.tab_23)
        self.gridLayout_42.setContentsMargins(0, 0, 0, 50)
        self.gridLayout_42.setHorizontalSpacing(20)
        self.gridLayout_42.setVerticalSpacing(10)
        self.gridLayout_42.setObjectName("gridLayout_42")
        self.scrollArea_16 = QtWidgets.QScrollArea(self.tab_23)
        self.scrollArea_16.setStyleSheet("border-radius: 5px;")
        self.scrollArea_16.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_16.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_16.setWidgetResizable(True)
        self.scrollArea_16.setObjectName("scrollArea_16")
        self.scrollAreaWidgetContents_16 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_16.setGeometry(QtCore.QRect(0, 0, 993, 364))
        self.scrollAreaWidgetContents_16.setObjectName("scrollAreaWidgetContents_16")
        self.gridLayout_43 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_16)
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.label_172 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_172.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_172.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_172.setObjectName("label_172")
        self.gridLayout_43.addWidget(self.label_172, 9, 0, 1, 1)
        self.label_168 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_168.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_168.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_168.setObjectName("label_168")
        self.gridLayout_43.addWidget(self.label_168, 7, 0, 1, 1)
        self.label_169 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_169.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_169.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_169.setObjectName("label_169")
        self.gridLayout_43.addWidget(self.label_169, 8, 0, 1, 1)
        self.label_176 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_176.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_176.setText("")
        self.label_176.setObjectName("label_176")
        self.gridLayout_43.addWidget(self.label_176, 11, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_178 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_178.setMinimumSize(QtCore.QSize(0, 0))
        self.label_178.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_178.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_178.setObjectName("label_178")
        self.gridLayout_43.addWidget(self.label_178, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_174 = QtWidgets.QLabel(self.scrollAreaWidgetContents_16)
        self.label_174.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_174.setObjectName("label_174")
        self.gridLayout_43.addWidget(self.label_174, 6, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.BuscarBotonEliminar_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_16)
        self.BuscarBotonEliminar_5.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonEliminar_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonEliminar_5.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonEliminar_5.setObjectName("BuscarBotonEliminar_5")
        self.gridLayout_43.addWidget(self.BuscarBotonEliminar_5, 1, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.ID_BuscarEliminarPaciente_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_16)
        self.ID_BuscarEliminarPaciente_5.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarEliminarPaciente_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ID_BuscarEliminarPaciente_5.setObjectName("ID_BuscarEliminarPaciente_5")
        self.gridLayout_43.addWidget(self.ID_BuscarEliminarPaciente_5, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.BuscarRegistradosCombobox_14 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_16)
        self.BuscarRegistradosCombobox_14.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_14.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_14.setObjectName("BuscarRegistradosCombobox_14")
        self.BuscarRegistradosCombobox_14.addItem("")
        self.BuscarRegistradosCombobox_14.addItem("")
        self.gridLayout_43.addWidget(self.BuscarRegistradosCombobox_14, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.lineEdit_32 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_16)
        self.lineEdit_32.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.gridLayout_43.addWidget(self.lineEdit_32, 7, 3, 1, 1)
        self.lineEdit_33 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_16)
        self.lineEdit_33.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.gridLayout_43.addWidget(self.lineEdit_33, 8, 3, 1, 1)
        self.lineEdit_34 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_16)
        self.lineEdit_34.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.gridLayout_43.addWidget(self.lineEdit_34, 9, 3, 1, 1)
        self.Eliminar_NombrePaciente_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_16)
        self.Eliminar_NombrePaciente_4.setMinimumSize(QtCore.QSize(600, 0))
        self.Eliminar_NombrePaciente_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Eliminar_NombrePaciente_4.setObjectName("Eliminar_NombrePaciente_4")
        self.gridLayout_43.addWidget(self.Eliminar_NombrePaciente_4, 6, 2, 1, 2)
        self.EliminarPacienteBoton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_16)
        self.EliminarPacienteBoton_5.setMinimumSize(QtCore.QSize(130, 70))
        self.EliminarPacienteBoton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EliminarPacienteBoton_5.setStyleSheet("QPushButton{\n"
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
"")
        self.EliminarPacienteBoton_5.setObjectName("EliminarPacienteBoton_5")
        self.gridLayout_43.addWidget(self.EliminarPacienteBoton_5, 11, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea_16.setWidget(self.scrollAreaWidgetContents_16)
        self.gridLayout_42.addWidget(self.scrollArea_16, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_23, "")
        self.tab_16 = QtWidgets.QWidget()
        self.tab_16.setObjectName("tab_16")
        self.gridLayout_32 = QtWidgets.QGridLayout(self.tab_16)
        self.gridLayout_32.setObjectName("gridLayout_32")
        self.scrollArea_17 = QtWidgets.QScrollArea(self.tab_16)
        self.scrollArea_17.setStyleSheet("border-radius: 5px;")
        self.scrollArea_17.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_17.setWidgetResizable(True)
        self.scrollArea_17.setObjectName("scrollArea_17")
        self.scrollAreaWidgetContents_17 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_17.setGeometry(QtCore.QRect(0, 0, 980, 245))
        self.scrollAreaWidgetContents_17.setObjectName("scrollAreaWidgetContents_17")
        self.gridLayout_46 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_17)
        self.gridLayout_46.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_46.setHorizontalSpacing(20)
        self.gridLayout_46.setVerticalSpacing(0)
        self.gridLayout_46.setObjectName("gridLayout_46")
        self.NombreRegistrar_13 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_17)
        self.NombreRegistrar_13.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_13.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.NombreRegistrar_13.setStyleSheet("font: 63 18pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_13.setReadOnly(True)
        self.NombreRegistrar_13.setObjectName("NombreRegistrar_13")
        self.gridLayout_46.addWidget(self.NombreRegistrar_13, 0, 1, 1, 1)
        self.GuardarRegistrarPaciente_6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_17)
        self.GuardarRegistrarPaciente_6.setMinimumSize(QtCore.QSize(200, 70))
        self.GuardarRegistrarPaciente_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GuardarRegistrarPaciente_6.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  18pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 19pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.GuardarRegistrarPaciente_6.setObjectName("GuardarRegistrarPaciente_6")
        self.gridLayout_46.addWidget(self.GuardarRegistrarPaciente_6, 8, 3, 1, 2)
        self.label_134 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_134.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_134.setObjectName("label_134")
        self.gridLayout_46.addWidget(self.label_134, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_35 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_17)
        self.lineEdit_35.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.gridLayout_46.addWidget(self.lineEdit_35, 5, 1, 1, 1)
        self.label_173 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_173.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_173.setObjectName("label_173")
        self.gridLayout_46.addWidget(self.label_173, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_39 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_17)
        self.lineEdit_39.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_39.setReadOnly(True)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.gridLayout_46.addWidget(self.lineEdit_39, 4, 1, 1, 1)
        self.label_153 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_153.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_153.setObjectName("label_153")
        self.gridLayout_46.addWidget(self.label_153, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.lineEdit_38 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_17)
        self.lineEdit_38.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.gridLayout_46.addWidget(self.lineEdit_38, 3, 1, 1, 1)
        self.label_177 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_177.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_177.setObjectName("label_177")
        self.gridLayout_46.addWidget(self.label_177, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_136 = QtWidgets.QLabel(self.scrollAreaWidgetContents_17)
        self.label_136.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_136.setObjectName("label_136")
        self.gridLayout_46.addWidget(self.label_136, 6, 0, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_17)
        self.lineEdit_16.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_46.addWidget(self.lineEdit_16, 6, 1, 1, 1)
        self.scrollArea_17.setWidget(self.scrollAreaWidgetContents_17)
        self.gridLayout_32.addWidget(self.scrollArea_17, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_16, "")
        self.tab_22 = QtWidgets.QWidget()
        self.tab_22.setObjectName("tab_22")
        self.gridLayout_41 = QtWidgets.QGridLayout(self.tab_22)
        self.gridLayout_41.setContentsMargins(-1, -1, -1, 30)
        self.gridLayout_41.setObjectName("gridLayout_41")
        self.TablaEmpleados_8 = QtWidgets.QTableWidget(self.tab_22)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_8.setFont(font)
        self.TablaEmpleados_8.setStyleSheet("QHeaderView::section{\n"
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
        self.TablaEmpleados_8.setDragEnabled(False)
        self.TablaEmpleados_8.setWordWrap(True)
        self.TablaEmpleados_8.setObjectName("TablaEmpleados_8")
        self.TablaEmpleados_8.setColumnCount(9)
        self.TablaEmpleados_8.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_8.setHorizontalHeaderItem(8, item)
        self.TablaEmpleados_8.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_8.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_8.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_8.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_8.verticalHeader().setVisible(False)
        self.TablaEmpleados_8.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_41.addWidget(self.TablaEmpleados_8, 2, 0, 1, 4)
        self.BuscarBotonRegistrados_8 = QtWidgets.QPushButton(self.tab_22)
        self.BuscarBotonRegistrados_8.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonRegistrados_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonRegistrados_8.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonRegistrados_8.setObjectName("BuscarBotonRegistrados_8")
        self.gridLayout_41.addWidget(self.BuscarBotonRegistrados_8, 1, 3, 1, 1)
        self.RefrescarBotonRegistrados_6 = QtWidgets.QPushButton(self.tab_22)
        self.RefrescarBotonRegistrados_6.setMinimumSize(QtCore.QSize(130, 70))
        self.RefrescarBotonRegistrados_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RefrescarBotonRegistrados_6.setStyleSheet("QPushButton{\n"
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
"    border: 1.5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"")
        self.RefrescarBotonRegistrados_6.setObjectName("RefrescarBotonRegistrados_6")
        self.gridLayout_41.addWidget(self.RefrescarBotonRegistrados_6, 3, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.BuscarRegistradosCombobox_13 = QtWidgets.QComboBox(self.tab_22)
        self.BuscarRegistradosCombobox_13.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_13.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_13.setObjectName("BuscarRegistradosCombobox_13")
        self.BuscarRegistradosCombobox_13.addItem("")
        self.BuscarRegistradosCombobox_13.addItem("")
        self.gridLayout_41.addWidget(self.BuscarRegistradosCombobox_13, 1, 0, 1, 2)
        self.BuscarRegistradosPacientesText_8 = QtWidgets.QLineEdit(self.tab_22)
        self.BuscarRegistradosPacientesText_8.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.BuscarRegistradosPacientesText_8.setObjectName("BuscarRegistradosPacientesText_8")
        self.gridLayout_41.addWidget(self.BuscarRegistradosPacientesText_8, 1, 2, 1, 1)
        self.tabWidget_4.addTab(self.tab_22, "")
        self.gridLayout_44.addWidget(self.tabWidget_4, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.page_2)
        self.Ventas = QtWidgets.QWidget()
        self.Ventas.setObjectName("Ventas")
        self.gridLayout_30 = QtWidgets.QGridLayout(self.Ventas)
        self.gridLayout_30.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_30.setHorizontalSpacing(10)
        self.gridLayout_30.setVerticalSpacing(15)
        self.gridLayout_30.setObjectName("gridLayout_30")
        self.BuscarRegistradosCombobox_10 = QtWidgets.QComboBox(self.Ventas)
        self.BuscarRegistradosCombobox_10.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_10.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_10.setObjectName("BuscarRegistradosCombobox_10")
        self.BuscarRegistradosCombobox_10.addItem("")
        self.BuscarRegistradosCombobox_10.addItem("")
        self.gridLayout_30.addWidget(self.BuscarRegistradosCombobox_10, 1, 0, 1, 1)
        self.BuscarRegistradosCombobox_11 = QtWidgets.QComboBox(self.Ventas)
        self.BuscarRegistradosCombobox_11.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_11.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_11.setObjectName("BuscarRegistradosCombobox_11")
        self.BuscarRegistradosCombobox_11.addItem("")
        self.BuscarRegistradosCombobox_11.addItem("")
        self.BuscarRegistradosCombobox_11.addItem("")
        self.gridLayout_30.addWidget(self.BuscarRegistradosCombobox_11, 3, 3, 1, 1)
        self.TablaEmpleados_7 = QtWidgets.QTableWidget(self.Ventas)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_7.setFont(font)
        self.TablaEmpleados_7.setStyleSheet("QHeaderView::section{\n"
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
        self.TablaEmpleados_7.setDragEnabled(False)
        self.TablaEmpleados_7.setObjectName("TablaEmpleados_7")
        self.TablaEmpleados_7.setColumnCount(8)
        self.TablaEmpleados_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_7.setHorizontalHeaderItem(7, item)
        self.TablaEmpleados_7.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_7.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_7.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_7.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_7.verticalHeader().setVisible(False)
        self.TablaEmpleados_7.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_30.addWidget(self.TablaEmpleados_7, 2, 0, 1, 5)
        self.BuscarRegistradosPacientesText_7 = QtWidgets.QLineEdit(self.Ventas)
        self.BuscarRegistradosPacientesText_7.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.BuscarRegistradosPacientesText_7.setObjectName("BuscarRegistradosPacientesText_7")
        self.gridLayout_30.addWidget(self.BuscarRegistradosPacientesText_7, 1, 1, 1, 3)
        self.label_124 = QtWidgets.QLabel(self.Ventas)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_124.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_124.setFont(font)
        self.label_124.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_124.setAlignment(QtCore.Qt.AlignCenter)
        self.label_124.setObjectName("label_124")
        self.gridLayout_30.addWidget(self.label_124, 0, 0, 1, 4)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_30.addItem(spacerItem6, 3, 2, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.Ventas)
        self.pushButton_15.setStyleSheet("QPushButton{\n"
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
"")
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_30.addWidget(self.pushButton_15, 3, 0, 1, 2)
        self.BuscarBotonRegistrados_7 = QtWidgets.QPushButton(self.Ventas)
        self.BuscarBotonRegistrados_7.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonRegistrados_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonRegistrados_7.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonRegistrados_7.setObjectName("BuscarBotonRegistrados_7")
        self.gridLayout_30.addWidget(self.BuscarBotonRegistrados_7, 0, 4, 2, 1)
        self.stackedWidget_2.addWidget(self.Ventas)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_31 = QtWidgets.QFrame(self.page)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.gridLayout_57 = QtWidgets.QGridLayout(self.frame_31)
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.frame_73 = QtWidgets.QFrame(self.frame_31)
        self.frame_73.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_73.setObjectName("frame_73")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_73)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.frame_74 = QtWidgets.QFrame(self.frame_73)
        self.frame_74.setStyleSheet("\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_74.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_74.setObjectName("frame_74")
        self.gridLayout_54 = QtWidgets.QGridLayout(self.frame_74)
        self.gridLayout_54.setVerticalSpacing(10)
        self.gridLayout_54.setObjectName("gridLayout_54")
        self.label_199 = QtWidgets.QLabel(self.frame_74)
        self.label_199.setObjectName("label_199")
        self.gridLayout_54.addWidget(self.label_199, 3, 0, 1, 2)
        self.label_201 = QtWidgets.QLabel(self.frame_74)
        self.label_201.setObjectName("label_201")
        self.gridLayout_54.addWidget(self.label_201, 0, 0, 1, 2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_54.addItem(spacerItem7, 2, 3, 1, 1)
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_74)
        self.pushButton_37.setMinimumSize(QtCore.QSize(120, 50))
        self.pushButton_37.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_37.setObjectName("pushButton_37")
        self.gridLayout_54.addWidget(self.pushButton_37, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.lineEdit_52 = QtWidgets.QLineEdit(self.frame_74)
        self.lineEdit_52.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_52.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_52.setReadOnly(True)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.gridLayout_54.addWidget(self.lineEdit_52, 2, 2, 1, 1)
        self.lineEdit_53 = QtWidgets.QLineEdit(self.frame_74)
        self.lineEdit_53.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_53.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_53.setReadOnly(True)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.gridLayout_54.addWidget(self.lineEdit_53, 4, 2, 1, 1)
        self.label_200 = QtWidgets.QLabel(self.frame_74)
        self.label_200.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_200.setObjectName("label_200")
        self.gridLayout_54.addWidget(self.label_200, 2, 0, 1, 2)
        self.lineEdit_54 = QtWidgets.QLineEdit(self.frame_74)
        self.lineEdit_54.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_54.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_54.setReadOnly(True)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.gridLayout_54.addWidget(self.lineEdit_54, 3, 2, 1, 1)
        self.lineEdit_55 = QtWidgets.QLineEdit(self.frame_74)
        self.lineEdit_55.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_55.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.gridLayout_54.addWidget(self.lineEdit_55, 0, 2, 1, 1)
        self.label_198 = QtWidgets.QLabel(self.frame_74)
        self.label_198.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_198.setObjectName("label_198")
        self.gridLayout_54.addWidget(self.label_198, 4, 0, 1, 2)
        self.horizontalLayout_31.addWidget(self.frame_74)
        self.frame_75 = QtWidgets.QFrame(self.frame_73)
        self.frame_75.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_75.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_75.setObjectName("frame_75")
        self.gridLayout_56 = QtWidgets.QGridLayout(self.frame_75)
        self.gridLayout_56.setObjectName("gridLayout_56")
        self.label_202 = QtWidgets.QLabel(self.frame_75)
        self.label_202.setObjectName("label_202")
        self.gridLayout_56.addWidget(self.label_202, 1, 0, 1, 1)
        self.label_203 = QtWidgets.QLabel(self.frame_75)
        self.label_203.setObjectName("label_203")
        self.gridLayout_56.addWidget(self.label_203, 4, 0, 1, 1)
        self.label_204 = QtWidgets.QLabel(self.frame_75)
        self.label_204.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_204.setObjectName("label_204")
        self.gridLayout_56.addWidget(self.label_204, 2, 0, 1, 1)
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_75)
        self.pushButton_38.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_38.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_38.setObjectName("pushButton_38")
        self.gridLayout_56.addWidget(self.pushButton_38, 6, 1, 1, 1)
        self.lineEdit_56 = QtWidgets.QLineEdit(self.frame_75)
        self.lineEdit_56.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_56.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_56.setReadOnly(True)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.gridLayout_56.addWidget(self.lineEdit_56, 4, 1, 1, 1)
        self.lineEdit_57 = QtWidgets.QLineEdit(self.frame_75)
        self.lineEdit_57.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_57.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.gridLayout_56.addWidget(self.lineEdit_57, 1, 1, 1, 1)
        self.lineEdit_58 = QtWidgets.QLineEdit(self.frame_75)
        self.lineEdit_58.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_58.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_58.setObjectName("lineEdit_58")
        self.gridLayout_56.addWidget(self.lineEdit_58, 2, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_56.addItem(spacerItem8, 4, 2, 1, 1)
        self.horizontalLayout_31.addWidget(self.frame_75)
        self.gridLayout_57.addWidget(self.frame_73, 0, 0, 1, 1)
        self.verticalLayout_20.addWidget(self.frame_31)
        self.frame_35 = QtWidgets.QFrame(self.page)
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_35)
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.frame_52 = QtWidgets.QFrame(self.frame_35)
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_52)
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.frame_60 = QtWidgets.QFrame(self.frame_52)
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.gridLayout_33 = QtWidgets.QGridLayout(self.frame_60)
        self.gridLayout_33.setObjectName("gridLayout_33")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.frame_60)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_6.setFont(font)
        self.tableWidget_6.setStyleSheet("QHeaderView::section{\n"
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
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(6)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        self.tableWidget_6.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_6.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_33.addWidget(self.tableWidget_6, 0, 0, 1, 1)
        self.horizontalLayout_26.addWidget(self.frame_60)
        self.frame_61 = QtWidgets.QFrame(self.frame_52)
        self.frame_61.setStyleSheet("\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.gridLayout_55 = QtWidgets.QGridLayout(self.frame_61)
        self.gridLayout_55.setObjectName("gridLayout_55")
        self.label_196 = QtWidgets.QLabel(self.frame_61)
        self.label_196.setAlignment(QtCore.Qt.AlignCenter)
        self.label_196.setObjectName("label_196")
        self.gridLayout_55.addWidget(self.label_196, 0, 0, 1, 1)
        self.label_195 = QtWidgets.QLabel(self.frame_61)
        self.label_195.setObjectName("label_195")
        self.gridLayout_55.addWidget(self.label_195, 1, 0, 1, 1)
        self.lineEdit_51 = QtWidgets.QLineEdit(self.frame_61)
        self.lineEdit_51.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_51.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_51.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_51.setReadOnly(True)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.gridLayout_55.addWidget(self.lineEdit_51, 2, 0, 1, 1)
        self.pushButton_31 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_31.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_31.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_31.setObjectName("pushButton_31")
        self.gridLayout_55.addWidget(self.pushButton_31, 3, 0, 1, 1)
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_23.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_23.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_23.setObjectName("pushButton_23")
        self.gridLayout_55.addWidget(self.pushButton_23, 4, 0, 1, 1)
        self.horizontalLayout_26.addWidget(self.frame_61)
        self.horizontalLayout_26.setStretch(0, 8)
        self.horizontalLayout_26.setStretch(1, 3)
        self.horizontalLayout_25.addWidget(self.frame_52)
        self.verticalLayout_20.addWidget(self.frame_35)
        self.stackedWidget_2.addWidget(self.page)
        self.gridLayout_21.addWidget(self.stackedWidget_2, 0, 1, 1, 1)
        self.verticalLayout_10.addWidget(self.frame_14)
        self.verticalLayout_10.setStretch(0, 2)
        self.verticalLayout_9.addWidget(self.frame_13)
        self.verticalLayout_9.setStretch(0, 6)
        self.stackedWidget.addWidget(self.PuntoVenta)
        self.VentaTicket = QtWidgets.QWidget()
        self.VentaTicket.setObjectName("VentaTicket")
        self.gridLayout_28 = QtWidgets.QGridLayout(self.VentaTicket)
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName("gridLayout_28")
        self.frame = QtWidgets.QFrame(self.VentaTicket)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 60))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_138 = QtWidgets.QLabel(self.frame_8)
        self.label_138.setMinimumSize(QtCore.QSize(70, 0))
        self.label_138.setStyleSheet("image: url(:/menu/adorno.png);")
        self.label_138.setText("")
        self.label_138.setObjectName("label_138")
        self.horizontalLayout_6.addWidget(self.label_138)
        self.label_Bienvenida_3 = QtWidgets.QLabel(self.frame_8)
        self.label_Bienvenida_3.setStyleSheet("font: 87 32pt \"Helvetica Black\";\n"
"    color: whitesmoke;")
        self.label_Bienvenida_3.setObjectName("label_Bienvenida_3")
        self.horizontalLayout_6.addWidget(self.label_Bienvenida_3)
        spacerItem9 = QtWidgets.QSpacerItem(715, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.label_5 = QtWidgets.QLabel(self.frame_8)
        self.label_5.setMinimumSize(QtCore.QSize(70, 0))
        self.label_5.setStyleSheet("image: url(:/logos/logo.png);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.verticalLayout_6.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.frame_44 = QtWidgets.QFrame(self.frame_9)
        self.frame_44.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_44.setMaximumSize(QtCore.QSize(700, 16777215))
        self.frame_44.setStyleSheet("")
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_44)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_10 = QtWidgets.QFrame(self.frame_44)
        self.frame_10.setMinimumSize(QtCore.QSize(600, 0))
        self.frame_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_10.setStyleSheet("QFrame{\n"
"    background-color: whitesmoke;\n"
"    \n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_29.setContentsMargins(10, 0, 10, 0)
        self.verticalLayout_29.setSpacing(10)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.label_7 = QtWidgets.QLabel(self.frame_10)
        self.label_7.setMinimumSize(QtCore.QSize(70, 70))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"image: url(:/menu/logonegro.png);\n"
"border: 0px solid #e6b31e;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_29.addWidget(self.label_7)
        self.label_9 = QtWidgets.QLabel(self.frame_10)
        self.label_9.setMinimumSize(QtCore.QSize(270, 0))
        self.label_9.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 20pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_29.addWidget(self.label_9)
        self.FechaTicket = QtWidgets.QLabel(self.frame_10)
        self.FechaTicket.setMinimumSize(QtCore.QSize(170, 0))
        self.FechaTicket.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 87 10pt \"Helvetica Black\";")
        self.FechaTicket.setAlignment(QtCore.Qt.AlignCenter)
        self.FechaTicket.setObjectName("FechaTicket")
        self.verticalLayout_29.addWidget(self.FechaTicket)
        self.label_139 = QtWidgets.QLabel(self.frame_10)
        self.label_139.setMinimumSize(QtCore.QSize(170, 0))
        self.label_139.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 87 10pt \"Helvetica Black\";")
        self.label_139.setAlignment(QtCore.Qt.AlignCenter)
        self.label_139.setObjectName("label_139")
        self.verticalLayout_29.addWidget(self.label_139)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_10)
        self.tableWidget_3.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setStyleSheet("QHeaderView::section{\n"
"    color: rgb(30, 15, 0);\n"
"    padding: 5px;\n"
"    border: 2px dashed gray;\n"
"    font: 87 13pt \"Arial Black\";\n"
"\n"
"}\n"
"QTableWidget::Item {\n"
"    font: 87 13pt \"Arial Black\";\n"
"    color: #343434;\n"
"    border:  .3px solid #034aa6;\n"
"}\n"
"")
        self.tableWidget_3.setProperty("showDropIndicator", True)
        self.tableWidget_3.setShowGrid(True)
        self.tableWidget_3.setGridStyle(QtCore.Qt.DashLine)
        self.tableWidget_3.setCornerButtonEnabled(True)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(5)
        self.tableWidget_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_29.addWidget(self.tableWidget_3)
        self.frame_48 = QtWidgets.QFrame(self.frame_10)
        self.frame_48.setMinimumSize(QtCore.QSize(510, 0))
        self.frame_48.setStyleSheet("background-color: rgb(230, 179, 30);\n"
"font: 63 16pt \"Bahnschrift SemiBold SemiConden\";")
        self.frame_48.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_48.setObjectName("frame_48")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_48)
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem10 = QtWidgets.QSpacerItem(213, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem10)
        self.label_143 = QtWidgets.QLabel(self.frame_48)
        self.label_143.setStyleSheet("color: rgb(30, 15, 0);")
        self.label_143.setObjectName("label_143")
        self.horizontalLayout_22.addWidget(self.label_143)
        spacerItem11 = QtWidgets.QSpacerItem(212, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem11)
        self.label_144 = QtWidgets.QLabel(self.frame_48)
        self.label_144.setStyleSheet("color: rgb(30, 15, 0);\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(245, 245, 245);\n"
"")
        self.label_144.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_144.setObjectName("label_144")
        self.horizontalLayout_22.addWidget(self.label_144)
        self.verticalLayout_29.addWidget(self.frame_48)
        self.label_149 = QtWidgets.QLabel(self.frame_10)
        self.label_149.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 87 10pt \"Helvetica Black\";")
        self.label_149.setAlignment(QtCore.Qt.AlignCenter)
        self.label_149.setObjectName("label_149")
        self.verticalLayout_29.addWidget(self.label_149)
        self.label_147 = QtWidgets.QLabel(self.frame_10)
        self.label_147.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 87 10pt \"Helvetica Black\";")
        self.label_147.setAlignment(QtCore.Qt.AlignCenter)
        self.label_147.setObjectName("label_147")
        self.verticalLayout_29.addWidget(self.label_147)
        self.verticalLayout_8.addWidget(self.frame_10, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_44)
        self.pushButton_29.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_29.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_29.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_29.setObjectName("pushButton_29")
        self.verticalLayout_8.addWidget(self.pushButton_29, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_19.addWidget(self.frame_44)
        self.frame_45 = QtWidgets.QFrame(self.frame_9)
        self.frame_45.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_45.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_45.setStyleSheet("")
        self.frame_45.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_45.setObjectName("frame_45")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_45)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_43 = QtWidgets.QFrame(self.frame_45)
        self.frame_43.setMinimumSize(QtCore.QSize(500, 0))
        self.frame_43.setStyleSheet("QFrame{\n"
"    background-color: whitesmoke;\n"
"};\n"
"")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_43)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.frame_46 = QtWidgets.QFrame(self.frame_43)
        self.frame_46.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_46.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";\n"
"\n"
"")
        self.frame_46.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_46.setObjectName("frame_46")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_46)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_140 = QtWidgets.QLabel(self.frame_46)
        self.label_140.setMinimumSize(QtCore.QSize(270, 0))
        self.label_140.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_140.setAlignment(QtCore.Qt.AlignCenter)
        self.label_140.setObjectName("label_140")
        self.horizontalLayout_20.addWidget(self.label_140)
        spacerItem12 = QtWidgets.QSpacerItem(427, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.Tota_label = QtWidgets.QLabel(self.frame_46)
        self.Tota_label.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";")
        self.Tota_label.setObjectName("Tota_label")
        self.horizontalLayout_20.addWidget(self.Tota_label)
        self.verticalLayout_28.addWidget(self.frame_46)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_43)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setStyleSheet("QHeaderView::section{\n"
"    padding: 5px;\n"
"    background-color: #1e0f00;\n"
"    border: 50px solid #fffff;\n"
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
"}\n"
"")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_28.addWidget(self.tableWidget_2)
        self.frame_47 = QtWidgets.QFrame(self.frame_43)
        self.frame_47.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_47.setStyleSheet("background-color: rgb(230, 179, 30);\n"
"font: 63 16pt \"Bahnschrift SemiBold SemiConden\";")
        self.frame_47.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_47.setObjectName("frame_47")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_47)
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem13 = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem13)
        self.label_142 = QtWidgets.QLabel(self.frame_47)
        self.label_142.setStyleSheet("color: rgb(30, 15, 0);\n"
"")
        self.label_142.setObjectName("label_142")
        self.horizontalLayout_21.addWidget(self.label_142)
        spacerItem14 = QtWidgets.QSpacerItem(355, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem14)
        self.label_141 = QtWidgets.QLabel(self.frame_47)
        self.label_141.setStyleSheet("color: rgb(30, 15, 0);\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(245, 245, 245);\n"
"")
        self.label_141.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_141.setObjectName("label_141")
        self.horizontalLayout_21.addWidget(self.label_141)
        self.verticalLayout_28.addWidget(self.frame_47)
        self.frame_49 = QtWidgets.QFrame(self.frame_43)
        self.frame_49.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_49.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";\n"
"\n"
"")
        self.frame_49.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_49.setObjectName("frame_49")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_49)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_145 = QtWidgets.QLabel(self.frame_49)
        self.label_145.setMinimumSize(QtCore.QSize(270, 50))
        self.label_145.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_145.setAlignment(QtCore.Qt.AlignCenter)
        self.label_145.setObjectName("label_145")
        self.horizontalLayout_23.addWidget(self.label_145)
        spacerItem15 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem15)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_49)
        self.lineEdit_13.setMinimumSize(QtCore.QSize(150, 0))
        self.lineEdit_13.setMaximumSize(QtCore.QSize(150, 16777215))
        self.lineEdit_13.setStyleSheet("background-color: rgb(245, 245, 245);\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.horizontalLayout_23.addWidget(self.lineEdit_13)
        self.verticalLayout_28.addWidget(self.frame_49)
        self.frame_50 = QtWidgets.QFrame(self.frame_43)
        self.frame_50.setMinimumSize(QtCore.QSize(0, 60))
        self.frame_50.setStyleSheet("\n"
"background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";\n"
"\n"
"")
        self.frame_50.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_50.setObjectName("frame_50")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_50)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_146 = QtWidgets.QLabel(self.frame_50)
        self.label_146.setMinimumSize(QtCore.QSize(270, 50))
        self.label_146.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";")
        self.label_146.setAlignment(QtCore.Qt.AlignCenter)
        self.label_146.setObjectName("label_146")
        self.horizontalLayout_24.addWidget(self.label_146)
        spacerItem16 = QtWidgets.QSpacerItem(369, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem16)
        self.Tota_label_3 = QtWidgets.QLabel(self.frame_50)
        self.Tota_label_3.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"border: 0px solid #e6b31e;\n"
"font: 63 32pt \"Bahnschrift SemiBold SemiConden\";")
        self.Tota_label_3.setObjectName("Tota_label_3")
        self.horizontalLayout_24.addWidget(self.Tota_label_3)
        self.verticalLayout_28.addWidget(self.frame_50)
        self.verticalLayout_7.addWidget(self.frame_43, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_45)
        self.pushButton_28.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_28.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_28.setStyleSheet("QPushButton{\n"
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
"}")
        self.pushButton_28.setObjectName("pushButton_28")
        self.verticalLayout_7.addWidget(self.pushButton_28, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_19.addWidget(self.frame_45)
        self.verticalLayout_6.addWidget(self.frame_9)
        self.gridLayout_28.addWidget(self.frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.VentaTicket)
        self.RegistrarVisita = QtWidgets.QWidget()
        self.RegistrarVisita.setObjectName("RegistrarVisita")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.RegistrarVisita)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.frame_11 = QtWidgets.QFrame(self.RegistrarVisita)
        self.frame_11.setStyleSheet("font: 87 16pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout.setContentsMargins(100, -1, 0, 100)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.frame_11)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 3, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.frame_11)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 8, QtCore.Qt.AlignHCenter)
        self.Buscar_Visita_3 = QtWidgets.QPushButton(self.frame_11)
        self.Buscar_Visita_3.setMinimumSize(QtCore.QSize(150, 70))
        self.Buscar_Visita_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Buscar_Visita_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buscar_Visita_3.setStyleSheet("QPushButton{\n"
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
"")
        self.Buscar_Visita_3.setObjectName("Buscar_Visita_3")
        self.gridLayout.addWidget(self.Buscar_Visita_3, 1, 5, 1, 1, QtCore.Qt.AlignHCenter)
        self.Buscar_Visita_4 = QtWidgets.QPushButton(self.frame_11)
        self.Buscar_Visita_4.setMinimumSize(QtCore.QSize(200, 70))
        self.Buscar_Visita_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buscar_Visita_4.setStyleSheet("QPushButton{\n"
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
"")
        self.Buscar_Visita_4.setObjectName("Buscar_Visita_4")
        self.gridLayout.addWidget(self.Buscar_Visita_4, 9, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.Buscar_Visita_5 = QtWidgets.QPushButton(self.frame_11)
        self.Buscar_Visita_5.setMinimumSize(QtCore.QSize(200, 70))
        self.Buscar_Visita_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Buscar_Visita_5.setStyleSheet("QPushButton{\n"
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
"")
        self.Buscar_Visita_5.setObjectName("Buscar_Visita_5")
        self.gridLayout.addWidget(self.Buscar_Visita_5, 9, 5, 1, 1, QtCore.Qt.AlignRight)
        self.label_12 = QtWidgets.QLabel(self.frame_11)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 7, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.frame_11)
        self.plainTextEdit_3.setMinimumSize(QtCore.QSize(500, 0))
        self.plainTextEdit_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEdit_3.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.gridLayout.addWidget(self.plainTextEdit_3, 6, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_11)
        self.plainTextEdit_2.setMinimumSize(QtCore.QSize(500, 0))
        self.plainTextEdit_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEdit_2.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 4, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_11)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(500, 0))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(16777215, 50))
        self.plainTextEdit.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 1, 4, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame_11)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.frame_11)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.frame_11)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 6, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_7.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.RegistrarVisita)
        self.CRUD_Entrenadores = QtWidgets.QWidget()
        self.CRUD_Entrenadores.setEnabled(True)
        self.CRUD_Entrenadores.setMouseTracking(False)
        self.CRUD_Entrenadores.setTabletTracking(False)
        self.CRUD_Entrenadores.setObjectName("CRUD_Entrenadores")
        self.gridLayout_45 = QtWidgets.QGridLayout(self.CRUD_Entrenadores)
        self.gridLayout_45.setObjectName("gridLayout_45")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.CRUD_Entrenadores)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy)
        self.tabWidget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_2.setMouseTracking(False)
        self.tabWidget_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_2.setStyleSheet("QTabWidget::pane {\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"  font: 63 18pt \"Bahnschrift SemiBold SemiConden\";\n"
"  color: whitesmoke;\n"
"  background-color: #343434;\n"
"  border: 1px solid #cacaca; \n"
"  padding: 20px;\n"
"    width: 180px;\n"
"    height: 50px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: #e6b31e; \n"
"border: 1px solid rgb(161, 161, 161);\n"
"  margin-bottom: -1px; \n"
"}\n"
"\n"
"")
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_2.setUsesScrollButtons(False)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(False)
        self.tabWidget_2.setMovable(True)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.scrollArea_5 = QtWidgets.QScrollArea(self.tab_5)
        self.scrollArea_5.setStyleSheet("border-radius: 5px;")
        self.scrollArea_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollArea_5.setObjectName("scrollArea_5")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 1098, 632))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.gridLayout_29 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_4)
        self.gridLayout_29.setObjectName("gridLayout_29")
        self.label_48 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_48.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_48.setObjectName("label_48")
        self.gridLayout_29.addWidget(self.label_48, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_27 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_27.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_27.setObjectName("label_27")
        self.gridLayout_29.addWidget(self.label_27, 6, 0, 1, 1, QtCore.Qt.AlignRight)
        self.NombreRegistrar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.NombreRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_2.setObjectName("NombreRegistrar_2")
        self.gridLayout_29.addWidget(self.NombreRegistrar_2, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.UltimaCitaRegistrar_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_4)
        self.UltimaCitaRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.UltimaCitaRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);")
        self.UltimaCitaRegistrar_2.setObjectName("UltimaCitaRegistrar_2")
        self.gridLayout_29.addWidget(self.UltimaCitaRegistrar_2, 5, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_28 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_28.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_28.setObjectName("label_28")
        self.gridLayout_29.addWidget(self.label_28, 7, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_46.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_46.setObjectName("label_46")
        self.gridLayout_29.addWidget(self.label_46, 10, 0, 1, 1, QtCore.Qt.AlignRight)
        self.FechaNacimientoRegistrar_2 = QtWidgets.QDateEdit(self.scrollAreaWidgetContents_4)
        self.FechaNacimientoRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.FechaNacimientoRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);")
        self.FechaNacimientoRegistrar_2.setObjectName("FechaNacimientoRegistrar_2")
        self.gridLayout_29.addWidget(self.FechaNacimientoRegistrar_2, 6, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_47.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_47.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_47.setFont(font)
        self.label_47.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_47.setObjectName("label_47")
        self.gridLayout_29.addWidget(self.label_47, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_23.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_23.setObjectName("label_23")
        self.gridLayout_29.addWidget(self.label_23, 9, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_22 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_22.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_22.setObjectName("label_22")
        self.gridLayout_29.addWidget(self.label_22, 8, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_38.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_38.setObjectName("label_38")
        self.gridLayout_29.addWidget(self.label_38, 5, 0, 1, 1, QtCore.Qt.AlignRight)
        self.AlergiasRegistrar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.AlergiasRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.AlergiasRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.AlergiasRegistrar_2.setObjectName("AlergiasRegistrar_2")
        self.gridLayout_29.addWidget(self.AlergiasRegistrar_2, 8, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.GuardarRegistrarPaciente_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_4)
        self.GuardarRegistrarPaciente_2.setMinimumSize(QtCore.QSize(200, 80))
        self.GuardarRegistrarPaciente_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GuardarRegistrarPaciente_2.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.GuardarRegistrarPaciente_2.setObjectName("GuardarRegistrarPaciente_2")
        self.gridLayout_29.addWidget(self.GuardarRegistrarPaciente_2, 13, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.TelefonoRegistrar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.TelefonoRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.TelefonoRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.TelefonoRegistrar_2.setObjectName("TelefonoRegistrar_2")
        self.gridLayout_29.addWidget(self.TelefonoRegistrar_2, 7, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.MedicamentosRegistrar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.MedicamentosRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosRegistrar_2.setObjectName("MedicamentosRegistrar_2")
        self.gridLayout_29.addWidget(self.MedicamentosRegistrar_2, 10, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.EnfermedadesRegistrar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_4)
        self.EnfermedadesRegistrar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.EnfermedadesRegistrar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EnfermedadesRegistrar_2.setObjectName("EnfermedadesRegistrar_2")
        self.gridLayout_29.addWidget(self.EnfermedadesRegistrar_2, 9, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_12.addWidget(self.scrollArea_5, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_14.setSpacing(0)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.scrollArea_6 = QtWidgets.QScrollArea(self.tab_6)
        self.scrollArea_6.setStyleSheet("border-radius: 5px;")
        self.scrollArea_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollArea_6.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_6.setObjectName("scrollArea_6")
        self.scrollAreaWidgetContents_6 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_6.setGeometry(QtCore.QRect(0, 0, 1009, 605))
        self.scrollAreaWidgetContents_6.setObjectName("scrollAreaWidgetContents_6")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_6)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 50)
        self.gridLayout_15.setHorizontalSpacing(20)
        self.gridLayout_15.setVerticalSpacing(15)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.BuscarBotonActualizar_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.BuscarBotonActualizar_2.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_2.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_2.setObjectName("BuscarBotonActualizar_2")
        self.gridLayout_15.addWidget(self.BuscarBotonActualizar_2, 0, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.FechNacActu_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.FechNacActu_2.setMinimumSize(QtCore.QSize(600, 0))
        self.FechNacActu_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.FechNacActu_2.setObjectName("FechNacActu_2")
        self.gridLayout_15.addWidget(self.FechNacActu_2, 8, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_51.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_51.setObjectName("label_51")
        self.gridLayout_15.addWidget(self.label_51, 3, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_53.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_53.setObjectName("label_53")
        self.gridLayout_15.addWidget(self.label_53, 11, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_56.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_56.setObjectName("label_56")
        self.gridLayout_15.addWidget(self.label_56, 8, 0, 1, 1, QtCore.Qt.AlignRight)
        self.BuscarPor_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_6)
        self.BuscarPor_7.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarPor_7.setObjectName("BuscarPor_7")
        self.BuscarPor_7.addItem("")
        self.BuscarPor_7.addItem("")
        self.gridLayout_15.addWidget(self.BuscarPor_7, 0, 0, 1, 1, QtCore.Qt.AlignRight)
        self.EnfermedadesActualizar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.EnfermedadesActualizar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.EnfermedadesActualizar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EnfermedadesActualizar_2.setObjectName("EnfermedadesActualizar_2")
        self.gridLayout_15.addWidget(self.EnfermedadesActualizar_2, 11, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_54 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_54.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_54.setObjectName("label_54")
        self.gridLayout_15.addWidget(self.label_54, 12, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_58.setObjectName("label_58")
        self.gridLayout_15.addWidget(self.label_58, 10, 0, 1, 1, QtCore.Qt.AlignRight)
        self.NombreActualizarPaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.NombreActualizarPaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_2.setObjectName("NombreActualizarPaciente_2")
        self.gridLayout_15.addWidget(self.NombreActualizarPaciente_2, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.AlergiasActualizar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.AlergiasActualizar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.AlergiasActualizar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.AlergiasActualizar_2.setObjectName("AlergiasActualizar_2")
        self.gridLayout_15.addWidget(self.AlergiasActualizar_2, 10, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.ActualizarBotonPaciente_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_6)
        self.ActualizarBotonPaciente_2.setMinimumSize(QtCore.QSize(130, 70))
        self.ActualizarBotonPaciente_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActualizarBotonPaciente_2.setStyleSheet("QPushButton{\n"
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
"")
        self.ActualizarBotonPaciente_2.setObjectName("ActualizarBotonPaciente_2")
        self.gridLayout_15.addWidget(self.ActualizarBotonPaciente_2, 13, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_55.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_55.setObjectName("label_55")
        self.gridLayout_15.addWidget(self.label_55, 4, 0, 1, 1, QtCore.Qt.AlignRight)
        self.ID_BuscarActualizarPaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.ID_BuscarActualizarPaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarActualizarPaciente_2.setMaximumSize(QtCore.QSize(600, 16777215))
        self.ID_BuscarActualizarPaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.ID_BuscarActualizarPaciente_2.setObjectName("ID_BuscarActualizarPaciente_2")
        self.gridLayout_15.addWidget(self.ID_BuscarActualizarPaciente_2, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.MedicamentosActualizar_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.MedicamentosActualizar_2.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosActualizar_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosActualizar_2.setObjectName("MedicamentosActualizar_2")
        self.gridLayout_15.addWidget(self.MedicamentosActualizar_2, 12, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.TelefonoActualizarPaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.TelefonoActualizarPaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.TelefonoActualizarPaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.TelefonoActualizarPaciente_2.setObjectName("TelefonoActualizarPaciente_2")
        self.gridLayout_15.addWidget(self.TelefonoActualizarPaciente_2, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_57.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_57.setObjectName("label_57")
        self.gridLayout_15.addWidget(self.label_57, 9, 0, 1, 1, QtCore.Qt.AlignRight)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents_6)
        self.label_50.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_50.setObjectName("label_50")
        self.gridLayout_15.addWidget(self.label_50, 2, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.UltimCitActu_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_6)
        self.UltimCitActu_2.setMinimumSize(QtCore.QSize(600, 0))
        self.UltimCitActu_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.UltimCitActu_2.setObjectName("UltimCitActu_2")
        self.gridLayout_15.addWidget(self.UltimCitActu_2, 9, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)
        self.gridLayout_14.addWidget(self.scrollArea_6, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.tab_7)
        self.gridLayout_16.setContentsMargins(-1, -1, -1, 30)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.BuscarRegistradosPacientesText_2 = QtWidgets.QLineEdit(self.tab_7)
        self.BuscarRegistradosPacientesText_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.BuscarRegistradosPacientesText_2.setObjectName("BuscarRegistradosPacientesText_2")
        self.gridLayout_16.addWidget(self.BuscarRegistradosPacientesText_2, 1, 2, 1, 1)
        self.BuscarBotonRegistrados_2 = QtWidgets.QPushButton(self.tab_7)
        self.BuscarBotonRegistrados_2.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonRegistrados_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonRegistrados_2.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonRegistrados_2.setObjectName("BuscarBotonRegistrados_2")
        self.gridLayout_16.addWidget(self.BuscarBotonRegistrados_2, 1, 3, 1, 1)
        self.BuscarRegistradosCombobox_3 = QtWidgets.QComboBox(self.tab_7)
        self.BuscarRegistradosCombobox_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_3.setObjectName("BuscarRegistradosCombobox_3")
        self.BuscarRegistradosCombobox_3.addItem("")
        self.BuscarRegistradosCombobox_3.addItem("")
        self.BuscarRegistradosCombobox_3.addItem("")
        self.BuscarRegistradosCombobox_3.setItemText(2, "")
        self.gridLayout_16.addWidget(self.BuscarRegistradosCombobox_3, 1, 0, 1, 2)
        self.TablaEmpleados_2 = QtWidgets.QTableWidget(self.tab_7)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_2.setFont(font)
        self.TablaEmpleados_2.setStyleSheet("QHeaderView::section{\n"
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
        self.TablaEmpleados_2.setDragEnabled(False)
        self.TablaEmpleados_2.setObjectName("TablaEmpleados_2")
        self.TablaEmpleados_2.setColumnCount(9)
        self.TablaEmpleados_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_2.setHorizontalHeaderItem(8, item)
        self.TablaEmpleados_2.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_2.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_2.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_2.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_2.verticalHeader().setVisible(False)
        self.TablaEmpleados_2.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_16.addWidget(self.TablaEmpleados_2, 2, 0, 1, 4)
        self.label_152 = QtWidgets.QLabel(self.tab_7)
        self.label_152.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_152.setObjectName("label_152")
        self.gridLayout_16.addWidget(self.label_152, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.gridLayout_64 = QtWidgets.QGridLayout(self.tab_9)
        self.gridLayout_64.setObjectName("gridLayout_64")
        self.BuscarRegistradosCombobox_5 = QtWidgets.QComboBox(self.tab_9)
        self.BuscarRegistradosCombobox_5.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_5.setObjectName("BuscarRegistradosCombobox_5")
        self.BuscarRegistradosCombobox_5.addItem("")
        self.BuscarRegistradosCombobox_5.addItem("")
        self.BuscarRegistradosCombobox_5.addItem("")
        self.BuscarRegistradosCombobox_5.setItemText(2, "")
        self.gridLayout_64.addWidget(self.BuscarRegistradosCombobox_5, 0, 0, 1, 1)
        self.BuscarRegistradosPacientesText_3 = QtWidgets.QLineEdit(self.tab_9)
        self.BuscarRegistradosPacientesText_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.BuscarRegistradosPacientesText_3.setObjectName("BuscarRegistradosPacientesText_3")
        self.gridLayout_64.addWidget(self.BuscarRegistradosPacientesText_3, 0, 1, 1, 1)
        self.BuscarBotonRegistrados_3 = QtWidgets.QPushButton(self.tab_9)
        self.BuscarBotonRegistrados_3.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonRegistrados_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonRegistrados_3.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonRegistrados_3.setObjectName("BuscarBotonRegistrados_3")
        self.gridLayout_64.addWidget(self.BuscarBotonRegistrados_3, 0, 2, 1, 1)
        self.TablaEmpleados_3 = QtWidgets.QTableWidget(self.tab_9)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_3.setFont(font)
        self.TablaEmpleados_3.setStyleSheet("QHeaderView::section{\n"
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
        self.TablaEmpleados_3.setDragEnabled(False)
        self.TablaEmpleados_3.setObjectName("TablaEmpleados_3")
        self.TablaEmpleados_3.setColumnCount(8)
        self.TablaEmpleados_3.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_3.setHorizontalHeaderItem(7, item)
        self.TablaEmpleados_3.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_3.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_3.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_3.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_3.verticalHeader().setVisible(False)
        self.TablaEmpleados_3.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_64.addWidget(self.TablaEmpleados_3, 1, 0, 1, 3)
        self.RefrescarBotonRegistrados_3 = QtWidgets.QPushButton(self.tab_9)
        self.RefrescarBotonRegistrados_3.setMinimumSize(QtCore.QSize(130, 70))
        self.RefrescarBotonRegistrados_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RefrescarBotonRegistrados_3.setStyleSheet("QPushButton{\n"
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
"    border: 1.5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"")
        self.RefrescarBotonRegistrados_3.setObjectName("RefrescarBotonRegistrados_3")
        self.gridLayout_64.addWidget(self.RefrescarBotonRegistrados_3, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 50)
        self.gridLayout_17.setHorizontalSpacing(20)
        self.gridLayout_17.setVerticalSpacing(10)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.scrollArea_7 = QtWidgets.QScrollArea(self.tab_8)
        self.scrollArea_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_7.setStyleSheet("border-radius: 5px;")
        self.scrollArea_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollArea_7.setObjectName("scrollArea_7")
        self.scrollAreaWidgetContents_7 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_7.setGeometry(QtCore.QRect(0, 0, 83, 16))
        self.scrollAreaWidgetContents_7.setObjectName("scrollAreaWidgetContents_7")
        self.BuscarRegistradosCombobox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_7)
        self.BuscarRegistradosCombobox_4.setGeometry(QtCore.QRect(20, 20, 227, 37))
        self.BuscarRegistradosCombobox_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_4.setObjectName("BuscarRegistradosCombobox_4")
        self.BuscarRegistradosCombobox_4.addItem("")
        self.BuscarRegistradosCombobox_4.addItem("")
        self.BuscarRegistradosCombobox_4.addItem("")
        self.BuscarRegistradosCombobox_4.setItemText(2, "")
        self.ID_BuscarEliminarPaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.ID_BuscarEliminarPaciente_2.setGeometry(QtCore.QRect(260, 20, 600, 35))
        self.ID_BuscarEliminarPaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarEliminarPaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ID_BuscarEliminarPaciente_2.setObjectName("ID_BuscarEliminarPaciente_2")
        self.BuscarBotonEliminar_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.BuscarBotonEliminar_2.setGeometry(QtCore.QRect(870, 0, 130, 70))
        self.BuscarBotonEliminar_2.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonEliminar_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonEliminar_2.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonEliminar_2.setObjectName("BuscarBotonEliminar_2")
        self.label_66 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_66.setGeometry(QtCore.QRect(330, 100, 458, 40))
        self.label_66.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_66.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_66.setFont(font)
        self.label_66.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_66.setObjectName("label_66")
        self.label_64 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_64.setGeometry(QtCore.QRect(9, 174, 95, 35))
        self.label_64.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_64.setObjectName("label_64")
        self.NombreRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.NombreRegistrar_3.setGeometry(QtCore.QRect(254, 174, 600, 35))
        self.NombreRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_3.setObjectName("NombreRegistrar_3")
        self.label_65 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_65.setGeometry(QtCore.QRect(9, 215, 198, 35))
        self.label_65.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_65.setObjectName("label_65")
        self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_52.setGeometry(QtCore.QRect(9, 256, 239, 35))
        self.label_52.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_52.setObjectName("label_52")
        self.label_63 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_63.setGeometry(QtCore.QRect(9, 297, 97, 35))
        self.label_63.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_63.setObjectName("label_63")
        self.TelefonoRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.TelefonoRegistrar_3.setGeometry(QtCore.QRect(254, 297, 600, 35))
        self.TelefonoRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.TelefonoRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.TelefonoRegistrar_3.setObjectName("TelefonoRegistrar_3")
        self.label_62 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_62.setGeometry(QtCore.QRect(9, 338, 65, 35))
        self.label_62.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_62.setObjectName("label_62")
        self.AlergiasRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.AlergiasRegistrar_3.setGeometry(QtCore.QRect(254, 338, 600, 35))
        self.AlergiasRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.AlergiasRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.AlergiasRegistrar_3.setObjectName("AlergiasRegistrar_3")
        self.label_61 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_61.setGeometry(QtCore.QRect(9, 379, 51, 35))
        self.label_61.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_61.setObjectName("label_61")
        self.EnfermedadesRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.EnfermedadesRegistrar_3.setGeometry(QtCore.QRect(254, 379, 600, 35))
        self.EnfermedadesRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.EnfermedadesRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EnfermedadesRegistrar_3.setObjectName("EnfermedadesRegistrar_3")
        self.label_68 = QtWidgets.QLabel(self.scrollAreaWidgetContents_7)
        self.label_68.setGeometry(QtCore.QRect(9, 420, 49, 35))
        self.label_68.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_68.setObjectName("label_68")
        self.MedicamentosRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.MedicamentosRegistrar_3.setGeometry(QtCore.QRect(254, 420, 600, 35))
        self.MedicamentosRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosRegistrar_3.setObjectName("MedicamentosRegistrar_3")
        self.EliminarPacienteBoton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_7)
        self.EliminarPacienteBoton_2.setGeometry(QtCore.QRect(890, 400, 130, 70))
        self.EliminarPacienteBoton_2.setMinimumSize(QtCore.QSize(130, 70))
        self.EliminarPacienteBoton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EliminarPacienteBoton_2.setStyleSheet("QPushButton{\n"
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
"")
        self.EliminarPacienteBoton_2.setObjectName("EliminarPacienteBoton_2")
        self.UltimaCitaRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.UltimaCitaRegistrar_3.setGeometry(QtCore.QRect(254, 215, 600, 35))
        self.UltimaCitaRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.UltimaCitaRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.UltimaCitaRegistrar_3.setObjectName("UltimaCitaRegistrar_3")
        self.FechaNacimientoRegistrar_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_7)
        self.FechaNacimientoRegistrar_3.setGeometry(QtCore.QRect(254, 256, 600, 35))
        self.FechaNacimientoRegistrar_3.setMinimumSize(QtCore.QSize(600, 0))
        self.FechaNacimientoRegistrar_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.FechaNacimientoRegistrar_3.setObjectName("FechaNacimientoRegistrar_3")
        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)
        self.gridLayout_17.addWidget(self.scrollArea_7, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.gridLayout_45.addWidget(self.tabWidget_2, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.CRUD_Entrenadores)
        self.CRUD_Clientes = QtWidgets.QWidget()
        self.CRUD_Clientes.setObjectName("CRUD_Clientes")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.CRUD_Clientes)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.CRUD_Clientes)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_3.setFont(font)
        self.tabWidget_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.tabWidget_3.setMouseTracking(False)
        self.tabWidget_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget_3.setStyleSheet("QTabWidget::pane {\n"
"} \n"
"\n"
"QTabBar::tab {  \n"
"  font: 63 14pt \"Bahnschrift SemiBold SemiConden\";\n"
"  color: whitesmoke;\n"
"  background-color: #343434;\n"
"  border: 1px solid #cacaca; \n"
"  padding: 15px;\n"
"    width: 150px;\n"
"    height: 50px;\n"
"} \n"
"\n"
"QTabBar::tab:selected { \n"
"  background: #e6b31e; \n"
"border: 1px solid rgb(161, 161, 161);\n"
"  margin-bottom: -1px; \n"
"}\n"
"\n"
"")
        self.tabWidget_3.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget_3.setUsesScrollButtons(False)
        self.tabWidget_3.setDocumentMode(False)
        self.tabWidget_3.setTabsClosable(False)
        self.tabWidget_3.setMovable(True)
        self.tabWidget_3.setTabBarAutoHide(False)
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scrollArea_8 = QtWidgets.QScrollArea(self.tab_10)
        self.scrollArea_8.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea_8.setStyleSheet("border-radius: 5px;")
        self.scrollArea_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollArea_8.setObjectName("scrollArea_8")
        self.scrollAreaWidgetContents_8 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_8.setGeometry(QtCore.QRect(0, 0, 1098, 642))
        self.scrollAreaWidgetContents_8.setObjectName("scrollAreaWidgetContents_8")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_8)
        self.gridLayout_25.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_49.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_49.setObjectName("label_49")
        self.gridLayout_25.addWidget(self.label_49, 6, 1, 1, 1, QtCore.Qt.AlignRight)
        self.NombreRegistrar_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.NombreRegistrar_4.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_4.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_4.setObjectName("NombreRegistrar_4")
        self.gridLayout_25.addWidget(self.NombreRegistrar_4, 1, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.MedicamentosRegistrar_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.MedicamentosRegistrar_4.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosRegistrar_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosRegistrar_4.setObjectName("MedicamentosRegistrar_4")
        self.gridLayout_25.addWidget(self.MedicamentosRegistrar_4, 8, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.AlergiasRegistrar_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.AlergiasRegistrar_4.setMinimumSize(QtCore.QSize(600, 0))
        self.AlergiasRegistrar_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.AlergiasRegistrar_4.setText("")
        self.AlergiasRegistrar_4.setObjectName("AlergiasRegistrar_4")
        self.gridLayout_25.addWidget(self.AlergiasRegistrar_4, 6, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.EnfermedadesRegistrar_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.EnfermedadesRegistrar_4.setMinimumSize(QtCore.QSize(600, 0))
        self.EnfermedadesRegistrar_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EnfermedadesRegistrar_4.setObjectName("EnfermedadesRegistrar_4")
        self.gridLayout_25.addWidget(self.EnfermedadesRegistrar_4, 7, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_71 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_71.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_71.setObjectName("label_71")
        self.gridLayout_25.addWidget(self.label_71, 7, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_77 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_77.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_77.setObjectName("label_77")
        self.gridLayout_25.addWidget(self.label_77, 5, 1, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.TelefonoRegistrar_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.TelefonoRegistrar_4.setMinimumSize(QtCore.QSize(600, 0))
        self.TelefonoRegistrar_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.TelefonoRegistrar_4.setObjectName("TelefonoRegistrar_4")
        self.gridLayout_25.addWidget(self.TelefonoRegistrar_4, 4, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_74 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_74.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_74.setObjectName("label_74")
        self.gridLayout_25.addWidget(self.label_74, 8, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_72 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_72.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_72.setObjectName("label_72")
        self.gridLayout_25.addWidget(self.label_72, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.label_75 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_75.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_75.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_75.setFont(font)
        self.label_75.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_75.setObjectName("label_75")
        self.gridLayout_25.addWidget(self.label_75, 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.GuardarRegistrarPaciente_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
        self.GuardarRegistrarPaciente_3.setMinimumSize(QtCore.QSize(250, 80))
        self.GuardarRegistrarPaciente_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.GuardarRegistrarPaciente_3.setStyleSheet("QPushButton{\n"
"    background-color: #343434;\n"
"    font: 87  22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: .5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: #e6b31e;\n"
"    font: 87 22pt \"Arial Black\";\n"
"    color: whitesmoke;\n"
"    border-radius: 5px;\n"
"    border: 1.5px solid #343434;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"")
        self.GuardarRegistrarPaciente_3.setObjectName("GuardarRegistrarPaciente_3")
        self.gridLayout_25.addWidget(self.GuardarRegistrarPaciente_3, 10, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.AlergiasRegistrar_5 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.AlergiasRegistrar_5.setMinimumSize(QtCore.QSize(600, 0))
        self.AlergiasRegistrar_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.AlergiasRegistrar_5.setText("")
        self.AlergiasRegistrar_5.setObjectName("AlergiasRegistrar_5")
        self.gridLayout_25.addWidget(self.AlergiasRegistrar_5, 5, 2, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_76 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_76.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_76.setObjectName("label_76")
        self.gridLayout_25.addWidget(self.label_76, 1, 1, 1, 1, QtCore.Qt.AlignRight)
        self.MedicamentosRegistrar_8 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_8)
        self.MedicamentosRegistrar_8.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosRegistrar_8.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.MedicamentosRegistrar_8.setTabletTracking(True)
        self.MedicamentosRegistrar_8.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosRegistrar_8.setText("")
        self.MedicamentosRegistrar_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.MedicamentosRegistrar_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MedicamentosRegistrar_8.setObjectName("MedicamentosRegistrar_8")
        self.gridLayout_25.addWidget(self.MedicamentosRegistrar_8, 9, 2, 1, 1)
        self.label_150 = QtWidgets.QLabel(self.scrollAreaWidgetContents_8)
        self.label_150.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_150.setObjectName("label_150")
        self.gridLayout_25.addWidget(self.label_150, 9, 1, 1, 1, QtCore.Qt.AlignRight)
        self.pushButton_5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_8)
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
        self.gridLayout_25.addWidget(self.pushButton_5, 9, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)
        self.gridLayout_10.addWidget(self.scrollArea_8, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_10, "")
        self.tab_14 = QtWidgets.QWidget()
        self.tab_14.setObjectName("tab_14")
        self.gridLayout_31 = QtWidgets.QGridLayout(self.tab_14)
        self.gridLayout_31.setObjectName("gridLayout_31")
        self.label_95 = QtWidgets.QLabel(self.tab_14)
        self.label_95.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_95.setObjectName("label_95")
        self.gridLayout_31.addWidget(self.label_95, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        self.BuscarBotonActualizar_4 = QtWidgets.QPushButton(self.tab_14)
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
        self.gridLayout_31.addWidget(self.BuscarBotonActualizar_4, 2, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.NombreRegistrar_5 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_5.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_5.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_5.setObjectName("NombreRegistrar_5")
        self.gridLayout_31.addWidget(self.NombreRegistrar_5, 2, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.NombreRegistrar_7 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_7.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_7.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.NombreRegistrar_7.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_7.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_7.setText("")
        self.NombreRegistrar_7.setObjectName("NombreRegistrar_7")
        self.gridLayout_31.addWidget(self.NombreRegistrar_7, 5, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_96 = QtWidgets.QLabel(self.tab_14)
        self.label_96.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_96.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_96.setFont(font)
        self.label_96.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_96.setObjectName("label_96")
        self.gridLayout_31.addWidget(self.label_96, 0, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_98 = QtWidgets.QLabel(self.tab_14)
        self.label_98.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_98.setObjectName("label_98")
        self.gridLayout_31.addWidget(self.label_98, 4, 2, 1, 1, QtCore.Qt.AlignRight)
        self.NombreRegistrar_6 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_6.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_6.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.NombreRegistrar_6.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_6.setMouseTracking(True)
        self.NombreRegistrar_6.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_6.setObjectName("NombreRegistrar_6")
        self.gridLayout_31.addWidget(self.NombreRegistrar_6, 4, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_100 = QtWidgets.QLabel(self.tab_14)
        self.label_100.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_100.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_100.setFont(font)
        self.label_100.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_100.setObjectName("label_100")
        self.gridLayout_31.addWidget(self.label_100, 7, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_97 = QtWidgets.QLabel(self.tab_14)
        self.label_97.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_97.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_97.setFont(font)
        self.label_97.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_97.setObjectName("label_97")
        self.gridLayout_31.addWidget(self.label_97, 3, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_99 = QtWidgets.QLabel(self.tab_14)
        self.label_99.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_99.setObjectName("label_99")
        self.gridLayout_31.addWidget(self.label_99, 5, 1, 1, 2, QtCore.Qt.AlignRight)
        self.NombreRegistrar_10 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_10.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.NombreRegistrar_10.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_10.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_10.setObjectName("NombreRegistrar_10")
        self.gridLayout_31.addWidget(self.NombreRegistrar_10, 10, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_104 = QtWidgets.QLabel(self.tab_14)
        self.label_104.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_104.setObjectName("label_104")
        self.gridLayout_31.addWidget(self.label_104, 11, 1, 1, 2, QtCore.Qt.AlignRight)
        self.label_103 = QtWidgets.QLabel(self.tab_14)
        self.label_103.setMaximumSize(QtCore.QSize(600, 50))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_103.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_103.setFont(font)
        self.label_103.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_103.setObjectName("label_103")
        self.gridLayout_31.addWidget(self.label_103, 9, 2, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_101 = QtWidgets.QLabel(self.tab_14)
        self.label_101.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_101.setObjectName("label_101")
        self.gridLayout_31.addWidget(self.label_101, 10, 2, 1, 1, QtCore.Qt.AlignRight)
        self.NombreRegistrar_9 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_9.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.NombreRegistrar_9.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_9.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_9.setText("")
        self.NombreRegistrar_9.setObjectName("NombreRegistrar_9")
        self.gridLayout_31.addWidget(self.NombreRegistrar_9, 11, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.NombreRegistrar_8 = QtWidgets.QLineEdit(self.tab_14)
        self.NombreRegistrar_8.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreRegistrar_8.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.NombreRegistrar_8.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.NombreRegistrar_8.setObjectName("NombreRegistrar_8")
        self.gridLayout_31.addWidget(self.NombreRegistrar_8, 8, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_102 = QtWidgets.QLabel(self.tab_14)
        self.label_102.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_102.setObjectName("label_102")
        self.gridLayout_31.addWidget(self.label_102, 8, 2, 1, 1, QtCore.Qt.AlignRight)
        self.BuscarBotonActualizar_5 = QtWidgets.QPushButton(self.tab_14)
        self.BuscarBotonActualizar_5.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_5.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_5.setObjectName("BuscarBotonActualizar_5")
        self.gridLayout_31.addWidget(self.BuscarBotonActualizar_5, 8, 4, 1, 1, QtCore.Qt.AlignLeft)
        self.BuscarBotonActualizar_6 = QtWidgets.QPushButton(self.tab_14)
        self.BuscarBotonActualizar_6.setMinimumSize(QtCore.QSize(400, 70))
        self.BuscarBotonActualizar_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_6.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_6.setObjectName("BuscarBotonActualizar_6")
        self.gridLayout_31.addWidget(self.BuscarBotonActualizar_6, 12, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.tabWidget_3.addTab(self.tab_14, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.tab_11)
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_13.setSpacing(0)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.scrollArea_9 = QtWidgets.QScrollArea(self.tab_11)
        self.scrollArea_9.setStyleSheet("border-radius: 5px;")
        self.scrollArea_9.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_9.setWidgetResizable(True)
        self.scrollArea_9.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea_9.setObjectName("scrollArea_9")
        self.scrollAreaWidgetContents_9 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_9.setGeometry(QtCore.QRect(0, 0, 100, 30))
        self.scrollAreaWidgetContents_9.setObjectName("scrollAreaWidgetContents_9")
        self.label_78 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_78.setGeometry(QtCore.QRect(420, 180, 281, 35))
        self.label_78.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_78.setObjectName("label_78")
        self.label_79 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_79.setGeometry(QtCore.QRect(270, 250, 95, 35))
        self.label_79.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_79.setObjectName("label_79")
        self.ID_BuscarActualizarPaciente_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.ID_BuscarActualizarPaciente_3.setGeometry(QtCore.QRect(280, 114, 600, 41))
        self.ID_BuscarActualizarPaciente_3.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarActualizarPaciente_3.setMaximumSize(QtCore.QSize(600, 16777215))
        self.ID_BuscarActualizarPaciente_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.ID_BuscarActualizarPaciente_3.setObjectName("ID_BuscarActualizarPaciente_3")
        self.BuscarPor_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_9)
        self.BuscarPor_8.setGeometry(QtCore.QRect(34, 116, 226, 37))
        self.BuscarPor_8.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarPor_8.setObjectName("BuscarPor_8")
        self.BuscarPor_8.addItem("")
        self.BuscarPor_8.addItem("")
        self.UltimCitActu_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.UltimCitActu_3.setGeometry(QtCore.QRect(380, 400, 600, 35))
        self.UltimCitActu_3.setMinimumSize(QtCore.QSize(600, 0))
        self.UltimCitActu_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.UltimCitActu_3.setObjectName("UltimCitActu_3")
        self.NombreActualizarPaciente_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.NombreActualizarPaciente_3.setGeometry(QtCore.QRect(380, 250, 600, 35))
        self.NombreActualizarPaciente_3.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_3.setObjectName("NombreActualizarPaciente_3")
        self.label_83 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_83.setGeometry(QtCore.QRect(150, 300, 221, 35))
        self.label_83.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_84.setGeometry(QtCore.QRect(120, 350, 251, 35))
        self.label_84.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_84.setObjectName("label_84")
        self.TelefonoActualizarPaciente_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.TelefonoActualizarPaciente_3.setGeometry(QtCore.QRect(380, 300, 600, 35))
        self.TelefonoActualizarPaciente_3.setMinimumSize(QtCore.QSize(600, 0))
        self.TelefonoActualizarPaciente_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.TelefonoActualizarPaciente_3.setObjectName("TelefonoActualizarPaciente_3")
        self.label_85 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_85.setGeometry(QtCore.QRect(110, 400, 261, 35))
        self.label_85.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_85.setObjectName("label_85")
        self.FechNacActu_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_9)
        self.FechNacActu_3.setGeometry(QtCore.QRect(380, 350, 600, 35))
        self.FechNacActu_3.setMinimumSize(QtCore.QSize(600, 0))
        self.FechNacActu_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.FechNacActu_3.setObjectName("FechNacActu_3")
        self.label_87 = QtWidgets.QLabel(self.scrollAreaWidgetContents_9)
        self.label_87.setGeometry(QtCore.QRect(410, 50, 281, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_87.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_87.setFont(font)
        self.label_87.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_87.setObjectName("label_87")
        self.BuscarBotonActualizar_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_9)
        self.BuscarBotonActualizar_3.setGeometry(QtCore.QRect(900, 100, 130, 70))
        self.BuscarBotonActualizar_3.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_3.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_3.setObjectName("BuscarBotonActualizar_3")
        self.scrollArea_9.setWidget(self.scrollAreaWidgetContents_9)
        self.gridLayout_13.addWidget(self.scrollArea_9, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_11, "")
        self.tab_15 = QtWidgets.QWidget()
        self.tab_15.setObjectName("tab_15")
        self.label_80 = QtWidgets.QLabel(self.tab_15)
        self.label_80.setGeometry(QtCore.QRect(230, 230, 95, 35))
        self.label_80.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_80.setObjectName("label_80")
        self.label_105 = QtWidgets.QLabel(self.tab_15)
        self.label_105.setGeometry(QtCore.QRect(360, 30, 441, 40))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_105.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_105.setFont(font)
        self.label_105.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_105.setObjectName("label_105")
        self.BuscarPor_9 = QtWidgets.QComboBox(self.tab_15)
        self.BuscarPor_9.setGeometry(QtCore.QRect(54, 96, 226, 37))
        self.BuscarPor_9.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarPor_9.setObjectName("BuscarPor_9")
        self.BuscarPor_9.addItem("")
        self.BuscarPor_9.addItem("")
        self.label_81 = QtWidgets.QLabel(self.tab_15)
        self.label_81.setGeometry(QtCore.QRect(320, 160, 531, 35))
        self.label_81.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_81.setObjectName("label_81")
        self.ActualizarBotonPaciente_4 = QtWidgets.QPushButton(self.tab_15)
        self.ActualizarBotonPaciente_4.setGeometry(QtCore.QRect(490, 580, 130, 70))
        self.ActualizarBotonPaciente_4.setMinimumSize(QtCore.QSize(130, 70))
        self.ActualizarBotonPaciente_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ActualizarBotonPaciente_4.setStyleSheet("QPushButton{\n"
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
"")
        self.ActualizarBotonPaciente_4.setObjectName("ActualizarBotonPaciente_4")
        self.NombreActualizarPaciente_4 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_4.setGeometry(QtCore.QRect(340, 230, 600, 35))
        self.NombreActualizarPaciente_4.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_4.setObjectName("NombreActualizarPaciente_4")
        self.label_107 = QtWidgets.QLabel(self.tab_15)
        self.label_107.setGeometry(QtCore.QRect(230, 280, 101, 35))
        self.label_107.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_107.setObjectName("label_107")
        self.ID_BuscarActualizarPaciente_4 = QtWidgets.QLineEdit(self.tab_15)
        self.ID_BuscarActualizarPaciente_4.setGeometry(QtCore.QRect(300, 94, 600, 41))
        self.ID_BuscarActualizarPaciente_4.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarActualizarPaciente_4.setMaximumSize(QtCore.QSize(600, 16777215))
        self.ID_BuscarActualizarPaciente_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;")
        self.ID_BuscarActualizarPaciente_4.setObjectName("ID_BuscarActualizarPaciente_4")
        self.BuscarBotonActualizar_7 = QtWidgets.QPushButton(self.tab_15)
        self.BuscarBotonActualizar_7.setGeometry(QtCore.QRect(920, 80, 130, 70))
        self.BuscarBotonActualizar_7.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonActualizar_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonActualizar_7.setStyleSheet("QPushButton{\n"
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
        self.BuscarBotonActualizar_7.setObjectName("BuscarBotonActualizar_7")
        self.label_108 = QtWidgets.QLabel(self.tab_15)
        self.label_108.setGeometry(QtCore.QRect(110, 330, 221, 35))
        self.label_108.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_108.setObjectName("label_108")
        self.label_109 = QtWidgets.QLabel(self.tab_15)
        self.label_109.setGeometry(QtCore.QRect(260, 380, 61, 35))
        self.label_109.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_109.setObjectName("label_109")
        self.label_110 = QtWidgets.QLabel(self.tab_15)
        self.label_110.setGeometry(QtCore.QRect(180, 430, 141, 35))
        self.label_110.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_110.setObjectName("label_110")
        self.label_111 = QtWidgets.QLabel(self.tab_15)
        self.label_111.setGeometry(QtCore.QRect(240, 480, 91, 35))
        self.label_111.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_111.setObjectName("label_111")
        self.NombreActualizarPaciente_5 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_5.setGeometry(QtCore.QRect(340, 280, 600, 35))
        self.NombreActualizarPaciente_5.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_5.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_5.setObjectName("NombreActualizarPaciente_5")
        self.NombreActualizarPaciente_6 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_6.setGeometry(QtCore.QRect(340, 330, 600, 35))
        self.NombreActualizarPaciente_6.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_6.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_6.setObjectName("NombreActualizarPaciente_6")
        self.NombreActualizarPaciente_7 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_7.setGeometry(QtCore.QRect(340, 380, 600, 35))
        self.NombreActualizarPaciente_7.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_7.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_7.setObjectName("NombreActualizarPaciente_7")
        self.NombreActualizarPaciente_8 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_8.setGeometry(QtCore.QRect(340, 430, 600, 35))
        self.NombreActualizarPaciente_8.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_8.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_8.setObjectName("NombreActualizarPaciente_8")
        self.NombreActualizarPaciente_9 = QtWidgets.QLineEdit(self.tab_15)
        self.NombreActualizarPaciente_9.setGeometry(QtCore.QRect(340, 480, 600, 35))
        self.NombreActualizarPaciente_9.setMinimumSize(QtCore.QSize(600, 0))
        self.NombreActualizarPaciente_9.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"border-radius: 5px;")
        self.NombreActualizarPaciente_9.setObjectName("NombreActualizarPaciente_9")
        self.label_151 = QtWidgets.QLabel(self.tab_15)
        self.label_151.setGeometry(QtCore.QRect(180, 530, 136, 40))
        self.label_151.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_151.setObjectName("label_151")
        self.MedicamentosRegistrar_9 = QtWidgets.QLineEdit(self.tab_15)
        self.MedicamentosRegistrar_9.setGeometry(QtCore.QRect(340, 530, 600, 35))
        self.MedicamentosRegistrar_9.setMinimumSize(QtCore.QSize(600, 0))
        self.MedicamentosRegistrar_9.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.MedicamentosRegistrar_9.setTabletTracking(True)
        self.MedicamentosRegistrar_9.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.MedicamentosRegistrar_9.setText("")
        self.MedicamentosRegistrar_9.setEchoMode(QtWidgets.QLineEdit.Password)
        self.MedicamentosRegistrar_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MedicamentosRegistrar_9.setObjectName("MedicamentosRegistrar_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_15)
        self.pushButton_6.setGeometry(QtCore.QRect(950, 530, 40, 40))
        self.pushButton_6.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/ojo.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_6.setText("")
        self.pushButton_6.setObjectName("pushButton_6")
        self.tabWidget_3.addTab(self.tab_15, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_19.setContentsMargins(-1, -1, -1, 30)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.RefrescarBotonRegistrados_4 = QtWidgets.QPushButton(self.tab_12)
        self.RefrescarBotonRegistrados_4.setMinimumSize(QtCore.QSize(130, 70))
        self.RefrescarBotonRegistrados_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RefrescarBotonRegistrados_4.setStyleSheet("QPushButton{\n"
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
"    border: 1.5px solid #e6b31e;\n"
"    margin: 10 px;\n"
"    right-margin: 10px;\n"
"}\n"
"\n"
"")
        self.RefrescarBotonRegistrados_4.setObjectName("RefrescarBotonRegistrados_4")
        self.gridLayout_19.addWidget(self.RefrescarBotonRegistrados_4, 4, 1, 1, 2, QtCore.Qt.AlignHCenter)
        self.BuscarRegistradosPacientesText_4 = QtWidgets.QLineEdit(self.tab_12)
        self.BuscarRegistradosPacientesText_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.BuscarRegistradosPacientesText_4.setObjectName("BuscarRegistradosPacientesText_4")
        self.gridLayout_19.addWidget(self.BuscarRegistradosPacientesText_4, 2, 2, 1, 1)
        self.BuscarBotonRegistrados_4 = QtWidgets.QPushButton(self.tab_12)
        self.BuscarBotonRegistrados_4.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonRegistrados_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonRegistrados_4.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonRegistrados_4.setObjectName("BuscarBotonRegistrados_4")
        self.gridLayout_19.addWidget(self.BuscarBotonRegistrados_4, 2, 4, 1, 1)
        self.BuscarRegistradosCombobox_6 = QtWidgets.QComboBox(self.tab_12)
        self.BuscarRegistradosCombobox_6.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_6.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_6.setObjectName("BuscarRegistradosCombobox_6")
        self.BuscarRegistradosCombobox_6.addItem("")
        self.BuscarRegistradosCombobox_6.addItem("")
        self.BuscarRegistradosCombobox_6.addItem("")
        self.BuscarRegistradosCombobox_6.setItemText(2, "")
        self.gridLayout_19.addWidget(self.BuscarRegistradosCombobox_6, 2, 0, 1, 2)
        self.TablaEmpleados_4 = QtWidgets.QTableWidget(self.tab_12)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.TablaEmpleados_4.setFont(font)
        self.TablaEmpleados_4.setStyleSheet("QHeaderView::section{\n"
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
        self.TablaEmpleados_4.setDragEnabled(False)
        self.TablaEmpleados_4.setObjectName("TablaEmpleados_4")
        self.TablaEmpleados_4.setColumnCount(9)
        self.TablaEmpleados_4.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.TablaEmpleados_4.setHorizontalHeaderItem(8, item)
        self.TablaEmpleados_4.horizontalHeader().setCascadingSectionResizes(False)
        self.TablaEmpleados_4.horizontalHeader().setHighlightSections(False)
        self.TablaEmpleados_4.horizontalHeader().setSortIndicatorShown(False)
        self.TablaEmpleados_4.horizontalHeader().setStretchLastSection(True)
        self.TablaEmpleados_4.verticalHeader().setVisible(False)
        self.TablaEmpleados_4.verticalHeader().setSortIndicatorShown(False)
        self.gridLayout_19.addWidget(self.TablaEmpleados_4, 3, 0, 1, 5)
        self.label_88 = QtWidgets.QLabel(self.tab_12)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_88.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_88.setFont(font)
        self.label_88.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_88.setObjectName("label_88")
        self.gridLayout_19.addWidget(self.label_88, 0, 0, 1, 5, QtCore.Qt.AlignHCenter)
        self.tabWidget_3.addTab(self.tab_12, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 50)
        self.gridLayout_20.setHorizontalSpacing(20)
        self.gridLayout_20.setVerticalSpacing(10)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.scrollArea_10 = QtWidgets.QScrollArea(self.tab_13)
        self.scrollArea_10.setStyleSheet("border-radius: 5px;")
        self.scrollArea_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.scrollArea_10.setWidgetResizable(True)
        self.scrollArea_10.setObjectName("scrollArea_10")
        self.scrollAreaWidgetContents_10 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_10.setGeometry(QtCore.QRect(0, 0, 83, 16))
        self.scrollAreaWidgetContents_10.setObjectName("scrollAreaWidgetContents_10")
        self.Eliminar_NombrePaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.Eliminar_NombrePaciente_2.setGeometry(QtCore.QRect(320, 200, 600, 35))
        self.Eliminar_NombrePaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.Eliminar_NombrePaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Eliminar_NombrePaciente_2.setObjectName("Eliminar_NombrePaciente_2")
        self.EliminarUltima_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.EliminarUltima_2.setGeometry(QtCore.QRect(320, 350, 600, 35))
        self.EliminarUltima_2.setMinimumSize(QtCore.QSize(600, 0))
        self.EliminarUltima_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EliminarUltima_2.setObjectName("EliminarUltima_2")
        self.label_89 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_89.setGeometry(QtCore.QRect(210, 200, 95, 35))
        self.label_89.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_89.setObjectName("label_89")
        self.label_90 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_90.setGeometry(QtCore.QRect(250, 350, 61, 35))
        self.label_90.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_90.setObjectName("label_90")
        self.label_91 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_91.setGeometry(QtCore.QRect(210, 250, 97, 35))
        self.label_91.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_91.setObjectName("label_91")
        self.ID_BuscarEliminarPaciente_3 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.ID_BuscarEliminarPaciente_3.setGeometry(QtCore.QRect(294, 87, 600, 35))
        self.ID_BuscarEliminarPaciente_3.setMinimumSize(QtCore.QSize(600, 0))
        self.ID_BuscarEliminarPaciente_3.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.ID_BuscarEliminarPaciente_3.setObjectName("ID_BuscarEliminarPaciente_3")
        self.label_92 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_92.setGeometry(QtCore.QRect(90, 300, 221, 35))
        self.label_92.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_92.setObjectName("label_92")
        self.EliminarFecha_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.EliminarFecha_2.setGeometry(QtCore.QRect(320, 300, 600, 35))
        self.EliminarFecha_2.setMinimumSize(QtCore.QSize(600, 0))
        self.EliminarFecha_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EliminarFecha_2.setObjectName("EliminarFecha_2")
        self.EliminarPacienteBoton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.EliminarPacienteBoton_3.setGeometry(QtCore.QRect(490, 520, 131, 70))
        self.EliminarPacienteBoton_3.setMinimumSize(QtCore.QSize(130, 70))
        self.EliminarPacienteBoton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.EliminarPacienteBoton_3.setStyleSheet("QPushButton{\n"
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
"")
        self.EliminarPacienteBoton_3.setObjectName("EliminarPacienteBoton_3")
        self.BuscarBotonEliminar_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_10)
        self.BuscarBotonEliminar_3.setGeometry(QtCore.QRect(900, 70, 130, 70))
        self.BuscarBotonEliminar_3.setMinimumSize(QtCore.QSize(130, 70))
        self.BuscarBotonEliminar_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.BuscarBotonEliminar_3.setStyleSheet("QPushButton{\n"
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
"")
        self.BuscarBotonEliminar_3.setObjectName("BuscarBotonEliminar_3")
        self.BuscarRegistradosCombobox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents_10)
        self.BuscarRegistradosCombobox_7.setGeometry(QtCore.QRect(62, 86, 226, 37))
        self.BuscarRegistradosCombobox_7.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.BuscarRegistradosCombobox_7.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.BuscarRegistradosCombobox_7.setObjectName("BuscarRegistradosCombobox_7")
        self.BuscarRegistradosCombobox_7.addItem("")
        self.BuscarRegistradosCombobox_7.addItem("")
        self.BuscarRegistradosCombobox_7.addItem("")
        self.BuscarRegistradosCombobox_7.setItemText(2, "")
        self.label_93 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_93.setGeometry(QtCore.QRect(430, 150, 271, 30))
        self.label_93.setMinimumSize(QtCore.QSize(0, 0))
        self.label_93.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_93.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_93.setObjectName("label_93")
        self.Eliminar_TelefenoPaciente_2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.Eliminar_TelefenoPaciente_2.setGeometry(QtCore.QRect(320, 250, 600, 35))
        self.Eliminar_TelefenoPaciente_2.setMinimumSize(QtCore.QSize(600, 0))
        self.Eliminar_TelefenoPaciente_2.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.Eliminar_TelefenoPaciente_2.setObjectName("Eliminar_TelefenoPaciente_2")
        self.label_94 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_94.setGeometry(QtCore.QRect(450, 40, 221, 39))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(35, 31, 32))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_94.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiBold SemiConden")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(7)
        self.label_94.setFont(font)
        self.label_94.setStyleSheet("font: 63 25pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_94.setObjectName("label_94")
        self.EliminarFecha_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.EliminarFecha_4.setGeometry(QtCore.QRect(320, 400, 600, 35))
        self.EliminarFecha_4.setMinimumSize(QtCore.QSize(600, 0))
        self.EliminarFecha_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EliminarFecha_4.setObjectName("EliminarFecha_4")
        self.EliminarUltima_4 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents_10)
        self.EliminarUltima_4.setGeometry(QtCore.QRect(320, 450, 600, 35))
        self.EliminarUltima_4.setMinimumSize(QtCore.QSize(600, 0))
        self.EliminarUltima_4.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.EliminarUltima_4.setObjectName("EliminarUltima_4")
        self.label_117 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_117.setGeometry(QtCore.QRect(230, 450, 81, 35))
        self.label_117.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_117.setObjectName("label_117")
        self.label_118 = QtWidgets.QLabel(self.scrollAreaWidgetContents_10)
        self.label_118.setGeometry(QtCore.QRect(170, 400, 141, 35))
        self.label_118.setStyleSheet("font: 63 22pt \"Bahnschrift SemiBold SemiConden\";\n"
"color: rgb(255, 255, 255);")
        self.label_118.setObjectName("label_118")
        self.scrollArea_10.setWidget(self.scrollAreaWidgetContents_10)
        self.gridLayout_20.addWidget(self.scrollArea_10, 0, 0, 1, 1)
        self.tabWidget_3.addTab(self.tab_13, "")
        self.horizontalLayout_8.addWidget(self.tabWidget_3)
        self.stackedWidget.addWidget(self.CRUD_Clientes)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.frame_4)
        self.gridLayout_26.addWidget(self.Frame_Inferior, 1, 0, 1, 1)
        MenuEmpleados.setCentralWidget(self.centralwidget)

        self.retranslateUi(MenuEmpleados)
        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MenuEmpleados)


        """
        Aqui inician las instrucciones a las funciones:
        """
        #Bienvenida
        SQL="""select Nombre from empleadosyadmin where cast(id_empleado as varchar)='{}' """.format(id)
        cursor.execute(SQL)
        row=cursor.fetchall()
        for rows in row: 
            name = rows[0]
        self.label_Bienvenida.setText("¡Bienvenido "+name+"!")
        fechaActual = datetime.datetime.now()
        fecha=datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
        
        #Botones menu desplegable (Navegacion)
        self.pushButton_35.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.RegistrarVisita))
        self.pushButton_33.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPuntoVenta))
        self.pushButton_30.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.CRUD_Entrenadores))
        self.pushButton_24.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.CRUD_Clientes))
        self.pushButton_36.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPrincipal))
        self.pushButton_32.clicked.connect(lambda: self.cerrarSesion(MenuEmpleados, cursor, LogIn))
        #Clickear menu (Navegacion)
        self.pushButton.clicked.connect(lambda: self.desplegrMenu())
        #Botones Menu principal (Navegacion)
        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.RegistrarVisita))
        self.pushButton_25.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPuntoVenta))
        self.pushButton_27.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.CRUD_Entrenadores))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.CRUD_Clientes))
        #Botones Menu punto de venta (Navegacion)
        self.pushButton_11.clicked.connect(lambda: self.puntoVentaOpc(1))
        self.pushButton_12.clicked.connect(lambda: self.puntoVentaOpc(2))
        self.pushButton_14.clicked.connect(lambda: self.puntoVentaOpc(3))
        #Botones punto de venta (Navegacion)
        self.radioButton.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Puntodeventas))
        self.radioButton_2.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page_2))
        self.radioButton_3.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.Ventas))
        self.radioButton_4.clicked.connect(lambda: self.stackedWidget_2.setCurrentWidget(self.page))
        self.radioButton.clicked.connect(lambda: self.limpiaVar())
        self.radioButton_4.clicked.connect(lambda: self.limpiaVar())
        
        #CRUD ENTRENADORES - Botón (Agregar)
        self.GuardarRegistrarPaciente_2.clicked.connect(lambda: self.Agregar_Entrenador(cursor))
        #CRUD ENTRENADORES - Botón  (Actualizar)
        self.BuscarBotonActualizar_2.clicked.connect(lambda: self.buscarActualizarEntrenador(cursor))
        self.ActualizarBotonPaciente_2.clicked.connect(lambda: self.actualizarEntrenador(cursor))
        #CRUD ENTRENADORES - Botón (Clientes asignados)
        self.BuscarBotonRegistrados_2.clicked.connect(lambda: self.MostrarCliente_Entrenador(cursor))
        #CRUD ENTRENADORES - Botón (Mostrar)
        self.BuscarBotonRegistrados_3.clicked.connect(lambda: self.BuscarMostrar_Entrenador(cursor))
        self.RefrescarBotonRegistrados_3.clicked.connect(lambda: self.refrescarMostrar_Entrenador(cursor))
        #CRUD ENTRENADORES - Botón (Eliminar)
        self.BuscarBotonEliminar_2.clicked.connect(lambda: self.buscarEliminar_Entrenador(cursor))
        self.EliminarPacienteBoton_2.clicked.connect(lambda: self.eliminar_Entrenador(cursor))
        
        #Botones CRUD Clientes (Registrar)
        self.GuardarRegistrarPaciente_3.clicked.connect(lambda: self.registrarCliente(cursor,fecha))
        self.pushButton_5.clicked.connect(lambda: self.passwordHide(self.MedicamentosRegistrar_8))
        #Botones CRUD Clientes (AsignarEntrenador)
        self.BuscarBotonActualizar_4.clicked.connect(lambda: self.buscarCliente(cursor))
        self.BuscarBotonActualizar_5.clicked.connect(lambda: self.buscarEntrenador(cursor))
        self.BuscarBotonActualizar_6.clicked.connect(lambda: self.asignarEntrenador(cursor))
        #Botones CRUD Clientes (Membresia)
        self.BuscarBotonActualizar_3.clicked.connect(lambda: self.ConsultarMembresia(cursor))
        #Botones CRUD Clientes (Actualizar Cliente)
        self.BuscarBotonActualizar_7.clicked.connect(lambda: self.Buscarcliente(cursor))
        self.pushButton_6.clicked.connect(lambda: self.passwordHide(self.MedicamentosRegistrar_9))
        self.ActualizarBotonPaciente_4.clicked.connect(lambda: self.ActualizarCliente(cursor))
        #Botones CRUD Clientes (Mostrar)
        self.BuscarBotonRegistrados_4.clicked.connect(lambda: self.MostrarCliente(cursor))
        self.RefrescarBotonRegistrados_4.clicked.connect(lambda: self.RefrescarClientess(cursor))
        #Botones CRUD Clientes (Eliminar)
        self.BuscarBotonEliminar_3.clicked.connect(lambda: self.BuscarCliente(cursor))
        self.EliminarPacienteBoton_3.clicked.connect(lambda: self.EliminarCliente(cursor))
        
        
        #Punto de venta (VENTA)
        self.pushButton_11.clicked.connect(lambda: self.getFolio(cursor))
        self.radioButton.clicked.connect(lambda: self.getFolio(cursor))
        self.lineEdit_2.setText(fecha)
        self.lineEdit_4.setText(name)
        self.lineEdit.setText(str(id))
        self.CantidadTotal = 0.0
        self.carrito=[]
        self.folio=0
            #Buscar producto venta
        self.pushButton_7.clicked.connect(lambda: self.buscarProductoVenta(cursor))
        self.pushButton_8.clicked.connect(lambda: self.agregarProductoVenta(cursor))
            #Realizar venta
        self.pushButton_10.clicked.connect(lambda: self.realizarVentaProducto(cursor))
            #Generar Ticket
        self.pushButton_28.clicked.connect(lambda: self.generarTicket(cursor, fecha, name, self.opc))
            #Cancelar venta
        self.pushButton_9.clicked.connect(lambda: self.cancelarVentaProducto())
            #Finalizar venta
        self.pushButton_29.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPuntoVenta))   
            #Buscar Membresia
        self.pushButton_37.clicked.connect(lambda: self.buscarMembresiaVenta(cursor))
        self.pushButton_38.clicked.connect(lambda: self.agregarMembresiaVenta(cursor))
            #Cancelar Venta Membresia
        self.pushButton_31.clicked.connect(lambda: self.cancelarMembresiaVenta())
            #Realizar Venta Membresia
        self.pushButton_23.clicked.connect(lambda: self.realizarVentaMembresia(cursor))
            #Funciones del inventario
            #Registrar producto 
        self.GuardarRegistrarPaciente_5.clicked.connect(lambda: self.registrarProducto(cursor))
            #Registrar membresia 
        self.GuardarRegistrarPaciente_6.clicked.connect(lambda: self.registrarMembresia(cursor))
            #Actualizar producto
        self.BuscarBotonActualizar_9.clicked.connect(lambda: self.buscarActualizarProducto(cursor))
        self.ActualizarBotonPaciente_6.clicked.connect(lambda: self.actualizarProducto(cursor))
            #Eliminar producto
        self.BuscarBotonEliminar_5.clicked.connect(lambda: self.buscarEliminarProducto(cursor))
        self.EliminarPacienteBoton_5.clicked.connect(lambda: self.eliminarProducto(cursor))        
            #Mostrar inventario
        self.radioButton_2.clicked.connect(lambda: self.mostrarInventario(cursor))
        self.BuscarBotonRegistrados_8.clicked.connect(lambda: self.buscarInventario(cursor))
        self.RefrescarBotonRegistrados_6.clicked.connect(lambda: self.refrescarInvenatario(cursor))
            #Registrar Foto de producto
        self.pushButton_13.clicked.connect(lambda: self.seleccionarFoto(cursor))
        self.pushButton_16.clicked.connect(lambda: self.seleccionarNuevaFoto(cursor))
             #mostrar Ventas self.mostrarVentas(cursor)
        self.radioButton_3.clicked.connect(lambda: self.mostrarVentas(cursor))
        self.pushButton_14.clicked.connect(lambda: self.mostrarVentas(cursor))
        self.pushButton_15.clicked.connect(lambda: self.mostrarVentas(cursor))  
        self.pushButton_15.clicked.connect(lambda: self.refrescarVentas(cursor))
             #Buscar Ventas 
        self.BuscarBotonRegistrados_7.clicked.connect(lambda: self.buscarVentas(cursor))  
             #Buscar Visita
        self.Buscar_Visita_3.clicked.connect(lambda: self.buscarVisita(cursor, fecha))  
        #RegistrarVisita Volver al menu
        self.Buscar_Visita_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPrincipal)) 
        #Registrar Visita
        self.Buscar_Visita_4.clicked.connect(lambda: self.registrarVisita(cursor)) 
        self.pushButton_35.clicked.connect(lambda: self.limpiarVisita())
        self.pushButton_22.clicked.connect(lambda: self.limpiarVisita())
        self.Buscar_Visita_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.MenuPrincipal))
        
        """
        Aqui inician las funciones:
        """
    def cerrarSesion(self, MenuPrincipal, cursor, Login):
        MenuPrincipal.close()
        Login.show()
        
    def desplegrMenu(self):
        
        if True:
            width = self.Menu_Lateral_Frame.width()
            normal = 0
            if width==0:
                extender = 100
            else:
                extender = normal
            
            self.animacion = QtCore.QPropertyAnimation(self.Menu_Lateral_Frame, b'minimumWidth') 
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width) 
            self.animacion.setEndValue(extender) 
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart) 
            self.animacion.start()
    
    def puntoVentaOpc(self,opc):
        if opc==1:
            self.stackedWidget.setCurrentWidget(self.PuntoVenta)
            self.stackedWidget_2.setCurrentWidget(self.Puntodeventas)
            self.radioButton.setChecked(True)
        elif opc==2:
            self.stackedWidget.setCurrentWidget(self.PuntoVenta)
            self.stackedWidget_2.setCurrentWidget(self.page_2)
            self.radioButton_2.setChecked(True)
        elif opc==3:
            self.stackedWidget.setCurrentWidget(self.PuntoVenta)
            self.stackedWidget_2.setCurrentWidget(self.Ventas)
            self.radioButton_3.setChecked(True)
        elif opc==4:
            self.stackedWidget.setCurrentWidget(self.PuntoVenta)
            self.stackedWidget_2.setCurrentWidget(self.page)
            self.radioButton_4.setCheckable(True)

    def passwordHide(self, passw):
        if passw.echoMode() == QLineEdit.Password:
            passw.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            passw.setEchoMode(QtWidgets.QLineEdit.Password)
    """
    CRUD Entrenadores
    """ 
        
    def Agregar_Entrenador(self, cursor):
        nombre=self.NombreRegistrar_2.text()
        fechIngreso=self.UltimaCitaRegistrar_2.text()
        naci=self.FechaNacimientoRegistrar_2.text()
        tel=self.TelefonoRegistrar_2.text()
        curp=self.AlergiasRegistrar_2.text()
        NSS=self.EnfermedadesRegistrar_2.text()
        RFC=self.MedicamentosRegistrar_2.text() 
        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre para poder registrar a un entrenador")
        elif len(fechIngreso)==0:
            self.msgError("Falta de informacion", "Debes ingresar una fecha de ingreso para poder registrar a un entrenador")
        elif len(naci)==0:
            self.msgError("Falta de informacion", "Debes ingresar una fecha de nacimiento para poder registrar a un entrenador")
        elif (len(tel)==0) or (len(tel)!=10):
            self.msgError("Falta de informacion", "Debes ingresar un numero de telefono valido de almenos 10 digitos")
        elif (len(curp)==0) or (len(curp)!=18):
            self.msgError("Falta de informacion", "Debes ingresar una CURP valida la cual se compone de 18 digitos") 
        elif (len(NSS)==0) or (len(NSS)!=11):
            self.msgError("Falta de informacion", "Debes ingresar un NSS valido de almenos 11 digitos")
        elif (len(RFC)==0) or (len(RFC)!=13):
            self.msgError("Falta de informacion", "Debes ingresar un RFC valido de almenos 13 digitos")
        else:
            SQL=""" insert into entrenador(Nombre_Entrenador, Fecha_Ingreso, Fecha_nacimiento, Telefono_Entrenador, CURP_Entrenador, NSS_Entrenador, RFC_Entrenador)\
                values ('{}','{}','{}','{}','{}','{}','{}'); """.format(nombre, fechIngreso, naci, tel, curp, NSS, RFC)
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                print(ex)
            self.NombreRegistrar_2.clear()
            self.TelefonoRegistrar_2.clear()
            self.AlergiasRegistrar_2.clear()
            self.EnfermedadesRegistrar_2.clear()
            self.MedicamentosRegistrar_2.clear()
    
    def buscarActualizarEntrenador(self, cursor):
        self.NombreActualizarPaciente_2.clear()
        self.TelefonoActualizarPaciente_2.clear()
        self.FechNacActu_2.clear()
        self.UltimCitActu_2.clear()
        self.AlergiasActualizar_2.clear()
        self.EnfermedadesActualizar_2.clear()
        self.MedicamentosActualizar_2.clear()
        data=self.ID_BuscarActualizarPaciente_2.text()
        if len(data)==0:
            self.msgError("Busqueda no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarPor_7.currentText()
            if opc == "Buscar por ID:":
                SQL="""select *from entrenador where cast(ID_entrenador as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe entrenador registrado con ese ID")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_2.setText(str(rows[1]))
                        self.TelefonoActualizarPaciente_2.setText(str(rows[2]))
                        self.FechNacActu_2.setText(str(rows[3]))
                        self.UltimCitActu_2.setText(str(rows[4]))
                        self.AlergiasActualizar_2.setText(str(rows[5]))
                        self.EnfermedadesActualizar_2.setText(str(rows[6]))
                        self.MedicamentosActualizar_2.setText(str(rows[7]))
            else:
                SQL="""select *from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe entrenador registrado con ese Nombre")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_2.setText(str(rows[1]))
                        self.TelefonoActualizarPaciente_2.setText(str(rows[2]))
                        self.FechNacActu_2.setText(str(rows[3]))
                        self.UltimCitActu_2.setText(str(rows[4]))
                        self.AlergiasActualizar_2.setText(str(rows[5]))
                        self.EnfermedadesActualizar_2.setText(str(rows[6]))
                        self.MedicamentosActualizar_2.setText(str(rows[7]))
         
    def actualizarEntrenador(self, cursor):
        
        opc = self.BuscarPor_7.currentText()
        data = self.ID_BuscarActualizarPaciente_2.text()
        if opc == "Buscar por Nombre:":
            SQL="""select ID_entrenador from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de actualizar")
            else:
                for rows in row:
                    id = str(rows[0])
        else:
            id = data
        if len(id)==0:
            self.msgError("Busqueda", "Debes realizar una busqueda primero antes de actualizar")
            return
        nombre=self.NombreActualizarPaciente_2.text()
        fechIngreso=self.TelefonoActualizarPaciente_2.text()
        naci=self.FechNacActu_2.text()
        tel=self.UltimCitActu_2.text()
        curp=self.AlergiasActualizar_2.text()
        NSS=self.EnfermedadesActualizar_2.text()
        RFC=self.MedicamentosActualizar_2.text() 
        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre o dejar el anterior antes de actualizar a un entrenador")
        elif len(fechIngreso)==0:
            self.msgError("Falta de informacion", "Debes ingresar una fecha de ingreso o dejar la anterior antes de actualizar a un entrenador")
        elif len(naci)==0:
            self.msgError("Falta de informacion", "Debes ingresar una fecha de nacimiento o dejar la anterior antes de actualizar a un entrenador")
        elif (len(tel)==0) or (len(tel)!=10):
            self.msgError("Falta de informacion", "Debes ingresar un numero de telefono valido de almenos 10 digitos o dejar el anterior antes de actualizar")
        elif (len(curp)==0) or (len(curp)!=18):
            self.msgError("Falta de informacion", "Debes ingresar una CURP valida la cual se compone de 18 digitos o dejar el anterior antes de actualizar") 
        elif (len(NSS)==0) or (len(NSS)!=11):
            self.msgError("Falta de informacion", "Debes ingresar un NSS valido de almenos 11 digitos o dejar el anterior antes de actualizar")
        elif (len(RFC)==0) or (len(RFC)!=13):
            self.msgError("Falta de informacion", "Debes ingresar un RFC valido de almenos 13 digitos o dejar el anterior antes de actualizar")
        else:
            SQL=""" update entrenador set Nombre_Entrenador='{}', Fecha_Ingreso='{}', Fecha_nacimiento='{}',Telefono_Entrenador='{}', 
            CURP_Entrenador='{}', NSS_Entrenador='{}', RFC_Entrenador='{}' where ID_entrenador='{}' """.format(nombre, fechIngreso, naci, tel, curp, NSS, RFC, id)
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
                print(id)
            except Exception as ex:
                print(ex)
            self.NombreActualizarPaciente_2.clear()
            self.TelefonoActualizarPaciente_2.clear()
            self.FechNacActu_2.clear()
            self.UltimCitActu_2.clear()
            self.AlergiasActualizar_2.clear()
            self.EnfermedadesActualizar_2.clear()
            self.MedicamentosActualizar_2.clear()

    def MostrarCliente_Entrenador(self, cursor):
        data=self.BuscarRegistradosPacientesText_2.text()
        self.TablaEmpleados_2.clearContents()
        self.TablaEmpleados_2.setRowCount(0)
        if len(data)==0:
            self.msgError("Busqueda", "Debes ingresar informacion antes de buscar")
        else:
            opc=self.BuscarRegistradosCombobox_3.currentText() 
            if opc == "Buscar por Nombre:":

                SQL="""select ID_entrenador from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                        self.msgError("Sin coincidencia", "No existe coincidencia con ese nombre de cliente")
                        return

                for rows in row:
                        idEntrenador=rows[0]

                SQL="""select * from cliente where cast(ID_entrenador as varchar)='{}' """.format(idEntrenador)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese nombre de entrenador")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_2.setRowCount(tablerow + 1)
                        self.TablaEmpleados_2.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_2.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_2.setItem(tablerow,2,QTableWidgetItem(str(rows[9])))
                        self.TablaEmpleados_2.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_2.setItem(tablerow,4,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_2.setItem(tablerow,5,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_2.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_2.setItem(tablerow,7,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_2.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            elif opc == "Buscar por ID:":
                SQL="""select * from cliente where cast(ID_entrenador as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de entrenador")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_2.setRowCount(tablerow + 1)
                        self.TablaEmpleados_2.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_2.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_2.setItem(tablerow,2,QTableWidgetItem(str(rows[9])))
                        self.TablaEmpleados_2.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_2.setItem(tablerow,4,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_2.setItem(tablerow,5,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_2.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_2.setItem(tablerow,7,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_2.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            else:
                self.msgError("Seleccion", "Selecciona un modo de busqueda")
    
    def BuscarMostrar_Entrenador(self, cursor):
        data=self.BuscarRegistradosPacientesText_3.text()
        self.TablaEmpleados_3.clearContents()
        self.TablaEmpleados_3.setRowCount(0)
        
        if len(data)==0:
            self.msgError("Busqueda", "Debes ingresar informacion antes de buscar")
        else:
            opc=self.BuscarRegistradosCombobox.currentText() 
            if opc == "Buscar por Nombre:":
                SQL="""select *from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese nombre de entrenador")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_3.setRowCount(tablerow + 1)
                        self.TablaEmpleados_3.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_3.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_3.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_3.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_3.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_3.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_3.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_3.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
            elif opc == "Buscar por ID:":
                SQL="""select *from entrenador where cast(ID_entrenador as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de entrenador")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_3.setRowCount(tablerow + 1)
                        self.TablaEmpleados_3.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_3.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_3.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_3.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_3.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_3.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_3.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_3.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
            else:
                self.msgError("Seleccion", "Selecciona un modo de busqueda")
    
    def refrescarMostrar_Entrenador(self, cursor):
        self.TablaEmpleados_3.clearContents()
        cursor.execute("SELECT *FROM entrenador")
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
            self.TablaEmpleados_3.setRowCount(tablerow + 1)
            self.TablaEmpleados_3.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.TablaEmpleados_3.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.TablaEmpleados_3.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.TablaEmpleados_3.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.TablaEmpleados_3.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
            self.TablaEmpleados_3.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
            self.TablaEmpleados_3.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
            self.TablaEmpleados_3.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
            print(rows[3])
            tablerow+=1
            
    def buscarEliminar_Entrenador(self, cursor):
        self.NombreRegistrar_3.clear()
        self.UltimaCitaRegistrar_3.clear()
        self.FechaNacimientoRegistrar_3.clear()
        self.TelefonoRegistrar_3.clear()
        self.AlergiasRegistrar_3.clear()
        self.EnfermedadesRegistrar_3.clear()
        self.MedicamentosRegistrar_3.clear()
        
        data=self.ID_BuscarEliminarPaciente_2.text()
        if len(data)==0:
            self.msgError("Busqued no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarRegistradosCombobox_4.currentText()
            if opc == "Buscar por ID:":
                SQL="""select *from entrenador where cast(ID_entrenador as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe entrenador registrado con ese ID")
                else:
                    for rows in row:
                        self.NombreRegistrar_3.setText(str(rows[1]))
                        self.UltimaCitaRegistrar_3.setText(str(rows[2]))
                        self.FechaNacimientoRegistrar_3.setText(str(rows[3]))
                        self.TelefonoRegistrar_3.setText(str(rows[4]))
                        self.AlergiasRegistrar_3.setText(str(rows[5]))
                        self.EnfermedadesRegistrar_3.setText(str(rows[6]))
                        self.MedicamentosRegistrar_3.setText(str(rows[7]))
            else:
                SQL="""select *from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe entrenador registrado con ese Nombre")
                else:
                    for rows in row:
                        self.NombreRegistrar_3.setText(str(rows[1]))
                        self.UltimaCitaRegistrar_3.setText(str(rows[2]))
                        self.FechaNacimientoRegistrar_3.setText(str(rows[3]))
                        self.TelefonoRegistrar_3.setText(str(rows[4]))
                        self.AlergiasRegistrar_3.setText(str(rows[5]))
                        self.EnfermedadesRegistrar_3.setText(str(rows[6]))
                        self.MedicamentosRegistrar_3.setText(str(rows[7]))
                                
    def eliminar_Entrenador(self, cursor):
        opc = self.BuscarRegistradosCombobox_4.currentText()
        data = self.ID_BuscarEliminarPaciente_2.text()
        if opc == "Buscar por Nombre:":
            SQL="""select ID_entrenador from entrenador where Nombre_Entrenador like '%{}%' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de eliminar")
            else:
                for rows in row:
                    id = str(rows[0])
        id=str(data)
        
        nombre=self.NombreRegistrar_3.text()
        fechIngreso=self.UltimaCitaRegistrar_3.text()
        naci=self.FechaNacimientoRegistrar_3.text()
        tel=self.TelefonoRegistrar_3.text()
        curp=self.AlergiasRegistrar_3.text()
        NSS=self.EnfermedadesRegistrar_3.text()
        RFC=self.MedicamentosRegistrar_3.text() 
        
        if len(nombre)==0 or len(fechIngreso)==0 or len(naci)==0 or len(tel)==0 or len(curp)==0 or len(NSS)==0 or len(RFC)==0:
            self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de eliminar")
        else:
            SQL='''delete from entrenador where ID_entrenador='{}' '''.format(id)   
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                #self.msgError("No fue posible eliminar el entrenador", ex)
                print(ex)
            SQL='''update cliente set id_entrenador=null where id_entrenador='{}' '''.format(id)   
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                #self.msgError("No fue posible eliminar el entrenador", ex)
                print(ex)
                
        
            self.NombreRegistrar_3.clear()
            self.UltimaCitaRegistrar_3.clear()
            self.FechaNacimientoRegistrar_3.clear()
            self.TelefonoRegistrar_3.clear()
            self.AlergiasRegistrar_3.clear()
            self.EnfermedadesRegistrar_3.clear()
            self.MedicamentosRegistrar_3.clear()    
    
    """
    CRUD Clientes
    """ 
    def registrarCliente(self, cursor, date):
        nombre=self.NombreRegistrar_4.text()
        telefono=self.TelefonoRegistrar_4.text()
        correo=self.AlergiasRegistrar_5.text()
        edad=self.AlergiasRegistrar_4.text()
        peso=self.EnfermedadesRegistrar_4.text()
        altura=self.MedicamentosRegistrar_4.text()
        password_cliente=self.MedicamentosRegistrar_8.text()
        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre para poder registrar a un cliente")
        elif (len(telefono)==0) or (len(telefono)!=10):
            self.msgError("Falta de informacion", "Debes ingresar un numero de telefono valido de almenos 10 digitos")
        elif (len(correo)==0):
            self.msgError("Falta de informacion", "Debes ingresar un correo") 
        elif (len(edad)==0):
            self.msgError("Falta de informacion", "Debes ingresar una edad")
        elif (len(peso)==0):
            self.msgError("Falta de informacion", "Debes ingresar un peso")
        elif (len(altura)==0) or (float(altura)<=1.0) or (float(altura)>=2.5):
            self.msgError("Campo incompleto","Debes ingresar una altura valida en formato (1.50) y no dejarlo vacio")
        elif (len(password_cliente)<8):
            self.msgError("Falta de informacion", "Debes ingresar una contraseña de almenos 8 digitos")
        else:
            alt=float(altura)
            pes=float(peso) 
            IMC = pes / (alt**2)
            
            if IMC<18.5:
                IMCS= str(self.truncate(IMC),2)+" Bajo peso"
            elif (IMC<=24.9) and (IMC>=18.5):
                IMCS= str(self.truncate(IMC,2))+" Peso saludable"
            elif (IMC<=29.9) and (IMC>=25):
                IMCS= str(self.truncate(IMC,2))+" Sobrepeso"  
            elif (IMC>30):
                IMCS= str(self.truncate(IMC,2))+" Obesidad" 
            SQL=""" insert into cliente (nombre_cliente, telefono_cliente, correo_cliente, edad, peso_act, altura, IMC, Fecha_Vencimiento, contraseña, Fecha_ingreso)\
                values ('{}','{}','{}','{}',{},'{}','{}','{}','{}','{}'); """.format(nombre,telefono,correo,edad,peso,altura,IMCS,date,password_cliente,date)
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                print(ex)
            self.NombreRegistrar_4.clear()
            self.TelefonoRegistrar_4.clear()
            self.AlergiasRegistrar_5.clear()
            self.AlergiasRegistrar_4.clear()
            self.EnfermedadesRegistrar_4.clear()
            self.MedicamentosRegistrar_4.clear()
            self.MedicamentosRegistrar_8.clear()
      
    def buscarCliente(self, cursor):
        self.NombreRegistrar_6.clear()
        self.NombreRegistrar_7.clear()
        ID_Cliente=self.NombreRegistrar_5.text()
        if len(ID_Cliente)==0:
            self.msgError("Busqueda no valida", "Debes ingresar un ID valido para buscar")
        else:  
            SQL="""select * from cliente where cast(id_cliente as varchar)='{}' """.format(ID_Cliente)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe cliente registrado con ese ID")
            else:
                for rows in row:
                    self.NombreRegistrar_6.setText(str(rows[1]))
                    self.NombreRegistrar_7.setText(str(rows[3]))
    
    def buscarEntrenador(self, cursor):
        self.NombreRegistrar_9.clear()
        self.NombreRegistrar_10.clear()
        ID_Entrenador=self.NombreRegistrar_8.text()
        if len(ID_Entrenador)==0:
            self.msgError("Busqueda no valida", "Debes ingresar un ID valido para buscar")
        else:  
            SQL="""select * from entrenador where cast(id_entrenador as varchar)='{}' """.format(ID_Entrenador)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe entrenador registrado con ese ID")
            else:
                for rows in row:
                    self.NombreRegistrar_10.setText(str(rows[1]))
                    self.NombreRegistrar_9.setText(str(rows[2]))
    
    def asignarEntrenador(self, cursor):
        ID_Cliente=self.NombreRegistrar_5.text()
        if len(ID_Cliente)==0:
            self.msgError("Asignacion no valida", "Debes ingresar un ID valido para cliente")
        else:
            ID_Entrenador=self.NombreRegistrar_8.text()
            if len(ID_Entrenador)==0:
                self.msgError("Asignacion no valida", "Debes ingresar un ID valido para entrenador")
            else:  
                SQL=""" update cliente set id_entrenador='{}' where cast(id_cliente as varchar)='{}' """.format(ID_Entrenador,ID_Cliente)
                try:
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                except Exception as ex:
                    print(ex)
                self.NombreRegistrar_5.clear()
                self.NombreRegistrar_6.clear()
                self.NombreRegistrar_7.clear()
                self.NombreRegistrar_8.clear()
                self.NombreRegistrar_9.clear()
                self.NombreRegistrar_10.clear()
                
    def ConsultarMembresia(self, cursor):
        self.NombreActualizarPaciente_3.clear()
        self.TelefonoActualizarPaciente_3.clear()
        self.FechNacActu_3.clear()
        self.UltimCitActu_3.clear()
        data=self.ID_BuscarActualizarPaciente_3.text()
        if len(data)==0:
            self.msgError("Busqueda no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarPor_8.currentText()
            if opc == "Buscar por ID:":
                SQL="""select * from cliente where cast(id_cliente as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese ID")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_3.setText(str(rows[1]))
                        self.TelefonoActualizarPaciente_3.setText(str(rows[3]))
                        self.FechNacActu_3.setText(str(rows[8]))
                        self.UltimCitActu_3.setText(str(rows[9]))
            else:
                SQL="""select * from cliente where nombre_cliente like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese Nombre")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_3.setText(str(rows[1]))
                        self.TelefonoActualizarPaciente_3.setText(str(rows[3]))
                        self.FechNacActu_3.setText(str(rows[8]))
                        self.UltimCitActu_3.setText(str(rows[9]))
                
    def Buscarcliente(self, cursor):
        self.NombreActualizarPaciente_4.clear()
        self.NombreActualizarPaciente_5.clear()
        self.NombreActualizarPaciente_6.clear()
        self.NombreActualizarPaciente_7.clear()
        self.NombreActualizarPaciente_8.clear()
        self.NombreActualizarPaciente_9.clear()
        self.MedicamentosRegistrar_9.clear()
        data=self.ID_BuscarActualizarPaciente_4.text()
        if len(data)==0:
            self.msgError("Busqueda no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarPor_9.currentText()
            if opc == "Buscar por ID:":
                SQL="""select * from cliente where cast(id_cliente as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese ID")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_4.setText(str(rows[1]))
                        self.NombreActualizarPaciente_5.setText(str(rows[2]))
                        self.NombreActualizarPaciente_6.setText(str(rows[3]))
                        self.NombreActualizarPaciente_7.setText(str(rows[4]))
                        self.NombreActualizarPaciente_8.setText(str(rows[5]))
                        self.NombreActualizarPaciente_9.setText(str(rows[6]))
                        self.MedicamentosRegistrar_9.setText(str(rows[10]))
            else:
                SQL="""select * from cliente where nombre_cliente like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese Nombre")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_4.setText(str(rows[1]))
                        self.NombreActualizarPaciente_5.setText(str(rows[2]))
                        self.NombreActualizarPaciente_6.setText(str(rows[3]))
                        self.NombreActualizarPaciente_7.setText(str(rows[4]))
                        self.NombreActualizarPaciente_8.setText(str(rows[5]))
                        self.NombreActualizarPaciente_9.setText(str(rows[6]))
                        self.MedicamentosRegistrar_9.setText(str(rows[10]))
                        
    def ActualizarCliente(self, cursor):
        opc = self.BuscarPor_9.currentText()
        data = self.ID_BuscarActualizarPaciente_4.text()
        if opc == "Buscar por Nombre:":
            SQL="""select id_cliente from cliente where nombre_cliente like '%{}%' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "Debes realizar una busqueda valida primero antes de actualizar")
            else:
                for rows in row:
                    id = str(rows[0])
        else:
            id = data
        if len(id)==0:
            self.msgError("Sin coincidencia", "Debes realizar una busqueda primero antes de actualizar")
            return
        nombre=self.NombreActualizarPaciente_4.text()
        telefono=self.NombreActualizarPaciente_5.text()
        correo=self.NombreActualizarPaciente_6.text()
        edad=self.NombreActualizarPaciente_7.text()
        peso=self.NombreActualizarPaciente_8.text()
        altura=self.NombreActualizarPaciente_9.text()
        password=self.MedicamentosRegistrar_9.text()
        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre o dejar el anterior antes de actualizar a un cliente")
        elif (len(telefono)==0) or (len(telefono)!=10):
            self.msgError("Falta de informacion", "Debes ingresar un numero de telefono valido de almenos 10 digitos o dejar el anterior antes de actualizar")
        elif (len(correo)==0):
            self.msgError("Falta de informacion", "Debes ingresar un correo o dejar el anterior antes de actualizar") 
        elif (len(edad)==0):
            self.msgError("Falta de informacion", "Debes ingresar una edad o dejar el anterior antes de actualizar")
        elif (len(peso)==0):
            self.msgError("Falta de informacion", "Debes ingresar un peso o dejar el anterior antes de actualizar")
        elif (len(altura)==0):
            self.msgError("Falta de informacion", "Debes ingresar una altura o dejar la anterior antes de actualizar")
        elif (len(password)==0) or (len(password)<8):
            self.msgError("Falta de informacion", "Debes ingresar una contraseña valida de almenos 8 digitos o dejar la anterior antes de actualizar")
        else:
            SQL=""" update cliente set nombre_cliente='{}', telefono_cliente='{}', correo_cliente='{}', edad='{}', peso_act='{}', 
            altura='{}', contraseña='{}' where id_cliente='{}' """.format(nombre, telefono, correo, edad, peso, altura, password, id)
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                print(ex)            
            self.NombreActualizarPaciente_4.clear()
            self.NombreActualizarPaciente_5.clear()
            self.NombreActualizarPaciente_6.clear()
            self.NombreActualizarPaciente_7.clear()
            self.NombreActualizarPaciente_8.clear()
            self.NombreActualizarPaciente_9.clear()
            self.MedicamentosRegistrar_9.clear()
            
    def MostrarCliente(self, cursor):
        data=self.BuscarRegistradosPacientesText_4.text()
        self.TablaEmpleados_4.clearContents()
        self.TablaEmpleados_4.setRowCount(0)
        if len(data)==0:
            self.msgError("Busqueda", "Debes ingresar informacion antes de buscar")
        else:
            opc=self.BuscarRegistradosCombobox_6.currentText() 
            if opc == "Buscar por Nombre:":
                SQL="""select * from cliente where nombre_cliente like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese nombre de cliente")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_4.setRowCount(tablerow + 1)
                        self.TablaEmpleados_4.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_4.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_4.setItem(tablerow,2,QTableWidgetItem(str(rows[9])))
                        self.TablaEmpleados_4.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_4.setItem(tablerow,4,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_4.setItem(tablerow,5,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_4.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_4.setItem(tablerow,7,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_4.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            elif opc == "Buscar por ID:":
                SQL="""select * from cliente where cast(id_cliente as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de cliente")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_4.setRowCount(tablerow + 1)
                        self.TablaEmpleados_4.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_4.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_4.setItem(tablerow,2,QTableWidgetItem(str(rows[9])))
                        self.TablaEmpleados_4.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_4.setItem(tablerow,4,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_4.setItem(tablerow,5,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_4.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_4.setItem(tablerow,7,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_4.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            else:
                self.msgError("Seleccion", "Selecciona un modo de busqueda")
    
    def RefrescarClientess(self, cursor):
        self.TablaEmpleados.clearContents()
        cursor.execute("select *from cliente")
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
            self.TablaEmpleados_4.setRowCount(tablerow + 1)
            self.TablaEmpleados_4.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.TablaEmpleados_4.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.TablaEmpleados_4.setItem(tablerow,2,QTableWidgetItem(str(rows[9])))
            self.TablaEmpleados_4.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
            self.TablaEmpleados_4.setItem(tablerow,4,QTableWidgetItem(str(rows[2])))
            self.TablaEmpleados_4.setItem(tablerow,5,QTableWidgetItem(str(rows[3])))
            self.TablaEmpleados_4.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
            self.TablaEmpleados_4.setItem(tablerow,7,QTableWidgetItem(str(rows[5])))
            self.TablaEmpleados_4.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
            tablerow+=1
            
    def BuscarCliente(self, cursor):
        self.Eliminar_NombrePaciente_2.clear()
        self.Eliminar_TelefenoPaciente_2.clear()
        self.EliminarFecha_2.clear()
        self.EliminarUltima_2.clear()
        self.EliminarFecha_4.clear()
        self.EliminarUltima_4.clear()
        data=self.ID_BuscarEliminarPaciente_3.text()
        if len(data)==0:
            self.msgError("Busqueda no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarRegistradosCombobox_7.currentText()
            if opc == "Buscar por ID:":
                SQL="""select * from cliente where cast(id_cliente as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese ID")
                else:
                    for rows in row:
                        self.Eliminar_NombrePaciente_2.setText(str(rows[1]))
                        self.Eliminar_TelefenoPaciente_2.setText(str(rows[2]))
                        self.EliminarFecha_2.setText(str(rows[3]))
                        self.EliminarUltima_2.setText(str(rows[4]))
                        self.EliminarFecha_4.setText(str(rows[5]))
                        self.EliminarUltima_4.setText(str(rows[6]))
            else:
                SQL="""select * from cliente where nombre_cliente like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe cliente registrado con ese Nombre")
                else:
                    for rows in row:
                        self.Eliminar_NombrePaciente_2.setText(str(rows[1]))
                        self.Eliminar_TelefenoPaciente_2.setText(str(rows[2]))
                        self.EliminarFecha_2.setText(str(rows[3]))
                        self.EliminarUltima_2.setText(str(rows[4]))
                        self.EliminarFecha_4.setText(str(rows[5]))
                        self.EliminarUltima_4.setText(str(rows[6]))
        
        
    def EliminarCliente(self, cursor):
        data = self.ID_BuscarEliminarPaciente_3.text()
        if len(data)==0:
            self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de eliminar")
        else:
            opc = self.BuscarRegistradosCombobox_7.currentText()
            if opc == "Buscar por Nombre:":
                SQL="""select * from cliente where nombre_cliente like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de eliminar")
                else:
                    for rows in row:
                        id = str(rows[0])
                    SQL='''delete from cliente where id_cliente='{}' '''.format(id)   
                    try:
                        cursor.execute(SQL)     
                        cursor.connection.commit()
                    except Exception as ex:
                        print(ex)
                    self.Eliminar_NombrePaciente_2.clear()
                    self.Eliminar_TelefenoPaciente_2.clear()
                    self.EliminarFecha_2.clear()
                    self.EliminarUltima_2.clear()
                    self.EliminarFecha_4.clear()
                    self.EliminarUltima_4.clear()
            else:
                SQL='''delete from cliente where id_cliente='{}' '''.format(data)   
                try:
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                except Exception as ex:
                    print(ex)
                self.Eliminar_NombrePaciente_2.clear()
                self.Eliminar_TelefenoPaciente_2.clear()
                self.EliminarFecha_2.clear()
                self.EliminarUltima_2.clear()
                self.EliminarFecha_4.clear()
                self.EliminarUltima_4.clear()
    
    """
    CRUD Productos
    
    """
    def registrarMembresia(self, cursor):
        nombre = "Membresia"
        categoria = "Membresia"
        meses=self.lineEdit_38.text()
        precio=self.lineEdit_35.text()
        descripcion=self.lineEdit_16.text()
        if len(meses)==0:
            self.msgError("Falta de informacion", "Debes ingresar los meses de duracion de la membresia")
        elif (len(precio)==0) or ((float(precio)) < 1):
            self.msgError("Falta de informacion", "Debes ingresar el precio correcto de la membresia")
        elif len(descripcion)==0:
            self.msgError("Falta de informacion", "Debes ingresar una descripcion a la membresia")
        else:
            sql="insert into inventario(nombre_material,cantidad,categoria,precio,descripcion_material)\
                values('"+nombre+"','"+meses+"','"+categoria+"','"+precio+"','"+descripcion+"')"
            print(sql)
            try:
                cursor.execute(sql)
                cursor.connection.commit()
            except Exception as ex:
                print(ex)
            self.lineEdit_38.clear()
            self.lineEdit_35.clear()
            self.lineEdit_16.clear()
    
    def registrarProducto(self,cursor):
        nombre=self.NombreRegistrar_12.text()
        cantidad=self.lineEdit_21.text()
        distribui=self.lineEdit_22.text()
        lote=self.lineEdit_31.text()
        categoria=self.comboBox.currentText()
        precio=self.lineEdit_24.text()
        caducidad=self.dateEdit.text()
        descripcion=self.lineEdit_14.text()
        foto=self.label_156.pixmap()
        sql1="SELECT * FROM inventario ORDER BY codigo DESC LIMIT 1;"
        cursor.execute(sql1)
        row=cursor.fetchall()
        print(row)
        if (len(row)) == 0:
            codigo = 1
        else:
            for rows in row:
                codigo = (rows[0])+1
        print("hola" +str(codigo))
        if not QFile.exists("Fotos"):
            makedirs("Fotos") 
        print("Sexo")
        foto.save("Fotos/{}.png".format(codigo), quality = 100) 
        direccionfoto="Fotos/{}.png".format(codigo)
        
        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre para poder registrar un producto")
        elif len(cantidad)==0:
            self.msgError("Falta de informacion", "Debes ingresar la cantidad para registrar un producto")
        elif len(distribui)==0:
            self.msgError("Falta de informacion", "Debes ingresar el distribuidor para registrar un producto")
        elif len(lote)==0:
            self.msgError("Falta de informacion", "Debes ingresar el lote para registrar un producto")
        elif len(categoria)==0:
            self.msgError("Falta de informacion", "Debes ingresar la categoria para registrar un producto")
        elif len(precio)==0:
            self.msgError("Falta de informacion", "Debes ingresar el precio para registrar un producto")
        elif len(caducidad)==0:
            self.msgError("Falta de informacion", "Debes ingresar la caducidad para registrar un producto")
        elif len(descripcion)==0:
            self.msgError("Falta de informacion", "Agrega una descripcion al producto para continuar")
        else: 
            sql="insert into inventario(nombre_material,cantidad,distribuidor,lote_material,categoria,precio,caducidad,descripcion_material,foto)\
                values('"+nombre+"','"+cantidad+"','"+distribui+"','"+lote+"','"+categoria+"','"+precio+"','"+caducidad+"','"+descripcion+"','"+direccionfoto+"')"
            print(sql)
            try:
                cursor.execute(sql)
                cursor.connection.commit()
            except Exception as ex:
                print(ex)
            self.NombreRegistrar_12.clear()
            self.lineEdit_21.clear()
            self.lineEdit_22.clear()
            self.lineEdit_31.clear()
            self.lineEdit_24.clear()
            self.dateEdit.clear()
            self.lineEdit_14.clear()
            self.label_156.clear()
        
    def buscarActualizarProducto(self,cursor):
        self.NombreActualizarPaciente_11.text()
        self.lineEdit_25.clear()
        self.lineEdit_26.clear()
        self.lineEdit_28.clear()
        self.lineEdit_29.clear()
        self.lineEdit_15.clear()
        data=self.ID_BuscarActualizarPaciente_6.text()
        if len(data)==0:
            self.msgError("Busqueda no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc = self.BuscarPor_13.currentText()
            if opc == "Buscar por Codigo:": 
                sql="select *from inventario where cast(codigo as varchar) like"
                cursor.execute(sql+"'%"+data+"%'")
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe producto registrado con ese codigo")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_11.setText(str(rows[1]))
                        self.lineEdit_25.setText(str(rows[2]))
                        self.lineEdit_26.setText(str(rows[3]))
                        self.lineEdit_30.setText(str(rows[4]))
                        self.comboBox_2.setCurrentText(str(rows[5]))
                        self.lineEdit_28.setText(str(rows[6]))
                        self.lineEdit_29.setText(str(rows[7]))
                        self.lineEdit_15.setText(str(rows[8]))
                        direccionfoto=str(rows[9])
                        foto=QPixmap(direccionfoto)
                        self.label_157.setPixmap(foto)
            else:
                sql="select *from inventario where cast(nombre_material as varchar) like"
                cursor.execute(sql+"'%"+data+"%'")
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe producto registrado con ese nombre")
                else:
                    for rows in row:
                        self.NombreActualizarPaciente_11.setText(str(rows[1]))
                        self.lineEdit_25.setText(str(rows[2]))
                        self.lineEdit_26.setText(str(rows[3]))
                        self.lineEdit_30.setText(str(rows[4]))
                        self.comboBox_2.setCurrentText(str(rows[5]))
                        self.lineEdit_28.setText(str(rows[6]))
                        self.lineEdit_29.setText(str(rows[7]))
                        self.lineEdit_15.setText(str(rows[8]))
                        direccionfoto=str(rows[9])
                        foto=QPixmap(direccionfoto)
                        self.label_157.setPixmap(foto)
                        
    def actualizarProducto(self,cursor):
        data=self.ID_BuscarActualizarPaciente_6.text()
        opc = self.BuscarPor_13.currentText()
        if opc == "Buscar por Nombre:":
            sql="select *from inventario where cast(nombre_material as varchar) like"
            cursor.execute(sql+"'%"+data+"%'")
            row=cursor.fetchall()
            if len(row)==0:
               self.msgError("Busquda", "Debes realizar una busqueda valida primero antes de actualizar")
            else:
                for rows in row:
                    id = str(rows[0])
        else:
            id = data
            if len(id)==0:
                self.msgError("Busquda", "Debes realizar una busqueda primero antes de actualizar")
                return
        nombre=self.NombreActualizarPaciente_11.text()
        cantidad=self.lineEdit_25.text()
        distribui=self.lineEdit_26.text()
        lote=self.lineEdit_30.text()
        categoria=self.comboBox_2.currentText()
        precio=self.lineEdit_28.text()
        caducidad=self.lineEdit_29.text()
        descripcion=self.lineEdit_15.text()

        foto=self.label_157.pixmap()
        foto.save("Fotos/{}.png".format(id), quality = 100)  
        direccionfoto="Fotos/{}.png".format(id)

        if len(nombre)==0:
            self.msgError("Falta de informacion", "Debes ingresar un nombre para poder registrar un producto")
        elif len(cantidad)==0:
            self.msgError("Falta de informacion", "Debes ingresar la cantidad para registrar un producto")
        elif len(distribui)==0:
            self.msgError("Falta de informacion", "Debes ingresar el distribuidor para registrar un producto")
        elif len(lote)==0:
            self.msgError("Falta de informacion", "Debes ingresar el lote para registrar un producto")
        elif len(categoria)==0:
            self.msgError("Falta de informacion", "Debes ingresar la categoria para registrar un producto")
        elif len(precio)==0:
            self.msgError("Falta de informacion", "Debes ingresar el precio para registrar un producto")
        elif len(caducidad)==0:
            self.msgError("Falta de informacion", "Debes ingresar la caducidad para registrar un producto")
        elif len(descripcion)==0:
            self.msgError("Falta de informacion", "Agrega una descripcion al producto para continuar")
        else:
            sql="""update inventario set nombre_material='{}',cantidad='{}',distribuidor='{}',lote_material='{}',categoria='{}',
            precio='{}',caducidad='{}',descripcion_material='{}' where codigo='{}'""".format(nombre,cantidad,distribui,lote,categoria,precio,caducidad,descripcion,id)
            print(sql)
            try:
                cursor.execute(sql)
                cursor.connection.commit()
            except Exception as ex:
                print(ex)
            self.NombreActualizarPaciente_11.text()
            self.lineEdit_25.clear()
            self.lineEdit_26.clear()
            self.lineEdit_30.clear()
            self.lineEdit_28.clear()
            self.lineEdit_29.clear()
            self.lineEdit_15.clear()
        
    def buscarEliminarProducto(self,cursor):
        self.Eliminar_NombrePaciente_4.clear()
        self.lineEdit_32.clear()
        self.lineEdit_33.clear()
        self.lineEdit_34.clear()
        data=self.ID_BuscarEliminarPaciente_5.text()
        if len(data)==0:
            self.msgError("Busqued no valida", "Debes Ingresar informacion valida para buscar")
        else:
            opc=self.BuscarRegistradosCombobox_14.currentText()
            if opc == "Buscar por Codigo:": 
                sql="select *from inventario where cast(codigo as varchar) like"
                cursor.execute(sql+"'%"+data+"%'")
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe producto registrado con ese codigo")
                else:
                    for rows in row:
                        self.Eliminar_NombrePaciente_4.setText(str(rows[1]))
                        self.lineEdit_32.setText(str(rows[2]))
                        self.lineEdit_33.setText(str(rows[4]))
                        self.lineEdit_34.setText(str(rows[5]))
            else:
                sql="select *from inventario where cast(nombre_material as varchar) like"
                cursor.execute(sql+"'%"+data+"%'")
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe producto registrado con ese nombre")
                else:
                    for rows in row:
                        for rows in row:
                            self.Eliminar_NombrePaciente_4.setText(str(rows[1]))
                            self.lineEdit_32.setText(str(rows[2]))
                            self.lineEdit_33.setText(str(rows[4]))
                            self.lineEdit_34.setText(str(rows[5]))
        
    def eliminarProducto(self,cursor):
        data=self.ID_BuscarEliminarPaciente_5.text()
        opc=self.BuscarRegistradosCombobox_14.currentText()
        if opc == "Buscar por Nombre:":
            sql="select *from inventario where cast(nombre_material as varchar) like"
            cursor.execute(sql+"'%"+data+"%'")
            row=cursor.fetchall()
            if len(row)==0:
               self.msgError("Busquda", "Debes realizar una busqueda valida primero antes de actualizar")
            else:
                for rows in row:
                    id = str(rows[0])
        else:
            id = data
            if len(id)==0:
                self.msgError("Busquda", "Debes realizar una busqueda primero antes de actualizar")
                return
        nombre=self.Eliminar_NombrePaciente_4.text()
        cantidad=self.lineEdit_32.text()
        lote=self.lineEdit_33.text()
        categoria=self.lineEdit_34.text()
        
        if len(nombre)==0 or len(cantidad)==0 or len(lote)==0 or len(categoria)==0:
            self.msgError("Busqueda", "Debes realizar una busqueda valida primero antes de eliminar")
        else:
            SQL='''delete from inventario where codigo='{}' '''.format(id)   
            try:
                cursor.execute(SQL)     
                cursor.connection.commit()
            except Exception as ex:
                #self.msgError("No fue posible eliminar el empleado", ex)
                print(ex)
            self.Eliminar_NombrePaciente_4.clear()
            self.lineEdit_32.clear()
            self.lineEdit_33.clear()
            self.lineEdit_34.clear()
        
    def mostrarInventario(self,cursor):
        self.TablaEmpleados_8.clearContents()
        cursor.execute("SELECT *FROM inventario")
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
            self.TablaEmpleados_8.setRowCount(tablerow + 1)
            self.TablaEmpleados_8.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.TablaEmpleados_8.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.TablaEmpleados_8.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.TablaEmpleados_8.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.TablaEmpleados_8.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
            self.TablaEmpleados_8.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
            self.TablaEmpleados_8.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
            self.TablaEmpleados_8.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
            self.TablaEmpleados_8.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
            tablerow+=1
    
    def buscarInventario(self,cursor):
        data=self.BuscarRegistradosPacientesText_8
        self.TablaEmpleados_8.clearContents()
        self.TablaEmpleados_8.setRowCount(0)
        if len(data)==0:
            self.msgError("Busqueda", "Debes ingresar informacion antes de buscar")
        else:
            opc=self.BuscarRegistradosCombobox_13.currentText()
            if opc == "Buscar por Nombre:":
                SQL="""select *from inventario where nombre_material like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese producto")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_8.setRowCount(tablerow + 1)
                        self.TablaEmpleados_8.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_8.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_8.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_8.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_8.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_8.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_8.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_8.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        self.TablaEmpleados_8.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            elif opc == "Buscar por Codigo:":
                SQL="""select *from inventario where cast(codigo as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese codigo de producto")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados.setRowCount(tablerow + 1)
                        self.TablaEmpleados.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        self.TablaEmpleados.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
                        tablerow+=1
            else:
                self.msgError("Seleccion", "Selecciona un modo de busqueda")
        
    def refrescarInvenatario(self,cursor):
        self.TablaEmpleados_8.clearContents()
        cursor.execute("SELECT *FROM inventario")
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
            self.TablaEmpleados_8.setRowCount(tablerow + 1)
            self.TablaEmpleados_8.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.TablaEmpleados_8.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.TablaEmpleados_8.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.TablaEmpleados_8.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.TablaEmpleados_8.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
            self.TablaEmpleados_8.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
            self.TablaEmpleados_8.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
            self.TablaEmpleados_8.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
            self.TablaEmpleados_8.setItem(tablerow,8,QTableWidgetItem(str(rows[8])))
            tablerow+=1
    
    def seleccionarFoto(self,cursor):
        global filename
        filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        imagen = cv2.imread(filename)
        frame = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
        self.label_156.setPixmap(QtGui.QPixmap.fromImage(imagen))
        
    def seleccionarNuevaFoto(self,cursor):
        global filename
        filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        imagen = cv2.imread(filename)
        frame = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        imagen = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        imagen = imagen.scaled(400, 280, Qt.KeepAspectRatio)
        self.label_157.setPixmap(QtGui.QPixmap.fromImage(imagen))
    
    """
    Punto de venta productos y membresia
    """       
    def limpiaVar(self):
        self.lineEdit_55.clear()
        self.lineEdit_52.clear()
        self.lineEdit_54.clear()
        self.lineEdit_53.clear()
        self.tableWidget_6.setRowCount(0)
        self.lineEdit_57.clear()
        self.lineEdit_58.clear()
        self.lineEdit_56.clear()
        self.lineEdit_51.clear()

        self.lineEdit_7.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.tableWidget.setRowCount(0)
        self.lineEdit_5.clear()
        self.lineEdit_8.clear()
        self.lineEdit_6.clear()
        self.lineEdit_9.clear()
        
        self.vencimientoClient=""
        self.idcliente=0
        self.carrito.clear()

    def buscarProductoVenta(self, cursor):
        data = self.lineEdit_5.text()
        if (len(data)) ==0:
            self.msgError("Ingresa informacion valida", "Debes ingresar un ID para realizar una busqueda")
        else:
            SQL="""select codigo, nombre_material, cantidad, precio from inventario where codigo='{}' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de producto")
            else:
                for rows in row:
                    
                    self.lineEdit_8.setText(str(rows[1]))
                    self.lineEdit_6.setText(str(rows[2]))
                    self.lineEdit_9.setText(str(rows[3]))
                         
    def agregarProductoVenta(self, cursor):
        #Validacion de la cantidad a vender
        cantidad  = self.lineEdit_7.text()
        data = self.lineEdit_8.text()
        if data == "Membresia":
            self.msgError("Membresia", "No puedes agregar membresias al carrito de ventas, para ello es necesario acceder a venta membresias")
            return 


        if ((len(cantidad)) == 0) or (int(cantidad) < 1):
            self.msgError("Cantidad no especificada", "Necesitas indicar correctamente la cantidad de productos que quieres vender")
            return
        
        prec = 0;
        
        #Busco y obtengo los datos del producto
        if (len(data)) ==0:
            self.msgError("Busqueda", "Debes realizar la busqueda del producto primero")
            return
        else:
            SQL="""select codigo, nombre_material, cantidad, precio from inventario where codigo='{}' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de producto")
            else:
                for rows in row:
                    
                    self.lineEdit_8.setText(str(rows[1]))
                    self.lineEdit_6.setText(str(rows[2]))
                    self.lineEdit_9.setText(str(rows[3]))
                    codigo = rows[0]
                    nombre = rows[1]
                    precio=float(rows[3])
                    inv=int(rows[2])
                    
        caritem = False
        if (len(self.carrito)) != 0:
            for car in self.carrito:
                if car[0] == codigo:
                    caritem = True
                    inv=inv-int(car[2])
                    
        if int(inv) < int(cantidad):
            self.msgError("Sin inventario :(", "Desafortunadamente no se cuenta con el inventario suficiente para dicha cantidad")
            return
        
        prec = precio * float(cantidad);
        
        desc = self.lineEdit_10.text()
        if (len(desc)) != 0:
            if (int(desc)) <0:
                self.msgError("Descuento", "La cantidad rebajada en el descuento debe ser ingresada en positivo")
                return
            else:
                prec = float(prec) - float(desc) 
                
                
        self.lineEdit_11.setText(str(prec))
        print(caritem)
        if caritem == True:
            for car in self.carrito:
                if car[0] == codigo:
                    car[2] = int(car[2]) + int(cantidad)
                    car[4] = float(car[4]) + float(prec)
        else:    
            self.carrito.append([codigo, nombre, cantidad, precio, prec])
        
        tablerow = 0
        for rows in self.carrito:
            print(rows)
            self.tableWidget.setRowCount(tablerow + 1)
            self.tableWidget.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.tableWidget.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.tableWidget.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.tableWidget.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.tableWidget.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
            tablerow+=1
            
        #print(self.carrito)
        
        self.CantidadTotal = float(self.CantidadTotal) + prec
        self.lineEdit_12.setText(str(self.CantidadTotal))
        
    def cancelarVentaProducto(self):
        self.lineEdit_7.clear()
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_12.clear()
        self.tableWidget.setRowCount(0)
        self.lineEdit_5.clear()
        self.lineEdit_8.clear()
        self.lineEdit_6.clear()
        self.lineEdit_9.clear()
        
        self.carrito.clear()
        self.CantidadTotal=0.0
        
    def realizarVentaProducto(self, cursor):
        if (len(self.carrito))!=0:
            
            self.lineEdit_7.clear()
            self.lineEdit_10.clear()
            self.lineEdit_11.clear()
            self.lineEdit_12.clear()
            self.tableWidget.setRowCount(0)
            self.lineEdit_5.clear()
            self.lineEdit_8.clear()
            self.lineEdit_6.clear()
            self.lineEdit_9.clear()
            
            self.lineEdit_13.clear()
            self.stackedWidget.setCurrentWidget(self.VentaTicket)
            self.Tota_label.setText("$" + str(self.CantidadTotal))
            self.label_141.setText("$" + str(self.CantidadTotal))
            tablerow = 0
            for rows in self.carrito:
                print(rows)
                self.tableWidget_2.setRowCount(tablerow + 1)
                self.tableWidget_2.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                self.tableWidget_2.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                self.tableWidget_2.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                self.tableWidget_2.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                self.tableWidget_2.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                tablerow+=1
            self.opc=0
        else:
            self.msgError("Venta no posbible", "Primero deberas agregar productos a tu carrito antes de realizar una venta")
    
    def getFolio(self, cursor):
        SQL="select folio from venta"
        cursor.execute(SQL)
        data=cursor.fetchall()
        if (len(data)) == 0:
            self.folio += 1
            
        else:
            for row in data:
                fol=row[0]
            self.folio = int(fol) + 1
        self.lineEdit_3.setText(str(self.folio))
    
    def generarTicket(self, cursor, date, name, opc):
        data = self.lineEdit_13.text()
        print(opc)
        if (len(data)) == 0:
            self.msgError("Cantidad pagada", "Debes ingresar la cantidad pagada por el cliente para continuar")
        elif float(data) < 0:
            self.msgError("Cantidad no valida", "Debes ingresar una cantidad valida pagada por el cliente para continuar")
        elif float(data) < self.CantidadTotal:
            self.msgError("Cantidad no valida", "El cliente no puede pagar menos de la cantidad total")
        else:
            cantidad = float(self.CantidadTotal)
            data = float(data) - cantidad
            msg = "$"+str(data)
            self.Tota_label_3.setText(msg)
            tablerow = 0
            for rows in self.carrito:
                print(rows)
                if opc == 0 :
                    
                    self.tableWidget_3.setRowCount(tablerow + 1)
                    self.tableWidget_3.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                    self.tableWidget_3.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                    self.tableWidget_3.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                    self.tableWidget_3.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                    self.tableWidget_3.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
                    
                    
                    SQL=""" insert into venta (folio, codigo_producto, nombre_producto, cantidad, precio, total, fecha, vendedor) values ('{}','{}','{}','{}','{}','{}','{}','{}'); """.format(self.folio, rows[0], rows[1], rows[2], rows[3], rows[4], str(date), name)
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                    
                    SQL="""select cantidad from inventario where codigo='{}' """.format(rows[0])
                    cursor.execute(SQL)
                    cant=cursor.fetchall()
                    for row in cant:
                        invact = row[0]
                    invact = int(invact) - int(rows[2])
                    
                    SQL = """ update inventario set cantidad='{}' where codigo='{}' """.format(invact, rows[0])
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                else:
                    self.tableWidget_3.setRowCount(tablerow + 1)
                    self.tableWidget_3.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                    self.tableWidget_3.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                    self.tableWidget_3.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                    self.tableWidget_3.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                    self.tableWidget_3.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                    
                    
                    SQL=""" insert into venta (folio, codigo_producto, nombre_producto, cantidad, precio, total, fecha, vendedor) values ('{}','{}','{}','{}','{}','{}','{}','{}'); """.format(self.folio, rows[0], rows[1], rows[3], rows[4], rows[5], str(date), name)
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                    
                    venci = str(self.vencimientoClient)
                    ano = venci[:4]
                    mes = venci[5:7]
                    dia = venci[8:11]
                    venc = datetime.datetime(int(ano), int(mes), int(dia))
                    today = datetime.datetime.today()
                    
                    if venc > today:
                        venc = venc + relativedelta(months=int(rows[2]))
                    else:
                        venc = today + relativedelta(months=int(rows[2]))
                    msg="Activa"
                    SQL = """ update cliente set Fecha_Vencimiento='{}', situacion_membresia='{}' where ID_cliente='{}' """.format(venc, msg, str(self.idcliente))
                    cursor.execute(SQL)     
                    cursor.connection.commit()
                
                tablerow+=1
            
            self.FechaTicket.setText(("Fecha: "+date))
            self.label_149.setText(("Folio: "+str(self.folio)))
            self.label_144.setText(("$"+str(self.CantidadTotal)))
            self.carrito.clear()
            self.CantidadTotal=0.0
            self.folio=0
    
    def buscarMembresiaVenta(self, cursor):
        data = self.lineEdit_55.text()
        if (len(data)) ==0:
            self.msgError("Ingresa informacion valida", "Debes ingresar un ID para realizar una busqueda")
        else:
            SQL="""select codigo, nombre_material, cantidad, precio from inventario where codigo='{}' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe coincidencia con ese ID de producto")
            else:
                for rows in row:
                    name=str(rows[1])
                    print(name)
                    if (name != "Membresia"): 
                        self.msgError("Producto no valido", "Debes buscar un tipo de membresia registrado o registrar uno")
                        return
                    self.lineEdit_52.setText(str(rows[1]))
                    meses=(str(rows[2])+" meses")
                    self.lineEdit_54.setText(meses)
                    self.lineEdit_53.setText(str(rows[3]))
       
    def agregarMembresiaVenta(self, cursor):
        #Validacion de la cantidad a vender
        cantidad  = 1
        id = self.lineEdit_57.text()
        
        data = self.lineEdit_55.text()
        prec = 0;
        
        #Busco y obtengo los datos del producto
        if (len(data)) ==0:
            self.msgError("Busqueda", "Debes realizar la busqueda de la membresia primero")
            return
        elif (len(id)) ==0:
            self.msgError("Id no valido", "Debes ingresar un id de cliente para despues asignarle la membresia")
        else:
            SQL="""select codigo, nombre_material, cantidad, precio from inventario where codigo='{}' """.format(data)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe coincidencia con ese ID")
            else:
                for rows in row:
                    
                    name=str(rows[1])
                    print(name)
                    if (name != "Membresia"): 
                        self.msgError("Producto no valido", "Debes buscar un tipo de membresia registrado o registrar uno")
                        return
                    self.lineEdit_52.setText(str(rows[1]))
                    meses=(str(rows[2])+" meses")
                    self.lineEdit_54.setText(meses)
                    self.lineEdit_53.setText(str(rows[3]))
                    
                    codigo = rows[0]
                    precio=float(rows[3])
                    inv=int(rows[2])
                    
        
        if (len(self.carrito)) != 0:
            self.msgError("1 a la vez", "Solo puedes realizar la venta de una membresia a la vez")
            return
        prec =precio 
        desc = self.lineEdit_58.text()
        if (len(desc)) != 0:
            if (int(desc)) <0:
                self.msgError("Descuento", "La cantidad rebajada en el descuento debe ser ingresada en positivo")
            else:
                prec = float(prec) - float(desc) 
                
                
        self.lineEdit_56.setText(str(prec))
       
        
        self.carrito.append([codigo, name, inv, cantidad,precio, prec])
        
        tablerow = 0
        for rows in self.carrito:
            print(rows)
            self.tableWidget_6.setRowCount(tablerow + 1)
            self.tableWidget_6.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.tableWidget_6.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.tableWidget_6.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.tableWidget_6.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.tableWidget_6.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
            self.tableWidget_6.setItem(tablerow,5,QTableWidgetItem(str(rows[5])))
            tablerow+=1
            
        #print(self.carrito)
        
        self.CantidadTotal = float(self.CantidadTotal) + prec
        self.lineEdit_51.setText(str(self.CantidadTotal))
    
    def cancelarMembresiaVenta(self):
        self.lineEdit_55.clear()
        self.lineEdit_52.clear()
        self.lineEdit_54.clear()
        self.lineEdit_53.clear()
        self.tableWidget_6.setRowCount(0)
        self.lineEdit_57.clear()
        self.lineEdit_58.clear()
        self.lineEdit_56.clear()
        self.lineEdit_51.clear()
        
        self.carrito.clear()
        self.CantidadTotal=0.0
      
    def realizarVentaMembresia(self, cursor):
        id = self.lineEdit_57.text() 
        if (len(id)) == 0:
            self.msgError("Venta no posbible", "Primero deberas ingresar un id")
            return
        else:
            SQL="""select Nombre_Cliente, Fecha_Vencimiento from cliente where ID_cliente='{}' """.format(id)
            cursor.execute(SQL)
            row=cursor.fetchall()
            if len(row)==0:
                self.msgError("Sin coincidencia", "No existe coincidencia con ese ID, debes ingresar un cliente ya registrado")
                return
            else:
                for rows in row:
                    self.nameclient=rows[0]
                    self.vencimientoClient=rows[1]
                self.idcliente=id
                
        if (len(self.carrito))!=0:
            
            self.lineEdit_55.clear()
            self.lineEdit_52.clear()
            self.lineEdit_54.clear()
            self.lineEdit_53.clear()
            self.tableWidget_6.setRowCount(0)
            self.lineEdit_57.clear()
            self.lineEdit_58.clear()
            self.lineEdit_56.clear()
            self.lineEdit_51.clear()
            
            self.FechaTicket.clear()
            self.label_149.clear()
            self.label_144.setText("$")
            self.tableWidget_3.setRowCount(0)
            
            self.lineEdit_13.clear()
            self.stackedWidget.setCurrentWidget(self.VentaTicket)
            self.Tota_label.setText("$" + str(self.CantidadTotal))
            self.label_141.setText("$" + str(self.CantidadTotal))
            tablerow = 0
            for rows in self.carrito:
                print(rows)
                self.tableWidget_2.setRowCount(tablerow + 1)
                self.tableWidget_2.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                self.tableWidget_2.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                self.tableWidget_2.setItem(tablerow,2,QTableWidgetItem(str(rows[3])))
                self.tableWidget_2.setItem(tablerow,3,QTableWidgetItem(str(rows[4])))
                self.tableWidget_2.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                tablerow+=1
            self.opc=1
        else:
            self.msgError("Venta no posbible", "Primero deberas agregar productos a tu carrito antes de realizar una venta")
    
    def mostrarVentas(self, cursor):
        self.TablaEmpleados_7.clearContents()
        cursor.execute("SELECT *FROM venta")
        row=cursor.fetchall()
        tablerow = 0
        for rows in row:
            self.TablaEmpleados_7.setRowCount(tablerow + 1)
            self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
            self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
            self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
            self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
            self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[4])))
            self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[5])))
            self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
            self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
            tablerow+=1
    
    def buscarVentas(self, cursor):
        data = self.BuscarRegistradosPacientesText_7.text()
        self.TablaEmpleados_7.clearContents()
        self.TablaEmpleados_7.setRowCount(0)
        if len(data)==0:
            self.msgError("Busqueda", "Debes ingresar informacion antes de buscar")
        else:
            opc=self.BuscarRegistradosCombobox_10.currentText()
            if opc == "Buscar por Nombre:":
                SQL="""select *from venta where nombre_producto like '%{}%' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese producto")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_7.setRowCount(tablerow + 1)
                        self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
            elif opc == "Buscar por ID venta:":
                SQL="""select *from venta where cast(folio as varchar)='{}' """.format(data)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin coincidencia", "No existe coincidencia con ese codigo de producto")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_7.setRowCount(tablerow + 1)
                        self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
            else:
                self.msgError("Seleccion", "Selecciona un modo de busqueda")
        
    def refrescarVentas(self, cursor):
        opc = self.BuscarRegistradosCombobox_11.currentText()
        self.TablaEmpleados_7.clearContents()
        self.TablaEmpleados_7.setRowCount(0)
        if opc == "Ordenar por ID":
                SQL="select *from venta order by folio "
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin elementos", "No hay ventas realizadas aun")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_7.setRowCount(tablerow + 1)
                        self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
        elif opc == "Ordenar por fecha":
                SQL="select *from venta order by fecha "
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin elementos", "No hay ventas realizadas aun")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_7.setRowCount(tablerow + 1)
                        self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1
        elif opc == "Ordenar por cantidad":
                SQL="select *from venta order by cantidad "
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                    self.msgError("Sin elementos", "No hay ventas realizadas aun")
                else:
                    tablerow = 0
                    for rows in row:
                        self.TablaEmpleados_7.setRowCount(tablerow + 1)
                        self.TablaEmpleados_7.setItem(tablerow,0,QTableWidgetItem(str(rows[0])))
                        self.TablaEmpleados_7.setItem(tablerow,1,QTableWidgetItem(str(rows[1])))
                        self.TablaEmpleados_7.setItem(tablerow,2,QTableWidgetItem(str(rows[2])))
                        self.TablaEmpleados_7.setItem(tablerow,3,QTableWidgetItem(str(rows[3])))
                        self.TablaEmpleados_7.setItem(tablerow,4,QTableWidgetItem(str(rows[5])))
                        self.TablaEmpleados_7.setItem(tablerow,5,QTableWidgetItem(str(rows[4])))
                        self.TablaEmpleados_7.setItem(tablerow,6,QTableWidgetItem(str(rows[6])))
                        self.TablaEmpleados_7.setItem(tablerow,7,QTableWidgetItem(str(rows[7])))
                        tablerow+=1

    """
    Registrar visita
    """
    def buscarVisita(self, cursor, date):
        id = self.plainTextEdit.toPlainText()
        if (len(id)) != 0:
                SQL="""select Nombre_Cliente, fecha_Vencimiento from cliente where ID_cliente='{}' """.format(id)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                        self.msgError("Sin coincidencia", "No existe coincidencia con ese ID, debes ingresar un cliente ya registrado")
                        return
                else:
                        for rows in row:
                                self.plainTextEdit_2.setPlainText(rows[0])
                                venci = str(rows[1])
                self.plainTextEdit_3.setPlainText(date)
                ano = venci[:4]
                mes = venci[5:7]
                dia = venci[8:11]
                print(venci)
                venc = datetime.datetime(int(ano), int(mes), int(dia))
                venci =datetime.datetime.strftime(venc, '%d/%m/%Y')
                print("Vencimiento: "+str(venc))
                today = datetime.datetime.today()
                if today >= venc:
                        resta = today - venc
                        msg ="Tu membresia vencio hace "+str(resta.days)+" dias el dia "+str(venci)
                        self.label_12.setText(msg)
                        self.msgError("Membresia vencida", "La membresia del cliente ha vencido")
                else:
                        resta = venc - today
                        msg ="Tu membresia vencera en "+str(resta.days)+" dias el dia "+str(venci)
                        self.label_12.setText(msg)

        else:
                self.msgError("Busqueda", "Debes ingresar un ID para poder buscar")
                return
    
    def registrarVisita(self, cursor):
        fechaActual = datetime.datetime.now()
        fecha = datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
        hora = str(fechaActual.hour) + ":"+ str(fechaActual.minute)+":"+str(fechaActual.second)
        id = self.plainTextEdit.toPlainText()
        if (len(id)) != 0:
                SQL="""select Nombre_Cliente, situacion_Membresia from cliente where ID_cliente='{}' """.format(id)
                cursor.execute(SQL)
                row=cursor.fetchall()
                if len(row)==0:
                        self.msgError("Sin coincidencia", "No existe coincidencia con ese ID, debes ingresar un cliente ya registrado")
                        return
                else:
                        for rows in row:
                                name = rows[0]
                                status = rows[1]
                
                if status == "Vencida":
                        self.msgError("Membresia Vencida", "No se puede registrar visita de un cliente con una membresia vencida")
                        return
                print("Fecha: "+str(fecha)+" Hora: "+hora+" id= "+id+" Nombre: "+name)
                SQL=""" insert into visita (id, Nombre_Cliente, fecha, hora) values ('{}','{}','{}','{}'); """.format(id,name,fecha,hora)
                cursor.execute(SQL)     
                cursor.connection.commit()
                self.limpiarVisita()
                self.msgError("Visita Registrada", "Visita Registrada correctamente")
                return
        else:
                self.msgError("Busqueda", "Debes iprimero buscar un ID para poder registrar visita")
                return

    def limpiarVisita(self):
        self.label_12.setText("Tu membresía vence en: 00 dias.")
        self.plainTextEdit.clear()
        self.plainTextEdit_2.clear()
        self.plainTextEdit_3.clear()

    """
    Otros
    """ 
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        x = msg.exec_()
    
    def truncate(self, number: float, max_decimals: int) -> float:
        int_part, dec_part = str(number).split(".")
        return float(".".join((int_part, dec_part[:max_decimals])))


    def retranslateUi(self, MenuEmpleados):
        _translate = QtCore.QCoreApplication.translate
        MenuEmpleados.setWindowTitle(_translate("MenuEmpleados", "Empleados Teflon Academy"))
        self.label_4.setText(_translate("MenuEmpleados", "Teflon Academy"))
        self.label_131.setText(_translate("MenuEmpleados", "Teflon Academy by GoldenSharks"))
        self.label_Bienvenida.setText(_translate("MenuEmpleados", "Bienvenido ....!"))
        self.label_13.setText(_translate("MenuEmpleados", "Registrar visita"))
        self.label_15.setText(_translate("MenuEmpleados", "Punto de venta"))
        self.label_137.setText(_translate("MenuEmpleados", "Administrar Entrenadores"))
        self.label_135.setText(_translate("MenuEmpleados", "Administrar Clientes"))
        self.label_Bienvenida_2.setText(_translate("MenuEmpleados", "¡Bienvenido al punto de venta!"))
        self.label_127.setText(_translate("MenuEmpleados", "Realizar venta"))
        self.label_128.setText(_translate("MenuEmpleados", "Administrar inventario"))
        self.label_130.setText(_translate("MenuEmpleados", "Reporte de ventas"))
        self.label_70.setText(_translate("MenuEmpleados", "ID Usuario:"))
        self.label_86.setText(_translate("MenuEmpleados", "Nombre:"))
        self.radioButton.setText(_translate("MenuEmpleados", "Punto de venta"))
        self.radioButton_2.setText(_translate("MenuEmpleados", "Inventario"))
        self.radioButton_3.setText(_translate("MenuEmpleados", "Ventas"))
        self.radioButton_4.setText(_translate("MenuEmpleados", "Membresía"))
        self.label_82.setText(_translate("MenuEmpleados", "Folio de venta:"))
        self.label_73.setText(_translate("MenuEmpleados", "Fecha:"))
        self.label_106.setText(_translate("MenuEmpleados", "Venta de productos"))
        self.label_120.setText(_translate("MenuEmpleados", "Precio:"))
        self.label_116.setText(_translate("MenuEmpleados", "Cantidad en stock:"))
        self.label_115.setText(_translate("MenuEmpleados", "Nombre producto:"))
        self.label_112.setText(_translate("MenuEmpleados", "Código producto:"))
        self.pushButton_7.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_119.setText(_translate("MenuEmpleados", "Cantidad a vender:"))
        self.label_122.setText(_translate("MenuEmpleados", "Total:"))
        self.label_121.setText(_translate("MenuEmpleados", "Descuento:"))
        self.pushButton_8.setText(_translate("MenuEmpleados", "Agregar"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "Codigo"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Total"))
        self.label_113.setText(_translate("MenuEmpleados", "Resumen"))
        self.label_114.setText(_translate("MenuEmpleados", "Total a pagar: "))
        self.pushButton_9.setText(_translate("MenuEmpleados", "Cancelar venta"))
        self.pushButton_10.setText(_translate("MenuEmpleados", "Realizar Venta"))
        self.label_67.setText(_translate("MenuEmpleados", "Cantidad:"))
        self.label_37.setText(_translate("MenuEmpleados", "Distribuidor:"))
        self.label_60.setText(_translate("MenuEmpleados", "Categoria:"))
        self.label_163.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_164.setText(_translate("MenuEmpleados", "Precio:"))
        self.label_26.setText(_translate("MenuEmpleados", "Caducidad:"))
        self.label_129.setText(_translate("MenuEmpleados", "Descripción:"))
        self.label_171.setText(_translate("MenuEmpleados", "Lote:"))
        self.GuardarRegistrarPaciente_5.setText(_translate("MenuEmpleados", "Registrar"))
        self.label_155.setText(_translate("MenuEmpleados", "Foto del producto:"))
        self.pushButton_13.setText(_translate("MenuEmpleados", "Seleccionar foto del producto"))
        self.comboBox.setItemText(0, _translate("MenuEmpleados", "Suplementos"))
        self.comboBox.setItemText(1, _translate("MenuEmpleados", "Membresías"))
        self.comboBox.setItemText(2, _translate("MenuEmpleados", "Consumibles"))
        self.comboBox.setItemText(3, _translate("MenuEmpleados", "Accesorios"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_20), _translate("MenuEmpleados", "Registrar producto"))
        self.label_14.setText(_translate("MenuEmpleados", "Cantidad:"))
        self.label_133.setText(_translate("MenuEmpleados", "Descripción"))
        self.label_69.setText(_translate("MenuEmpleados", "Categoria:"))
        self.label_162.setText(_translate("MenuEmpleados", "Precio:"))
        self.pushButton_16.setText(_translate("MenuEmpleados", "Seleccionar nueva foto del producto"))
        self.label_59.setText(_translate("MenuEmpleados", "Distribuidor:"))
        self.label_167.setText(_translate("MenuEmpleados", "Caducidad:"))
        self.label_166.setText(_translate("MenuEmpleados", "Nombre:"))
        self.BuscarBotonActualizar_9.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarPor_13.setItemText(0, _translate("MenuEmpleados", "Buscar por Codigo:"))
        self.BuscarPor_13.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.label_165.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Actualiza la información del producto necesaria:</span></p></body></html>"))
        self.ActualizarBotonPaciente_6.setText(_translate("MenuEmpleados", "Actualizar"))
        self.label_170.setText(_translate("MenuEmpleados", "Lote:"))
        self.label_158.setText(_translate("MenuEmpleados", "Foto del producto:"))
        self.comboBox_2.setItemText(0, _translate("MenuEmpleados", "Suplementos"))
        self.comboBox_2.setItemText(1, _translate("MenuEmpleados", "Membresías"))
        self.comboBox_2.setItemText(2, _translate("MenuEmpleados", "Consumibles"))
        self.comboBox_2.setItemText(3, _translate("MenuEmpleados", "Accesorios"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_21), _translate("MenuEmpleados", "Actualizar producto"))
        self.label_172.setText(_translate("MenuEmpleados", "Costo:"))
        self.label_168.setText(_translate("MenuEmpleados", "Cantidad:"))
        self.label_169.setText(_translate("MenuEmpleados", "Lote:"))
        self.label_178.setText(_translate("MenuEmpleados", "Datos del producto encontrados:"))
        self.label_174.setText(_translate("MenuEmpleados", "Nombre:"))
        self.BuscarBotonEliminar_5.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarRegistradosCombobox_14.setItemText(0, _translate("MenuEmpleados", "Buscar por Codigo:"))
        self.BuscarRegistradosCombobox_14.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.EliminarPacienteBoton_5.setText(_translate("MenuEmpleados", "Eliminar prodcuto"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_23), _translate("MenuEmpleados", "Elminar producto"))
        self.NombreRegistrar_13.setText(_translate("MenuEmpleados", "Membresia"))
        self.GuardarRegistrarPaciente_6.setText(_translate("MenuEmpleados", "Registrar"))
        self.label_134.setText(_translate("MenuEmpleados", "Categoria:"))
        self.label_173.setText(_translate("MenuEmpleados", "Precio:"))
        self.lineEdit_39.setText(_translate("MenuEmpleados", "Membresia"))
        self.label_153.setText(_translate("MenuEmpleados", "Meses:"))
        self.label_177.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_136.setText(_translate("MenuEmpleados", "Descripción:"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_16), _translate("MenuEmpleados", "Registrar Membresia"))
        self.TablaEmpleados_8.setSortingEnabled(False)
        item = self.TablaEmpleados_8.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "Codigo"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Distribuidor"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Categoria"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "Lote"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(6)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(7)
        item.setText(_translate("MenuEmpleados", "Caducidad"))
        item = self.TablaEmpleados_8.horizontalHeaderItem(8)
        item.setText(_translate("MenuEmpleados", "Descripcion"))
        self.BuscarBotonRegistrados_8.setText(_translate("MenuEmpleados", "Buscar"))
        self.RefrescarBotonRegistrados_6.setText(_translate("MenuEmpleados", "Refrescar"))
        self.BuscarRegistradosCombobox_13.setItemText(0, _translate("MenuEmpleados", "Buscar por Codigo:"))
        self.BuscarRegistradosCombobox_13.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_22), _translate("MenuEmpleados", "Inventario actual"))
        self.BuscarRegistradosCombobox_10.setItemText(0, _translate("MenuEmpleados", "Buscar por ID venta:"))
        self.BuscarRegistradosCombobox_10.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.BuscarRegistradosCombobox_11.setItemText(0, _translate("MenuEmpleados", "Ordenar por ID"))
        self.BuscarRegistradosCombobox_11.setItemText(1, _translate("MenuEmpleados", "Ordenar por fecha"))
        self.BuscarRegistradosCombobox_11.setItemText(2, _translate("MenuEmpleados", "Ordenar por cantidad"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "ID Venta"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Codigo Producto"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "Total"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(6)
        item.setText(_translate("MenuEmpleados", "Fecha venta"))
        item = self.TablaEmpleados_7.horizontalHeaderItem(7)
        item.setText(_translate("MenuEmpleados", "Vendedor"))
        self.label_124.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Ventas</span></p></body></html>"))
        self.pushButton_15.setText(_translate("MenuEmpleados", "Refrescar"))
        self.BuscarBotonRegistrados_7.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_199.setText(_translate("MenuEmpleados", "Tipo de membresía:"))
        self.label_201.setText(_translate("MenuEmpleados", "Código producto:"))
        self.pushButton_37.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_200.setText(_translate("MenuEmpleados", "Nombre producto:"))
        self.label_198.setText(_translate("MenuEmpleados", "Precio:"))
        self.label_202.setText(_translate("MenuEmpleados", "ID del cliente:"))
        self.label_203.setText(_translate("MenuEmpleados", "Total:"))
        self.label_204.setText(_translate("MenuEmpleados", "Descuento:"))
        self.pushButton_38.setText(_translate("MenuEmpleados", "Agregar"))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "Codigo"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Meses"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "Total"))
        self.label_196.setText(_translate("MenuEmpleados", "Resumen"))
        self.label_195.setText(_translate("MenuEmpleados", "Total a pagar: "))
        self.pushButton_31.setText(_translate("MenuEmpleados", "Cancelar venta"))
        self.pushButton_23.setText(_translate("MenuEmpleados", "Realizar Venta"))
        self.label_Bienvenida_3.setText(_translate("MenuEmpleados", "Venta"))
        self.label_9.setText(_translate("MenuEmpleados", "Gimnasio Teflon Academy"))
        self.FechaTicket.setText(_translate("MenuEmpleados", "Fecha: 06/11/2022\n"
""))
        self.label_139.setText(_translate("MenuEmpleados", "RFC:HDGT128745HJCRTA7\n"
"Factura No.3596\n"
"Av. Lopez Mateos #156\n"
"Tel: 3364646565\n"
"Ciudad: Guadalajara\n"
"Ventas"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "Codigo"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Total"))
        self.label_143.setText(_translate("MenuEmpleados", "Total neto"))
        self.label_144.setText(_translate("MenuEmpleados", "Total: $0000.00"))
        self.label_149.setText(_translate("MenuEmpleados", "Folio: 56444654566"))
        self.label_147.setText(_translate("MenuEmpleados", "Pago en una sola Exhibición\n"
"¡Gracias por su compra!"))
        self.pushButton_29.setText(_translate("MenuEmpleados", "Finalizar Venta"))
        self.label_140.setText(_translate("MenuEmpleados", "Total a Pagar:"))
        self.Tota_label.setText(_translate("MenuEmpleados", "$0000.00"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "Codigo"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Cantidad"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Precio"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Total"))
        self.label_142.setText(_translate("MenuEmpleados", "Total"))
        self.label_141.setText(_translate("MenuEmpleados", "Total: 0000.00"))
        self.label_145.setText(_translate("MenuEmpleados", "Cantidad Pagada"))
        self.lineEdit_13.setText(_translate("MenuEmpleados", "00000"))
        self.label_146.setText(_translate("MenuEmpleados", "Dar Cambio:"))
        self.Tota_label_3.setText(_translate("MenuEmpleados", "$0000.0"))
        self.pushButton_28.setText(_translate("MenuEmpleados", "Generar Ticket"))
        self.label_8.setText(_translate("MenuEmpleados", "Información del usuario"))
        self.label_2.setText(_translate("MenuEmpleados", "Ingrese el código del usuario para registrar la visita."))
        self.Buscar_Visita_3.setText(_translate("MenuEmpleados", "Buscar"))
        self.Buscar_Visita_4.setText(_translate("MenuEmpleados", "Registrar visita"))
        self.Buscar_Visita_5.setText(_translate("MenuEmpleados", "Volver al menu"))
        self.label_12.setText(_translate("MenuEmpleados", "Tu membresía vence en: 00 dias."))
        self.label_6.setText(_translate("MenuEmpleados", "ID usuario:"))
        self.label_10.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_11.setText(_translate("MenuEmpleados", "Fecha de hoy:"))
        self.label_48.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_27.setText(_translate("MenuEmpleados", "Fecha de nacimiento:"))
        self.label_28.setText(_translate("MenuEmpleados", "Teléfono:"))
        self.label_46.setText(_translate("MenuEmpleados", "RFC:"))
        self.label_47.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Ingrese la información del entrenador</span></p></body></html>"))
        self.label_23.setText(_translate("MenuEmpleados", "NSS:"))
        self.label_22.setText(_translate("MenuEmpleados", "CURP:"))
        self.label_38.setText(_translate("MenuEmpleados", "Fecha de ingreso:"))
        self.GuardarRegistrarPaciente_2.setText(_translate("MenuEmpleados", "Registrar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MenuEmpleados", "Agregar"))
        self.BuscarBotonActualizar_2.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_51.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_53.setText(_translate("MenuEmpleados", "NSS:"))
        self.label_56.setText(_translate("MenuEmpleados", "Fecha de nacimiento:"))
        self.BuscarPor_7.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarPor_7.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.label_54.setText(_translate("MenuEmpleados", "RFC:"))
        self.label_58.setText(_translate("MenuEmpleados", "CURP:"))
        self.ActualizarBotonPaciente_2.setText(_translate("MenuEmpleados", "Actualizar"))
        self.label_55.setText(_translate("MenuEmpleados", "Fecha de ingreso:"))
        self.label_57.setText(_translate("MenuEmpleados", "Teléfono:"))
        self.label_50.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Actualiza la información del usuario necesaria:</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MenuEmpleados", "Actualizar"))
        self.BuscarBotonRegistrados_2.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarRegistradosCombobox_3.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarRegistradosCombobox_3.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "ID"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Fecha Ingreso"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Edad"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Telefono"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "Correo Electronico"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(6)
        item.setText(_translate("MenuEmpleados", "Altura"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(7)
        item.setText(_translate("MenuEmpleados", "Peso"))
        item = self.TablaEmpleados_2.horizontalHeaderItem(8)
        item.setText(_translate("MenuEmpleados", "Membrecia Actual"))
        self.label_152.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Ingresa el id del entrenador para ver sus clientes asignados</span></p></body></html>"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MenuEmpleados", "Clientes asignados"))
        self.BuscarRegistradosCombobox_5.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarRegistradosCombobox_5.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.BuscarBotonRegistrados_3.setText(_translate("MenuEmpleados", "Buscar"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "ID"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Fecha Ingreso"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Fecha de Nacimineto"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Telefono"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "CURP"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(6)
        item.setText(_translate("MenuEmpleados", "NSS"))
        item = self.TablaEmpleados_3.horizontalHeaderItem(7)
        item.setText(_translate("MenuEmpleados", "RFC"))
        self.RefrescarBotonRegistrados_3.setText(_translate("MenuEmpleados", "Refrescar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MenuEmpleados", "Mostrar"))
        self.BuscarRegistradosCombobox_4.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarRegistradosCombobox_4.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.BuscarBotonEliminar_2.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_66.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Informacion del usuario a eliminar :</span></p></body></html>"))
        self.label_64.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_65.setText(_translate("MenuEmpleados", "Fecha de ingreso:"))
        self.label_52.setText(_translate("MenuEmpleados", "Fecha de nacimiento:"))
        self.label_63.setText(_translate("MenuEmpleados", "Teléfono:"))
        self.label_62.setText(_translate("MenuEmpleados", "CURP:"))
        self.label_61.setText(_translate("MenuEmpleados", "NSS:"))
        self.label_68.setText(_translate("MenuEmpleados", "RFC:"))
        self.EliminarPacienteBoton_2.setText(_translate("MenuEmpleados", "Eliminar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MenuEmpleados", "Elminar"))
        self.label_49.setText(_translate("MenuEmpleados", "Edad:"))
        self.label_71.setText(_translate("MenuEmpleados", "Peso actual:"))
        self.label_77.setText(_translate("MenuEmpleados", "Correo electronico:"))
        self.label_74.setText(_translate("MenuEmpleados", "Altura:"))
        self.label_72.setText(_translate("MenuEmpleados", "Teléfono:"))
        self.label_75.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Ingrese la información del cliente</span></p></body></html>"))
        self.GuardarRegistrarPaciente_3.setText(_translate("MenuEmpleados", "Registrar"))
        self.label_76.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_150.setText(_translate("MenuEmpleados", "Contraseña:"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_10), _translate("MenuEmpleados", "Agregar"))
        self.label_95.setText(_translate("MenuEmpleados", "Buscar por ID cliente:"))
        self.BuscarBotonActualizar_4.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_96.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Selecciona el cliente</span></p></body></html>"))
        self.label_98.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_100.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Selecciona el entrenador</span></p></body></html>"))
        self.label_97.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Informacion del cliente</span></p></body></html>"))
        self.label_99.setText(_translate("MenuEmpleados", "Correo electronico:"))
        self.label_104.setText(_translate("MenuEmpleados", "Correo electronico:"))
        self.label_103.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Informacion del entrenador</span></p></body></html>"))
        self.label_101.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_102.setText(_translate("MenuEmpleados", "Buscar por ID entrenador:"))
        self.BuscarBotonActualizar_5.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarBotonActualizar_6.setText(_translate("MenuEmpleados", "Asignar entrenador"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_14), _translate("MenuEmpleados", "Asignar Entrenador"))
        self.label_78.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-weight:696; color:#ffffff;\">Informacion del cliente:</span></p></body></html>"))
        self.label_79.setText(_translate("MenuEmpleados", "Nombre:"))
        self.BuscarPor_8.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarPor_8.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.label_83.setText(_translate("MenuEmpleados", "Correo electronico:"))
        self.label_84.setText(_translate("MenuEmpleados", "Situacion Membresia:"))
        self.label_85.setText(_translate("MenuEmpleados", "Fecha de vencimiento: "))
        self.label_87.setText(_translate("MenuEmpleados", "<html><head/><body><p>Seleccionar el cliente</p></body></html>"))
        self.BuscarBotonActualizar_3.setText(_translate("MenuEmpleados", "Buscar"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), _translate("MenuEmpleados", "Membresia"))
        self.label_80.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_105.setText(_translate("MenuEmpleados", "<html><head/><body><p>Actualizar informacion del cliente</p></body></html>"))
        self.BuscarPor_9.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarPor_9.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.label_81.setText(_translate("MenuEmpleados", "<html><head/><body><p>Actualizar informacion del usuario necesaria:</p></body></html>"))
        self.ActualizarBotonPaciente_4.setText(_translate("MenuEmpleados", "Actualizar"))
        self.label_107.setText(_translate("MenuEmpleados", "Telefono:"))
        self.BuscarBotonActualizar_7.setText(_translate("MenuEmpleados", "Buscar"))
        self.label_108.setText(_translate("MenuEmpleados", "Correo electronico:"))
        self.label_109.setText(_translate("MenuEmpleados", "Edad:"))
        self.label_110.setText(_translate("MenuEmpleados", "Peso actual:"))
        self.label_111.setText(_translate("MenuEmpleados", "Altura:"))
        self.label_151.setText(_translate("MenuEmpleados", "Contraseña:"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_15), _translate("MenuEmpleados", "Actualizar cliente"))
        self.RefrescarBotonRegistrados_4.setText(_translate("MenuEmpleados", "Refrescar"))
        self.BuscarBotonRegistrados_4.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarRegistradosCombobox_6.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarRegistradosCombobox_6.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(0)
        item.setText(_translate("MenuEmpleados", "ID"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(1)
        item.setText(_translate("MenuEmpleados", "Nombre"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(2)
        item.setText(_translate("MenuEmpleados", "Fecha Ingreso"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(3)
        item.setText(_translate("MenuEmpleados", "Edad"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(4)
        item.setText(_translate("MenuEmpleados", "Telefono"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(5)
        item.setText(_translate("MenuEmpleados", "Correo Electronico"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(6)
        item.setText(_translate("MenuEmpleados", "Altura"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(7)
        item.setText(_translate("MenuEmpleados", "Peso"))
        item = self.TablaEmpleados_4.horizontalHeaderItem(8)
        item.setText(_translate("MenuEmpleados", "Membresia Actual"))
        self.label_88.setText(_translate("MenuEmpleados", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Clientes asignados</span></p></body></html>"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_12), _translate("MenuEmpleados", "Mostrar"))
        self.label_89.setText(_translate("MenuEmpleados", "Nombre:"))
        self.label_90.setText(_translate("MenuEmpleados", "Edad:"))
        self.label_91.setText(_translate("MenuEmpleados", "Telefono:"))
        self.label_92.setText(_translate("MenuEmpleados", "Correo Electronico:"))
        self.EliminarPacienteBoton_3.setText(_translate("MenuEmpleados", "Eliminar"))
        self.BuscarBotonEliminar_3.setText(_translate("MenuEmpleados", "Buscar"))
        self.BuscarRegistradosCombobox_7.setItemText(0, _translate("MenuEmpleados", "Buscar por ID:"))
        self.BuscarRegistradosCombobox_7.setItemText(1, _translate("MenuEmpleados", "Buscar por Nombre:"))
        self.label_93.setText(_translate("MenuEmpleados", "Informacion del Cliente:"))
        self.label_94.setText(_translate("MenuEmpleados", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; color:#ffffff;\">Eliminar cliente</span></p></body></html>"))
        self.label_117.setText(_translate("MenuEmpleados", "Altura:"))
        self.label_118.setText(_translate("MenuEmpleados", "Peso Actual:"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_13), _translate("MenuEmpleados", "Elminar"))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MenuEmpleados = QtWidgets.QMainWindow()
    ui = Ui_MenuEmpleados()
    ui.setupUi(MenuEmpleados)
    MenuEmpleados.show()
    sys.exit(app.exec_())

