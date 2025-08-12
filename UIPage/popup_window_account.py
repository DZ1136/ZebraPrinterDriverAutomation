from pywinauto import Desktop


class pp_win_account():
    def __init__(self):
        #login in section
        self.no_account_menu_bt = Desktop(backend="uia").window(class_name="Popup").child_window(title="!", control_type="Text")
        self.youAreSignOut = Desktop(backend="uia").window(class_name="Popup").child_window(title="You Are Signed Out", control_type="Text")
        self.please_sign_in_hint = Desktop(backend="uia").window(class_name="Popup").child_window(title_re="Problem signing in. Please try again later.|Please sign into your account", control_type="Text")
        # self.please_sign_in_bt = Desktop(backend="uia").window(class_name="Popup").child_window(title="Please Sign In", control_type="Button")
        self.please_sign_in_bt = Desktop(backend="uia").window(class_name="Popup").child_window(best_match="Please Sign In")
        #account section
        self.account = Desktop(backend="uia").window(class_name="Popup").child_window(title="Account", control_type="Text")
        self.close_bt_account_section = Desktop(backend="uia").window(class_name="Popup").child_window(found_index=0,class_name='Button')
        self.sign_out_button_bt = Desktop(backend="uia").window(class_name="Popup").child_window(title="Sign Out", control_type="Button")

        # Due to a bug 'User has no icon', we need such an element for judgment.
        self.account_error = Desktop(backend="uia").window(class_name="Popup").child_window(title="", control_type="Text")



    # account section
    def get_small_single_account_icon_element(self,username):
        first_letter = username[0].upper()
        element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{first_letter}", control_type="Text")
        return element

    def get_big_single_account_icon_element(self,username):
        first_letter = username[0].upper()
        element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{first_letter}",control_type="Text")
        return element

    def get_username_element(self,username):
        if "@" in username:
            username = username.split('@')[0]
            username = username[0].upper() + username[1:]
        else:
            username = username
        element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{username}", control_type="Text")
        return element

    def get_printer_num_element(self,digit):
        element = Desktop(backend="uia").window(class_name="Popup").child_window(title=f"{digit}", control_type="Text")
        return element