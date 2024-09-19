# scripts/download_docs.py

from src.data.downloader import HTMLDownloader
from config.settings import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main function to download HTML documents from the specified base URL.
    """
    downloader = HTMLDownloader(settings.BASE_URL, settings.RAW_DATA_DIR)
    downloader.download_all()
    logger.info("Completed downloading documents")

if __name__ == "__main__":
    main()