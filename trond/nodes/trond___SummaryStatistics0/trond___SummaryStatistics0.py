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
class SummaryStatistics_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(SummaryStatistics_NodeInstance, self).__init__(params)
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        if not isinstance(self.input(0), type(None)):
            data = np.array(self.input(0))
            axis = 1 if self.input(1)=="" else self.input(1)
            axis = 1 if len(data.shape)==1 else axis
            self.set_output_val(0, np.mean(data, axis=axis))
            self.set_output_val(1, np.median(data, axis=axis))
            self.set_output_val(2, np.std(data, axis=axis))
        

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
