# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\AN24\branches\simulation version\Holter_mother_edition2.6\_eric4project\Holter.ui'
#
# Created: Mon Jan 11 21:54:13 2016
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Holter(object):
    def setupUi(self, Holter):
        Holter.setObjectName(_fromUtf8("Holter"))
        Holter.resize(1388, 790)
        Holter.setMinimumSize(QtCore.QSize(925, 700))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        Holter.setFont(font)
        self.centralWidget = QtGui.QWidget(Holter)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.frame = QtGui.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(1210, 70, 171, 651))
        self.frame.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);"))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.recvStop = QtGui.QPushButton(self.frame)
        self.recvStop.setGeometry(QtCore.QRect(20, 100, 71, 71))
        self.recvStop.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/stop.png);\n"
"background-repeat:no-repeat;"))
        self.recvStop.setText(_fromUtf8(""))
        self.recvStop.setFlat(True)
        self.recvStop.setObjectName(_fromUtf8("recvStop"))
        self.pushSearch = QtGui.QPushButton(self.frame)
        self.pushSearch.setGeometry(QtCore.QRect(20, 20, 71, 71))
        self.pushSearch.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/search_button_static.png);\n"
"background-repeat:no-repeat;"))
        self.pushSearch.setText(_fromUtf8(""))
        self.pushSearch.setCheckable(False)
        self.pushSearch.setAutoRepeat(False)
        self.pushSearch.setAutoExclusive(False)
        self.pushSearch.setAutoDefault(False)
        self.pushSearch.setDefault(False)
        self.pushSearch.setFlat(True)
        self.pushSearch.setObjectName(_fromUtf8("pushSearch"))
        self.visualChange = QtGui.QPushButton(self.frame)
        self.visualChange.setGeometry(QtCore.QRect(90, 100, 71, 71))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.visualChange.sizePolicy().hasHeightForWidth())
        self.visualChange.setSizePolicy(sizePolicy)
        self.visualChange.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.visualChange.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/visual.png);\n"
"background-repeat:no-repeat;"))
        self.visualChange.setInputMethodHints(QtCore.Qt.ImhNone)
        self.visualChange.setText(_fromUtf8(""))
        self.visualChange.setDefault(False)
        self.visualChange.setFlat(True)
        self.visualChange.setObjectName(_fromUtf8("visualChange"))
        self.pushSoundSwitch = QtGui.QPushButton(self.frame)
        self.pushSoundSwitch.setGeometry(QtCore.QRect(90, 260, 71, 71))
        self.pushSoundSwitch.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/sound.png);\n"
"background-repeat:no-repeat;"))
        self.pushSoundSwitch.setText(_fromUtf8(""))
        self.pushSoundSwitch.setFlat(True)
        self.pushSoundSwitch.setObjectName(_fromUtf8("pushSoundSwitch"))
        self.pushButtonSettings = QtGui.QPushButton(self.frame)
        self.pushButtonSettings.setGeometry(QtCore.QRect(90, 340, 71, 71))
        self.pushButtonSettings.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/settings.png);\n"
"background-repeat: no-repeat;"))
        self.pushButtonSettings.setText(_fromUtf8(""))
        self.pushButtonSettings.setFlat(True)
        self.pushButtonSettings.setObjectName(_fromUtf8("pushButtonSettings"))
        self.device_1 = QtGui.QPushButton(self.frame)
        self.device_1.setGeometry(QtCore.QRect(20, 430, 141, 39))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_1.sizePolicy().hasHeightForWidth())
        self.device_1.setSizePolicy(sizePolicy)
        self.device_1.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/button_1234_blank.png);\n"
"background-repeat:no-repeat;\n"
""))
        self.device_1.setFlat(True)
        self.device_1.setObjectName(_fromUtf8("device_1"))
        self.device_2 = QtGui.QPushButton(self.frame)
        self.device_2.setGeometry(QtCore.QRect(20, 480, 141, 39))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_2.sizePolicy().hasHeightForWidth())
        self.device_2.setSizePolicy(sizePolicy)
        self.device_2.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/button_1234_blank.png);\n"
"background-repeat:no-repeat;\n"
""))
        self.device_2.setFlat(True)
        self.device_2.setObjectName(_fromUtf8("device_2"))
        self.device_3 = QtGui.QPushButton(self.frame)
        self.device_3.setGeometry(QtCore.QRect(20, 530, 141, 39))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_3.sizePolicy().hasHeightForWidth())
        self.device_3.setSizePolicy(sizePolicy)
        self.device_3.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/button_1234_blank.png);\n"
"background-repeat:no-repeat;\n"
""))
        self.device_3.setFlat(True)
        self.device_3.setObjectName(_fromUtf8("device_3"))
        self.device_4 = QtGui.QPushButton(self.frame)
        self.device_4.setGeometry(QtCore.QRect(20, 580, 141, 39))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.device_4.sizePolicy().hasHeightForWidth())
        self.device_4.setSizePolicy(sizePolicy)
        self.device_4.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/button_1234_blank.png);\n"
"background-repeat:no-repeat;\n"
""))
        self.device_4.setFlat(True)
        self.device_4.setObjectName(_fromUtf8("device_4"))
        self.pushButtonAlarm = QtGui.QPushButton(self.frame)
        self.pushButtonAlarm.setGeometry(QtCore.QRect(120, 430, 40, 40))
        self.pushButtonAlarm.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/diable_heart.png);\n"
"background-repeat:no-repeat;"))
        self.pushButtonAlarm.setText(_fromUtf8(""))
        self.pushButtonAlarm.setFlat(True)
        self.pushButtonAlarm.setObjectName(_fromUtf8("pushButtonAlarm"))
        self.pushButtonAlarm_2 = QtGui.QPushButton(self.frame)
        self.pushButtonAlarm_2.setGeometry(QtCore.QRect(120, 480, 40, 40))
        self.pushButtonAlarm_2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/diable_heart.png);\n"
"background-repeat:no-repeat;"))
        self.pushButtonAlarm_2.setText(_fromUtf8(""))
        self.pushButtonAlarm_2.setFlat(True)
        self.pushButtonAlarm_2.setObjectName(_fromUtf8("pushButtonAlarm_2"))
        self.pushButtonAlarm_3 = QtGui.QPushButton(self.frame)
        self.pushButtonAlarm_3.setGeometry(QtCore.QRect(120, 530, 40, 40))
        self.pushButtonAlarm_3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/diable_heart.png);\n"
"background-repeat:no-repeat;"))
        self.pushButtonAlarm_3.setText(_fromUtf8(""))
        self.pushButtonAlarm_3.setFlat(True)
        self.pushButtonAlarm_3.setObjectName(_fromUtf8("pushButtonAlarm_3"))
        self.pushButtonAlarm_4 = QtGui.QPushButton(self.frame)
        self.pushButtonAlarm_4.setGeometry(QtCore.QRect(120, 580, 40, 40))
        self.pushButtonAlarm_4.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/diable_heart.png);\n"
"background-repeat:no-repeat;"))
        self.pushButtonAlarm_4.setText(_fromUtf8(""))
        self.pushButtonAlarm_4.setFlat(True)
        self.pushButtonAlarm_4.setObjectName(_fromUtf8("pushButtonAlarm_4"))
        self.full_or_normal = QtGui.QPushButton(self.frame)
        self.full_or_normal.setGeometry(QtCore.QRect(90, 20, 70, 70))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.full_or_normal.sizePolicy().hasHeightForWidth())
        self.full_or_normal.setSizePolicy(sizePolicy)
        self.full_or_normal.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/normal_screen.png);\n"
"background-repeat:no-repeat;"))
        self.full_or_normal.setText(_fromUtf8(""))
        self.full_or_normal.setAutoDefault(False)
        self.full_or_normal.setDefault(False)
        self.full_or_normal.setFlat(True)
        self.full_or_normal.setObjectName(_fromUtf8("full_or_normal"))
        self.xscale1 = QtGui.QPushButton(self.frame)
        self.xscale1.setGeometry(QtCore.QRect(20, 180, 70, 70))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale1.sizePolicy().hasHeightForWidth())
        self.xscale1.setSizePolicy(sizePolicy)
        self.xscale1.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/1.png);\n"
"background-repeat:no-repeat;"))
        self.xscale1.setText(_fromUtf8(""))
        self.xscale1.setAutoDefault(False)
        self.xscale1.setDefault(False)
        self.xscale1.setFlat(True)
        self.xscale1.setObjectName(_fromUtf8("xscale1"))
        self.xscale2 = QtGui.QPushButton(self.frame)
        self.xscale2.setGeometry(QtCore.QRect(20, 260, 70, 70))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale2.sizePolicy().hasHeightForWidth())
        self.xscale2.setSizePolicy(sizePolicy)
        self.xscale2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/2.png);\n"
"background-repeat:no-repeat;"))
        self.xscale2.setText(_fromUtf8(""))
        self.xscale2.setAutoDefault(False)
        self.xscale2.setDefault(False)
        self.xscale2.setFlat(True)
        self.xscale2.setObjectName(_fromUtf8("xscale2"))
        self.xscale3 = QtGui.QPushButton(self.frame)
        self.xscale3.setGeometry(QtCore.QRect(20, 340, 70, 70))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xscale3.sizePolicy().hasHeightForWidth())
        self.xscale3.setSizePolicy(sizePolicy)
        self.xscale3.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/3.png);\n"
"background-repeat:no-repeat;"))
        self.xscale3.setText(_fromUtf8(""))
        self.xscale3.setAutoDefault(False)
        self.xscale3.setDefault(False)
        self.xscale3.setFlat(True)
        self.xscale3.setObjectName(_fromUtf8("xscale3"))
        self.pushPrint = QtGui.QPushButton(self.frame)
        self.pushPrint.setGeometry(QtCore.QRect(90, 180, 64, 64))
        self.pushPrint.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/print.png);\n"
"background-repeat:no-repeat;"))
        self.pushPrint.setText(_fromUtf8(""))
        self.pushPrint.setAutoDefault(False)
        self.pushPrint.setDefault(False)
        self.pushPrint.setFlat(True)
        self.pushPrint.setObjectName(_fromUtf8("pushPrint"))
        self.pinTest = QtGui.QPushButton(self.frame)
        self.pinTest.setGeometry(QtCore.QRect(50, 620, 75, 23))
        self.pinTest.setText(_fromUtf8(""))
        self.pinTest.setFlat(True)
        self.pinTest.setObjectName(_fromUtf8("pinTest"))
        self.frame_2 = QtGui.QFrame(self.centralWidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1391, 51))
        self.frame_2.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/panel-ground.png);"))
        self.frame_2.setFrameShape(QtGui.QFrame.Panel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.label_hospitalization = QtGui.QLabel(self.frame_2)
        self.label_hospitalization.setGeometry(QtCore.QRect(320, 10, 281, 29))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_hospitalization.setFont(font)
        self.label_hospitalization.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_hospitalization.setTextFormat(QtCore.Qt.AutoText)
        self.label_hospitalization.setObjectName(_fromUtf8("label_hospitalization"))
        self.label_bed = QtGui.QLabel(self.frame_2)
        self.label_bed.setGeometry(QtCore.QRect(650, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        self.label_bed.setFont(font)
        self.label_bed.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_bed.setTextFormat(QtCore.Qt.AutoText)
        self.label_bed.setObjectName(_fromUtf8("label_bed"))
        self.label_name = QtGui.QLabel(self.frame_2)
        self.label_name.setGeometry(QtCore.QRect(60, 10, 161, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blank-ground.png);"))
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.label_blueTooth = QtGui.QLabel(self.frame_2)
        self.label_blueTooth.setGeometry(QtCore.QRect(1300, 10, 31, 31))
        self.label_blueTooth.setMaximumSize(QtCore.QSize(41, 16777215))
        self.label_blueTooth.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/blueToothNo.png);\n"
"background-repeat: no-repeat"))
        self.label_blueTooth.setText(_fromUtf8(""))
        self.label_blueTooth.setObjectName(_fromUtf8("label_blueTooth"))
        self.label_battry = QtGui.QLabel(self.frame_2)
        self.label_battry.setGeometry(QtCore.QRect(1340, 10, 31, 31))
        self.label_battry.setMaximumSize(QtCore.QSize(41, 16777215))
        self.label_battry.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/power_question.png);\n"
"background-repeat: no-repeat"))
        self.label_battry.setText(_fromUtf8(""))
        self.label_battry.setObjectName(_fromUtf8("label_battry"))
        self.pushButton_fill_information = QtGui.QPushButton(self.frame_2)
        self.pushButton_fill_information.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton_fill_information.setStyleSheet(_fromUtf8("background-image: url(:/picture/imgs/info.png);\n"
"background-repeat: no-repeat;"))
        self.pushButton_fill_information.setText(_fromUtf8(""))
        self.pushButton_fill_information.setFlat(True)
        self.pushButton_fill_information.setObjectName(_fromUtf8("pushButton_fill_information"))
        self.pushExit = QtGui.QPushButton(self.frame_2)
        self.pushExit.setGeometry(QtCore.QRect(1250, 5, 40, 40))
        self.pushExit.setStyleSheet(_fromUtf8("background-image:url(:/picture/imgs/close.png);\n"
"background-repeat:no-repeat;"))
        self.pushExit.setText(_fromUtf8(""))
        self.pushExit.setFlat(True)
        self.pushExit.setObjectName(_fromUtf8("pushExit"))
        self.restTime = QtGui.QLabel(self.centralWidget)
        self.restTime.setGeometry(QtCore.QRect(750, 690, 71, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.restTime.setFont(font)
        self.restTime.setStyleSheet(_fromUtf8(""))
        self.restTime.setText(_fromUtf8(""))
        self.restTime.setObjectName(_fromUtf8("restTime"))
        Holter.setCentralWidget(self.centralWidget)

        self.retranslateUi(Holter)
        QtCore.QMetaObject.connectSlotsByName(Holter)

    def retranslateUi(self, Holter):
        Holter.setWindowTitle(_translate("Holter", "MainWindow", None))
        self.device_1.setText(_translate("Holter", "1", None))
        self.device_2.setText(_translate("Holter", "2", None))
        self.device_3.setText(_translate("Holter", "3", None))
        self.device_4.setText(_translate("Holter", "4", None))
        self.label_hospitalization.setText(_translate("Holter", "Hospitalization NO:", None))
        self.label_bed.setText(_translate("Holter", "Bed NO:", None))
        self.label_name.setText(_translate("Holter", "Name:", None))

import images_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Holter = QtGui.QMainWindow()
    ui = Ui_Holter()
    ui.setupUi(Holter)
    Holter.show()
    sys.exit(app.exec_())

