import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Opens a PDF in binary mode and extracts all text."""
    text = ""
    try:
        with open(pdf_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            # Loop through every page in the PDF and grab the text
            for page in reader.pages:
                text += page.extract_text() + " "
        return text.lower() # Convert to lowercase for easy matching
    except FileNotFoundError:
        print(f"CRITICAL ERROR: Could not find '{pdf_path}'. Check the file name!")
        return None

def calculate_match(resume_text, job_keywords):
    """Compares resume text against required job keywords."""
    matched_keywords = []
    
    # Check if each required keyword exists in the resume
    for keyword in job_keywords:
        if keyword in resume_text:
            matched_keywords.append(keyword)
            
    # Calculate the percentage
    total_required = len(job_keywords)
    total_matched = len(matched_keywords)
    match_score = (total_matched / total_required) * 100
    
    # Find what is missing by subtracting matched words from required words
    missing_keywords = list(set(job_keywords) - set(matched_keywords))
    
    # Print the final report
    print("\n--- 📊 Resume Analysis Report ---")
    print(f"Keywords Found: {', '.join(matched_keywords)}")
    print(f"Missing Keywords: {', '.join(missing_keywords)}")
    print(f"Match Score: {match_score:.0f}%\n")

# ==========================================
# MAIN SCRIPT EXECUTION
# ==========================================
if __name__ == "__main__":
    # 1. Setup the target file and requirements
    resume_file = "my_resume.pdf" 
    
    # These are the skills a theoretical job posting is asking for
    required_skills = ["python", "git", "github", "api", "json", "requests", "data"]
    
    print("Initializing Stage 5: Resume Analyzer...")
    
    # 2. Extract the text
    my_resume_text = extract_text_from_pdf(resume_file)
    
    # 3. If extraction worked, run the analysis
    if my_resume_text:
        calculate_match(my_resume_text, required_skills)