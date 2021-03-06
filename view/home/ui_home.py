# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Home(object):
    def setupUi(self, widget_2):
        widget_2.setObjectName("widget_2")
        widget_2.resize(1200, 800)
        widget_2.setMinimumSize(QtCore.QSize(1200, 800))
        widget_2.setMaximumSize(QtCore.QSize(1200, 800))
        widget_2.setStyleSheet("background-image: url(view/assets/Background.png);")
        self.gridLayoutWidget = QtWidgets.QWidget(widget_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1202, 814))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 14, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.widget = QtWidgets.QWidget(self.gridLayoutWidget)
        self.widget.setMinimumSize(QtCore.QSize(1200, 800))
        self.widget.setMaximumSize(QtCore.QSize(1200, 800))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.tvTitle = QtWidgets.QLabel(self.widget)
        self.tvTitle.setGeometry(QtCore.QRect(100, 20, 1031, 61))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(54)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.tvTitle.setFont(font)
        self.tvTitle.setStyleSheet("color: #ffffff;\n"
                                   "background: transparent;")
        self.tvTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.tvTitle.setObjectName("tvTitle")
        self.edt_age = QtWidgets.QLineEdit(self.widget)
        self.edt_age.setGeometry(QtCore.QRect(420, 390, 411, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        self.edt_age.setFont(font)
        self.edt_age.setStyleSheet("background: #FFFFFF;\n"
                                   "border-radius: 24px;\n"
                                   "padding-left: 14px;")
        self.edt_age.setInputMethodHints(QtCore.Qt.ImhNone)
        self.edt_age.setInputMask("")
        self.edt_age.setText("")
        self.edt_age.setClearButtonEnabled(True)
        self.edt_age.setObjectName("edt_age")
        self.edt_height = QtWidgets.QLineEdit(self.widget)
        self.edt_height.setGeometry(QtCore.QRect(420, 460, 411, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        self.edt_height.setFont(font)
        self.edt_height.setStyleSheet("background: #FFFFFF;\n"
                                      "border-radius: 24px;\n"
                                      "padding-left: 14px;")
        self.edt_height.setText("")
        self.edt_height.setClearButtonEnabled(True)
        self.edt_height.setObjectName("edt_height")
        self.btnSubmit = QtWidgets.QPushButton(self.widget)
        self.btnSubmit.setGeometry(QtCore.QRect(420, 640, 411, 51))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btnSubmit.setFont(font)
        self.btnSubmit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSubmit.setStyleSheet("* {\n"
                                     "    background: #686DE0;\n"
                                     "    border-radius: 24;\n"
                                     "    color: #FFFFFF;    \n"
                                     "    padding: 12px;\n"
                                     "}\n"
                                     "\n"
                                     "*:hover {\n"
                                     "    background: #6350E8;\n"
                                     "}")
        self.btnSubmit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.btnSubmit.setObjectName("btnSubmit")
        self.edt_weight = QtWidgets.QLineEdit(self.widget)
        self.edt_weight.setGeometry(QtCore.QRect(420, 530, 411, 51))
        self.edt_weight.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("SF Pro Display")
        font.setPointSize(14)
        self.edt_weight.setFont(font)
        self.edt_weight.setStyleSheet("background: #FFFFFF;\n"
                                      "border-radius: 24px;\n"
                                      "padding-left: 14px;\n"
                                      "")
        self.edt_weight.setInputMask("")
        self.edt_weight.setText("")
        self.edt_weight.setClearButtonEnabled(True)
        self.edt_weight.setObjectName("edt_weight")
        self.btnMale = QtWidgets.QRadioButton(self.widget)
        self.btnMale.setGeometry(QtCore.QRect(510, 330, 61, 16))
        self.btnMale.setStyleSheet("background: #130F40;\n"
                                   "color: #130F40;")
        self.btnMale.setText("")
        self.btnMale.setChecked(False)
        self.btnMale.setObjectName("btnMale")
        self.btnFemale = QtWidgets.QRadioButton(self.widget)
        self.btnFemale.setGeometry(QtCore.QRect(730, 330, 71, 17))
        self.btnFemale.setStyleSheet("background: #130F40;\n"
                                     "color: #130F40;")
        self.btnFemale.setText("")
        self.btnFemale.setCheckable(True)
        self.btnFemale.setChecked(False)
        self.btnFemale.setObjectName("btnFemale")
        self.imgMale = QtWidgets.QLabel(self.widget)
        self.imgMale.setGeometry(QtCore.QRect(450, 190, 121, 121))
        self.imgMale.setStyleSheet("border-radius: 60px;\n"
                                   "background-image: url(view/assets/boy.png);\n"
                                   "background-repeat: no-repeat;\n"
                                   "background-attachment: fixed;\n"
                                   "background-position: center;\n"
                                   "background-size: 15px 15px;\n"
                                   "border: 4px solid #686de0;\n"
                                   "")
        self.imgMale.setText("")
        self.imgMale.setObjectName("imgMale")
        self.imgFemale = QtWidgets.QLabel(self.widget)
        self.imgFemale.setGeometry(QtCore.QRect(670, 190, 121, 121))
        self.imgFemale.setStyleSheet("border-radius: 60px;\n"
                                     "background-image: url(view/assets/girl.png);\n"
                                     "background-repeat: no-repeat;\n"
                                     "background-attachment: fixed;\n"
                                     "background-position: center;\n"
                                     "background-size: 15px 15px;\n"
                                     "border: 4px solid #686de0;")
        self.imgFemale.setText("")
        self.imgFemale.setObjectName("imgFemale")
        self.gridLayout_2.addWidget(self.widget, 5, 0, 1, 1)

        self.retranslateUi(widget_2)
        QtCore.QMetaObject.connectSlotsByName(widget_2)

    def retranslateUi(self, widget_2):
        _translate = QtCore.QCoreApplication.translate
        widget_2.setWindowTitle(_translate("widget_2", "Bobotin - Home"))
        self.tvTitle.setText(_translate("widget_2", "BOBOTIN"))
        self.edt_age.setToolTip(
            _translate("widget_2", "<html><head/><body><p>Masukan berat badan anda</p></body></html>"))
        self.edt_age.setPlaceholderText(_translate("widget_2", "Umur"))
        self.edt_height.setToolTip(
            _translate("widget_2", "<html><head/><body><p>Masukan tinggi anda</p></body></html>"))
        self.edt_height.setPlaceholderText(_translate("widget_2", "Tinggi (cm)"))
        self.btnSubmit.setText(_translate("widget_2", "SUBMIT"))
        self.edt_weight.setToolTip(_translate("widget_2", "<html><head/><body><p>Masukan umur anda</p></body></html>"))
        self.edt_weight.setPlaceholderText(_translate("widget_2", "Berat (kg)"))
        self.imgMale.setToolTip(_translate("widget_2", "<html><head/><body><p>Laki-Laki</p></body></html>"))
        self.imgFemale.setToolTip(_translate("widget_2", "<html><head/><body><p>Perempuan</p></body></html>"))
