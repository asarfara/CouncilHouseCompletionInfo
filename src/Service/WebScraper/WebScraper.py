from urllib.request import Request, urlopen
import ssl

class WebScraper:
    def scrape_page(self, url: str) -> str:
        """
        Scrapes the price from the page.
        Returns:
            str: Scraped price from the web.
        """

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3',
            'Content': 'Type: application/json',
            'Referer': 'https://places.nbnco.net.au/'
        }

        req = Request(url=url, headers=headers)

        return urlopen(req, context=ctx)
