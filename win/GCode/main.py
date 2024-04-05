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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTextEdit, QVBoxLayout, QWidget)

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
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.openButton = QPushButton(Form)
        self.openButton.setObjectName(u"openButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openButton.sizePolicy().hasHeightForWidth())
        self.openButton.setSizePolicy(sizePolicy)
        self.openButton.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout.addWidget(self.openButton)

        self.saveButton = QPushButton(Form)
        self.saveButton.setObjectName(u"saveButton")
        sizePolicy.setHeightForWidth(self.saveButton.sizePolicy().hasHeightForWidth())
        self.saveButton.setSizePolicy(sizePolicy)
        self.saveButton.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout.addWidget(self.saveButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"border: 1px solid #d6d6d6;\n"
"}")

        self.verticalLayout.addWidget(self.textEdit)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 18)

        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.openButton.setText(QCoreApplication.translate("Form", u"\u6253\u5f00G\u4ee3\u7801", None))
        self.saveButton.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58G\u4ee3\u7801", None))
    # retranslateUi

