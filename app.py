import streamlit as st
from openai import OpenAI

# 1. Setup the Web Page Title and Design
st.set_page_config(page_title="AI Root Cause Analysis Generator", page_icon="⚙️")
st.title("📟 AI Root Cause Analysis (RCA) Generator")
st.write("Paste your raw logs and system metrics below to instantly generate a professional SRE Incident Report.")

# 2. Add an Input Box for the User's OpenAI Key
# This ensures your app can access the AI model securely
api_key = st.sidebar.text_input("Enter your OpenAI API Key", type="password")

# 3. Create the Main Inputs on the Screen
incident_title = st.text_input("Incident Title", placeholder="e.g., Payment Gateway 500 Errors")
raw_data = st.text_area("Paste System Logs / Metrics Here", height=200, placeholder="Paste raw error codes, CPU spikes, or application logs...")

# 4. Create the "Magic" Button
if st.button("Generate RCA Report"):
    # Check if the user forgot their API key or data
    if not api_key:
        st.error("Please enter your OpenAI API Key in the sidebar to proceed.")
    elif not raw_data:
        st.warning("Please paste some log or metric data first.")
    else:
        with st.spinner("Analyzing data and generating report..."):
            try:
                # Connect to the OpenAI Engine
                client = OpenAI(api_key=api_key)
                
                # Formulate the instructions for the AI
                system_instruction = (
                    "You are an expert Principal Site Reliability Engineer (SRE). "
                    "Analyze the provided logs/metrics and generate a highly professional "
                    "Root Cause Analysis (RCA) report in Markdown format. Include sections for: "
                    "Executive Summary, Incident Timeline Hypothesis, Root Cause Determination, and Short/Long-term Preventative Actions."
                )
                
                # Send the data to the AI model
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_instruction},
                        {"role": "user", "content": f"Incident: {incident_title}\n\nData:\n{raw_data}"}
                    ],
                    temperature=0.2
                )
                
                # Display the result beautifully on the screen
                st.success("RCA Report Generated Successfully!")
                st.markdown("---")
                st.markdown(response.choices[0].message.content)
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
