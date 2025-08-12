from time import sleep
from pywinauto import Desktop

ele_test = Desktop(backend="uia").window(title='Settings',control_type="Window").child_window(title_re='ZDesigner.*', control_type="Button")

sleep(4)
ele_test.print_control_identifiers()

#allure serve .\report_Allure\