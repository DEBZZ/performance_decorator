import PyPDF2
import sys


class InputException(Exception):
    def __init__(self):
        super().__init__('Kindly check the files provided as input.')


class PdfMerger:
    def __init__(self, inp_files):
        self.lst_files = inp_files
        self.merger()

    def merger(self):
        merger = PyPDF2.PdfFileMerger()
        for file_name in self.lst_files:
            merger.append(file_name)
        merger.write('merged_pdf.pdf')


if __name__ == '__main__':
    list_pdf = sys.argv[1:]
    if all(list(map(lambda file: True if file.endswith('pdf') else False, list_pdf))):
        PdfMerger(list_pdf)
    else:
        raise InputException
