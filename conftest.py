import logging
import shutil
import signal
import threading
from datetime import datetime
from time import sleep
import pytest
from common.commonmethod import commonmethod
from common.filepath import *
from common.initialBaseValue import initialBaseValue


recording_thread=''
current_time_str=''
timeInfo_folder=''
full_name =''
test_file =''
test_class =''
test_name = ''
output_filename = ''
output_filename_path = ''
testcase_folder= ''
call_result = ''
setup_result = ''
printer_log_path = r"C:\Driver"


@pytest.fixture(scope="session",autouse=True)
def session_fixture():
    global current_time_str,timeInfo_folder
    if not os.path.exists(report_path):
        os.makedirs(report_path)
        logging.info("create file: "+report_path)
    # Generate a string of the current time, for example: 2023-11-10-15-30-45
    current_time_str = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    timeInfo_folder = os.path.join(report_path, current_time_str)
    if not os.path.exists(timeInfo_folder):
        os.makedirs(timeInfo_folder)
        logging.info("create file: " + timeInfo_folder)

    common_method = commonmethod()
    # Modify the configuration file for the printer log and delete the previous log.
    common_method.update_printer_log_config()
    common_method.delete_files_with_prefix(printer_log_path,"Printer Driver")

    yield

    common_method.copy_file_with_prefix(printer_log_path, timeInfo_folder,"Printer Driver")
    shutil.make_archive(timeInfo_folder,'zip',timeInfo_folder)

@pytest.fixture(scope="function",autouse=True)
def function_fixture():
    global recording_thread,timeInfo_folder,current_time_str,full_name, test_file, test_class, test_name,output_filename,output_filename_path,current_time_str,testcase_folder,process
    #make sure initial elements successfully
    sleep(2)
    initial_Element = initialBaseValue()
    full_name, test_file, test_class, test_name = commonmethod().get_current_test()
    testcase_folder = os.path.join(timeInfo_folder,test_name)
    if not os.path.exists(testcase_folder):
        os.makedirs(testcase_folder)
    # Use the current time to construct the output filename
    output_filename = f"{current_time_str}_{test_name}.mp4"
    output_filename_path= os.path.join(testcase_folder, output_filename)
    #recording_thread.start()
    process = commonmethod().start_recording(output_filename_path)

    #pp_win_Utilities().close_zsb_popup_dialog()
    sleep(2)
    #pp_win_Utilities().open_zsb_popup_dialog()
    yield initial_Element
    commonmethod().close_recording(process)
    # process.send_signal(signal.SIGINT)
    # process.wait()
    # process.terminate()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    result = yield
    global recording_thread,testcase_folder,call_result,setup_result,caseErrorLog,process
    report = result.get_result()

    try:
        if report.when == "call" and report.outcome == 'failed':
            item.cls.caseFail = True
            caseErrorLog = report.longrepr
            call_result = False
            logging.info('call: '+str(call_result))
            # recording_thread.join()
            # commonmethod().kill_ffmpeg()
        elif report.when == "call" and report.outcome == 'passed':
            item.cls.caseFail = False
            call_result = True
            logging.info('call: '+str(call_result))
        elif report.when == "setup" and report.outcome == 'failed':
            item.cls.caseFail = True
            setup_result = False
            caseErrorLog = report.longrepr
            commonmethod().close_recording(process)
            # recording_thread.join()
            # commonmethod().kill_ffmpeg()
            # macUtilities().get_zsb_crash_log(testcase_folder)
            # macUtilities().get_zsb_log(testcase_folder)
            # macUtilities().delete_zsb_log()
            # macUtilities().delete_zsb_crash_log()
            logging.info('setup: '+str(setup_result))
        elif report.when == "setup" and report.outcome == 'passed':
            setup_result = True
            logging.info('setup: '+str(setup_result))
        if call_result == True and setup_result == True:
            # commonmethod().delete_target_filesr(testcase_folder,'.mp4')
            logging.info('testcase_folder: '+testcase_folder)
            logging.info("remove mp4 file")
            call_result = False
            setup_result = False
    except Exception as e:
        print("Exception occurred:", e)




