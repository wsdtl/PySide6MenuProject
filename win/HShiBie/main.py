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
    QPushButton, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
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
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.inputImg = QPushButton(Form)
        self.inputImg.setObjectName(u"inputImg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.inputImg.sizePolicy().hasHeightForWidth())
        self.inputImg.setSizePolicy(sizePolicy1)
        self.inputImg.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout_2.addWidget(self.inputImg)

        self.horizontalSpacer_2 = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.inputVideo = QPushButton(Form)
        self.inputVideo.setObjectName(u"inputVideo")
        sizePolicy1.setHeightForWidth(self.inputVideo.sizePolicy().hasHeightForWidth())
        self.inputVideo.setSizePolicy(sizePolicy1)
        self.inputVideo.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout_2.addWidget(self.inputVideo)

        self.startButton = QPushButton(Form)
        self.startButton.setObjectName(u"startButton")
        sizePolicy1.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy1)
        self.startButton.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout_2.addWidget(self.startButton)

        self.stopButton = QPushButton(Form)
        self.stopButton.setObjectName(u"stopButton")
        sizePolicy1.setHeightForWidth(self.stopButton.sizePolicy().hasHeightForWidth())
        self.stopButton.setSizePolicy(sizePolicy1)
        self.stopButton.setStyleSheet(u"QPushButton\n"
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

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.video = QLabel(Form)
        self.video.setObjectName(u"video")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.video.sizePolicy().hasHeightForWidth())
        self.video.setSizePolicy(sizePolicy2)
        self.video.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.video)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 18)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.textEdit = QTextEdit(Form)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFont(font)
        self.textEdit.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"border: 1px solid #d6d6d6;\n"
"}")

        self.horizontalLayout.addWidget(self.textEdit)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.inputImg.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u56fe\u7247", None))
        self.inputVideo.setText(QCoreApplication.translate("Form", u"\u5bfc\u5165\u89c6\u9891", None))
        self.startButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb", None))
        self.stopButton.setText(QCoreApplication.translate("Form", u"\u505c\u6b62", None))
        self.video.setText(QCoreApplication.translate("Form", u"\u8bf7\u70b9\u51fb\u4e0a\u9762\u6309\u94ae\u5bfc\u5165\u56fe\u7247", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; -qt-user-state:65536;\"><span style=\" font-size:9pt;\">\u5207\u5272\u6807\u51c6\uff1a</span></p></body></html>", None))
    # retranslateUi

