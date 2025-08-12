import logging
from time import sleep

import pytest
import allure

from Utilities.printer_driver_Utilities import printer_driver_win_Utilities


class Test_Printer_Driver():

    @pytest.mark.sso
    @allure.feature("test_printer_driver_case_64491")
    def test_printer_driver_case_64491(self,function_fixture):

        printer_driver_win_Utilities().printer_driver_testcase_64491()

    @pytest.mark.sso
    @allure.feature("test_printer_driver_case_64492")
    def test_printer_driver_case_64492(self, function_fixture):
        printer_driver_win_Utilities().printer_driver_testcase_64492()