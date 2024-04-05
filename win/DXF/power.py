# -*- coding: utf-8 -*-
import dxfgrabber
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from math import sin, cos, pi
from pathlib import Path
from .main import Ui_Form
from XNPySide6Menu.mainwindow import MainWindow

from ezdxf import recover
from ezdxf import DXFStructureError
from ezdxf.addons.drawing import RenderContext, Frontend
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend


class DxfGCode():
    
    def __init__(self, path: str) -> None:
        self.dxfData = []
        self.GCore = ""
        self.dxf = dxfgrabber.readfile(Path(path))
        self.getDxfData()
    
    def getDxfData(self) -> None:
        for e in self.dxf.entities:
            if e.dxftype == "LINE":
                data = {
                    "type": e.dxftype,
                    "x_start": round(e.start[0], 4),
                    "y_start": round(e.start[1], 4),
                    "x_end": round(e.end[0], 4),
                    "y_end": round(e.end[1], 4)
                }
                self.dxfData.append(data)
            if e.dxftype == "ARC":
                x_start, y_start, x_end, y_end = self.centerToxy(e.center[0], e.center[1], e.radius, abs(e.end_angle - e.start_angle))
                data = {
                    "type": e.dxftype,
                    "x_start": round(x_start, 4),
                    "y_start": round(y_start, 4),
                    "x_end": round(x_end, 4),
                    "y_end":round(y_end, 4),
                    "r":round(e.radius, 4)
                }
                self.dxfData.append(data)

    def toGcode(self, deep: int = 5, speed: int = 1000) -> str:
        gcode = "G90\nG01 Z30\n"
        try:
            if self.dxfData[0]["type"] == "LINE":
                gcode += f"G01 X{self.dxfData[0]['x_start']} Y{self.dxfData[0]['y_start']} F{speed}\n"
                gcode += f"G01 Z-{deep}\n"
                gcode += f"G01 X{self.dxfData[0]['x_end']} Y{self.dxfData[0]['y_end']}\n"
            elif self.dxfData[0]["type"] == "ARC":
                gcode += f"G01 X{self.dxfData[0]['x_start']} Y{self.dxfData[0]['y_start']} F{speed}\n" 
                gcode += f"G01 Z-{deep}\n"
                gcode += f"G02 X{self.dxfData[0]['x_end']} Y{self.dxfData[0]['y_end']} R{self.dxfData[0]['r']}\n"
            else:
                gcode += f"G01 Z-{deep}\n"
        except:
            gcode += f"G01 Z-{deep}\n"
            
        for data in self.dxfData: 
            if data["type"] == "LINE":
                # gcode += f"G01 X{d['x_start']} Y{d['y_start']}\n"
                gcode += f"G01 X{data['x_end']} Y{data['y_end']}\n"
            elif data["type"] == "ARC":
                gcode += f"G01 X{data['x_start']} Y{data['y_start']}\n" 
                gcode += f"G02 X{data['x_end']} Y{data['y_end']} R{data['r']}\n"
            else:
                pass
        return gcode.strip()
        
    def centerToxy(self, x_center: float, y_center: float, r: float, rad: float) -> set:
        rad = rad / 180
        x_start = r * cos(rad)
        y_start = r * sin(rad)
        x_end = r * cos(pi + rad)
        y_end = r * sin(pi + rad)
        return round(x_start + x_center, 4), round(y_start + y_center, 4), round(x_end + x_center, 4), round(y_end + y_center,4)


class DXF(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dxfPath = ""
        
        self.ui.setDxfButton.clicked.connect(self.getDxfPath)
        self.ui.gCodeButton.clicked.connect(self.goGCode)
        self.ui.saveGCodeButton.clicked.connect(self.saveGCode)
    
    def DxfImage(self, destination_name):
        try:
            doc, auditor = recover.readfile(Path(self.dxfPath))
        except IOError as e:
            MainWindow.add_popup("读取失败", flag = "warning")
            raise IOError("Not a DXF file or a generic I/O error.") from e
        except DXFStructureError as e:
            MainWindow.add_popup("读取失败", flag = "warning")
            raise DXFStructureError("Invalid or corrupted DXF file.") from e
        # The auditor.errors attribute stores severe errors,
        # which may raise exceptions when rendering.
        if not auditor.has_errors:
            fig = plt.figure()
            ax = fig.add_axes([0, 0, 1, 1])
            ctx = RenderContext(doc)
            out = MatplotlibBackend(ax)
            Frontend(ctx, out).draw_layout(doc.modelspace(), finalize=True)
            fig.savefig(destination_name, dpi=300)  
        MainWindow.add_popup("读取成功")
        
    def getDxfPath(self) -> None:
        fileUrl, _ = QFileDialog.getOpenFileName(self, "选择一个DXF文件", filter = "DXF(*.dxf)")
        if fileUrl:
            self.dxfPath = fileUrl
            self.DxfImage("dxf_output.jpg")
            pixmap = QPixmap("dxf_output.jpg").scaled(
                self.ui.img.width() - 15, 
                self.ui.img.height() - 15, Qt.KeepAspectRatio
            )
            # self.ui.img.setScaledContents(True)
            self.ui.img.setAlignment(Qt.AlignCenter)
            self.ui.img.setPixmap(pixmap)
            self.ui.img.show()
                    
    def goGCode(self) -> None:
        if self.dxfPath:
            try: 
                deep = int(self.ui.deepEdit.text())
            except:
                deep = 5
            try: 
                speed = int(self.ui.speedEdit.text())
            except:
                speed = 1000
            # 鼠标繁忙
            self.setCursor(Qt.BusyCursor)
            text = DxfGCode(self.dxfPath).toGcode(deep, speed)
            self.ui.gcode.setText(text)
            self.ui.gcode.ensureCursorVisible()  # 每次添加文本光标都在最后一行
            # 鼠标恢复
            self.setCursor(Qt.ArrowCursor)    
    
    def saveGCode(self) -> None:
        fileUrl, _ = QFileDialog.getSaveFileName(self, "文件保存", filter = "txt(*.txt)")
        if fileUrl:
            with open(Path(fileUrl), "w", encoding= "utf-8") as f:
                f.write(self.ui.gcode.toPlainText())
