from pathlib import Path

from src.extractor import pdf_to_markdown
from src.chunker import split_sections
from src.retriever import Retriever
from src.llm import ask_llm

# Path to the PDF document
PDF_PATH = "documents/Machine_Learning.pdf"

# Convert PDF to Markdown
md_file = pdf_to_markdown(PDF_PATH)

# Read markdown file
markdown = Path(md_file).read_text(encoding="utf-8")

# Split document into sections
sections = split_sections(markdown)

# Create retriever
retriever = Retriever(sections)

print("Document loaded successfully!")

# Ask questions continuously
while True:
    question = input("\nAsk a question (or type 'exit' to quit): ")

    if question.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve relevant context
    context = "\n\n".join(retriever.search(question))

    print("\nRetrieved Context:")
    print("=" * 50)
    print(context[:1000])
    print("=" * 50)

    # Get answer from LLM
    answer = ask_llm(question, context)

    print("\nAnswer:")
    print(answer)
