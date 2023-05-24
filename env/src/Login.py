import datetime
import pickle 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QLineEdit,QAction
from MenuAdmin import Ui_MenuAdministrativo
from MenuEmpleados import Ui_MenuEmpleados
from MenuClientes import Ui_MainWindow

class Ui_LogIn(object):

    def setupUi(self, LogIn, cursor):
        LogIn.setObjectName("LogIn")
        LogIn.resize(921, 685)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        LogIn.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(LogIn)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(244, 244, 244);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("border: 0px solid #e6b31e;\n"
"font: 63 40pt \"Bahnschrift SemiBold SemiConden\";")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255, 0);\n"
"image: url(:/menu/LogoLogin.png);\n"
"border: 0px solid #e6b31e;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 0, 0, 1, 2)
        self.verticalLayout.addWidget(self.frame_4)
        self.verticalLayout.setStretch(0, 3)
        self.verticalLayout.setStretch(1, 8)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setStyleSheet("background-color: #231f20;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setStyleSheet("border: 0px solid #e6b31e;\n"
"font: 63 40pt \"Bahnschrift SemiBold SemiConden\";\n"
"color:#e6b31e;")
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 4, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(400, 40))
        self.lineEdit_7.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 5, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        self.label_120 = QtWidgets.QLabel(self.frame_6)
        self.label_120.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_120.setObjectName("label_120")
        self.gridLayout_3.addWidget(self.label_120, 1, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 5, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 0, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(200, 40))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(400, 40))
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_8.setStyleSheet("background-color: #343434;\n"
"font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;\n"
"border: 3px solid #e6b31e;\n"
"border-radius: 10px;\n"
"")
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem5, 0, 4, 1, 1)
        self.label_119 = QtWidgets.QLabel(self.frame_6)
        self.label_119.setStyleSheet("font: 87 14pt \"Arial Black\";\n"
"color: whitesmoke;")
        self.label_119.setObjectName("label_119")
        self.gridLayout_3.addWidget(self.label_119, 0, 1, 1, 1)
        self.pushButton_28 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_28.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_28.setMaximumSize(QtCore.QSize(400, 60))
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
        self.gridLayout_3.addWidget(self.pushButton_28, 5, 1, 1, 2)
        self.SeleccionRol = QtWidgets.QComboBox(self.frame_6)
        self.SeleccionRol.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.SeleccionRol.setStyleSheet("font: 63 20pt \"Bahnschrift SemiBold SemiConden\";\n"
"border: .5px solid #e6b31e;\n"
"background-color: rgb(52, 52, 52);\n"
"color: whitesmoke;")
        self.SeleccionRol.setObjectName("SeleccionRol")
        self.SeleccionRol.addItem("")
        self.SeleccionRol.addItem("")
        self.gridLayout_3.addWidget(self.SeleccionRol, 4, 1, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_3.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    border: 0px;\n"
"    image: url(:/menu/ojo.png);\n"
"    \n"
"}\n"
"QPushButton:hover{\n"
"    border: 10px;\n"
"}")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_3.addWidget(self.pushButton_3, 1, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 10)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 9)
        self.horizontalLayout.setStretch(1, 10)
        LogIn.setCentralWidget(self.centralwidget)

        self.retranslateUi(LogIn)
        QtCore.QMetaObject.connectSlotsByName(LogIn)
        
        """
        Aqui inician las instrucciones a las funciones:
        """
        self.pushButton_28.clicked.connect(lambda: self.iniciarSesion(cursor, LogIn))
        self.pushButton_3.clicked.connect(lambda: self.passwordHide(self.lineEdit_8))
        #Actualizacion de STATUS
        self.actualizarClientesSituacion(cursor)
        self.load_text()
        
        """
        Parte de pickle
        """
        """
        Aqui inician las funciones:
        """
    def closeEvent(self, event):
        self.save_text()  # Guardar el texto antes de cerrar la ventana
        event.accept()

    def save_text(self):
        texto = self.lineEdit_8.text()
        with open('estado.pickle', 'wb') as archivo:
            pickle.dump(texto, archivo)

    def load_text(self):
        try:
            with open('estado.pickle', 'rb') as archivo:
                texto = pickle.load(archivo)
                print(texto);
                self.lineEdit_8.setText(str(texto))
        except (FileNotFoundError, EOFError):
            pass
        
    def iniciarSesion(self, cursor, LogIn):
        user=self.lineEdit_7.text()
        passw = self.lineEdit_8.text()
        rol = self.SeleccionRol.currentText()
        if (len(user)==0) or (len(passw)==0):
            self.msgError("Falta de informacion", "Debes llenar todos los campos para poder iniciar sesion")
        else:
            if rol=="Cliente":
                sql='''select id_cliente,contraseña from cliente where cast(id_cliente as varchar)='{}' '''.format(user)
            else:
                sql='''select id_empleado,contraseña, rol from empleadosyadmin where cast(id_empleado as varchar)='{}' '''.format(user)
            cursor.execute(sql)
            row=cursor.fetchall()
            print(row)
            if len(row)==0:
                msg="No hay ningun usuario registrado con ese ID en "+rol+"s"
                self.msgError("Sin coincidencia", msg)
                proceso="Intento de ingresar erroneo(usuario incorrecto) con el ID: {} de Cliente".format(user);
                self.cambios(proceso);
            else:
                for rows in row: 
                    if rol=="Cliente":
                        if str(rows[1])!=passw:
                            self.msgError("Contraseña Incorrecta", "La contraseña no coincide con el usuario")
                            proceso="Intento de ingresar erroneo(password incorrecta) con el ID: {} de Cliente".format(user);
                            self.cambios(proceso);
                        else:
                            id=rows[0]
                            #Conecto al usuario
                            proceso="Ingreso el cliente con ID: {}".format(user);
                            self.cambios(proceso);
                            self.window = QtWidgets.QMainWindow()
                            self.ui = Ui_MainWindow()
                            self.ui.setupUi(self.window,cursor,id,LogIn)
                            LogIn.close()
                            self.lineEdit_7.setText("")
                            self.lineEdit_8.setText("")
                            self.window.show()
                    else:
                        if str(rows[1])!=passw:
                            self.msgError("Contraseña Incorrecta", "La contraseña no coincide con el usuario")
                            proceso="Intento de ingresar erroneo(usuario incorrecto) con el ID: {} de Admin".format(user);
                            self.cambios(proceso);
                        else:
                            id=rows[0]
                            rols=rows[2]
                            if rols == "Administrativo":
                                #Conecto al usuario al menu administrativo
                                proceso="Ingreso el admin con ID: {}".format(user);
                                self.cambios(proceso);
                                self.window = QtWidgets.QMainWindow()
                                self.ui = Ui_MenuAdministrativo()
                                self.ui.setupUi(self.window, cursor, id, LogIn)
                                LogIn.close()
                                self.lineEdit_7.setText("")
                                self.lineEdit_8.setText("")
                                self.window.show()
                            elif rols == "Empleado":
                                #Conecto al usuario al menu administrativo
                                proceso="Ingreso el empleado con ID: {}".format(user);
                                self.cambios(proceso);
                                self.window = QtWidgets.QMainWindow()
                                self.ui = Ui_MenuEmpleados()
                                self.ui.setupUi(self.window, cursor, id, LogIn)
                                LogIn.close()
                                self.lineEdit_7.setText("")
                                self.lineEdit_8.setText("")
                                self.window.show()
    
    def actualizarClientesSituacion(self, cursor):
        fechaActual = datetime.datetime.now()
        fecha=datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
        SQL="""select *from cliente where fecha_vencimiento<='{}' """.format(str(fecha))
        cursor.execute(SQL)
        row=cursor.fetchall()
        if (len(row)) != 0:
                for rows in row:
                        sql="""update cliente set situacion_Membresia='Vencida' where id_cliente='{}' """.format(str(rows[0]))
                        cursor.execute(sql)
                        cursor.connection.commit()


    def passwordHide(self, passw):
        if passw.echoMode() == QLineEdit.Password:
            passw.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            passw.setEchoMode(QtWidgets.QLineEdit.Password)
    def msgError(self,msg1,msg2):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle(msg1)
        msg.setText(msg2)
        msg.setIcon(QtWidgets.QMessageBox.Information)
        
        x = msg.exec_()
    
    def cambios(self,proceso):
        fechaActual = datetime.datetime.now()
        fecha = datetime.datetime.strftime(fechaActual, '%d/%m/%Y')
        hora = str(fechaActual.hour) + ":"+ str(fechaActual.minute)+":"+str(fechaActual.second)
        cambio=dict()
        cambio['Hecho por:']=" - ";
        cambio['Fecha:']=fecha;
        cambio['Hora:']=hora;
        cambio['Proceso hecho:']=proceso;
        print(cambio)
        archivo=open('procesos.pickle','ab');
        pickle.dump(cambio,archivo)
        archivo.close()
    
    def retranslateUi(self, LogIn):
        _translate = QtCore.QCoreApplication.translate
        LogIn.setWindowTitle(_translate("LogIn", "LogIn"))
        self.label.setText(_translate("LogIn", "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Gimnasio Teflon </span></p><p align=\"center\"><span style=\" font-size:28pt;\">Academy</span></p></body></html>"))
        self.label_3.setText(_translate("LogIn", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">¡Bienvenido!</span></p><p align=\"center\"><span style=\" font-size:22pt;\">Ingresa tus datos para </span></p><p align=\"center\"><span style=\" font-size:22pt;\">continuar...</span></p></body></html>"))
        self.label_120.setText(_translate("LogIn", "Contraseña:"))
        self.label_119.setText(_translate("LogIn", "ID de usuario:"))
        self.pushButton_28.setText(_translate("LogIn", "Ingresar"))
        self.SeleccionRol.setItemText(0, _translate("LogIn", "Cliente"))
        self.SeleccionRol.setItemText(1, _translate("LogIn", "Administrativo"))

import images_rc
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogIn = QtWidgets.QMainWindow()
    ui = Ui_LogIn()
    ui.setupUi(LogIn)
    LogIn.show()
    sys.exit(app.exec_())

