import typing
from borb.pdf.document import Document
from borb.pdf.pdf import PDF
from borb.toolkit.text.simple_text_extraction import SimpleTextExtraction


f=open("taxout.txt","w")

def main():
    d: typing.Optional[Document] = None
    l: SimpleTextExtraction = SimpleTextExtraction()
    with open("Invoices/Croma.pdf", "rb") as pdf_in_handle:
        d = PDF.loads(pdf_in_handle, [l])


    assert d is not None
    f.write(l.get_text_for_page(0))

if __name__ == "__main__":
    main()
    f.close()

with open('taxout.txt') as f:
    contents = f.read()
     
contents = contents.replace(',', '')
# delete(".").gsub(",", ".")
# replace(',', '')

import re

result = re.findall(r"\d{1,10}(?:[.,]\d{3})*(?:[.,]\d{2,3})", contents)
# (USD|₹|$|EUR|€|\$)\s?(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2}))|(\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?)\s?(USD|₹|$|EUR|€|\$)
# [-+]?([0-9]+[\.\,][0-9]*)[^%]
# \d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})

Total_amount= max(result, key=lambda x:float(x))
print("Total Amount:",Total_amount)  