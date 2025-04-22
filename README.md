# PubMed Paper Fetcher

A Python CLI tool to fetch PubMed research papers and filter by non-academic affiliations, such as biotech and pharmaceutical companies.

## Features
- Fetches top research papers using the PubMed API
- Filters based on organization affiliation (e.g., filters out "university", "hospital", "clinic")
- Saves results as `.xlsx` or `.csv` file

## Requirements
- Python 3.10+
- Poetry
- Installed libraries: `requests`, `lxml`, `pandas`

## Setup Instructions

1. Clone or download the project from GitHub.
2. Open a terminal inside the project folder and run:
   ```bash
   poetry install
