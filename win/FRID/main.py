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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(837, 659)
        Form.setMinimumSize(QSize(0, 30))
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 821, 641))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 0, 10, 0)
        self.horizontalLayout_connect = QHBoxLayout()
        self.horizontalLayout_connect.setObjectName(u"horizontalLayout_connect")
        self.change_com = QLabel(self.verticalLayoutWidget)
        self.change_com.setObjectName(u"change_com")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(80)
        sizePolicy.setVerticalStretch(25)
        sizePolicy.setHeightForWidth(self.change_com.sizePolicy().hasHeightForWidth())
        self.change_com.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.change_com)

        self.change_com_box = QComboBox(self.verticalLayoutWidget)
        self.change_com_box.setObjectName(u"change_com_box")
        sizePolicy.setHeightForWidth(self.change_com_box.sizePolicy().hasHeightForWidth())
        self.change_com_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.change_com_box)

        self.change_port = QLabel(self.verticalLayoutWidget)
        self.change_port.setObjectName(u"change_port")
        sizePolicy.setHeightForWidth(self.change_port.sizePolicy().hasHeightForWidth())
        self.change_port.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.change_port)

        self.change_port_box = QComboBox(self.verticalLayoutWidget)
        self.change_port_box.setObjectName(u"change_port_box")
        sizePolicy.setHeightForWidth(self.change_port_box.sizePolicy().hasHeightForWidth())
        self.change_port_box.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.change_port_box)

        self.horizontalSpacer = QSpacerItem(40, 30, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_connect.addItem(self.horizontalSpacer)

        self.connect_button = QPushButton(self.verticalLayoutWidget)
        self.connect_button.setObjectName(u"connect_button")
        sizePolicy.setHeightForWidth(self.connect_button.sizePolicy().hasHeightForWidth())
        self.connect_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.connect_button)

        self.disconnect_button = QPushButton(self.verticalLayoutWidget)
        self.disconnect_button.setObjectName(u"disconnect_button")
        sizePolicy.setHeightForWidth(self.disconnect_button.sizePolicy().hasHeightForWidth())
        self.disconnect_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_connect.addWidget(self.disconnect_button)


        self.verticalLayout.addLayout(self.horizontalLayout_connect)

        self.horizontalLayout_write = QHBoxLayout()
        self.horizontalLayout_write.setSpacing(6)
        self.horizontalLayout_write.setObjectName(u"horizontalLayout_write")
        self.write_box = QLineEdit(self.verticalLayoutWidget)
        self.write_box.setObjectName(u"write_box")
        self.write_box.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout_write.addWidget(self.write_box)

        self.write_button = QPushButton(self.verticalLayoutWidget)
        self.write_button.setObjectName(u"write_button")
        sizePolicy.setHeightForWidth(self.write_button.sizePolicy().hasHeightForWidth())
        self.write_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_write.addWidget(self.write_button)


        self.verticalLayout.addLayout(self.horizontalLayout_write)

        self.horizontalLayout_query = QHBoxLayout()
        self.horizontalLayout_query.setSpacing(6)
        self.horizontalLayout_query.setObjectName(u"horizontalLayout_query")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_query.addItem(self.horizontalSpacer_2)

        self.query_button = QPushButton(self.verticalLayoutWidget)
        self.query_button.setObjectName(u"query_button")
        sizePolicy.setHeightForWidth(self.query_button.sizePolicy().hasHeightForWidth())
        self.query_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_query.addWidget(self.query_button)

        self.querys_button = QPushButton(self.verticalLayoutWidget)
        self.querys_button.setObjectName(u"querys_button")
        sizePolicy.setHeightForWidth(self.querys_button.sizePolicy().hasHeightForWidth())
        self.querys_button.setSizePolicy(sizePolicy)

        self.horizontalLayout_query.addWidget(self.querys_button)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_query.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_query)

        self.tableView = QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setMinimumSize(QSize(0, 0))

        self.verticalLayout.addWidget(self.tableView)

        self.verticalSpacer = QSpacerItem(686, 3, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.log_box = QLabel(self.verticalLayoutWidget)
        self.log_box.setObjectName(u"log_box")
        self.log_box.setMinimumSize(QSize(0, 18))
        self.log_box.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.log_box)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.change_com.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u7aef\u53e3\u53f7", None))
        self.change_port.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6ce2\u7279\u7387", None))
        self.connect_button.setText(QCoreApplication.translate("Form", u"\u8fde\u63a5", None))
        self.disconnect_button.setText(QCoreApplication.translate("Form", u"\u65ad\u5f00\u8fde\u63a5", None))
        self.write_button.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.query_button.setText(QCoreApplication.translate("Form", u"\u5355\u6b21\u67e5\u8be2", None))
        self.querys_button.setText(QCoreApplication.translate("Form", u"\u8f6e\u8be2", None))
        self.log_box.setText(QCoreApplication.translate("Form", u"\u8bbe\u5907\u672a\u8fde\u63a5\uff01\uff01\uff01", None))
    # retranslateUi

