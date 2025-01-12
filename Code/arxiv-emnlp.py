import arxiv
import os

# Directory to save downloaded papers
save_dir = "arxiv_papers_emnlp"
os.makedirs(save_dir, exist_ok=True)

# Create a client for the arXiv API
client = arxiv.Client(page_size=100)  # Page size can be adjusted based on needs

# Search query to handle variations of "accepted by EMNLP"
search_query = (
    '"accepted by EMNLP" OR "accepted at EMNLP" OR "accepted to EMNLP" '
    'OR "accepted for EMNLP" OR "accepted in EMNLP"'
)

# Set up the search
search = arxiv.Search(
    query=search_query,
    max_results=2736,  # Adjust based on the number of papers
    sort_by=arxiv.SortCriterion.SubmittedDate
)
# Iterate over the results and download PDFs
for result in client.results(search):
    try:
        paper_title = result.title.replace("/", "-")  # Avoid issues with file names
        pdf_path = os.path.join(save_dir, f"{paper_title}.pdf")
        print(f"Downloading: {result.title}")
        result.download_pdf(filename=pdf_path)
    except Exception as e:
        print(f"Failed to download {result.title}: {e}")

print(f"Downloaded all papers to {save_dir}")
