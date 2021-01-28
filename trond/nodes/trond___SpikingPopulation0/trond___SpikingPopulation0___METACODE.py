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
import copy as cp

class %CLASS%(NodeInstance):
    
    types= {'default': {        
        'tau_recovery':0.02,
        'coupling':0.2,
        'reset_voltage':-65.0,
        'reset_recovery':8.0,},
    'intrinsically_bursting': {
        'tau_recovery':0.02,
        'coupling':0.2,
        'reset_voltage':-55.0,
        'reset_recovery':4.0,},
    'chattering': {
        'tau_recovery':0.02,
        'coupling':0.2,
        'reset_voltage':-50.0,
        'reset_recovery':2.0,},
    'fast_spiking': {
        'tau_recovery':0.1,
        'coupling':0.2,
        'reset_voltage':-65.0,
        'reset_recovery':8.0,},
    'low-threshold_spiking': {
        'tau_recovery':0.02,
        'coupling':0.25,
        'reset_voltage':-65.0,
        'reset_recovery':8.0,},
    'resonator': {
        'tau_recovery':0.1,
        'coupling':0.26,
        'reset_voltage':-65.0,
        'reset_recovery':8.0,},
                
        }
    inp = {'clock':0,
            'excitation':1,
            'inhibition':2,
            'direct':3,
            'size':4,
            'type':5,
            'exc_top':6,
            'inh_top':7,
            'int_top':8
    }
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.x = None
        self.substeps = 2
        self.threshold = 30
        self.size = 2

        # build a dictionary here
        # but start with regular spiking
        self.type = 'default'
        self.taurecovery = self.types[self.type]['tau_recovery'] #0.02
        self.coupling = self.types[self.type]['coupling'] #0.2
        self.resetvolt = self.types[self.type]['reset_voltage'] #-65.0
        self.resetrecovery = self.types[self.type]['reset_recovery'] #8.0
        
        self.vlt = np.ones(self.size) * self.resetvolt
        self.u = self.coupling*self.vlt

        # 
    def timestep_Iz(self,    
                    a_a,        # tau recovery
                    a_b,        # coupling
                    a_c,        # reset voltage
                    a_d,        # reset recovery
                    a_i,        # direct current
                    a_v,        # in out excitation
                    a_u,        # recovery
                    e_syn,      # excitation synapse
                    i_syn,      # inhibition synapse
                    int_syn     # internal synapse                                
                    ):

        v1 = cp.deepcopy(a_v)
        u1 = cp.deepcopy(a_u)
        #self.log_message('#1', target='global')
        fired = (a_v >= self.threshold)
        #v1[fired] = self.threshold
        print("v1 = " + str(v1) + "; ac=" + str(a_c))
        #self.log_message('#2a', target='global')
        v1[fired] = a_c
        #self.log_message('#2b', target='global')
        u1[fired] = a_u[fired] + a_d #[fired]
        #self.log_message('#2c', target='global')
        
        # synapses, topology
        exc = e_syn*(e_syn >= self.threshold)
        inh = i_syn*(i_syn >= self.threshold)
        internal_e = int_syn*(int_syn >= self.threshold)
        internal_i = int_syn*(int_syn <= -self.threshold)
        inpvlt = np.sum(internal_e, axis=1) \
                + np.sum(internal_i, axis=1)\
                + np.sum(exc, axis=1) \
                - np.sum(inh, axis=1)
        
        print("inpvlt = " + str(inpvlt))
        i1 = cp.deepcopy(a_i)
        i1 = np.ravel(i1 + inpvlt)
        stepfact = 1.0/self.substeps
        stepfact = 1.0/self.substeps
        tmp = cp.deepcopy(v1)
        #self.log_message('#3', target='global')
        for i in range(self.substeps):
            v1 += stepfact*(0.04*tmp**2 + 5*tmp + 140-a_u+i1)
        #print("v1 = " + str(v1))
        u1 += a_a*(a_b*v1 - u1)
        fired = (v1>self.threshold)
        v1[fired] = self.threshold
        #self.log_message('#4', target='global')
        print("v1_2 = " + str(v1))
        #a_v = cp.deepcopy(v1)
        #a_u = cp.deepcopy(u1)
        return (v1, u1)
    
    def reinit(self, a_size, a_type):
        # print("size cl: " + str(type(a_size)))
        if (isinstance(a_size, int) and a_size != self.size):
            self.log_message('setting size: ' + str(a_size) , target='global')
            self.size = a_size
            self.vlt = np.ones(self.size) * self.resetvolt
            self.u = self.vlt * self.coupling
        if(isinstance(a_type, str) and \
            a_type != self.type and \
            a_type in self.types.keys()):
            self.log_message('setting type: ' + str(a_type) , target='global')
            self.type = a_type
            self.taurecovery = self.types[self.type]['tau_recovery'] #0.02
            self.coupling = self.types[self.type]['coupling'] #0.2
            self.resetvolt = self.types[self.type]['reset_voltage'] #-65.0
            self.resetrecovery = self.types[self.type]['reset_recovery'] #8.0
            self.log_message('tau='+str(self.taurecovery), target = 'global')

    def update_event(self, input_called=-1):
        # check if type or size has changed
        self.log_message("inp 0: " + str(self.input(0)), target='global')
        self.log_message("inp 1: " + str(self.input(1)), target='global')
        self.log_message("inp 2: " + str(self.input(2)), target='global')
        self.log_message("inp 3: " + str(self.input(3)), target='global')
        self.log_message("inp 4: " + str(self.input(4)), target='global')
        self.log_message("inp 5: " + str(self.input(5)), target='global')
        self.log_message("inp 6: " + str(self.input(6)), target='global')
        self.log_message("inp 7: " + str(self.input(7)), target='global')
        
        self.reinit(self.input(self.inp['size']),
                    self.input(self.inp['type'])) # reinit if size changed
        # call timestep
        excitation = 0
        inhibition = 0
        internal_syn = 0
        if input_called == 0:
            
            dircur = np.reshape(np.array(self.input(self.inp['direct'])), (self.size)) if\
                              not isinstance(self.input(self.inp['direct']), type(None)) else\
                                np.zeros(self.size)   # todo: convert to array
            print("dircur: " + str(dircur))
            excitation = self.input(self.inp['exc_top'])\
                        * np.tile(self.input(self.inp['excitation']), (self.size, 1)) if \
                        not isinstance(self.input(self.inp['exc_top']), type(None)) and \
                        not isinstance(self.input(self.inp['excitation']), type(None)) else \
                        np.zeros([1,1])
            print("excitation: " + str(excitation))
            inhibition = self.input(self.inp['inh_top'])\
                        * np.tile(self.input(self.inp['inhibition']), (self.size, 1)) if \
                        not isinstance(self.input(self.inp['inh_top']), type(None)) and \
                        not isinstance(self.input(self.inp['inhibition']), type(None)) else \
                        np.zeros([1,1])
            print("inhibition: " + str(inhibition))
            internal_syn = self.input(self.inp['int_top'])\
                        * np.tile(self.vlt, (self.size, 1)) if \
                        not isinstance(self.input(self.inp['int_top']), type(None)) else \
                        np.zeros([1,1])
            print("internal: " + str(internal_syn))
            (self.vlt, self.u) = self.timestep_Iz(
                                                self.taurecovery,
                                                self.coupling,
                                                self.resetvolt,
                                                self.resetrecovery,
                                                dircur,
                                                self.vlt,
                                                self.u,
                                                excitation,
                                                inhibition,
                                                internal_syn
                                            )
            self.set_output_val(0, self.vlt)



    def get_data(self):
        # TODO: add type and internal topology
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
