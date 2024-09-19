# FastHTML Docs Bot
A Q&A bot for FastHTML docs

The FastHTML Docs Bot is designed to help users interact with FastHTML documentation seamlessly. It can download, process, and search through HTML documents using natural language queries. The bot uses advanced language models and embeddings to provide accurate and contextually relevant responses.

Key components of the project include:
1. **Data Handling**: Modules for downloading, extracting, and preprocessing HTML documents.
2. **Embedding**: Creating embeddings for text chunks using language models.
3. **Storage**: Storing document embeddings and facilitating similarity searches.
4. **Query Handling**: Performing search queries and managing response generation.
5. **Response Generation**: Generating responses from language models, handling both streaming and non-streaming responses.
6. **Frontend UI**: A chat application that allows users to input queries and receive responses.


project structure:

fasthtml-docs-bot/
│
├── src/
│   ├── data/
│   │   ├── init.py
│   │   ├── downloader.py
│   │   ├── extractor.py
│   │   └── preprocessor.py
│   │
│   ├── embedding/
│   │   ├── init.py
│   │   └── embedder.py
│   │
│   ├── storage/
│   │   ├── init.py
│   │   └── vector_store.py
│   │
│   ├── query/
│   │   ├── init.py
│   │   ├── searcher.py
│   │   └── agent.py
│   │
│   ├── llm/
│   │   ├── init.py
│   │   └── response_generator.py
│   │
│   └── utils/
│       ├── init.py
│       └── helpers.py
│
├── scripts/
│   ├── create_embeddings.py
│   ├── download_docs.py
│   ├── process_docs.py
│   └── query_docs.py
│
├── tests/
│   ├── test_downloader.py
│   ├── test_extractor.py
│   ├── test_embedder.py
│   └── test_searcher.py
│
├── data/
│   ├── raw-data/
│   ├── processed-data/
│   └── fasthtml_docs_db/
│
├── config/
│   ├── init.py
│   ├── settings.py
│   └── config.py
│
├── frontend/
│   ├── static/
│   │   └── (no files added yet)
│   ├── templates/
│   │   └── index.html
│   └── chat_app.py
│
├── run_chat_app.sh
├── run_query_docs.sh
├── requirements.txt
├── setup.py
├── README.md
└── .gitignore
