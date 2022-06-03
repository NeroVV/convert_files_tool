import PySimpleGUI as sg
from convert_files_tool_utils import pdf2word
from convert_files_tool_utils import word2pdf
from PyGUI_tools.PyGUI_parameters import *


def transfer_GUI():
    # chose theme
    sg.theme('BlueMono')

    # set up window
    layout = [
        [
            sg.Text(window_body,font=(font_format,font_size)),
            sg.Text('',key='filename',size=(50,1),font=(font_format,font_size))
        ],
        [
            sg.Output(size=(80,10),font=(font_format,font_size))
        ],
        [
            sg.FilesBrowse(
                'chose the file',
                key='file',
                target='filename',
                file_types=[
                    ("pdf files", "*.pdf"),
                    ("docx files", "*.docx"),
                    ("doc files", "*.doc"),
                ],
                files_delimiter=';'
            ),
            sg.Button(start_button),
            sg.Button(exit_button)
        ]
    ]

    # create window
    window = sg.Window(window_title,layout,font=(font_format,font_size),default_element_size=(50,1))
    return window


def file_process(file_name):
    #transfer_tools_dict = {
    #    'pdf': pdf2word(file_name),
    #    'docx': word2pdf(file_name),
    #    'doc': word2pdf(file_name)
    #}
    file_type = file_name.split('.')[1]
    #print(f'file name: {file_name}\nfile type: {file_type}\n')
    if file_type == 'pdf':
        file_path = pdf2word(file_name)
    elif file_type == 'docx' or file_type == 'doc':
        file_path = word2pdf(file_name)

    #file_path = transfer_tools_dict[file_type]
    print(convert_message)
    print(new_files_message.format(file_path))


