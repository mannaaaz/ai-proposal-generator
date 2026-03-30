from langchain_core.tools import tool

document_content = ""

@tool
def update(content: str) -> str:
    """Update the document with new content."""
    global document_content
    document_content = content
    return document_content


@tool
def save(filename: str) -> str:
    """Save the current document to a text file."""
    global document_content

    if not filename.endswith(".txt"):
        filename += ".txt"

    with open(filename, "w") as f:
        f.write(document_content)

    return f"Saved as {filename}"