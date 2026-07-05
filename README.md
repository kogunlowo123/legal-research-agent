# Legal Research Agent

[![CI](https://github.com/kogunlowo123/legal-research-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/legal-research-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Legal | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Legal research agent that searches case law, statutes, and regulations, analyzes legal precedents, summarizes court decisions, and generates legal memoranda on specific topics.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `search_case_law` | Search case law databases for relevant precedents |
| `analyze_precedent` | Analyze a legal precedent for applicability to current matter |
| `search_statutes` | Search statutes and regulations for applicable provisions |
| `summarize_decision` | Summarize a court decision with key holdings and reasoning |
| `draft_memo` | Draft a legal research memorandum on a specific issue |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/legal-research/analyze` | Analyze |
| `POST` | `/api/v1/legal-research/search` | Search |
| `POST` | `/api/v1/legal-research/generate` | Generate document |
| `GET` | `/api/v1/legal-research/track` | Track status |
| `POST` | `/api/v1/legal-research/report` | Generate report |

## Features

- Legal
- Research
- Compliance
- Audit Trail

## Integrations

- Relativity
- Logikcull
- Ironclad
- Docusign Clm
- Westlaw

## Architecture

```
legal-research-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── legal_research_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**Legal Tech Platform + LLM + Document Management**

---

Built as part of the Enterprise AI Agent Platform.
