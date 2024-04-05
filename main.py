# -*- coding: utf-8 -*-
import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from XNPySide6Menu import MainWindow

from win import HShiBie
from win import DXF
from win import GCode
from win import FRID


class Window(MainWindow):

    def __init__(self) -> None:
        super().__init__()
        # 设置软件logo
        self.setWindowIcon(QPixmap(":image/icon.png"))
        # 添加菜单
        self.addMuen(
            "钢结构工具集",
            ":image/set.svg",
            ":image/set_press.svg",
            ["H型钢识别界面", "DXF导入界面", "G代码保存界面", "FRID"]
        )
        # 添加窗口
        self.addWidget(HShiBie, "H型钢识别界面")
        self.addWidget(DXF, "DXF导入界面")
        self.addWidget(GCode, "G代码保存界面")
        self.addWidget(FRID, "FRID")


if __name__ == "__main__":
    
    # 解决界面模糊问题--解决电脑缩放比例问题
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    windows = Window()
    windows.show()
    sys.exit(app.exec())
