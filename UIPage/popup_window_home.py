from pywinauto import Desktop


class pp_win_home():
    def __init__(self):
        # have(s) printer
        self.printer_name = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=1,control_type="Text")
        self.printer_status = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=2,control_type="Text")
        self.prints_left = Desktop(backend="uia").window(class_name="Popup").child_window(title="prints left", control_type="Text")

        # no printer
        self.no_printer_found = Desktop(backend="uia").window(class_name="Popup").child_window(title="No Printers Found", control_type="Text")
        self.pleaseaddaprintertoyouraccount = Desktop(backend="uia").window(class_name="Popup").child_window(title="Please add a printer to your account", control_type="Text")
        self.HelloIsitmeyourelookingfor = Desktop(backend="uia").window(class_name="Popup").child_window(title="Hello... Is it me you're looking for?", control_type="Text")

        # only for multi printers
        self.leftward_bt = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=0, control_type="Button")
        self.rightward_bt = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=1, control_type="Button")

    # have(s) printer
    # def get_printer_name(self,printer_name):
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{printer_name}", control_type="Text")
    #     return element
    #
    # def get_printer_status(self,printer_status):
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{printer_status}",control_type="Text")
    #     return element

    def get_home_text(self,index):
        element = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=index,control_type="Text")
        return element

    # def get_cartridge_type(self,cartridge_type):
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{cartridge_type}",control_type="Text")
    #     return element
    #
    # def get_cartridge_left(self,one_part_cartridge_left):
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{one_part_cartridge_left}", control_type="Text")
    #     return element
    #
    # def get_cartridge_size(self,one_part_cartridge_size):
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{one_part_cartridge_size}", control_type="Text")
    #     return element
