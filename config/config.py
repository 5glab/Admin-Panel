import os
class config:
    def __init__(self):
        self.config_ = {}
        self.config_['base'] = os.getcwd()
        self.config_['auther'] = "Seyyedmohammad hosseini"
        self.config_['version']  = "0.5.9.1"
        self.config_['startTime'] = "07.15.2016"
        self.config_['error_log_dir'] = self.config_['base'] + "/log/error.txt"
        self.config_['panel'] = self.config_['base'] + "/panel/"
        self.config_['active_panel'] = "default"
        self.config_['module_loader'] = "__init__.py"
        self.config_['modules'] = ['tkinter']
        #---- ADMIN ----
        self.config_['client_ip'] = '192.168.12.35'
        self.config_['client_port'] = 10000
        pass

    def get(self, key):
        if self.config_.has_key(key):
            return self.config_[key]
        else:
            return False

    def set(self, key, value):
        if not self.config_.has_key(key):
            self.config_[key] = value
            return True
        else:
            return False

    def update(self, key, value):
        if self.config_.has_key(key):
            self.config_[key] = value
            return True
        else:
            return False


