import arxiv
import os

# Directory to save downloaded papers
save_dir = "arxiv_papers_neurips"
os.makedirs(save_dir, exist_ok=True)

# Search query and batch download
search_query = '"accepted by NeurIPS"'  # Query text
search = arxiv.Search(
    query=search_query,
    max_results=2736,  # Adjust based on the number of papers
    sort_by=arxiv.SortCriterion.SubmittedDate
)

for result in search.results():
    try:
        paper_title = result.title.replace("/", "-")  # Avoid issues with file names
        pdf_path = os.path.join(save_dir, f"{paper_title}.pdf")
        print(f"Downloading: {result.title}")
        result.download_pdf(filename=pdf_path)
    except Exception as e:
        print(f"Failed to download {result.title}: {e}")
print(f"Downloaded all papers to {save_dir}")
