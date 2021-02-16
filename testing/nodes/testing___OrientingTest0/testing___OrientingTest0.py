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
class OrientingTest_NodeInstance(NodeInstance):
#class OrientingTest:
    def __init__(self, params):
        super(OrientingTest_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.resolution = 3
        self.field = np.zeros((self.resolution))
        self.ix = 0
        self.init_pos = 0
        self.distance = 0
        self.init_distance = 0
        self.input_names = {
            "rotateleft":0,
            "rotateright":1,
            "forward":2,
            "resolution":3,
            "init_distance":4,
            "init_pos":5,

        }

    def rotate_left(self, aval):
        self.ix = min(self.resolution-1, self.ix + aval)
        self.update_field()
        
    def rotate_right(self, aval):
        self.ix = max(0, self.ix - aval)
        self.update_field()

    def forward(self, aval):
        self.distance = max(0, self.distance - aval)

    def set_resolution(self, aval):
        self.resolution = int(aval)
        self.ix = min(self.resolution, self.ix)
        self.update_field()
        
    def set_init_distance(self, aval):
        self.init_distance = float(max(0, aval))
        self.distance = self.init_distance

    def set_init_pos(self, aval):
        self.init_pos = aval
        self.ix = self.init_pos
        self.update_field()
    
    def update_field(self):
        self.field = np.zeros((self.resolution))
        self.field[int(round(self.ix))] = 1

    def sigmoid(self, p):
        # expit: (crosses at 0.5)
        #return 1.0 / (1.0 + math.exp(-p))
        # tanh; (crosses at 0)
        return (math.exp(p)-math.exp(-p))/(math.exp(-p) + math.exp(p))

    def get_output(self):
        return self.field * (1 - self.sigmoid(self.distance))


    def update_event(self, input_called=-1):
        rotleft = self.input(self.input_names["rotateleft"]) 
        rotright = self.input(self.input_names["rotateright"]) 
        fwd = self.input(self.input_names["forward"]) 
        rotleft = 0.0 if rotleft == None else rotleft
        rotright = 0.0 if rotright == None else rotright
        fwd = 0.0 if fwd == None else fwd
            
        if self.resolution != self.input(self.input_names["resolution"]):
            self.set_resolution(self.input(self.input_names["resolution"]))
        if self.init_pos !=  self.input(self.input_names["init_pos"]):
            self.set_init_pos(self.input(self.input_names["init_pos"]))
        if self.init_distance != self.input(self.input_names["init_distance"]):
            self.set_init_distance(self.input(self.input_names["init_distance"]))
        
        self.rotate_left(rotleft)
        self.rotate_right(rotright)
        self.forward(fwd)
        self.set_output_val(0, self.get_output())
        

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
    tst.set_init_distance(4.0)
    tst.set_init_pos(1)
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