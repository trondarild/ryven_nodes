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
            "inhbition":2,
            "ex_top":3,
            "inh_top":4,
            "size":5,
            "bias":6,
            "act_scale":7,
            "adaptation":8
        }
        self.size = 1
        self.activity = np.zeros(self.size)

    def update_event(self, input_called=-1):
        if input_called==0:
            # calculate output
            exc = self.input(self.input_names["excitation"])
            inh = self.input(self.input_names["inhibition"])
            ex_top = self.input(self.input_names["ex_top"])
            inh_top = self.input(self.input_names["inh_top"])
            size = self.input(self.input_names["size"])
            bias = self.input(self.input_names["bias"])
            act_scale = self.input(self.input_names["act_scale"])
            adapt = self.input(self.input_names["adaptation"])

            self.set_output_val(0, self.activity)
        pass  # ...

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
