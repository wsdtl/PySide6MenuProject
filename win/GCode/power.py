# -*- coding: utf-8 -*-
from .main import Ui_Form
from PySide6.QtWidgets import QWidget, QFileDialog
from pathlib import Path

class GCode(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.ui.saveButton.clicked.connect(self.saveGCode)
        self.ui.openButton.clicked.connect(self.openGCode)
    
    def saveGCode(self) -> None:
        fileUrl, _ = QFileDialog.getSaveFileName(self, "文件保存", filter = "txt(*.txt)")
        if fileUrl:
            with open(Path(fileUrl), "w", encoding= "utf-8") as f:
                f.write(self.ui.textEdit.toPlainText())
        
    def openGCode(self) -> None:
        fileUrl, _ = QFileDialog.getOpenFileName(self, "选择一个TXT文件", filter = "TXT(*.txt)")
        if fileUrl:
            with open(Path(fileUrl), "r", encoding= "utf-8") as f:
                text = f.read()
                self.ui.textEdit.setText(text)