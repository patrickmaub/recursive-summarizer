# Recursive Summarizer

Recursive Summarizer is a utility designed to create condensed summaries of large PDF documents by extracting text from the PDF and interacting with the OpenAI API. The summarizer uses a recursive approach to ensure the output summary stays within a specified length.

## Features
- Extract text from PDF documents
- Utilizes OpenAI's GPT-3.5 with the `ChatCompletion` API to generate summaries
- Splits the extracted text into smaller chunks
- Performs recurring summaries to reach the desired summary length
- Saves the final summary to a text file

## Dependencies
- openai
- pdfplumber

You must install these via `pip install` to use Recursive Summarizer.

## How to Use
1. Make sure all dependencies have been installed.
2. Replace `'API_KEY'` in the script with your OpenAI API key.
3. Set the `pdf_path` variable to the path of the PDF document you want to summarize.
4. Adjust other configuration parameters (e.g., `max_page_length`, `target_length`, `chunk_length`) as needed based on your document and desired output.
5. Run the script, and the resulting summary will be saved to a `summary.txt` file.

### Example Usage

```python
pdf_path = "example_document.pdf"
recursive_summarizer.py
```

After running the script, a `summary.txt` file will be created containing the final summary.

## Functions

The code consists of multiple functions to handle different tasks:

- **pdf_to_text(pdf_path)**: Extract text from a PDF document and return the textual content as a string.
- **get_summary(text, length)**: Call the OpenAI API with the given text and desired summary length to generate a summary of the text.
- **split_text(text, num_chars)**: Split the input text into equal-length chunks of specified `num_chars` characters.
- **Main script**: The main script drives the extraction, splitting, summarizing, and writing processes.

## Limitations
- The success of the summarization depends on the quality of the extracted text, which may be affected by the PDF formatting or OCR (if used).
- The desired summary length might not be achieved exactly, as the summary generation process is dependent on the GPT-3.5-turbo model output.
- Adjusting configuration parameters to fit specific documents or desired output may require trial and error.
- The recursive approach used for summarization may cause a loss of context or essential information when trying to fit the summary in a very limited length.
- Ensure you have the appropriate API Key and permission to use GPT-3.5-turbo for generating summaries.

## Final Thoughts

Recursive Summarizer showcases the power of natural language processing (NLP) and artificial intelligence (AI) in extracting and summarizing information from large documents. Keep in mind that the summarization quality depends on the capabilities of the GPT-3.5-turbo model. The program can be adapted or improved based on specific requirements and document types. Make sure to use an appropriate API Key and comply with any usage guidelines or restrictions for the GPT-3.5-turbo model provided by OpenAI.
