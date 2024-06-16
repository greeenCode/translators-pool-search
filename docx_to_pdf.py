# *.doc, *.docx >> *.pdf

import os
from docx2pdf import convert
import subprocess

def count_doc_files(source_folder):
    doc_count = 0
    docx_count = 0
    
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.doc'):
                doc_count += 1
            elif file.lower().endswith('.docx'):
                docx_count += 1
                
    return doc_count, docx_count

def convert_doc_files(source_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith('.docx'):
                docx_path = os.path.join(root, file)
                pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
                convert(docx_path, pdf_path)
                print(f"Converted {docx_path} to {pdf_path}")
            elif file.lower().endswith('.doc'):
                doc_path = os.path.join(root, file)
                pdf_path = os.path.splitext(doc_path)[0] + '.pdf'
                subprocess.run(['soffice', '--headless', '--convert-to', 'pdf', doc_path], check=True)
                print(f"Converted {doc_path} to {pdf_path}")

if __name__ == "__main__":
    source_folder = r"D:\Users\ie-woo\Documents\Google 드라이브\docs\인터비즈시스템N\_작업\2022 0516a 다국어 번역사\@Translators-Pool-Search"
    
    if not os.path.isdir(source_folder):
        print(f"The folder {source_folder} does not exist.")
        exit(1)
    
    doc_count, docx_count = count_doc_files(source_folder)
    print(f"Found {doc_count} .doc/.DOC files and {docx_count} .docx/.DOCX files in {source_folder} and its subfolders.")
    
    convert_choice = input("Do you want to convert all found .doc/.DOC and .docx/.DOCX files to .pdf? (y/n): ").strip().lower()
    
    if convert_choice in ['y', 'yes', '']:
        convert_doc_files(source_folder)
        print("Conversion completed.")
    else:
        print("Conversion cancelled.")
