import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="Analytics Dashboard", layout="wide")
st.title("Analytics Dashboard")


# Form for adding new entries
with st.form("add_entry_form"):
    date_entry = st.text_input("Date (YYYY-MM-DD)")
    metric_entry = st.number_input("Metric", min_value=0, value=100)
    submitted = st.form_submit_button("Add Entry")
    if submitted and date_entry:
        payload = {"date": date_entry, "metric": int(metric_entry)}
        response = requests.post("http://localhost:8080/api/analytics", json=payload)
        if response.status_code == 200:
            st.success(f"Added entry: {payload}")
        else:
            st.error("Failed to add entry")

response = requests.get("http://localhost:8080/api/analytics")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write("## Current Analytics Data")
    st.dataframe(df)
    if not df.empty:
        st.line_chart(df['metric'])
else:
    st.error("Failed to fetch analytics data")
