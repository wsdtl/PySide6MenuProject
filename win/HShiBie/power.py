# -*- coding: utf-8 -*-
import cv2
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap, QHideEvent

from .main import Ui_Form


class HShiBie(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.timer_camera = QTimer()
        self.video = None
        self.time_space = 25
        
        self.ui.startButton.clicked.connect(self.btnStart)
        self.ui.stopButton.clicked.connect(self.btnStop)

        self.ui.inputVideo.clicked.connect(self.openVedio)
        self.ui.inputImg.clicked.connect(self.openImg)
        
        
    def btnStart(self):
        # 定时器开启，每隔一段时间，读取一帧
        self.timer_camera.start(self.time_space)
        self.timer_camera.timeout.connect(self.openFrame)
 
    def btnStop(self):
        self.timer_camera.stop()
 
    def openVedio(self) -> None:
        fileUrl, _ = QFileDialog.getOpenFileName(self, "选择视频文件", filter = "video files(*.mp4 *.avi)")
        if fileUrl:
            self.video = cv2.VideoCapture(fileUrl)
            self.openFrame()
                
    def openImg(self) -> None:
        self.video = None
        fileUrl, _ = QFileDialog.getOpenFileName(self, "选择图片文件", filter = "image files(*.jpg *.png)")
        if fileUrl:
            self.ui.video.setPixmap(QPixmap(fileUrl).scaled(
            self.ui.video.width() - 15, 
            self.ui.video.height() - 15, 
            Qt.KeepAspectRatio 
        ))
        self.ui.video.setAlignment(Qt.AlignCenter)
        self.ui.video.show()
 
    def openFrame(self) -> None:
        # 设置帧速率为 45 fps
        if self.video:
            self.video.set(cv2.CAP_PROP_FPS, 45)
            ret, image = self.video.read()
            if ret:
                if len(image.shape) == 3:
                    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                    vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
                elif len(image.shape) == 1:
                    vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_Indexed8)
                else:
                    vedio_img = QImage(image.data, image.shape[1], image.shape[0], QImage.Format_RGB888)
    
                self.ui.video.setPixmap(QPixmap(vedio_img).scaled(
                    self.ui.video.width() - 15, 
                    self.ui.video.height() - 15, 
                    Qt.KeepAspectRatio 
                ))
                self.ui.video.setAlignment(Qt.AlignCenter)
            else:
                self.video = None
                self.timer_camera.stop()
            
    def hideEvent(self, event: QHideEvent) -> None:
        self.btnStop()
        return super().hideEvent(event)