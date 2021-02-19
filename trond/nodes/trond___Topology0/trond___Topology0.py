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
class Topology_NodeInstance(NodeInstance):
#class Topology:
    types = [
        "one_to_one", 
        "nearest_neighbor_1d",
        "nearest_neighbor_2d",
        "nearest_neighbor_3d",
        "nearest_neighbor_3_1d",
        "circle",
        "donut",
        "random",
        "empty"]

    def __init__(self, params):
        super(Topology_NodeInstance, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        pass

    def create_ix_matrix(self, x, y, border):
        retval = np.ones((y+2*border, x+2*border))
        ctr = 0.0
        retval = retval*-1.0
        for j in range(border, y+border):
            for i in range(border, x+border):
                retval[j,i] = ctr
                ctr += 1.0
        return retval

    def set_one_to_one(self, x, y):
        if x==y:
            return np.identity(x)
    
    def set_nearest_neighbor(self, x, y, adim):
        '''
        preconditions:
            a set of x*y nodes, arranged in a x,y matrix
        postconditions: 
            will produce a x*y, x*y matrix of connection values (0 or 1) 
        '''
        border = 1
        ctr = 0
        retval = np.zeros((y*x, x*y))
        if(adim==1):
            kernel = [[-1], [1]]
            # TODO implement one dim
        elif (adim==2):
            kernel = [[-1, -1], [-1, 0], [-1,1],
                [0, -1], [0, 1],
                [1, -1], [1, 0], [1, 1]]
            ixm = self.create_ix_matrix(x, y, border)
            for j in range(border, y+border):
                for i in range(border, x+border):
                    for k in kernel:
                        ix = int (ixm[j+k[0], i+k[1]])
                        if ix>=0: retval[ctr, ix] = 1
                    ctr += 1
        elif(adim==3):
            # TODO
            pass
        elif(adim==4):
            # TODO
            pass
        return retval
            
    def set_circle(self, x, y):
        retval = np.zeros((y, x))
        for j in range(y):
            if j==y-1: retval[j, 0] = 1
            else: retval[j, j+1] = 1
        return retval
    
    def set_random(self, x, y, rndlimit, recursion):
        def rnd(x, lim):
            tmp = np.random.random(1)
            retval = x * tmp if tmp > lim else 0
            return retval
        mat = np.ones((y, x))
        vfunc = np.vectorize(rnd)
        retval = vfunc(mat, rndlimit)
        if not recursion:
            mask = np.ones((y, x)) - np.identity(x)
            retval = retval*mask 
        return retval
        

    def update_event(self, input_called=-1):
        pass  # ...

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass

# if __name__ == '__main__':
#     tst = Topology(params=[])
#     #a  = tst.create_ix_matrix(5,5,1)
#     #a= tst.set_nearest_neighbor(3,3,2)
#     #a = tst.set_circle(5, 5)
#     a = tst.set_random(5,5, 0.3, False)
#     print (a)

