import requests

# REAL API: Remotive's open API for remote software dev jobs
api_url = "https://remotive.com/api/remote-jobs?category=software-dev&limit=100"
approved_jobs = []

print("Waking up Job Agent...")
print("Connecting to live job board...")

try:
    # 1. FETCH
    response = requests.get(api_url)
    
    if response.status_code == 200:
        print("Connection successful! Translating data...")
        data = response.json() 
        # Remotive puts the list of jobs inside a dictionary key called "jobs"
        live_jobs = data.get("jobs", []) 
        
        # 2. CLEAN & FILTER
        for job in live_jobs:
            raw_title = job.get("title", "")
            clean_title = raw_title.strip().lower()
            
            if "python" in clean_title:
                company = job.get("company_name", "Unknown")
                approved_jobs.append(clean_title.title() + " at " + company)
                
        # 3. SAVE
        with open("python_shortlist.txt", "w") as file:
            for match in approved_jobs:
                file.write(match + "\n")
                
        print("Agent finished! Saved " + str(len(approved_jobs)) + " jobs to python_shortlist.txt.")
        
    else:
        print("Server rejected request. Status:", response.status_code)
        
except Exception as e:
    print("CRITICAL ERROR:", e)