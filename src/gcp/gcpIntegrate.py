from google.api_core.client_options import ClientOptions
from google.cloud import documentai


import os
import openai

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file
openai.api_key = os.environ['OPENAI_API_KEY']

# Note for security, the below should be read via environment file !
PROJECT_ID = os.environ['THE_PROJECT_ID']
LOCATION = os.environ['THE_PROJECT_LOCATION'] # Format is 'us' or 'eu'
PROCESSOR_ID = os.environ['THE_PROCESSOR_ID'] # Create processor in Cloud Console
# print(PROJECT_ID)
# quit()
# The local file to process. In the future input can be flutter app used by employee
FILE_PATH = "images/Paid-time-off-policiy-from-indeed.pdf"

MIME_TYPE = "application/pdf"

# Instantiates a client
docai_client = documentai.DocumentProcessorServiceClient(
    client_options=ClientOptions(api_endpoint=f"{LOCATION}-documentai.googleapis.com")
)

# The full resource name of the processor, e.g.:

RESOURCE_NAME = docai_client.processor_path(PROJECT_ID, LOCATION, PROCESSOR_ID)

# Read the file into memory
with open(FILE_PATH, "rb") as image:
    image_content = image.read()

# Load Binary Data into Document AI RawDocument Object
raw_document = documentai.RawDocument(content=image_content, mime_type=MIME_TYPE)

# Configure the process request
request = documentai.ProcessRequest(name=RESOURCE_NAME, raw_document=raw_document)

# Use the Document AI client to process the sample form
result = docai_client.process_document(request=request)

document_object = result.document
print("Document processing complete.")
print(f"Text: {document_object.text}")