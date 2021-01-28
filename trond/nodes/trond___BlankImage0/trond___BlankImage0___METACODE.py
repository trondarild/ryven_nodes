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
        self.size = None
        self.colour = None
        self.img = None

    def update_event(self, input_called=-1):
        
        self.size = self.input(0)
        self.colour = self.input(1)
        self.img = np.zeros([self.size[0],self.size[1],3])

        self.img[:,:,0] = np.ones([self.size[0],self.size[1]])*self.colour[0]
        self.img[:,:,1] = np.ones([self.size[0],self.size[1]])*self.colour[1]
        self.img[:,:,2] = np.ones([self.size[0],self.size[1]])*self.colour[2]
        self.img = self.img.astype(np.uint8)
        # self.log_message(message='image: '+
        #                         np.array_str(self.img),
        #                      target='global')
        
        self.set_output_val(0, self.img)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
