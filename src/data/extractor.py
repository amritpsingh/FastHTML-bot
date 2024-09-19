# src/data/extractor.py


import re
from pathlib import Path
from typing import List, Dict
import logging
from bs4 import BeautifulSoup, NavigableString
import asyncio

from config.settings import settings

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class HTMLExtractor:
    """
    A class to extract text sections from HTML files.

    Attributes:
        scheme (str): The URL scheme (e.g., 'https://').
        domain (str): The domain of the website.
    """
    def __init__(self, scheme: str = "https://", domain: str = "docs.fastht.ml"):
        self.scheme = scheme
        self.domain = domain

    @staticmethod
    def extract_sections(soup: BeautifulSoup, uri: str) -> List[Dict]:
        """
        Extracts sections from a BeautifulSoup object.

        Args:
            soup (BeautifulSoup): The BeautifulSoup object containing the HTML content.
            uri (str): The URI of the HTML page.

        Returns:
            List[Dict]: A list of dictionaries containing section data.
        """
        sections = soup.find_all("section")
        section_list = []
        for i, section in enumerate(sections):
            section_id = section.get("id")
            section_text = HTMLExtractor.extract_text_from_section(section)
            if section_id:
                section_data = {
                    "source": f"{uri}#{section_id}",
                    "text": section_text,
                    "previous_section": section_list[i-1]['source'] if i > 0 else None,
                    "next_section": None,
                    "metadata": {
                        "page_heading": soup.find("h1").get_text().strip() if soup.find("h1") else Path(uri).stem,
                        "section_id": section_id
                    }
                }
                if i > 0:
                    section_list[i-1]['next_section'] = section_data['source']
                section_list.append(section_data)
        return section_list

    @staticmethod
    def extract_text_from_section(section: BeautifulSoup) -> str:
        """
        Extracts text from a section element.

        Args:
            section (BeautifulSoup): The section element.

        Returns:
            str: The extracted text.
        """
        texts = []
        for element in section.children:
            if isinstance(element, NavigableString):
                if element.strip():
                    texts.append(element.strip())
            elif element.name != 'section':
                texts.append(element.get_text().strip())
        return HTMLExtractor.clean_text(" ".join(texts))

    def path_to_uri(self, path: Path) -> str:
        """
        Converts a file path to a URI.

        Args:
            path (Path): The file path.

        Returns:
            str: The URI.
        """
        relative_path = str(path.relative_to(settings.RAW_DATA_DIR)).replace("\\", "/")
        return self.scheme + self.domain + "/" + relative_path

    @staticmethod
    def clean_text(text: str) -> str:
        """
        Cleans text by replacing multiple newlines with a single space.

        Args:
            text (str): The text to clean.

        Returns:
            str: The cleaned text.
        """
        return re.sub(r'\s+', ' ', text).strip()

    async def process_html_file(self, record: Path) -> List[Dict]:
        """
        Processes a single HTML file.

        Args:
            record (Path): The path to the HTML file.

        Returns:
            List[Dict]: A list of dictionaries containing section data.
        """
        logger.info(f"Processing: {record}")
        async with asyncio.Lock():
            with open(record, "r", encoding="utf-8") as html_file:
                soup = BeautifulSoup(html_file, "html.parser")
        uri = self.path_to_uri(path=record)
        sections = self.extract_sections(soup, uri)
        return sections

    async def process_html_files(self, html_files_path: List[Path]) -> List[Dict]:
        """
        Processes multiple HTML files.

        Args:
            html_files_path (List[Path]): A list of paths to HTML files.

        Returns:
            List[Dict]: A list of dictionaries containing section data.
        """
        tasks = [self.process_html_file(record) for record in html_files_path]
        return await asyncio.gather(*tasks)

# Usage example:
# async def main():
#     extractor = HTMLExtractor()
#     html_files_path = [path for path in settings.RAW_DATA_DIR.rglob("*.html") if not path.is_dir()]
#     docs_text = await extractor.process_html_files(html_files_path)
#     print(f"Total documents processed: {len(docs_text)}")

# if __name__ == "__main__":
#     asyncio.run(main())