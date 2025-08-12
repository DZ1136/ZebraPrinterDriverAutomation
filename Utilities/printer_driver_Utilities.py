import time
from datetime import datetime
from time import sleep

import pytest

from common.commonmethod import commonmethod
from common.initialBaseValue import initialBaseValue
from pywinauto import Desktop, Application

class printer_driver_win_Utilities(initialBaseValue):
    def __init__(self):
        super().__init__()
        self.common_method = commonmethod()

    def printer_driver_testcase_64491(self):

        self.common_method.click_element(self.PrinterDriver.Start_button)
        self.common_method.click_element(self.PrinterDriver.Settings_button)
        self.common_method.click_element(self.PrinterDriver.Bluetooth_Devices_option)
        self.common_method.click_element(self.PrinterDriver.Printer_Scanners_option)
        self.common_method.click_element(self.PrinterDriver.Printer_Item)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.Print_Test_Page)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.Printer_properties)
        self.common_method.click_element(self.PrinterDriver.Print_test_page)
        time.sleep(1)
        self.common_method.click_element(self.PrinterDriver.Close_Button_popup)
        time.sleep(1)
        self.common_method.click_element(self.PrinterDriver.Cancel_Button_Properties)
        time.sleep(1)
        self.common_method.click_element(self.PrinterDriver.Printer_preferences)
        self.common_method.click_element(self.PrinterDriver.Print_test_page_preferences)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.Print_test_page_preferences_OK)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.Cancel_Button_preferences)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.OK_Button_preferences)

    def printer_driver_testcase_64492(self):

        self.common_method.click_element(self.PrinterDriver.Start_button)
        self.common_method.click_element(self.PrinterDriver.Settings_button)
        self.common_method.click_element(self.PrinterDriver.Bluetooth_Devices_option)
        self.common_method.click_element(self.PrinterDriver.Printer_Scanners_option)
        self.common_method.click_element(self.PrinterDriver.Printer_Item)
        time.sleep(3)
        self.common_method.click_element(self.PrinterDriver.Printer_properties)
        self.common_method.click_element(self.PrinterDriver.Driver_Settings_Tab)
        # set up help doc
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Setup_Help_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # Maintenance help doc
        self.common_method.click_element(self.PrinterDriver.Maintenance_Tab)
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Maintenance_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # Settings help doc
        self.common_method.click_element(self.PrinterDriver.Settings_Tab)
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Settings_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # Support help doc
        self.common_method.click_element(self.PrinterDriver.Support_Tab)
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Support_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # Stocks help doc
        self.common_method.click_element(self.PrinterDriver.Stocks_Tab)
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Stocks_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # Fonts help doc
        self.common_method.click_element(self.PrinterDriver.Fonts_Tab)
        self.common_method.click_element(self.PrinterDriver.Help_Button)
        self.common_method.check_element_exist(self.PrinterDriver.Fonts_Text)
        self.common_method.click_element(self.PrinterDriver.Close_Help_Doc)
        # close the property dialog
        self.common_method.click_element(self.PrinterDriver.Cancel_Button_Properties)
        time.sleep(3)