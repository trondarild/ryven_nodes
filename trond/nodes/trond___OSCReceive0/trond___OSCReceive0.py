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

from pythonosc import dispatcher
from pythonosc import osc_server
import copy as cp
import asyncio
class OSCReceive_NodeInstance(NodeInstance):
    def __init__(self, params):
        super(OSCReceive_NodeInstance, self).__init__(params)
        self.adr_ix =  {}
        self.port = 0
        self.ip = ''
        self.addresses = []
        self.delim = ';'
        self.dispatcher = dispatcher.Dispatcher()
        self.dispatcher.set_default_handler(self.default_handler)
        self.server = None
        self.lock = False
        self.outdict = {}
        #self.server = osc_server.ThreadingOSCUDPServer(
        #        (self.ip, self.port), self.dispatcher)
        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
    def default_handler(self, address, *args):
        # handle addresses
        # look up address and output
        if(address in self.adr_ix.keys()):
          self.set_output_val(self.adr_ix[address], args)
        else:
            print(str(address))
            print(str(args[:5]) + " length: " + str(len(args)))
            print(self.to_string())
            print()
        
    def reinit(self, a_port, a_ip, a_addresses):
        self.lock = True
        restart = False
        if(isinstance(a_port, int) and \
            a_port != self.port):
            self.port = a_port
            restart = True
            print("changed port")
            
        if(isinstance(a_ip, str) and\
            self.ip != a_ip):
            self.ip = a_ip
            restart = True
            print("changed ip")
        adrstr = self.delim.join(self.addresses)
        print("adrstr=" + adrstr)
        print("a_addresses="+a_addresses)
        if(isinstance(a_addresses, str) and\
            adrstr != a_addresses):
            for o in range(len(self.outputs)):
                print("deleting: " + str(o))
                try:
                    self.delete_output(o)
                except :
                    # print( sys.exc_value)
                    print("tried to remove " + str(o))
            #to_remove = cp.deepcopy(self.addresses)
            #for adr in to_remove:
            #    try:
            #        self.dispatcher.unmap(adr, self.default_handler)
            #        self.delete_output(self.adr_ix[adr])
            #    except:
            #        print("tried to remove " + adr)
            #    print(len(self.outputs))
            self.adr_ix = {}
            self.addresses = a_addresses.split(self.delim)
            ctr = 0
            print("#1")
            for adr in self.addresses:
                self.dispatcher.map(adr, self.default_handler)
                self.create_new_output('data', 'Output_' + str(ctr), pos=ctr)
                self.adr_ix[adr] = ctr
                ctr += 1

            restart = True
            print("changed addresses")
        # print("#1")    
        if(restart):
            print(self.to_string())
            # if(self.server != None): self.server.shutdown()
            print("#2")
            #self.server = osc_server.ThreadingOSCUDPServer(
            #    (self.ip, self.port), self.dispatcher)
            try:
                self.server = osc_server. AsyncIOOSCUDPServer(
                    (self.ip, self.port), 
                    self.dispatcher, asyncio.get_event_loop())
                
            except:
                print("exception restarting server")
            print("started server")
            #self.server.serve_forever()
        self.lock = False
    def update_event(self, input_called=-1):
        # self.log_inputs()
        if (not self.lock):
            self.reinit( self.input(3), self.input(2), self.input(1))
        if input_called == 0:
            # pass
            #self.server.handle_request()
            self.server.serve()
            # print("clock")
            


    def to_string(self):
        retval = ''
        retval += 'port: ' + str(self.port) + '\n'
        retval += 'ip: ' + str(self.ip) + '\n'
        retval += 'addresses: ' + str(self.addresses) + '\n'
        retval += 'adr_ix: ' + str(self.adr_ix) + '\n'
        return retval
    def log_inputs(self):
        self.log_message("inp 0: " + str(self.input(0)), target='global')
        self.log_message("inp 1: " + str(self.input(1)), target='global')
        self.log_message("inp 2: " + str(self.input(2)), target='global')
        self.log_message("inp 3: " + str(self.input(3)), target='global')
        

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
