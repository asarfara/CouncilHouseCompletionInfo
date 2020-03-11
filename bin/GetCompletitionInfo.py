import yaml, sys

from os.path import dirname, join, abspath
sys.path.append(abspath(join(dirname(__file__), '..')))

from src.Service.CouncilInfoChecker.CouncilInfoChecker import CouncilInfoChecker
from src.Service.WebScraper.WebScraper import WebScraper
from src.Service.PDFScraper.PDFScraper import PDFScraper

document = open('config/info.yaml', 'r')
info = yaml.safe_load(document)
address = str(info['address']['street_number']) + ' ' + info['address']['street_name']

councilInfoChecker = CouncilInfoChecker(info, WebScraper(), PDFScraper())
councilInfo = councilInfoChecker.check_council(address)

print('Occupancy Permit Available: ' + str(councilInfo.occupancy_permit))
print('NBN Connectivity Available: ' + str(councilInfo.nbn_installed))




