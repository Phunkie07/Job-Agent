import streamlit as st
import requests
import time

# 1. Page Configuration
st.set_page_config(page_title="Job Agent Pro", page_icon="💼")

# 2. Header Section
st.title("💼 Automated Job Agent Pro")
st.markdown("Welcome to your personal AI recruiter. Enter your target job below to fetch live remote roles.")

# 3. User Input
target_role = st.text_input("Target Role (e.g., Virtual Assistant):")
uploaded_resume = st.file_uploader("Upload Your Base Resume (PDF or DOCX)", type=["pdf", "docx"])

# 4. Action Button
if st.button("🚀 Run Job Agent Pipeline"):
    if not target_role or not uploaded_resume:
        st.warning("Please enter a target role and upload a resume to begin.")
    else:
        st.info(f"Searching real live APIs for: **{target_role}**...")
        
        # We plug in the Remotive API from your earlier Stage 4 lessons
        api_url = f"https://remotive.com/api/remote-jobs?search={target_role}"
        
        try:
            # Python reaches out to the live internet
            response = requests.get(api_url)
            data = response.json()
            jobs = data.get('jobs', [])
            
            if jobs:
                st.success(f"Successfully pulled {len(jobs)} live jobs from the internet!")
                
                # We loop through the top 5 jobs and display their actual data
                for job in jobs[:5]:
                    
                    # Create a neat dropdown box for each job
                    with st.expander(f"🏢 {job['company_name']} - {job['title']}"):
                        st.write(f"**📍 Location Required:** {job['candidate_required_location']}")
                        
                        # Some employers leave salary blank, so we handle that cleanly
                        salary = job['salary'] if job['salary'] else "Not disclosed by employer"
                        st.write(f"**💰 Pay Range:** {salary}")
                        
                        st.write(f"**📂 Category:** {job['category']}")
                        st.markdown(f"**[🔗 Direct Link to Apply Here]({job['url']})**")
                        
                st.write("---")
                st.write("*Note: In a fully integrated pipeline, your browser automation script would now click those links and apply for you.*")
                
            else:
                st.error("No jobs found for that role right now. Try a different keyword!")
                
        except Exception as e:
            st.error("There was an issue connecting to the live API. Please try again.")