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


# from pythonosc import dispatcher
from pythonosc import udp_client
import copy as cp
# import asyncio
class %CLASS%(NodeInstance):
    def __init__(self, params):
        super(%CLASS%, self).__init__(params)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        # ...
        self.adr_ix =  {}
        self.port = 0
        self.ip = ''
        self.addresses = []
        self.delim = ';'
        self.client = None
        self.num_baseinps = 3

    def reinit(self, a_port, a_ip, a_addresses):
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
        if(isinstance(a_addresses, str) and\
            adrstr != a_addresses):
            to_remove = cp.deepcopy(self.addresses)
            for adr in to_remove:
                try:
                    # self.dispatcher.unmap(adr, self.default_handler)
                    self.delete_input(self.adr_ix[adr])
                except:
                    print("tried to remove " + adr)
            self.adr_ix = {}
            self.addresses = a_addresses.split(self.delim)
            ctr = len(self.inputs)
            for adr in self.addresses:
                # self.dispatcher.map(adr, self.default_handler)
                self.create_new_input('data', 'Input_' + str(ctr-self.num_baseinps+1), pos=ctr)
                self.adr_ix[adr] = ctr
                ctr += 1

            # restart = True
            print("changed addresses")
        # print("#1")    
        if(restart):
            print(self.to_string())
            # if(self.server != None): self.server.shutdown()
            print("#2")
            #self.server = osc_server.ThreadingOSCUDPServer(
            #    (self.ip, self.port), self.dispatcher)
            try:
                self.client = udp_client.SimpleUDPClient(
                    self.ip, self.port)
                    
                
            except:
                print("exception restarting client")
            print("started client")
            #self.server.serve_forever()

    def update_event(self, input_called=-1):
        # pass  # ...
        # client = udp_client.SimpleUDPClient(args.ip, args.port)
        self.reinit( self.input(2), self.input(1), self.input(0))
        for key in self.adr_ix.keys():
            self.client.send_message(key, self.input(self.adr_ix[key]))
            # time.sleep(1)
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
        # self.log_message("inp 3: " + str(self.input(3)), target='global')

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass
