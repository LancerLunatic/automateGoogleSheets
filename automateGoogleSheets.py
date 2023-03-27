import openai
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Authenticate with OpenAI API
openai.api_key = "YOUR_OPENAI_API_KEY_HERE"

# Authenticate with Google Docs API
creds = service_account.Credentials.from_service_account_file('path/to/credentials.json')
docs_service = build('docs', 'v1', credentials=creds)

# Function to paraphrase a single paragraph using the ChatGPT API
def paraphrase(text):
    response = openai.Completion.create(
        engine="davinci",
        prompt="Please paraphrase the following paragraph:\n\n" + text,
        max_tokens=60,
        temperature=0.7,
        n = 1,
        stop=None,
        timeout=5,
    )
    return response.choices[0].text.strip()

# Function to paraphrase each page in a Google Docs document
def paraphrase_doc(doc_id):
    # Get the document content
    doc = docs_service.documents().get(documentId=doc_id).execute()

    # Create a new document for the paraphrased content
    new_doc = docs_service.documents().create(body={'title': 'Paraphrased Document'}).execute()

    # Iterate over each page in the document
    for i, page in enumerate(doc['body']['content']):
        if page.get('paragraph'):
            # Create a new paragraph for the paraphrased content
            new_paragraph = {'insertText': {'location': {'index': 1}, 'text': 'Page ' + str(i+1) + '\n\n'}}

            # Iterate over each paragraph in the page
            for paragraph in page['paragraph']['elements']:
                text = paragraph['textRun']['content']
                # Paraphrase the paragraph
                paraphrased_text = paraphrase(text)
                # Add the paraphrased paragraph to the new document
                new_paragraph['insertText']['text'] += paraphrased_text + '\n\n'
                # Add the original page number to the new document
                new_paragraph['insertText']['text'] += 'Original Page: ' + str(i+1) + '\n\n'

            # Insert the new paragraph into the new document
            docs_service.documents().batchUpdate(documentId=new_doc['documentId'], body={'requests': [new_paragraph]}).execute()

    print('Paraphrased document created with ID: {0}'.format(new_doc['documentId']))

# Usage example
paraphrase_doc('YOUR_GOOGLE_DOCS_DOCUMENT_ID_HERE')
