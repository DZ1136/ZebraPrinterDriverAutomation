import os
from pathlib import Path

base_dir = str(Path(__file__).resolve().parent.parent)
report_path = os.path.join(base_dir, 'log')
result_path = os.path.join(base_dir, 'report_Allure')