from NIENV import *


# API METHODS --------------

# self.main_widget
# self.update_shape()

# Ports
# self.input(index)
# self.set_output_val(index, val)
# self.exec_output(index)

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index)

# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', target='global')
# self.log_message('that\'s not good', target='error')

# --------------------------

import numpy as np
import math
class %CLASS%(NodeInstance):
#class OrientingTest:
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.resolution = 3
        self.field = np.zeros((self.resolution))
        self.pos = 0
        self.initpos = 0
        self.distance = 0
        self.inputs = {
            "rotateleft":0,
            "rotateright":1,
            "forward":2,
            "resolution":3,
            "distance":4,
            "initpos":5,

        }

    def rotate_left(self, aval):
        self.pos = min(self.resolution-1, self.pos + aval)
        self.update()
        
    def rotate_right(self, aval):
        self.pos = max(0, self.pos - aval)
        self.update()

    def forward(self, aval):
        self.distance = max(0, self.distance - aval)

    def set_resolution(self, aval):
        self.resolution = int(aval)
        self.pos = min(self.resolution, self.pos)
        self.update()
        
    def set_distance(self, aval):
        self.distance = max(0, aval)

    def set_initpos(self, aval):
        self.initpos = aval
        self.pos = self.initpos
        self.update()
    
    def update(self):
        self.field = np.zeros(self.resolution)
        self.field[int(round(self.pos))] = 1

    def sigmoid(self, p):
        return 1 / (1 + math.exp(-p))

    def get_output(self):
        return self.field * (1 - self.sigmoid(self.distance))


    def update_event(self, input_called=-1):
        # if self.resolution != self.input(self.inputs["resolution"]):
        #     self.set_resolution(self.resolution)
        # self.
        # self.rotate_left(self.input(self.inputs["rotateleft"]))
        # self.rotate_right(self.input(self.inputs["rotateright"]))
        # self.forward(self.input(self.inputs["forward"]))
        # self.set_output_val(0, self.get_output())
        pass

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass

if __name__ == '__main__':
    tst = OrientingTest(params=[])
    tst.set_resolution(7)
    tst.set_distance(4.0)
    tst.set_initpos(1)
    print('init: ' + str(tst.get_output()))
    for i in range(4):
        
        tst.rotate_left(1)
        tst.forward(0.4)
        a = tst.get_output()
        print (str(i) + ': ' + str(a))
    print()
    for i in range(4):
        
        tst.rotate_right(1)
        a = tst.get_output()
        print (str(i) + ': ' + str(a))