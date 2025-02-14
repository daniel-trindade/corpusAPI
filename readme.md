# 📌 About CorpusAPI

This project is an API developed in Python using FastAPI. Its main goal is to create an API capable of returning text extracted from various sources to feed the database of LLMs  that use the RAG technique.

Currently, the API can:
- Extract and translate subtitles from YouTube videos.
- Transcribe audio files.
- Extract text from web pages.

The API is designed to be efficient and modular, facilitating integrations with other systems and allowing scalability as needed.

## 🚀 Features

- Extraction of subtitles from YouTube videos.
- Transcription of audio files.
- Extraction of text from web pages.

---

# 🛠 Getting Started

Follow the steps below to set up and run the API on your local machine.

## 📋 Prerequisites

Before starting, make sure you have the following installed:

- Python 3.x 
- Pip (Python package manager)

## 📥 Installation

1. **Clone the repository**

```bash
  git clone https://github.com/daniel-trindade/corpusAPI.git
  cd corpusAPI
```

2. **Create a virtual environment (optional but recommended)**

```bash
  python -m venv venv

  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate  # Windows
```

3. **Install dependencies**

```bash
  pip install -r requirements.txt
```

4. **Run the API**

```bash
  fastapi dev app/main.py
```

The API will be running at `http://127.0.0.1:8000` (or another specified port).


## 🧪 Docs

You can view the documentation when the API is running:

[Swagger UI](http://127.0.0.1:8000/docs) (automatically available with FastAPI)

---

## 🤝 Contributing

If you wish to contribute to the project, feel free to open issues or pull requests!

## 📜 License

To be defined.

