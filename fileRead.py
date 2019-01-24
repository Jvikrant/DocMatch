# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 11:38:46 2018

@author: jdhruwa
"""

#Read JD File

# =============================================================================
# #doc2Text
# import docx
# file=open("..\JD & GuideLine\JD_DotNet_Developer (002).doc","rb")
# content=file.read()
# 
# from docx import Document
# document = Document("..\JD & GuideLine\JD_DotNet_Developer (002).doc")
# con2=docx.process()
# =============================================================================


# =============================================================================
# #pdf2Text
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# from io import StringIO
# 
# def convert_pdf_to_txt(path):
#     rsrcmgr = PDFResourceManager()
#     retstr = StringIO()
#     codec = 'utf-8'
#     laparams = LAParams()
#     device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
#     fp = open(path, 'rb')
#     interpreter = PDFPageInterpreter(rsrcmgr, device)
#     password = ""
#     maxpages = 0
#     caching = True
#     pagenos=set()
# 
#     #read content of pages
#     for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
#         interpreter.process_page(page)
# 
#     text = retstr.getvalue()
# 
#     fp.close()
#     device.close()
#     retstr.close()
#     return text
# =============================================================================



# =============================================================================
# from io import StringIO
# from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
# from pdfminer.converter import TextConverter
# from pdfminer.layout import LAParams
# from pdfminer.pdfpage import PDFPage
# import os
# import sys, getopt
# 
# #converts pdf, returns its text content as a string
# def convertPDF2txt(fname, pages=None):
#     if not pages:
#         pagenums = set()
#     else:
#         pagenums = set(pages)
# 
#     output = StringIO()
#     manager = PDFResourceManager()
#     converter = TextConverter(manager, output, laparams=LAParams())
#     interpreter = PDFPageInterpreter(manager, converter)
# 
#     infile = open(fname, 'rb')
#     for page in PDFPage.get_pages(infile, pagenums):
#         interpreter.process_page(page)
#     infile.close()
#     converter.close()
#     text = output.getvalue()
#     output.close
#     return text
# =============================================================================


from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine

#converts pdf, returns its text content as a string
def convertPDF2txt(fname, pages=None):
    parser = PDFParser(open(fname,'rb'))
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)
    doc.initialize('')
    rsrcmgr = PDFResourceManager()
    laparams = LAParams()
    #I changed the following 2 parameters to get rid of white spaces inside words:
    laparams.char_margin = 1.0
    laparams.word_margin = 1.0
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    extracted_text = ''
    
    # Process each page contained in the document.
    for page in doc.get_pages():
        interpreter.process_page(page)
        layout = device.get_result()
        for lt_obj in layout:
            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
                extracted_text += lt_obj.get_text()
    
    print(extracted_text)
    return extracted_text

import docx2txt
#docx to string
def convertDOCX2txt(fname):
    return docx2txt.process(fname)


# =============================================================================
# import sys
# import pythoncom
# import System
# from System.Text import StringBuilder
# from System.IO import DirectoryInfo, File, FileInfo, Path, StreamWriter
# 
# clr.AddReference("Microsoft.Office.Interop.Word")
# import Microsoft.Office.Interop.Word as Word
# def doc_to_text(filename):
# 
#     word_application = Word.ApplicationClass()
#     word_application.visible = False
# 
#     document = word_application.Documents.Open(filename)
# 
#     result = StringBuilder()
# 
#     for p in document.Paragraphs:
#         result.Append(clean_text(p.Range.Text))
# 
#     document.Close()
#     document = None
# 
#     word_application.Quit()
#     word_application = None
# 
#     return result.ToString()
# =============================================================================



#main function to evalute text
def get_text(path):
    if ".PDF" in path.upper():
        return convertPDF2txt(path)
    elif ".DOCX" in path.upper():
        return convertDOCX2txt(path)
    else:
        return "Unsupported file type"



# =============================================================================
#qs=convertDOCX2txt("../CV/thotlasures.docx")
# =============================================================================
