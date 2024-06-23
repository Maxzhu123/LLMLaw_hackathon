import zipfile
import xml.etree.ElementTree as ET
from docx import Document
from lxml import etree

#input_docx = 'NDA1.docx'

def marker(input_docx):
    t = mark_changes_in_document(input_docx)
    return t

def get_word_xml(docx_filename):
    with zipfile.ZipFile(docx_filename) as docx_zip:
        xml_content = docx_zip.read('word/document.xml')
    return xml_content

def mark_changes_in_document(docx_filename):
    xml_content = get_word_xml(docx_filename)
    root = etree.fromstring(xml_content)

    # Define namespaces
    namespaces = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
    }

    # Initialize a list to collect document text
    document_text = []

    # Process paragraphs and runs to extract text, marking changes with ****
    for paragraph in root.findall('.//w:p', namespaces):
        para_text = ''
        for run in paragraph.findall('.//w:r', namespaces):
            for text_element in run.findall('.//w:t', namespaces):
                para_text += text_element.text or ''
        
        # Check for insertions marked with ****
        for ins in paragraph.findall('.//w:ins', namespaces):
            for text_element in ins.findall('.//w:t', namespaces):
                para_text += '[start_insert]' + (text_element.text or '') + '[end_insert]'

        # Check for deletions marked with ****
        for del_elem in paragraph.findall('.//w:del', namespaces):
            for text_element in del_elem.findall('.//w:t', namespaces):
                para_text += '[start_insert]' + (text_element.text or '') + '[end_insert]'

        # Append paragraph text to the document text list
        if para_text:
            document_text.append(para_text)

    # Join all paragraphs into a single long text string
    full_text = '\n'.join(document_text)

    return full_text

