from PyPDF2 import PdfReader as PdfReader2, PdfWriter as PdfWriter2
from PyPDF2.generic import AnnotationBuilder as AnnotationBuilder2

from pypdf import PdfReader, PdfWriter
from pypdf.generic import AnnotationBuilder

def produce_output(pdf_reader_cls: type, pdf_writer_cls: type, annotation_builder: type, output_name: str) -> None:
    reader = pdf_reader_cls("page_178.pdf")
    page = reader.pages[0]
    # this are lists to pass return the x and y from the visitor function
    x = [None]
    y = [None]
    def visitor_body(text, cm, tm, fontDict, fontSize):
        if text.startswith("5425."):
            x[0] = tm[4]
            y[0] = tm[5]
            print(output_name, x, y)
    
    page.extract_text(visitor_text=visitor_body)
    writer = pdf_writer_cls()
    writer.add_page(page)

    annotation = annotation_builder.rectangle(
        rect=(x[0], y[0], x[0] + 10, y[0] + 30),
        interiour_color="f1e740",
    )
    writer.add_annotation(page_number=0, annotation=annotation)

    with open(output_name, "wb") as f:
        writer.write(f)

produce_output(PdfReader, PdfWriter, AnnotationBuilder, "output-pypdf.pdf")
produce_output(PdfReader2, PdfWriter2, AnnotationBuilder2, "output-pypdf2.pdf")
