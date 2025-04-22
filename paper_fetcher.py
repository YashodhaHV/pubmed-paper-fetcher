from typing import List, Dict, Optional
import requests
import lxml.etree as ET

HEADERS = {"User-Agent": "Mozilla/5.0"}

def fetch_pubmed_ids(query: str, debug: bool = False) -> List[str]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": 100,
        "retmode": "xml"
    }
    if debug:
        print("Fetching PubMed IDs...")
    response = requests.get(url, params=params, headers=HEADERS)
    tree = ET.fromstring(response.content)
    return [id_elem.text for id_elem in tree.findall(".//Id")]

def fetch_paper_details(pmid: str, debug: bool = False) -> Optional[Dict]:
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": pmid,
        "retmode": "xml"
    }
    response = requests.get(url, params=params, headers=HEADERS)
    if response.status_code != 200:
        return None

    tree = ET.fromstring(response.content)
    article = tree.find(".//PubmedArticle")
    if article is None:
        return None

    title = article.findtext(".//ArticleTitle", default="N/A")
    pub_date_elem = article.find(".//PubDate")
    year = pub_date_elem.findtext("Year", "N/A") if pub_date_elem is not None else "N/A"

    non_academic_authors = []
    companies = []
    email = None

    for author in article.findall(".//Author"):
        affiliation = author.findtext(".//AffiliationInfo/Affiliation", "")
        if not affiliation:
            continue

        if not any(keyword in affiliation.lower() for keyword in ["university", "college", "institute", "hospital", "clinic" , "school"]):
            name = f"{author.findtext('ForeName', '')} {author.findtext('LastName', '')}".strip()
            non_academic_authors.append(name)
            companies.append(affiliation)

        if "@" in affiliation and not email:
            email = affiliation.split()[-1] if "@" in affiliation.split()[-1] else None

    return {
        "PubMedID": pmid,
        "Title": title,
        "Publication date": year,
        "Non-academic author(s)": "; ".join(non_academic_authors),
        "Company Affiliation(s)": "; ".join(companies),
        "Corresponding author Email": email or "N/A"
    }

def fetch_papers(query: str, debug: bool = False) -> List[Dict]:
    pmids = fetch_pubmed_ids(query, debug)
    if debug:
        print(f"Found {len(pmids)} IDs")

    results = []
    for pmid in pmids:
        if debug:
            print(f"Processing PMID: {pmid}")
        details = fetch_paper_details(pmid, debug)
        if details:
            results.append(details)
    return results
