from NIWENV import *

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...
from PySide2.QtGui import QImage, QPixmap

from PySide2.QtWidgets import QLabel

import cv2


class %CLASS%(QLabel, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QLabel.__init__(self)

        self.resize(200, 200)
        self.maxsize = (10, 5)
    
    def set_max_size(self, maxsize):
        self.maxsize = maxsize
    
    def show_image(self, cv_image):
        self.resize(200, 200)
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)
        img_w = self.maxsize[0] #min(self.maxsize[1], qt_image.width())
        img_h = self.maxsize[1] #min(self.maxsize[0], qt_image.height())
        print("img: " + str(img_w) + ", " + str(img_h))
        proportion = img_w / img_h
        #self.resize(self.width() * proportion, self.height)
        self.resize(img_w, img_h)
        qt_image = qt_image.scaled(img_w, img_h)
        self.setPixmap(QPixmap(qt_image))
        self.parent_node_instance.update_shape()

    def get_data(self):
        return self.text()

    def set_data(self, data):
        self.setText(data)


    def remove_event(self):
        pass
