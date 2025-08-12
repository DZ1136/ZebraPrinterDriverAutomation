import configparser
from common.filepath import *
import ast

class Readinifile():
    def __init__(self):
        self.path = base_dir + r"//config.ini"

    def readinifile(self,section,option):
        config = configparser.ConfigParser()
        config.read(self.path)
        value = config.get(section,option)
        return value

    def get_printer_num(self,printers_info):
        if printers_info == None or printers_info =='' or printers_info == []:
            return 0
        # printers_info=self.str_transfer_to_list(printers_info)
        num_groups = len(printers_info)
        return num_groups

    def str_transfer_to_list(self,str):
        if str == None or str =='' or str == []:
            return None
        list = ast.literal_eval(str)
        return list


