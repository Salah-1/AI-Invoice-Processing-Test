# Setting up Google Cloud (GCP) Document AI
# This proof of concept is now complete. Later benchmark testing will follow.

This guide outlines the necessary steps to configure Google Cloud Platform (GCP) for using the Document AI service, including setting up authentication and the local development environment.

## Prerequisites

*   A Google Cloud Platform Account
*   `gcloud` command-line tool installed and configured (or access to Cloud Shell)

## 1. Enable Required APIs

You need to enable the Document AI and Cloud Storage APIs for your project. You can do this via the GCP Console or the `gcloud` CLI.

*   **Option A: GCP Console**
    1.  Navigate to the [Google Cloud Console](https://console.cloud.google.com/).
    2.  Search for "Document AI API" and enable it.
    3.  Search for "Cloud Storage API" and ensure it is enabled (often enabled by default).

*   **Option B: Cloud Shell / `gcloud` CLI**
    *   Run the following command:
        ```bash
        gcloud services enable documentai.googleapis.com storage.googleapis.com
        ```

## 2. Access Document AI Workbench

*   In the [Google Cloud Console](https://console.cloud.google.com/), use the search bar to find and navigate to the **Document AI** service section (often called Workbench or Studio).

## 3. Configure Service Account & Permissions

A service account is needed for your application/code to authenticate and interact with GCP services securely.

1.  **Set Project Variable (Optional but Recommended):**
    ```bash
    export GOOGLE_CLOUD_PROJECT=$(gcloud config get-value core/project)
    ```

2.  **Create the Service Account (if it doesn't exist):**
    *   *Note:* The commands below assume a service account named `docai-service-account`. Replace this with your desired service account name if creating a new one or using an existing one. You might need to run `gcloud iam service-accounts create docai-service-account --display-name "My Document AI Service Account"` first if it doesn't exist.

3.  **Grant Necessary IAM Roles:**
    *   Assign the `Document AI Admin` role:
        ```bash
        gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
          --member="serviceAccount:docai-service-account@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
          --role="roles/documentai.admin"
        ```
    *   Assign the `Storage Admin` role (needed for accessing documents in GCS):
        ```bash
        gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
          --member="serviceAccount:docai-service-account@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
          --role="roles/storage.admin"
        ```
    *   Assign the `Service Usage Consumer` role (may be needed for API interactions):
        ```bash
        gcloud projects add-iam-policy-binding ${GOOGLE_CLOUD_PROJECT} \
          --member="serviceAccount:docai-service-account@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com" \
          --role="roles/serviceusage.serviceUsageConsumer"
        ```
    *   _**Important:**_ Replace `docai-service-account` with the actual name of your service account if different.

## 4. Generate Service Account Key

Create credentials (a JSON key file) that your application will use to authenticate as the service account.

1.  **Run the command:**
    ```bash
    gcloud iam service-accounts keys create ~/key.json \
      --iam-account docai-service-account@${GOOGLE_CLOUD_PROJECT}.iam.gserviceaccount.com
    ```
    *   _**Important:**_ Replace `docai-service-account` with the actual name of your service account.
    *   This command saves the key file as `key.json` in your home directory (`~`).

2.  **⚠️ Security Note:** Treat this `key.json` file like a password. Keep it secure and **do not** commit it to version control (e.g., Git). It's recommended to use environment variables (like `GOOGLE_APPLICATION_CREDENTIALS`) or secret management systems to handle this key in applications.

## 5. Configure Document AI Processor

Within the Document AI section of the GCP Console:

*   ✅ Choose a suitable **pre-built processor** (e.g., Invoice Parser, Form Parser).
*   *OR*
*   ✅ Create a **custom processor** using the options available in the left-hand menu (e.g., Custom Extractor, Custom Classifier).
*   ✅ **Tune** the processor settings as required for your specific documents and extraction needs.

## 6. Cloud Setup Complete

*   ✅ At this point, the necessary configuration within GCP is finished.

## Local Development Environment Setup

To interact with the Document AI service from your local Python environment, install the necessary Google Cloud client libraries:

```bash
pip3 install --upgrade google-cloud-documentai
pip3 install --upgrade google-cloud-storage
pip3 install --upgrade google-cloud-documentai-toolbox # Optional 

### Make certain that you copy over key.json file from your gcp console /home/user dir and over to your local dev env. Then export it as env variable as below
export GOOGLE_APPLICATION_CREDENTIALS="key.json"
