# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        Form.setFocusPolicy(Qt.NoFocus)
        Form.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setDxfButton = QPushButton(Form)
        self.setDxfButton.setObjectName(u"setDxfButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.setDxfButton.sizePolicy().hasHeightForWidth())
        self.setDxfButton.setSizePolicy(sizePolicy)
        self.setDxfButton.setStyleSheet(u"QPushButton\n"
"{\n"
"border-radius: 3px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"padding-bottom: 2px;\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"border-radius: 3px;\n"
"border-top: 1px solid #1ecc94;\n"
"background-color: #d8d8d8;\n"
"}\n"
"QPushButton:pressed     \n"
"{\n"
"border-radius: 3px;\n"
"background-color: #1ecc94;\n"
"} ")

        self.horizontalLayout_2.addWidget(self.setDxfButton)

        self.gCodeButton = QPushButton(Form)
        self.gCodeButton.setObjectName(u"gCodeButton")
        sizePolicy.setHeightForWidth(self.gCodeButton.sizePolicy().hasHeightForWidth())
        self.gCodeButton.setSizePolicy(sizePolicy)
        self.gCodeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"border-radius: 3px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"padding-bottom: 2px;\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"border-radius: 3px;\n"
"border-top: 1px solid #1ecc94;\n"
"background-color: #d8d8d8;\n"
"}\n"
"QPushButton:pressed     \n"
"{\n"
"border-radius: 3px;\n"
"background-color: #1ecc94;\n"
"} ")

        self.horizontalLayout_2.addWidget(self.gCodeButton)

        self.saveGCodeButton = QPushButton(Form)
        self.saveGCodeButton.setObjectName(u"saveGCodeButton")
        sizePolicy.setHeightForWidth(self.saveGCodeButton.sizePolicy().hasHeightForWidth())
        self.saveGCodeButton.setSizePolicy(sizePolicy)
        self.saveGCodeButton.setStyleSheet(u"QPushButton\n"
"{\n"
"border-radius: 3px;\n"
"padding-left: 8px;\n"
"padding-right: 8px;\n"
"padding-bottom: 2px;\n"
"}\n"
"QPushButton:hover \n"
"{\n"
"border-radius: 3px;\n"
"border-top: 1px solid #1ecc94;\n"
"background-color: #d8d8d8;\n"
"}\n"
"QPushButton:pressed     \n"
"{\n"
"border-radius: 3px;\n"
"background-color: #1ecc94;\n"
"} ")

        self.horizontalLayout_2.addWidget(self.saveGCodeButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.speedLabel = QLabel(Form)
        self.speedLabel.setObjectName(u"speedLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.speedLabel.sizePolicy().hasHeightForWidth())
        self.speedLabel.setSizePolicy(sizePolicy1)
        self.speedLabel.setStyleSheet(u"QLabel\n"
"{\n"
"border-radius: 3px;\n"
"background-color: #1ecc94;\n"
"padding-bottom: 2px;\n"
"}")
        self.speedLabel.setMidLineWidth(0)
        self.speedLabel.setTextFormat(Qt.AutoText)
        self.speedLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.speedLabel)

        self.speedEdit = QLineEdit(Form)
        self.speedEdit.setObjectName(u"speedEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.speedEdit.sizePolicy().hasHeightForWidth())
        self.speedEdit.setSizePolicy(sizePolicy2)
        self.speedEdit.setTabletTracking(False)
        self.speedEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius: 3px;\n"
"padding-bottom: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"border: 1px solid #1ecc94;\n"
"}")
        self.speedEdit.setInputMethodHints(Qt.ImhNone)
        self.speedEdit.setEchoMode(QLineEdit.Normal)
        self.speedEdit.setCursorPosition(0)
        self.speedEdit.setReadOnly(False)

        self.horizontalLayout_2.addWidget(self.speedEdit)

        self.deepLabel = QLabel(Form)
        self.deepLabel.setObjectName(u"deepLabel")
        sizePolicy1.setHeightForWidth(self.deepLabel.sizePolicy().hasHeightForWidth())
        self.deepLabel.setSizePolicy(sizePolicy1)
        self.deepLabel.setStyleSheet(u"QLabel\n"
"{\n"
"border-radius: 3px;\n"
"background-color: #1ecc94;\n"
"padding-bottom: 2px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.deepLabel)

        self.deepEdit = QLineEdit(Form)
        self.deepEdit.setObjectName(u"deepEdit")
        sizePolicy2.setHeightForWidth(self.deepEdit.sizePolicy().hasHeightForWidth())
        self.deepEdit.setSizePolicy(sizePolicy2)
        self.deepEdit.setStyleSheet(u"QLineEdit\n"
"{\n"
"border-radius: 3px;\n"
"padding-bottom: 2px;\n"
"padding-right: 2px;\n"
"}\n"
"QLineEdit:hover\n"
"{\n"
"border: 1px solid #1ecc94;\n"
"}")

        self.horizontalLayout_2.addWidget(self.deepEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.img = QLabel(Form)
        self.img.setObjectName(u"img")
        self.img.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.img)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 18)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.gcode = QTextBrowser(Form)
        self.gcode.setObjectName(u"gcode")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(10)
        self.gcode.setFont(font1)
        self.gcode.setStyleSheet(u"QTextBrowser{\n"
"border: 1px solid #d6d6d6;\n"
"}")

        self.horizontalLayout.addWidget(self.gcode)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2.setStretch(0, 12)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.setDxfButton.setText(QCoreApplication.translate("Form", u"\u8bf7\u9009\u62e9DXF\u6587\u4ef6", None))
        self.gCodeButton.setText(QCoreApplication.translate("Form", u"\u751f\u6210G\u4ee3\u7801", None))
        self.saveGCodeButton.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58G\u4ee3\u7801", None))
        self.speedLabel.setText(QCoreApplication.translate("Form", u"\u7ed9\u8fdb\u901f\u5ea6", None))
        self.speedEdit.setText("")
        self.speedEdit.setPlaceholderText("")
        self.deepLabel.setText(QCoreApplication.translate("Form", u"\u4e0b\u5200\u6df1\u5ea6", None))
        self.deepEdit.setText("")
        self.img.setText(QCoreApplication.translate("Form", u"\u8bf7\u70b9\u51fb\u4e0a\u9762\u6309\u94ae\u5bfc\u5165DXF\u6587\u4ef6", None))
    # retranslateUi

