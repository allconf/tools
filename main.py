from PyPDF2 import PdfFileMerger


def merge_pdf_files(input_files: list[str], output_file: str):
    merger = PdfFileMerger()
    for input_file in input_files:
        merger.append(input_file)
    merger.write(output_file)
    merger.close()

