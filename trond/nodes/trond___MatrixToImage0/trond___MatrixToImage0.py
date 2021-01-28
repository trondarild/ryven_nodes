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

class MatrixToImage_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(MatrixToImage_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...

    def update_event(self, input_called=-1):
        m = self.input(0)
        s = m.shape
        img = np.zeros([s[0], s[1], 3])
        m_norm = 255*m/np.max(m)
        img[:,:,0] = m_norm[:,:]/3.0
        img[:,:,1] = m_norm[:,:]/3.0
        img[:,:,2] = m_norm[:,:]/3.0
        img = img.astype(np.uint8)
        # self.log_message(message='image: '+
        #                         np.array_str(img),
        #                      target='global')
        self.set_output_val(0, img)
        


    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
