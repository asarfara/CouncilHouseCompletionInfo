import json
from pathlib import Path

from src.Entity.CouncilInfo import CouncilInfo
from typing import Union
from src.Service.WebScraper.WebScraper import WebScraper
from src.Service.PDFScraper.PDFScraper import PDFScraper


class CouncilInfoChecker:
    """
    Scrapes the council information for the different websites.
    """

    def __init__(self, details, web_scraper: WebScraper, pdf_scraper: PDFScraper):
        self.details = details
        self.web_scraper = web_scraper
        self.pdf_scraper = pdf_scraper

    def check_council(self, address) -> Union[CouncilInfo, None]:
        """
        Creates a collection of council information.
        Returns:
            Union[CouncilInfo, None]: Collection of CouncilInfo or None.
        """

        if not self.details or ('council' not in self.details):
            return None

        nbn_endpoint = self.details['council']['yarra_ranges_council']['nbn_endpoint']

        nbn_content = json.load(self.web_scraper.scrape_page(nbn_endpoint))
        nbn_connectivity = False

        if nbn_content['addressDetail']['serviceStatus'] != 'in_construction':
            nbn_connectivity = True

        occupancy_endpoint = self.details['council']['yarra_ranges_council']['occupancy_permit_pdf_endpoint']
        occupancy_content_pdf = self.web_scraper.scrape_page(occupancy_endpoint)

        filename = 'occupancy_register.pdf'
        occupancy_content_pdf_file = Path(filename)
        occupancy_content_pdf_file.write_bytes(occupancy_content_pdf.read())

        occupancy_permit = self.pdf_scraper.scrape_pdf(filename, address)

        return CouncilInfo(occupancy_permit, nbn_connectivity)
