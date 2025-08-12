from pywinauto import Desktop


class win():
    def __init__(self):
        # if platform == "win10":
            # self.taskbar_show_hidden_icons = Desktop(backend='uia').Taskbar.child_window(title='Notification Chevron')
            # self.zsb_tray_icon = Desktop(backend="uia").window(class_name="NotifyIconOverflowWindow").child_window(
            #     title='ZSB Printer Status Advisor')

        # elif platform == "win11":

            # self.zsb_tray_icon = Desktop(backend="uia").window(title="System tray overflow window.").child_window(title='ZSB Printer Status Advisor')
        self.show_desktop_bt = Desktop(backend='uia').Taskbar.child_window(title='Show Desktop')
        self.taskbar_show_hidden_icons = Desktop(backend='uia').Taskbar.child_window(best_match="Show Hidden Icons|Notification Chevron")
        self.zsb_tray_icon = Desktop(backend="uia").window(class_name_re="NotifyIconOverflowWindow|TopLevelWindowForOverflowXamlIsland").child_window(
            title='ZSB Status Advisor')
        self.show_desktop_bt = Desktop(backend='uia').Taskbar.child_window(title_re='Show desktop|Show Desktop')
        self.zsb_pop_up_window = Desktop(backend="uia").window(class_name="Popup")
