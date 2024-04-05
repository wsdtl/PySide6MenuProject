# -*- coding: utf-8 -*-
from .main import Ui_Form
from PySide6.QtWidgets import QWidget

class FRID(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
