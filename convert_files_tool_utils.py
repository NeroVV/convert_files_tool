from pdf2docx import Converter
from win32com import client

def pdf2word(file_path):
    file_name = file_path.split('.')[0]
    docx_file = f'{file_name}.docx'

    pdf_to_word = Converter(file_path)
    pdf_to_word.convert(docx_file,start=0,end=None)
    pdf_to_word.close()
    return docx_file

def word2pdf(file_path):
    # C:/xxx/ file can't find
    # translate file path
    file_path = str(file_path).replace('/','\\')
    word_app = client.Dispatch('Word.Application')
    file_name = file_path.split('.')[0]
    pdf_file = f'{file_name}.pdf'
    word = word_app.Documents.Open(file_path,ReadOnly=1)
    word.SaveAs(pdf_file,FileFormat=17)
    word.Close()
    word_app.Quit()
    return pdf_file

if __name__ == '__main__':
    file_path = 'C:/Users/mayn/Desktop/新建 Microsoft Word 文档.docx'
    word2pdf(file_path)

