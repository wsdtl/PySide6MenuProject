from typing import List, TYPE_CHECKING, Callable, Union
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QPaintEvent, QIcon
from PySide6.QtWidgets import (
    QStackedWidget,
    QWidget,
    QListWidget,
    QVBoxLayout,
    QListWidgetItem,
    QPushButton,
    QButtonGroup
)

from . import rc

if TYPE_CHECKING:
    from mainwindow import MainWindow


class PushButton(QPushButton):
    """菜单按钮父类

    参数:
        son (_type_): 子类对象，用于实现排它
    """

    _group = QButtonGroup()

    def __init__(self, son) -> None:
        super().__init__()
        PushButton._group.addButton(son)


class MenuLeftSideFirst(PushButton):
    """一级菜单

    参数:
        text (str): 菜单文本\n
        icon (str): 菜单图标\n
        icon_press (str): 菜单图标
    """

    _w: int = 170
    _h: int = 50

    def __init__(
        self,
        text: str,
        icon: str,
        icon_press: str,
    ) -> None:
        super().__init__(self)
        self._text = " " + text

        self._icon = QIcon()
        self._icon.addFile("{}".format(icon), QSize(), QIcon.Normal, QIcon.Off)
        self._icon.addFile("{}".format(icon), QSize(), QIcon.Selected, QIcon.Off)
        self._icon.addFile("{}".format(icon_press), QSize(), QIcon.Active, QIcon.On)
        self.setIcon(self._icon)
        self.setIconSize(QSize(20, 20))
        self.setText(self._text)

        self.setFixedSize(QSize(self._w - 10, self._h - 10))
        self.setCheckable(True)  # 设置可以被选中
        self.setAutoExclusive(True)  # 设置自动排它
        self.setObjectName("MenuLeftSideFirst")
        self.setStyleSheet(
            """
        QPushButton#MenuLeftSideFirst 
        {
            border-radius: 0px;
            padding-left: 8px;
            padding-top: 10px;
            padding-right: 5px;
            padding-bottom: 10px;
            text-align: left;
            font: normal normal 16px "Microsoft YaHei UI";
        }
        QPushButton#MenuLeftSideFirst:hover 
        {
            border-left: 2px solid #1ecc94;
        }
        QPushButton#MenuLeftSideFirst:checked     
        {
            border-radius: 5px;
            background-color: #1ecc94;
            color: #ffffff;
        }         
        """
        )

    def text(self) -> str:
        """获得菜单文本

        返回:
            str: 文本
        """
        return self._text


class MenuLeftSideSecondary(PushButton):
    """二级菜单

    参数:
        text (str): 菜单文本\n
        sign_func (MainWindow.display): 菜单按下后触发函数
    """

    _w: int = 170
    _h: int = 50

    def __init__(self, text: str, sign_func: "MainWindow.display") -> None:
        super().__init__(self)
        # self._text = " " + text
        self._text = text
        self._sign_func = sign_func

        self._icon = QIcon()
        self._icon.addFile(":image/arrow.svg", QSize(), QIcon.Normal, QIcon.Off)
        self._icon.addFile(":image/arrow.svg", QSize(), QIcon.Normal, QIcon.On)
        self._icon.addFile(":image/arrow_press.svg", QSize(), QIcon.Selected, QIcon.Off)
        self._icon.addFile(":image/arrow_press.svg", QSize(), QIcon.Active, QIcon.Off)
        self.setIcon(self._icon)
        self.setIconSize(QSize(16, 16))
        self.setText("  " + self._text)

        self.setFixedSize(QSize(self._w - 10, self._h - 10))
        self.setCheckable(True)  # 设置可以被选中
        self.setAutoExclusive(True)  # 设置自动排它
        self.setObjectName("MenuLeftSideSecondary")
        self.setStyleSheet(
        """
        QPushButton#MenuLeftSideSecondary 
        {
            border-radius: 0px;
            padding-left: 10px;
            padding-top: 10px;
            padding-right: 5px;
            padding-bottom: 10px;
            text-align: left;
            font: normal normal 14px "Microsoft YaHei UI";
        }
        QPushButton#MenuLeftSideSecondary:hover 
        {
            border-left: 2px solid #1ecc94;
            color: #1ecc94;
        }
        QPushButton#MenuLeftSideSecondary:checked     
        {
            border-radius: 5px;
            background-color: #1ecc94;
            color: #ffffff;
        }         
        """
        )
        self.clicked.connect(lambda: self._sign_func(self.text()))

    def text(self) -> str:
        """获得菜单文本

        返回:
            str: 文本
        """
        return self._text


class MenuLeftSideSecondaryList:
    """菜单列表生成函数

    参数:
        list_widget (QListWidget): 存储一二级菜单的QListWidget控件对象\n
        menu_main (MenuLeftSideFirst): 一级菜单实例\n
        menu_name (List[str]): 二级菜单名字\n
        sign_func (MainWindow.display): 二级菜单按下触发函数
    """

    _item_hidden = list()
    _item_hidden_num = None

    def __init__(
        self,
        list_widget: QListWidget,
        menu_main: MenuLeftSideFirst,
        menu_name: List[str],
        sign_func: "MainWindow.display",
    ) -> None:
        super().__init__()
        self._list_widget = list_widget
        self._menu_name = menu_name
        self._sign_func = sign_func
        self._num = len(self._menu_name)

        menu_main_widget = QWidget()
        menu_main_widget.setFixedSize(menu_main._w, menu_main._h)
        layout = QVBoxLayout(menu_main_widget)
        layout.addWidget(menu_main)
        self.item_mian_nenu = QListWidgetItem(self._list_widget)
        self.item_mian_nenu.setSizeHint(QSize(menu_main._w, menu_main._h))

        self._list_widget.setItemWidget(self.item_mian_nenu, menu_main_widget)

        self.item = QListWidgetItem(self._list_widget)
        self.item.setHidden(True)
        MenuLeftSideSecondaryList._item_hidden.append(self.item)
        menu_main.clicked.connect(lambda: self.set_setHidden(self.item))

        self.init_menu()

    def init_menu(self) -> None:
        """二级菜单生成函数"""
        menu_widget = QWidget()
        menu_widget.setFixedSize(
            MenuLeftSideSecondary._w, MenuLeftSideSecondary._h * self._num
        )
        layout = QVBoxLayout(menu_widget)

        for x in range(self._num):
            button = MenuLeftSideSecondary(self._menu_name[x], self._sign_func)
            layout.addWidget(button)
        self.item.setSizeHint(QSize(menu_widget.width(), menu_widget.height()))
        self._list_widget.setItemWidget(self.item, menu_widget)

    @classmethod
    def set_setHidden(cls, item: QListWidgetItem) -> None:
        """设置按下菜单

        参数:
            item (QListWidgetItem): 二级菜单item控件, 其一级菜单按下后将显示展开, 默认隐藏不显示
        """
        if cls._item_hidden_num is None:
            item.setHidden(not item.isHidden())
            cls._item_hidden_num = cls._item_hidden.index(item)
        else:
            if cls._item_hidden_num != cls._item_hidden.index(item):
                item_old = cls._item_hidden[cls._item_hidden_num]
                item_old.setHidden(not item_old.isHidden())

                item.setHidden(not item.isHidden())
                cls._item_hidden_num = cls._item_hidden.index(item)
            else:
                item.setHidden(not item.isHidden())
                cls._item_hidden_num = None


class MenuLeftList(QListWidget):
    """存储菜单的QListWidget控件"""

    def __init__(self) -> None:
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setObjectName("MenuLeftList")
        self.setStyleSheet(
        """QListWidget#MenuLeftList
            {
                background-color: qlineargradient(x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #f0f0f0, stop:0.9 #f0f0f0, stop:1 #f6f6f6);
                border: none;
            }
        """
        )

    def paintEvent(self, event: QPaintEvent) -> None:
        """忽略自身重绘事件

        参数:
            event (QPaintEvent): QPaintEvent
        """
        event.ignore()


class StackedWidget(QStackedWidget):
    """存储页面的QStackedWidget 控件

    参数:
        widget_zero (QWidget): 欢迎界面
    """

    _wins_tuple = dict()

    def __init__(self, widget_zero: QWidget) -> None:
        super().__init__()
        num = super().addWidget(widget_zero)
        super().setCurrentIndex(num)
        StackedWidget._wins_tuple["wecome"] = widget_zero

    def addWidget(self, widget: Union[Callable, QWidget], name: str) -> None:
        """添加子页面

        参数:
            widget (Union[Callable, QWidget]): 子页面名字或实例\n
            name (str): 子页面名字
        """
        result = self.indexOf(name)
        if result == 0:
            if isinstance(widget, QWidget):
                widget_new = widget
            else:
                widget_new = widget()
            StackedWidget._wins_tuple[name] = widget_new
            num = super().addWidget(widget_new)
            super().setCurrentIndex(num)
        else:
            super().setCurrentIndex(result)

    def indexOf(self, name: str) -> int:
        """工具子页面名字查找页面id

        参数:
            name (str): 子页面名字

        异常:
            IndexError: 不能再次传入欢迎界面

        返回:
            int: 子页面id
        """
        if name == "wecome":
            raise IndexError("再次传入了首页")
        if name in StackedWidget._wins_tuple:
            return super().indexOf(StackedWidget._wins_tuple[name])
        else:
            return 0
