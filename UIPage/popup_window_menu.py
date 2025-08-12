from pywinauto import Desktop



class pp_win_menu():
    def __init__(self):
        self.account_icon = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=0,control_type='Text')
        self.account_without_detail_info_item = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=0, control_type="MenuItem")
        self.about_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="About", control_type="MenuItem")
        self.settings_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="Settings", control_type="MenuItem")
        self.printer_utility_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="Printing Preferences", control_type="MenuItem")
        self.zsb_workspace_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="ZSB Workspace", control_type="MenuItem")
        self.help_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="Help", control_type="MenuItem")
        self.tutorials_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="Tutorials", control_type="MenuItem")
        self.buy_more_label_item = Desktop(backend="uia").window(class_name="Popup").child_window(title="Buy More Labels", control_type="MenuItem")

        self.zebra_image = Desktop(backend="uia").window(class_name="Popup").child_window(title="", found_index=0,control_type="Custom").child_window(title="",found_index=0,control_type="Image")


    # def get_account_item(self,username):
    #     if "@" in username:
    #         username = username.split('@')[0]
    #         username = username[0].upper() + username[1:]
    #     else:
    #         username = username
    #     element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{username}", control_type="MenuItem")
    #     return element
