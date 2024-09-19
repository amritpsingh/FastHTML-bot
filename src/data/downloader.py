# src/data/downloader.py

from pathlib import Path
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
from bs4 import BeautifulSoup
from tenacity import retry, stop_after_attempt, wait_fixed
from tqdm import tqdm
import logging

from config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class HTMLDownloader:
    """
    A class to download HTML pages from a base URL and save them locally.

    Attributes:
        base_url (str): The base URL to start downloading from.
        output_dir (Path): The directory to save downloaded HTML files.
        downloaded_urls (set): A set to keep track of downloaded URLs.
    """
    def __init__(self, base_url: str, output_dir: str):
        self.base_url = base_url
        self.output_dir = Path(output_dir)
        self.downloaded_urls = set()
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def fetch_url(self, url: str) -> requests.Response:
        """
        Fetches the content of a URL with retries.

        Args:
            url (str): The URL to fetch.

        Returns:
            requests.Response: The response object containing the fetched content.
        """
        response = requests.get(url)
        response.raise_for_status()
        return response

    def download_page(self, url: str) -> list:
        """
        Downloads a single HTML page and saves it locally.

        Args:
            url (str): The URL of the page to download.

        Returns:
            list: A list of URLs found on the downloaded page.
        """
        if url in self.downloaded_urls:
            return []

        try:
            response = self.fetch_url(url)
        except requests.exceptions.RequestException as e:
            logger.error(f'Failed to download: {url} due to {e}')
            return []

        self.downloaded_urls.add(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Create directory structure based on URL path
        parsed_url = urlparse(url)
        path_parts = parsed_url.path.strip('/').split('/')
        file_name = path_parts[-1] or 'index.html'
        dir_path = self.output_dir / Path(*path_parts[:-1])
        dir_path.mkdir(parents=True, exist_ok=True)
        file_path = dir_path / file_name
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())
        logger.info(f'Downloaded: {url}')

        return [
            urljoin(url, link['href'])
            for link in soup.find_all('a', href=True)
            if urljoin(url, link['href']).startswith(self.base_url) and 
               urljoin(url, link['href']).endswith('.html')
        ]

    def download_all(self):
        """
        Downloads all HTML pages starting from the base URL.
        """
        to_download = [self.base_url]
        with ThreadPoolExecutor(max_workers=10) as executor:
            with tqdm(total=len(to_download), desc="Downloading pages") as pbar:
                while to_download:
                    futures = [executor.submit(self.download_page, url) for url in to_download]
                    to_download = []
                    for future in as_completed(futures):
                        result = future.result()
                        if result:
                            to_download.extend(result)
                        pbar.update(1)
                    pbar.total = pbar.n + len(to_download)

if __name__ == "__main__":
    downloader = HTMLDownloader(settings.BASE_URL, settings.RAW_DATA_DIR)
    downloader.download_all()
