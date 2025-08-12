import pytest
from common.filepath import *

if __name__ == '__main__':
    # pytest.main(['-s', '-q',  '-v',
    #              "./testcase/dailySanity/test_installation.py::Test_installation::test_download_install_zsb_apps",
    #              '--alluredir', result_path ])

    pytest.main(['-s', '-q',  '-v',
                 "-m",'sso',
                 '--alluredir', result_path ])

    #To check the test report: allure serve .\report_Allure\