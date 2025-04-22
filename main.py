import argparse
import pandas as pd
from paper_fetcher import fetch_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, help="Output CSV file name")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug output")
    args = parser.parse_args()

    results = fetch_papers(args.query, debug=args.debug)

    if not results:
        print("No results found.")
        return

    df = pd.DataFrame(results)
    if args.file:
        df.to_csv(args.file, index=False)
        print(f"Saved to {args.file}")
    else:
        print(df.to_string(index=False))

if __name__ == "__main__":
    main()
