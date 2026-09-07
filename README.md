# Compass

Compass is a CLI tool that analyzes a software repository and builds an interactive map of how its files, modules, functions, classes, and APIs relate to one another.

The project is currently scaffolded. The architecture and interfaces are being established before implementing the analysis pipeline.

## Planned features

- Repository-wide source-file discovery
- Ignore-file and configurable path filtering
- Multi-language parsing through Tree-sitter
- Import and export extraction
- Function, method, class, interface, and variable discovery
- Function and method call extraction
- API and entry-point identification
- Cross-file symbol resolution
- Dependency and call-graph construction
- Circular dependency detection
- Unresolved-reference reporting
- Source locations and metadata for graph entities
- JSON, graph-format, terminal, and interactive exports
- Extensible language and output-format support

## How it works

Compass processes a repository through the following pipeline:

```text
Repository
    ↓
Repository Scanner
    ↓
Source Files
    ↓
Tree-sitter Parser
    ↓
Syntax Trees
    ↓
Import / Symbol / Call Extractors
    ↓
Normalized Entities and Relationships
    ↓
Symbol Resolver
    ↓
Dependency Graph
    ↓
Analysis Services
    ↓
JSON / Graph / Interactive Output
```

## Project architecture

```text
src/compass/
├── cli/        Command-line interface and commands
├── indexer/    Repository scanning and file filtering
├── parser/     Tree-sitter parser and grammar management
├── extractor/  Imports, symbols, calls, and APIs
├── graph/      Graph models and construction
├── analysis/   Relationship analysis and symbol resolution
├── output/     JSON, graph, and interactive exporters
└── config/     Project configuration
```

### Core graph model

The graph will support nodes such as:

- Repository
- Directory
- File
- Module
- Class
- Function
- Method
- API
- External package

Relationships will include:

- `contains`
- `imports`
- `exports`
- `defines`
- `calls`
- `inherits`
- `implements`
- `references`
- `depends_on`

Each node and relationship is expected to retain useful metadata, including source path, line and column range, language, visibility, and resolution status.

## CLI direction

The planned CLI surface is:

```bash
compass analyze <repository>
compass export <analysis>
compass serve <analysis>
```

The CLI will eventually support configuration for ignored paths, supported languages, output formats, and analysis depth.

## Output formats

Compass is designed to support several output targets:

- JSON for integrations and downstream tooling
- DOT, Mermaid, or similar graph formats
- Terminal summaries and relationship reports
- Self-contained interactive HTML exports

The analysis model will remain independent from the eventual frontend so that a visual interface can be added without coupling it to parsing or graph construction.

## Repository layout

```text
compass/
├── src/compass/  Application source code
├── tests/        Parser, extractor, graph, and integration tests
├── docs/         Architecture and design documentation
├── pyproject.toml
└── README.md
```

## Development phases

1. Core indexing and Tree-sitter parsing
2. Static symbol, import, API, and call extraction
3. Relationship resolution and dependency graph construction
4. Analysis services and export formats
5. Interactive visualization, caching, and incremental indexing

## Current status

The repository contains the initial Python package structure, CLI entrypoint placeholder, analysis modules, output modules, test directories, and architecture documentation. Feature implementation is planned for the phases above.
