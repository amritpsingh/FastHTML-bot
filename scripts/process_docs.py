# scripts/process_docs.py

import json
from pathlib import Path
from src.data.extractor import HTMLExtractor
from src.data.preprocessor import Preprocessor
from config.settings import settings
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Main function to process raw HTML documents and extract sections into JSON files.
    """
    extractor = HTMLExtractor()
    preprocessor = Preprocessor(settings.CHUNK_SIZE, settings.CHUNK_OVERLAP)

    raw_data_dir = Path(settings.RAW_DATA_DIR)
    processed_data_dir = Path(settings.PROCESSED_DATA_DIR)
    processed_data_dir.mkdir(parents=True, exist_ok=True)

    for html_file in raw_data_dir.glob("*.html"):
        sections = extractor.extract_sections(html_file)
        chunks = []
        for section in sections:
            chunks.extend(preprocessor.chunk_section(section))
        
        output_file = processed_data_dir / f"{html_file.stem}.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(chunks, f, ensure_ascii=False, indent=2)
        
        logger.info(f"Processed and saved sections for {html_file}")

if __name__ == "__main__":
    main()