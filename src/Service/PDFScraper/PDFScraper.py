from PyPDF2 import PdfFileReader
import re


class PDFScraper:
    def scrape_pdf(self, file_name, value_to_find) -> bool:
        """
        Scrapes the price from the page.
        Returns:
            str: Scraped price from the web.
        """

        with open(file_name, 'rb') as f:
            pdf = PdfFileReader(f)
            NumPages = pdf.getNumPages()

            for i in range(0, NumPages):
                PageObj = pdf.getPage(i)
                Text = PageObj.extractText()
                ResSearch = re.search(value_to_find, Text)

                if ResSearch is not None:
                    return True

        return False




