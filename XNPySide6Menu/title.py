from typing import TYPE_CHECKING
from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import QSize, QEvent
from PySide6.QtGui import (
    Qt,
    QPixmap,
    QIcon,
    QColor,
    QPaintEvent,
    QPainter,
    QEnterEvent,
    QMouseEvent,
    QFontMetrics,
)

from .menu_index import MenuLeftSideFirst

if TYPE_CHECKING:
    from mainwindow import MainWindow


class TitlePushButtonMax(QPushButton):
    """最大化按钮

    参数:
        parent (MainWindow): MainWindow窗口, 用于控制其是否最大化.
    """

    def __init__(self, parent: "MainWindow") -> None:
        super().__init__()
        self.setFixedSize(30, 30)
        self.icon_max = QIcon()
        self.icon_max.addFile(":image/max.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_max.addFile(":image/max.svg", QSize(), QIcon.Normal, QIcon.On)
        self.setIcon(self.icon_max)

        self.icon_max_press = QIcon()
        self.icon_max_press.addFile(
            ":image/max_press.svg", QSize(), QIcon.Normal, QIcon.Off
        )
        self.icon_max_press.addFile(
            ":image/max_press.svg", QSize(), QIcon.Normal, QIcon.On
        )

        self.setObjectName("TitlePushButtonMax")
        self.setStyleSheet(
            """
        QPushButton#TitlePushButtonMax 
        {
            border-radius: 0px;
        }
        QPushButton#TitlePushButtonMax:hover 
        {
            border-radius: 5px;
            background-color: #69e6bd;
        }        
        """
        )

        self._parent = parent
        self._falg = False
        self.clicked.connect(self._MaxState)

    def _MaxState(self):
        """设置MainWindow窗口窗口最大化状态"""
        if self._parent.isMaximized():
            self._parent.showNormal()
            self.setIcon(self.icon_max)
        else:
            self._parent.showMaximized()
            self.setIcon(self.icon_max_press)

    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)


class TitlePushButtonMin(QPushButton):
    """最小化按钮

    参数:
        parent (QWidget): MainWindowc窗口, 用于控制其是否最小化.
    """

    def __init__(self, parent: "MainWindow") -> None:
        super().__init__()
        self.setFixedSize(30, 30)
        self.icon_max = QIcon()
        self.icon_max.addFile(":image/min.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_max.addFile(":image/min.svg", QSize(), QIcon.Normal, QIcon.On)
        self.setIcon(self.icon_max)
        self.setObjectName("TitlePushButtonMin")
        self.setStyleSheet(
            """
        QPushButton#TitlePushButtonMin 
        {
            border-radius: 0px;
        }
        QPushButton#TitlePushButtonMin:hover 
        {
            border-radius: 5px;
            background-color: #69e6bd;
        }        
        """
        )

        self._falg = False
        self.clicked.connect(lambda: parent.showMinimized())

    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)


class TitlePushButtonExit(QPushButton):
    """关闭退出按钮

    参数:
        parent (QWidget): MainWindowc窗口, 用于控制其是否关闭退出.
    """

    def __init__(self, parent: "MainWindow") -> None:
        super().__init__()
        self.setFixedSize(30, 30)
        self.icon_max = QIcon()
        self.icon_max.addFile(":image/exit.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.icon_max.addFile(":image/exit.svg", QSize(), QIcon.Normal, QIcon.On)
        self.setIcon(self.icon_max)
        self.setObjectName("TitlePushButtonExit")
        self.setStyleSheet(
            """
        QPushButton#TitlePushButtonExit 
        {
            border-radius: 0px;
        }
        QPushButton#TitlePushButtonExit:hover 
        {
            border-radius: 5px;
            background-color: #69e6bd;
        }        
        """
        )

        self._falg = False
        self.clicked.connect(lambda: parent.close())

    def enterEvent(self, event: QEnterEvent) -> None:
        """鼠标进入事件

        参数:
            event (QEnterEvent): QEnterEvent

        返回:
            _type_: super().enterEvent(event)
        """
        self._falg = True
        return super().enterEvent(event)

    def leaveEvent(self, event: QEvent) -> None:
        """鼠标离开事件

        参数:
            event (QEvent): QEvent

        返回:
            _type_: super().leaveEvent(event)
        """
        self._falg = False
        return super().leaveEvent(event)


class MyTip(QWidget):
    """MainWindow上方标题栏

    参数:
        parent (MainWindow): MainWindow窗口
    """

    _h = 60

    def __init__(self, parent: "MainWindow") -> None:
        super().__init__()
        self.setFixedHeight(MyTip._h)
        self.moveFlag = False
        self._parent = parent
        self._logo = QPixmap(":/image/logo.png")
        self.layout = QHBoxLayout(self)

        self.layout.addStretch(1)
        self.layout.addWidget(TitlePushButtonMin(parent))
        self.layout.addWidget(TitlePushButtonMax(parent))
        self.layout.addWidget(TitlePushButtonExit(parent))
        self.layout.addSpacing(10)

    def paintEvent(self, event: QPaintEvent) -> None:
        """重绘事件

        参数:
            event (QPaintEvent): _description_
        """
        painter = QPainter(self)
        painter.setRenderHints(QPainter.Antialiasing | QPainter.TextAntialiasing)
        self.draw(event, painter)

    def draw(self, event: QPaintEvent, painter: QPainter) -> None:
        """重绘事件方法

        参数:
            event (QPaintEvent): QPaintEvent\n
            painter (QPainter): QPainter
        """

        painter.setPen(Qt.NoPen)
        w = MenuLeftSideFirst._w + 10
        h = self.height()

        painter.drawRect(0, 0, w, h)
        painter.setBrush(QColor("#f0f0f0"))

        painter.drawRect(0, 0, w, h)
        painter.drawPixmap(
            (w - self._logo.width()) // 2,
            (h - self._logo.height()) // 2,
            self._logo.width(),
            self._logo.height(),
            self._logo,
        )

        # textFont = QFont('Microsoft YaHei UI', 16)
        # painter.setFont(textFont)
        # painter.setPen(QColor("#000000"))
        # txt = ""
        # painter.drawText(
        #     QRect(MenuLeftSideFirst._w + 30, 5, QFontMetrics(textFont).horizontalAdvance(txt) * 1.5, MenuLeftSideFirst._h),
        #     txt,
        #     Qt.AlignLeft
        # )

    def mousePressEvent(self, event: QMouseEvent) -> None:
        """鼠标按下事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        if self._parent.isMaximized():
            self._parent._showNormal(event.globalPosition().toPoint())
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.pos_star = event.globalPosition().toPoint()
            self.win_pos = self._parent.pos()

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        """鼠标移动事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        if self.moveFlag:
            self._parent.move(
                self.win_pos + event.globalPosition().toPoint() - self.pos_star
            )

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """鼠标释放事件

        参数:
            event (QMouseEvent): QMouseEvent
        """
        self.moveFlag = False
