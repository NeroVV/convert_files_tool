from PyGUI_tools.PyGUI_utils import transfer_GUI
from PyGUI_tools.PyGUI_utils import file_process
from PyGUI_tools.PyGUI_parameters import *
import logging

def transfer_files():
    window = transfer_GUI()
    try:
        while True:
            # event is click button
            #  values is file info
            event,values = window.read(timeout=500)

            if event in (None,exit_button):
                break
            if event == start_button:
                # multiple files
                if ';' in values['file']:
                    file_list = values['file'].split(';')
                    # transfer files one by one
                    for file_name in file_list:
                        file_process(file_name)
                # no chose file
                elif values['file'] == '':
                    print('Please chose file')
                # chose one file
                else:
                    file_name = values['file']
                    file_process(file_name)

        window.close()
    except Exception as e:
        logging.error(str(e))


if __name__ == '__main__':
    transfer_files()