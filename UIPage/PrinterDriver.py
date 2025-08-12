from pywinauto import Desktop, Application


class PrinterDriver():
    def __init__(self):

        # printer driver

        self.Start_button = Desktop(backend="uia").Taskbar.child_window(title_re='Start', control_type="Button")
        self.Settings_button = Desktop(backend="uia").window(title_re = 'Start',control_type="Window").child_window(title_re='Settings', control_type="ListItem")
        self.Bluetooth_Devices_option = Desktop(backend="uia").window(title = 'Settings',control_type="Window").child_window(title='Bluetooth & devices', control_type="ListItem")
        self.Printer_Scanners_option = Desktop(backend="uia").window(title='Settings',control_type="Window").child_window(title='Printers & scanners', control_type="ListItem")
        self.Printer_Item = Desktop(backend="uia").window(title='Settings',control_type="Window").child_window(title_re='ZDesigner.*', control_type="Button")
        self.Print_Test_Page = Desktop(backend="uia").window(title='Settings', control_type="Window").child_window(title='Print test page', control_type="Text")
        self.Printer_properties = Desktop(backend="uia").window(title='Settings', control_type="Window").child_window(title='Printer properties', control_type="Text")
        self.Print_test_page = Desktop(backend="uia").window(title_re='.*Properties').child_window(title='Print Test Page', control_type="Button")
        self.Close_Button_popup = Desktop(backend="uia").window(title_re='.*Properties').child_window(title_re = 'ZDesigner.*').child_window(control_type="TitleBar").child_window(title = 'Close', control_type = 'Button')
        self.Cancel_Button_Properties = Desktop(backend="uia").window(title_re='.*Properties').child_window(title = 'Cancel',control_type="Button")
        self.Printer_preferences = Desktop(backend="uia").window(title='Settings', control_type="Window").child_window(title='Printing preferences', control_type="Text")

        self.Print_test_page_preferences = Desktop(backend="uia").window(title_re='.*Printing Preferences').child_window(title='Print test page', control_type="Button")
        self.Print_test_page_preferences_OK = Desktop(backend="uia").window(title_re='.*Printing Preferences').child_window(title='Test Page Print').child_window(title = 'OK', control_type = 'Button')
        self.Cancel_Button_preferences = Desktop(backend="uia").window(title_re='.*Printing Preferences').child_window(title = 'Cancel',control_type="Button")
        self.OK_Button_preferences = Desktop(backend="uia").window(title_re='.*Printing Preferences').child_window(title='OK', control_type="Button")
        self.Driver_Settings_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(auto_id="12320", control_type="Tab").child_window(title="Driver Settings", control_type="TabItem")
        self.Maintenance_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Maintenance", control_type="Button")
        self.Settings_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Settings",control_type="Button")
        self.Support_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Support",control_type="Button")
        self.Stocks_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Stocks",control_type="Button")
        self.Fonts_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Fonts",control_type="Button")
        self.Help_and_About_Tab = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help and About",control_type="Button")

        self.Help_Button = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help", auto_id="9", control_type="Button")

        self.Setup_Help_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Setup", control_type="Pane"))
        self.Maintenance_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Maintenance", control_type="Pane"))
        self.Settings_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Settings", control_type="Pane"))
        self.Support_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Support", control_type="Pane"))
        self.Stocks_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Stocks", control_type="Pane"))
        self.Fonts_Text = (Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",
                                                            control_type="Window").child_window(class_name = 'HH Child', control_type="Pane", found_index=0)
                                 .child_window(class_name = 'Shell Embedding', control_type="Pane").child_window(class_name = 'Shell DocObject View', control_type="Pane")
                                 .child_window(control_type="Pane", class_name = 'Internet Explorer_Server').child_window(title="Fonts", control_type="Pane"))
        self.Close_Help_Doc = Desktop(backend="uia").window(title_re='.*Properties').child_window(title="Help for Printer Drivers",control_type="Window").child_window(control_type="TitleBar").child_window(title="Close", control_type="Button")