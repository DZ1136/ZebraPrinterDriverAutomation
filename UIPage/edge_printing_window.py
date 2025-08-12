import pywinauto
from pywinauto import Desktop, Application


class EdgePrintingWindow:
    def __init__(self):
        # edge browser
        self.edge_browser = Desktop(backend="uia").window(title="New tab - Work - Microsoft​ Edge")
        self.pdf_edge_browser = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge")
        self.pdf_edge_browser_print_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Print (Ctrl+P)", control_type="Button")
        # self.pdf_edge_browser_print_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="", found_index=39)

        # Print window
        self.printer_text = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Printer", control_type="Text")
        self.printer = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title_re="Printer ZSB-DP1[24]", control_type="Button")

        self.copies_text = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Copies", control_type="Text")
        self.copies = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title_re="\d+", control_type="Spinner")

        self.layout_text = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Layout", control_type="Text")
        self.layout_portrait = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Portrait", control_type="RadioButton")
        self.layout_landscape = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Landscape", control_type="RadioButton")

        self.pages_text = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Pages", control_type="Group")
        self.pages_all = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="All", control_type="RadioButton")
        self.pages_odd = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Odd pages only", control_type="RadioButton")
        self.pages_even = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Even pages only", control_type="RadioButton")
        self.pages_custom = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Custom", control_type="RadioButton")
        self.pages_custom_edit = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Custom", control_type="Edit")

        self.more_settings = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="More settings", control_type="Button")
        self.print_using_system_dialog = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Print using system dialog… (Ctrl+Shift+P)", control_type="Button")
        self.fewer_settings = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Fewer settings", control_type="Button")

        self.paper_size = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="selecttrigger-2", control_type="Button")
        self.scale_fit_to_printable_area = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Fit to printable area", control_type="RadioButton")
        self.scale_actual_size = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Actual size", control_type="RadioButton")

        self.print_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Print", control_type="Button")
        self.cancel_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Cancel", control_type="Button")

        # Print using system dialog
        self.pusd_printer_list = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="ZSB-DP12", control_type="ListItem")

        self.pusd_preference_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Preferences", control_type="Button")
        self.pusd_find_printer_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Find Printer...", auto_id="1003", control_type="Button")

        self.pusd_pages_all = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="All", control_type="RadioButton")
        self.pusd_pages_selection = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Selection", control_type="RadioButton")
        self.pusd_pages_current = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Current Page", control_type="RadioButton")
        self.pusd_pages_current_edit = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Page range", auto_id="1152", control_type="Edit")

        self.pusd_copies = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Number of copies:", auto_id="1153", control_type="Edit")

        self.pusd_print_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Print", control_type="Button")
        self.pusd_cancel_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Cancel", control_type="Button")
        self.pusd_apply_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Apply", control_type="Button")

        # Printing Preferences
        self.pp_darkness_slider = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="1344", control_type="Slider")
        self.pp_darkness_left = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="1344", control_type="Slider").child_window(title="Page left",control_type="Button")
        self.pp_darkness_right = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="1344", control_type="Slider").child_window(title="Page right", control_type="Button")

        self.pp_graphic_slider = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="230448", control_type="Slider")
        self.pp_graphic_left = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="230448", control_type="Slider").child_window(title="Page left",control_type="Button")
        self.pp_graphic_right = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="230448", control_type="Slider").child_window(title="Page right", control_type="Button")

        self.pp_rotation = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(auto_id="295984", control_type="ComboBox")

        self.pp_ok_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="OK", control_type="Button")
        self.pp_cancel_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Cancel", control_type="Button")
        self.pp_help_button = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Help", control_type="Button")

        self.pp_print_test_page = Desktop(backend="uia").window(title_re=".*pdf - Work - Microsoft​ Edge").child_window(title="Print test page", control_type="Button")

