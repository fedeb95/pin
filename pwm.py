class PWMWorker:

    def __init__(self,channel,dc):
        self.channel=channel
        self.dc_list=[dc]
        self.start=False

    def start(self):
        self.start=True 

    def stop(self):
        self.start=False

    def ChangeDutyCycle(self,dc):
        self.dc_list.append(dc)
 
    def get_current_dc(self):
        return self.dc_list[-1]

    def get_all_dc(self):
        return self.dc_list

    def is_started(self):
        return self.start
