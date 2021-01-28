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
class SlidingBuffer_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(SlidingBuffer_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.size = [1, 10] # rows, cols (y, x)
        self.buffer = np.array(self.size)
        self.ix = 0

    
    def reinit(self, a_rows, a_cols):
        if(a_rows!= self.size[0] or a_cols != self.size[1]):
            self.size = [a_rows, a_cols]
            self.buffer = np.zeros(self.size)
            self.ix = 0
            self.log_message('new buffer sz: ' + str(self.size), target='global')

    def update_event(self, input_called=-1):
        rows = 1 if isinstance(self.input(0), float)\
            else len(self.input(0))
        self.reinit(rows, self.input(1))
        # self.log_message(message='buffer: '+
        #                          np.array_str(self.buffer),
        #                       target='global')
        self.buffer[:, self.ix] = np.array(self.input(0))
        self.ix = divmod(self.ix+1, self.size[1])[1]
        # self.log_message('ix: ' + str(self.ix), target='global')
        self.set_output_val(0, self.buffer)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
