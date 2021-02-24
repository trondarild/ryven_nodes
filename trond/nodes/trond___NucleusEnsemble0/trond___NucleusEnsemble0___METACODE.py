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
class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.input_names={
            "excitation":1,
            "inhibition":2,
            "ex_top":3,
            "inh_top":4,
            "size":5,
            "bias":6,
            "act_scale":7,
            "adaptation":8
        }
        self.default_vals = {
            "size":1,
            "bias":0,
            "act_scale":1,
            "adaptation":0.1
        
        }
        self.size = 1
        self.activity = np.zeros(self.size)

    def get_value(self, val_name):
        val = self.input(self.input_names[val_name])
        return self.default_vals[val_name] \
            if val == '' or val == None \
            else val
        
    def activate(self, a):
        return self.relu(a)
    def relu(self, a):
        filter = a > 0
        retval = filter * a
        return retval

    def update_event(self, input_called=-1):
        if input_called==0:
            # calculate output
            exc = self.input(self.input_names["excitation"])
            inh = self.input(self.input_names["inhibition"])
            ex_top = self.input(self.input_names["ex_top"])
            inh_top = self.input(self.input_names["inh_top"])
            size = self.get_value("size")
            bias = self.get_value("bias")
            act_scale = self.get_value("act_scale")
            adapt = self.get_value("adaptation")
            exc_sum = 0
            inh_sum = 0

            if type(exc) != type(None) and type(ex_top) != type(None):
                exc_sum = np.dot(ex_top, exc)
            # else: exc_sum = exc
            if type(inh) != type(None) and type(inh_top) != type(None):
                inh_sum = np.dot(inh_top, inh)

            a = exc_sum
            a = a - inh_sum
            self.activity = self.activity + adapt * (a - self.activity)
            a_final = bias + act_scale * self.activate(self.activity)

            self.set_output_val(0, np.ravel(a_final))
       

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
