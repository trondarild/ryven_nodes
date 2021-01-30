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

from copy import deepcopy
class Threshold_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(Threshold_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        #pass  # ...
        rslt = deepcopy(self.input(0)) # otherwise appears to affect randommatrix
        thr = self.input(1)
        
        rslt[rslt < thr[0]]  = thr[0]
        rslt[rslt >= thr[1]] = thr[1]
        retval = inp if isinstance(thr, type(None)) or thr == "" else rslt
        self.set_output_val(0, retval)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
