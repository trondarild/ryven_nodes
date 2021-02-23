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
from collections import deque

class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.size = 1
        self.data = deque(maxlen = self.size)
        self.input_names ={
            "input":1,
            "size":2
        }
        self.output_names = {
            "top":0,
            "bottom":1,
            "array":2
        }

    def push(self, data):
        self.data.appendleft(data)
        if len(self.data) > self.size: self.data.pop()

    def get_top(self):
        return (list(self.data))[0]
    def get_bottom(self):
        return (list(self.data))[len(self.data)-1]
    def get_array(self):
        retval = np.stack(list(self.data), axis=0)
        return retval

    def update_event(self, input_called=-1):
        if input_called==0:
            inp = self.input(self.input_names['input'])
            sz = self.input(self.input_names['size'])
            if type(sz)==int and sz != self.size:
                self.data = deque(maxlen = sz)
                self.size = sz
            if type(inp) != type(None):
                self.push(inp)
        self.set_output_val(self.output_names['top'], self.get_top())
        self.set_output_val(self.output_names['bottom'], self.get_bottom())
        self.set_output_val(self.output_names['array'], self.get_array())

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
