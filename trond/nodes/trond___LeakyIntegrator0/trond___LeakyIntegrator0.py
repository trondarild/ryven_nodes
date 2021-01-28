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


class LeakyIntegrator_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(LeakyIntegrator_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.store = None
        self.inp = {"growth": 1,
                    "leakage": 2,
                    "max": 3,
                    "min": 4,
                    "input": 5}

    def update_event(self, input_called=-1):
        # pass  # ...
        self.log_inputs()
        if input_called == 0:
            # is leakage single or distributed?
            # is growth single or distributed?
            growth = self.input( self.inp["growth"])
            leakage = self.input(self.inp["leakage"])
            inpval = self.input( self.inp["input"])
            maxval = self.input( self.inp["max"])
            minval = self.input( self.inp["min"])
            if(not isinstance(inpval, type(None))):
                if isinstance(self.store, type(None)):
                    self.store = growth * inpval
                else:
                    self.store = (1-leakage)*self.store + \
                        growth * inpval
                    if(isinstance(maxval, float)):
                        self.store = max(maxval, self.store)
                    if(isinstance(minval, float)):
                        self.store = min(minval, self.store)
            self.set_output_val(0, self.store)

    def log_inputs(self):
        ctr = 0
        for inp in self.inputs:
            self.log_message("inp " + str(ctr) + ": " \
                + str(inp.label_str), target='global')
            ctr+=1
        # self.log_message("inp 1: " + str(self.input(1)), target='global')
        # self.log_message("inp 2: " + str(self.input(2)), target='global')
        # self.log_message("inp 3: " + str(self.input(3)), target='global')
       
    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
