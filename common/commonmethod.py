import base64
import glob
import logging
import os
import re
import subprocess
import time
import xml.etree.ElementTree as ET
import shutil
from datetime import datetime
from time import sleep

import pytest
from pywinauto import Application, mouse, Desktop


class commonmethod(BaseException):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def run_terminal_command(self, command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()

    def check_element_exist(self, element, timeoutInSeconds=1):
        result = element.exists(timeoutInSeconds)
        return result

    def wait_element_appear(self, element, timeoutInSeconds=1):
        try:
            element.wait(wait_for='visible', timeout=timeoutInSeconds)
        except Exception as e:
            pytest.assume(str(e))

    def wait_element_disappear(self, element, timeoutInSeconds=1):
        try:
            element.wait_not(wait_for_not='visible', timeout=timeoutInSeconds)
        except Exception as e:
            pytest.assume(str(e))

    def check_element_enable(self,element, timeoutInSeconds=1, type="ready") -> bool:
        # 'enabled' means that the window is not disabled
        # 'ready' means that the window is visible and enabled
        try:
            element.wait(wait_for=type, timeout=timeoutInSeconds)
            return True
        except Exception as e:
            logging.info(f"Element is not ready: {e}")
            return False

    def click_element(self,element,timeoutInSeconds=1,button="left",double=False):
        #you can left click or right click, single click or double click
        self.wait_element_appear(element,timeoutInSeconds)
        element.click_input(button=button,double=double)

    def input_value_to_element(self,element,value,timeoutInSeconds=3):
        self.wait_element_appear(element, timeoutInSeconds)
        element.set_edit_text(value)

    def clear_inputbox_value(self,element,timeoutInSeconds=3):
        self.wait_element_appear(element, timeoutInSeconds)
        element.set_edit_text('')

    def get_element_value(self,element):
        value = element.window_text()
        return value

    def set_application_frontmost(self,element):
        element.set_focus()

    def start_recording(self,output_file):
        cmd_process = subprocess.Popen('cmd', stdin=subprocess.PIPE, universal_newlines=True)
        cmd_process.stdin.write(f'ffmpeg -f gdigrab -i desktop -r 30 -c:v libx264 {output_file}\n')
        cmd_process.stdin.flush()
        return cmd_process

    def close_recording(self,process):
        process.stdin.write('q\n')
        process.stdin.flush()

    def get_current_test(self):
        full_name = os.environ.get('PYTEST_CURRENT_TEST').split(' ')[0]
        test_file = full_name.split("::")[0].split('/')[-1].split('.py')[0]
        test_class = full_name.split("::")[-2]
        test_name= full_name.split("::")[-1]
        return full_name, test_file, test_class,test_name

    def update_printer_log_config(self):
        file_path = r"C:\ProgramData\Zebra Technologies\ZSBPrinter\product.config"
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            for tracing_element in root.iter('Tracing'):
                enabled_element = tracing_element.find('Enabled')
                if enabled_element is not None and enabled_element.text.lower() == 'false':
                    enabled_element.text = 'True'

            tree.write(file_path, encoding="utf-8")
        except FileNotFoundError:
            logging.info(f"Error: File not found at {file_path}, please check the printer tools is installed")
        except Exception as e:
            logging.info(f"An error occurred: {e}")

    # Mac method: download_target_files
    def copy_file_with_prefix(self, source_path, destination_path, prefix):
        try:
            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            for filename in os.listdir(source_path):
                if filename.startswith(prefix):
                    source_path = os.path.join(source_path,filename)
                    shutil.copy(source_path, destination_path)
                    source_path = os.path.dirname(source_path)
                    logging.info(f"{filename} copied from {source_path} to {destination_path}")
            logging.info(f"The printer log has been successfully copies")
        except FileNotFoundError:
            logging.info(f"Error: Source file not found at {source_path}")
        except Exception as e:
            logging.info(f"An error occurred: {e}")

    # Mac method: delete_target_files
    def delete_files_with_prefix(self, folder_path, prefix):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if filename.startswith(prefix):
                try:
                    os.remove(file_path)
                    logging.info(f"File deleted: {file_path}")
                except Exception as e:
                    logging.info(f"Error deleting file {file_path}: {e}")

    def decrypted_base64(self,encrypted_string):
        decoded_bytes = base64.b64decode(encrypted_string)
        decrypted_string = decoded_bytes.decode('utf-8')
        return decrypted_string

    def get_newest_file_in_folder(self,folder_path, file_pattern):
        files = glob.glob(os.path.join(folder_path, file_pattern))
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        if files:
            newest_file = files[0]
            return newest_file
        else:
            return None

    def get_log_line_time(self,line):
        match = re.search(r'(\d{8} \d{2}:\d{2}:\d{2}\.\d+) \| (.+)', line)
        log_time = datetime.strptime(match.group(1), "%Y%m%d %H:%M:%S.%f")
        return log_time

    def compare_log_line_time(self,line1,line2):
        return self.get_log_line_time(line1) > self.get_log_line_time(line2)

    def capture_content_after_timeframe(self,target_time,file_path):
        filtered_log_content = ''
        capture = False
        with open(file_path, 'r', encoding='utf-16') as file:
            for line in file:
                match = re.search(r'(\d{8} \d{2}:\d{2}:\d{2}\.\d+) \| (.+)', line)
                if match and not capture:
                    log_time = datetime.strptime(match.group(1), "%Y%m%d %H:%M:%S.%f")
                    if log_time > target_time and not capture:
                        capture = True
                if capture:
                    filtered_log_content += line
        return filtered_log_content

    def get_text_after_match(self,string, search_text):
        index = string.find(search_text)
        if index != -1:
            return string[index + len(search_text):].strip()
        else:
            return None

    # def extract_value(self,string, label):
    #     #how to use:
    #     #string = 'ormat_status","params":{"job_id":"01HMDN9WWWH2V10MW2FCZZX320","format_id":112,"labels_in_format":1,'
    #     #label = 'format_id'
    #     #value = extract_value(string, label)
    #     pattern = f'"{label}":(\d+)'
    #     match = re.search(pattern, string)
    #     if match:
    #         return match.group(1)
    #     else:
    #         return None

    def find_line_with_keywords(self,string, keywords, index):
        if string is not None:
            lines = string.split('\n')
            count = 0
            for line in lines:
                if all(keyword in line for keyword in keywords):
                    if count == index:
                        return line.strip()
                    count += 1
        return None

    def send_keys(self,window,key):
        window.type_keys(key)

    def select_dropdown_list_item(self, element, item):
        self.click_element(element)
        element.select(item)

    def get_propreties(self,element) -> dict:
        self.wait_element_appear(element)
        return element.get_properties()

    def get_legacy_properties(self,element,key) -> str:
        self.wait_element_appear(element)
        return element.legacy_properties().get(key)

    def get_element_rectangle(self, element) -> tuple:
        self.wait_element_appear(element)
        element_rect = element.rectangle()
        element_rectangle = (element_rect.left, element_rect.top, element_rect.right, element_rect.bottom)
        return element_rectangle

    def click_by_coords(self, element_rectangle):
        element_coords = (int((element_rectangle[0]+element_rectangle[2]) // 2), int((element_rectangle[1]+element_rectangle[3]) // 2))
        mouse.click(coords = element_coords)

