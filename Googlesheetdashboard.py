import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os

# Set up the Google Sheets API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Use environment variable to store the path to the JSON key file
json_key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if not json_key_path:
    st.error("The GOOGLE_APPLICATION_CREDENTIALS environment variable is not set.")
else:
    creds = ServiceAccountCredentials.from_json_keyfile_name(yasaranglebelearn-db34409d3f0c.json, scope)
    client = gspread.authorize(creds)

    # Use the spreadsheet ID from your Google Sheets link
    spreadsheet_id = "1_2rAj3WIYH5dswTwm2SZZwZITS5GoLuBSupLdKQaGrI"
    spreadsheet = client.open_by_key(spreadsheet_id)
    worksheet = spreadsheet.get_worksheet_by_id(106742000)  # Use the gid (sheet ID)

    # Get all values from the sheet
    data = worksheet.get_all_values()

    # Convert to DataFrame
    df = pd.DataFrame(data[1:], columns=data[0])  # Skipping the header row in the data

    st.title("Teacher's Data Dashboard")

    st.subheader('Filter')
    columns = df.columns.to_list()  # Get the list of columns

    selected_columns = st.multiselect('Select columns to filter by', columns)  # Allow multiple columns selection

    filtered_df = df.copy()  # Create a copy of the DataFrame to apply filters

    for column in selected_columns:
        unique_values = filtered_df[column].unique()  # Get unique values for the selected column
        selected_value = st.selectbox(f'Select value for {column}', unique_values)
        filtered_df = filtered_df[filtered_df[column] == selected_value]  # Apply filter for each column

    # Drop the filtered columns before displaying the result
    filtered_df = filtered_df.drop(columns=selected_columns)

    st.subheader('Filtered Data')
    st.write(filtered_df)  # Display the filtered DataFrame
