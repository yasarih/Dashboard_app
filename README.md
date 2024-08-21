# Teacher's Data Dashboard

This Streamlit app is designed to display and filter teacher data from a Google Sheets document.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the environment variable for your Google Cloud credentials:

    - On macOS/Linux:
    
        ```bash
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/json_key.json"
        ```

    - On Windows:
    
        ```cmd
        set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\your\json_key.json
        ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

## Deployment

To deploy this app using a service like Streamlit Cloud, make sure to set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable in the deployment settings.
