# AI-Invoice-Processing-Test
AI Invoice Processing Test (evaluating different solutions by the 3 cloud providers).

## Overview
#### For the impatient: look at the /src/ folder

AI-driven project to automatically process invoices, extract key business values, store and generate  reports. Extracted information is saved into `.csv` format for downstream processing.

## Key Features

*   ✅ Invoice Document Processing
*   ✅ Intelligent Extraction of Business Values
*   ✅ Report Generation from Extracted Data
*   ✅ Data Export to `.csv` for Further Analysis or System Input

## Technical Approach & Goals

The core development involves:

1.  **Python Implementation:** Building the primary logic using Python.
    *   *Initial Exploration:* Testing the use of Langchain for capabilities such as memory & prompt templates (Note: Specific tools like Langchain are under evaluation and may be adapted or replaced as development progresses).
I'm particularly, Interested In evaluating 'Azure Form Recognizer' and 'Azure AI search' and see how they perform compared to
AWS Intelligent document processing (IDP) GCP Document AI Form Parser (time permitting, I might not get to all of this)

2.  **API Accessibility:** Exposing the solution's functionality via an API endpoint upon deployment.
3.  **Multi-Cloud Deployment:** A key objective is to deploy and evaluate the solution across major cloud platforms:
    *   ☁️ Google Cloud Platform (GCP)
    *   ☁️ Amazon Web Services (AWS SageMaker)
    *   ☁️ Microsoft Azure (Azure AI)
    *   *Purpose:* To compare the integration steps, deployment processes, and operational nuances of AI solutions on each platform.

## Project Status

*   Currently under active development. The specific implementation details and technology choices (e.g., necessity of Langchain) are subject to refinement based on ongoing findings.
