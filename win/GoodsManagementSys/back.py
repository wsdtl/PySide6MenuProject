# This Python file uses the following encoding: utf-8
import re
from datetime import datetime
from math import ceil
from PySide6.QtGui import Qt
from PySide6.QtWidgets import (
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QHeaderView,
    QAbstractItemView,
    QComboBox,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QLineEdit,
    QSplitter,
    QMessageBox,
)
from PySide6.QtCore import Signal
from sqlalchemy import select, and_

from .sql import SELECT, ALL_TABLE, UPDATE, INSERT



class BackTableGoods(QTableWidget):
    def __init__(
        self,
        parent: "QWidget",
        FindSingal: "Signal",
        ChooseSingal: "Signal",
        IndexSingal: "Signal",
        BackSingal="Signal",
    ):
        super().__init__(parent)
        # 定义信号
        self.ChooseSingal = ChooseSingal
        self.FindSingal = FindSingal
        self.IndexSingal = IndexSingal
        self.BackSingal = BackSingal
        # 绑定槽
        self.FindSingal.connect(self.OnFindSingal)
        self.IndexSingal.connect(self.update_table)
        self.BackSingal.connect(self.OnBackSingal)
        # 将表格变为禁止编辑
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格整行选中
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 自适应宽度
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 表格头的显示与隐藏
        self.verticalHeader().setVisible(False)
        # 清除分割线
        self.setShowGrid(False)
        # 隔行变色
        self.setAlternatingRowColors(True)
        self.setObjectName("BackTableGoods")
        self.setStyleSheet(
            """
            QTableWidget#BackTableGoods{
                outline: none;
            }
            QTableWidget#BackTableGoods::item:selected
            {
                background-color: #1ecc94; 
            }
        """
        )

        self.clicked.connect(self.choose)

    def OnBackSingal(self):
        # 清空表格
        self.setRowCount(0)
        self.setColumnCount(0)
        self.data = None
        self.IndexSingal.emit("table", 0)

    def OnFindSingal(self, msg: str):
        if msg:
            query = select(ALL_TABLE["goods_out"]).filter(
                and_(
                    ALL_TABLE["goods_out"].c["货物名称"].regexp_match(msg),
                    ALL_TABLE["goods_out"].c["数量"] > 0,
                )
            )
        else:
            query = select(ALL_TABLE["goods_out"]).filter(
                ALL_TABLE["goods_out"].c["数量"] > 0
            )
        self.data = SELECT(query, True)
        if self.data:
            self.page = 30
            self.row_long = len(self.data)
            self.column_long = len(self.data[0])
            self.IndexSingal.emit("table", ceil(self.row_long / self.page))
            self.update_table(sender="box", msg=1)

    def update_table(self, sender: str, msg: int):
        if sender == "box" and msg != 0:
            # 清空表格
            self.setRowCount(0)
            self.setColumnCount(0)
            page = self.page
            row_long = self.row_long
            column_long = self.column_long
            index = msg
            if row_long <= page:
                self.setRowCount(row_long)
                self.setColumnCount(column_long)
                self.setHorizontalHeaderLabels(self.data[0].keys())
                for i, values in enumerate(self.data):
                    for j, value in enumerate(values.values()):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.setItem(i, j, item)
            else:
                if index * page > row_long:
                    self.setRowCount(row_long % page)
                    data = self.data[(index - 1) * page :]
                else:
                    self.setRowCount(page)
                    data = self.data[(index - 1) * page : index * page]
                self.setColumnCount(column_long)

                self.setHorizontalHeaderLabels(self.data[0].keys())

                for i, values in enumerate(data):
                    for j, value in enumerate(values.values()):
                        item = QTableWidgetItem(str(value))
                        item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                        self.setItem(i, j, item)

    def choose(self):
        # 获取当前行 Index
        index = self.currentIndex().row()
        self.ChooseSingal.emit(
            {
                "出库编号": self.item(index, 0).text(),
                "货物名称": self.item(index, 2).text(),
                "上限": self.item(index, 3).text(),
                "货物编号": self.item(index, 1).text(),
            },
        )


class BackTableChoose(QTableWidget):

    def __init__(
        self,
        parent: "QWidget",
        ChooseSingal: "Signal",
        ClearSingal: "Signal",
        BackSingal: "Signal",
    ):
        super().__init__(parent)
        # 定义信号
        self.ChooseSingal = ChooseSingal
        self.ClearSingal = ClearSingal
        self.BackSingal = BackSingal
        # 绑定槽
        self.ChooseSingal.connect(self.OnChooseSingal)
        self.ClearSingal.connect(self.OnClearSingal)
        self.BackSingal.connect(self.OnBackSingal)
        # 将表格变为禁止编辑
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 设置表格整行选中
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 自适应宽度
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # 表格头的显示与隐藏
        self.verticalHeader().setVisible(False)
        # 清除分割线
        self.setShowGrid(False)
        # 隔行变色
        self.setAlternatingRowColors(True)
        self.setObjectName("BackTableChoose")
        self.setStyleSheet(
            """
            QTableWidget#BackTableChoose{
                outline: none;
            }
            QTableWidget#BackTableChoose::item:selected
            {
                background-color: #1ecc94; 
            }
        """
        )
        # 物品字典
        self.goods_dict = dict()
        self.clicked.connect(self.choose)

    def choose(self):
        # 获取当前行 Index
        index = self.currentIndex().row()
        out_id = self.item(index, 3).text()
        self.goods_dict[out_id]["数量"] -= 1
        if self.goods_dict[out_id]["数量"] <= 0:
            self.goods_dict.pop(out_id)
        self.updata_table()

    def OnChooseSingal(self, msg: dict):

        if msg["出库编号"] in self.goods_dict:
            if self.goods_dict[msg["出库编号"]]["数量"] < int(msg["上限"]):
                self.goods_dict[msg["出库编号"]]["数量"] += 1
                self.updata_table()
            else:
                QMessageBox.critical(
                    self,
                    "出现问题",
                    "超过归还上线！！！",
                    buttons=QMessageBox.Ok | QMessageBox.Cancel,
                )
        else:
            self.goods_dict[msg["出库编号"]] = {
                "数量": 1,
                "货物名称": msg["货物名称"],
                "货物编号": msg["货物编号"],
                "出库编号":msg["出库编号"],
            }
            self.updata_table()

    def OnClearSingal(self):
        # 清空表格
        self.setRowCount(0)
        self.setColumnCount(0)
        self.goods_dict = dict()

    def OnBackSingal(self):
        if self.goods_dict:
            for x in self.goods_dict:
                query = (
                    ALL_TABLE["goods_base"]
                    .update()
                    .where(ALL_TABLE["goods_base"].c["货物编号"] == int(self.goods_dict[x]["货物编号"]))
                    .values(
                        {
                            "数量": ALL_TABLE["goods_base"].c["数量"]
                            + self.goods_dict[x]["数量"]
                        }
                    )
                )
                UPDATE(query)
                query = (
                    ALL_TABLE["goods_out"]
                    .update()
                    .where(ALL_TABLE["goods_out"].c["出库编号"] == int(self.goods_dict[x]["出库编号"]))
                    .values(
                        {
                            "数量": ALL_TABLE["goods_out"].c["数量"]
                            - self.goods_dict[x]["数量"]
                        }
                    )
                )
                UPDATE(query)
                query = (
                    ALL_TABLE["goods_in"]
                    .insert()
                    .values(
                        {
                            "货物编号": int(self.goods_dict[x]["货物编号"]),
                            "货物名称": self.goods_dict[x]["货物名称"],
                            "数量": self.goods_dict[x]["数量"],
                            "日期": datetime.now(),
                        }
                    )
                )
                INSERT(query)

        self.goods_dict = dict()
        self.OnClearSingal()

    def updata_table(self):

        if self.goods_dict:
            self.setRowCount(len(self.goods_dict))
            self.setColumnCount(
                len(list(self.goods_dict[list(self.goods_dict.keys())[0]].keys()))
            )
            self.setHorizontalHeaderLabels(
                self.goods_dict[list(self.goods_dict.keys())[0]].keys()
            )

            for i, values in enumerate(self.goods_dict):
                for j, value in enumerate(self.goods_dict[values].values()):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.setItem(i, j, item)
        else:
            # 清空表格
            self.setRowCount(0)
            self.setColumnCount(0)


class BackTableQwidget(QWidget):

    ChooseSingal = Signal(dict)
    FindSingal = Signal(str)
    ClearSingal = Signal()
    BackSingal = Signal()
    IndexSingal = Signal(str, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)

        self.layout_top = QHBoxLayout()
        self.find = QLineEdit()
        self.find.setFixedWidth(200)
        self.but_find = QPushButton(text="查找")
        self.but_find.setFixedWidth(100)
        self.Box = QComboBox()
        self.Box.setFixedWidth(100)
        self.but_clear = QPushButton(text="清空")
        self.but_clear.setFixedWidth(100)
        self.but_back = QPushButton(text="归还")
        self.but_back.setFixedWidth(100)
        self.layout_top.addWidget(self.find)
        self.layout_top.addWidget(self.but_find)
        self.layout_top.addWidget(self.Box)
        self.layout_top.addStretch()
        self.layout_top.addWidget(self.but_clear)
        self.layout_top.addWidget(self.but_back)
        self.layout.addLayout(self.layout_top)

        self.layout_bottom = QHBoxLayout()
        self.table_goods = BackTableGoods(
            self,
            FindSingal=self.FindSingal,
            ChooseSingal=self.ChooseSingal,
            IndexSingal=self.IndexSingal,
            BackSingal=self.BackSingal,
        )
        self.table_choose = BackTableChoose(
            self,
            ChooseSingal=self.ChooseSingal,
            ClearSingal=self.ClearSingal,
            BackSingal=self.BackSingal,
        )
        # 创建一个垂直方向的分割器
        self.splitter = QSplitter(Qt.Orientation.Horizontal)
        self.splitter.addWidget(self.table_goods)
        self.splitter.addWidget(self.table_choose)
        self.splitter.setSizes([650, 500])
        self.layout_bottom.addWidget(self.splitter)
        self.layout.addLayout(self.layout_bottom)
        # 绑定信号
        self.but_find.clicked.connect(lambda: self.FindSingal.emit(self.find.text()))
        self.but_clear.clicked.connect(lambda: self.ClearSingal.emit())
        self.but_back.clicked.connect(lambda: self.BackSingal.emit())
        # 索引变化时触发
        self.Box.currentIndexChanged.connect(
            lambda: self.IndexSingal.emit(
                "box",
                int(
                    re.findall(r"\d+", self.Box.currentText())[0]
                    if self.Box.currentText()
                    else 0
                ),
            )
        )
        self.IndexSingal.connect(self.update_box)

    def update_box(self, sender: str, msg: int):
        if sender == "table":
            self.Box.clear()
            if msg:
                self.Box.addItems(["第" + str(x + 1) + "页" for x in range(msg)])

