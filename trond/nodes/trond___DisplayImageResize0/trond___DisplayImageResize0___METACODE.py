from NIENV import *

import cv2

# API METHODS

# self.main_widget        <- access to main widget


# Ports
# self.input(index)                   <- access to input data
# set_output_val(self, index, val)    <- set output data port value
# self.exec_output(index)             <- executes an execution output

# self.create_new_input(type_, label, widget_name=None, widget_pos='under', pos=-1)
# self.delete_input(index or input)
# self.create_new_output(type_, label, pos=-1)
# self.delete_output(index or output)


# Logging
# mylog = self.new_log('Example Log')
# mylog.log('I\'m alive!!')
# self.log_message('hello global!', 'global')
# self.log_message('that\'s not good', 'error')

# ------------------------------------------------------------------------------


class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['update'] = {'method': M(self.update)}

    # don't call self.update_event() directly, use self.update() instead
    def update_event(self, input_called=-1):
        self.res = self.input(0)
        maxsz = self.input(1)
        if type(maxsz) == int: maxsz = (mazsz, maxsz)
        if type(maxsz) != type(None):
            self.main_widget.set_max_size(maxsz)
        self.main_widget.show_image(self.res)
        self.set_output_val(0, self.res)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass # ...


    def remove_event(self):
        pass
