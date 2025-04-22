# PubMed Paper Fetcher

This Python tool allows you to fetch research paper metadata from PubMed based on a search query. It filters results to show only those affiliated with biotech/pharmaceutical companies and saves them into an Excel file.

## Features
- Fetches top research papers using the PubMed API
- Filters based on organization affiliation (e.g., "pharma", "biotech")
- Saves results as `.xlsx` file

## Requirements
- Python 3.10+
- Poetry
- Installed libraries: `requests`, `lxml`, `pandas`

## Setup Instructions

1. Clone/download the project.
2. Open terminal inside the folder and run:
   ```bash
   poetry install
