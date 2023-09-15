

import openai
import pdfplumber

# Set up the OpenAI API
openai.api_key = 'API_KEY'

# Function to extract text from a PDF


def pdf_to_text(pdf_path):
    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:

                extracted_text += text + '\n'

    return extracted_text

# Function to get a summary from OpenAI API


def get_summary(text, length):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': f"Please provide a summary of the following text with a maximum length of {length} characters:\n{text}"}, ],
    )

    summary = response['choices'][0]['message']['content'].strip()
    print(summary)
    with open('intermediate_summary.txt', 'w') as f:
        f.write(summary + '\n' + '\n')
    return summary

# Function to split text into chunks


def split_text(text, num_chars):
    return [text[i:i + num_chars] for i in range(0, len(text), num_chars)]


# Main script
pdf_path = "Insert PDF Path"
# Assuming an average of 4500 characters per page (you can adjust this)
max_page_length = 3200
target_length = 10 * max_page_length
chunk_length = max_page_length * 3

# get intermediate summary.txt

extracted_text = pdf_to_text(pdf_path)

# Split the extracted text into 3-page chunks
chunks = split_text(extracted_text, chunk_length)

# Summarize each chunk
summarized_chunks = [get_summary(chunk, chunk_length // 3) for chunk in chunks]

# Concatenate the summarized chunks
concatenated_summary = ' '.join(summarized_chunks)


# Recursively summarize the concatenated summary until it fits the desired length
final_summary = concatenated_summary
while len(final_summary) > target_length:
    final_summary = get_summary(final_summary, target_length)

# Save the final summary to a text file
with open('summary.txt', 'w') as f:
    f.write(final_summary)

print("The final summary has been saved to summary.txt.")
