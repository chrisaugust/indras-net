# Indra’s Net 🕸  
AI-Powered Research Assistant & Knowledge Map Generator

Indra’s Net is an intelligent research assistant that analyzes input text, summarizes its key ideas, and builds a knowledge graph to reveal the relationships between concepts. You can chat with both the content and the map — making it a tool for interactive learning, structured reasoning, and building insight across domains.

---

## Features

- 🧠 Summarizes large bodies of text using OpenAI
- 🌐 Extracts key concepts and maps them as a network
- 🔗 Identifies relationships between concepts (e.g. "prerequisite", "related to", "enables")
- 💬 Allows you to chat with the content and its graph
- 📦 Fully containerized with Docker & FastAPI backend + PostgreSQL
- ⚙️ Versioned DB schema via Alembic
- 🔧 Built for extension into true agentic reasoning

---

## Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL (via Docker)
- OpenAI API (for summarization & extraction)
- React.js frontend (coming soon)
- Docker + Docker Compose

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/indras-net.git
cd indras-net
```

### 2. Set up environment variables
```
OPENAI_API_KEY=your-openai-key
```

### 3. Start the Docker stack
```bash
docker-compose up --build
```
This runs:
- FastAPI backend
- PostgreSQL
- Alembic-ready migration layer

### 4. Apply database migrations
```bash
docker-compose exec web alembic upgrade head
```
This will create the necessary tables (documents, concepts, relationships).

## Project Structure
```text
.
├── app/
│   ├── models/          # SQLAlchemy ORM models
│   ├── schemas/         # Pydantic request/response models
│   ├── crud/            # DB access logic
│   ├── api/             # Route handlers
│   ├── core/            # Config and DB session
│   └── main.py          # FastAPI app entry point
├── alembic/             # Alembic migration folder
│   └── versions/        # Versioned migration scripts
├── Dockerfile           # Builds FastAPI service
├── docker-compose.yml   # Runs FastAPI + Postgres together
├── requirements.txt     # Python dependencies
└── README.md
```
## Example Use Case

Paste in a long-form article (e.g. research paper, blog post, technical document).
Indra's Net will:
### 1. Summarize the core content
### 2. Extract a list of key concepts
### 3. Map the relationship of those concepts as a knowledge graph
### 4. Let you query or chat with the document and its map:
- "What concepts are prerequisites for X?"
- "Summarize the parts of this document related to Y."
- "How does Z connect to A, B, and C?"

## License
MIT License
You're free to use, modify, remix, and contribute!

## Author
Built by [Chris Danielson](https://www.chrisadanielson.com/) at Vimutti Software.

