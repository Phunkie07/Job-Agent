from playwright.sync_api import sync_playwright
import time

def run_job_application_bot(resume_path):
    print("🤖 Waking up Browser Automation Engine...")
    
    # Start Playwright context
    with sync_playwright() as p:
        # launch(headless=False) makes the browser visible so you can watch it work!
        print("Opening Chromium browser...")
        browser = p.chromium.launch(headless=False, slow_mo=1000) # slow_mo adds 1s delay per action so you can follow along
        
        # Create a new page tab
        page = browser.new_page()
        
        # 1. NAVIGATE: Go to a target application page / form
        print("Navigating to job application page...")
        page.goto("https://httpbin.org/forms/post") # Safe demo form for testing input automation
        
        # 2. TYPE / FILL: Fill out applicant details
        print("Filling out application form details...")
        page.fill('input[name="custname"]', 'David - Software Developer')
        page.fill('input[name="custtel"]', '+1-555-0199')
        page.fill('input[name="custemail"]', 'david@example.com')
        
        # Select options
        page.check('input[value="medium"]') # Choose pizza size as proxy for option select
        page.check('input[value="cheese"]') # Choose topping
        
        # Add comments / cover note
        page.fill('textarea[name="comments"]', 'Applied via Automated Job Agent Pipeline.')
        
        print("Form successfully filled by Python!")
        
        # Pause 3 seconds so you can see the result before closing
        time.sleep(3)
        
        # 3. CLOSE
        print("Closing browser session...")
        browser.close()

if __name__ == "__main__":
    # Path to our generated resume
    resume_file = "tailored_resume.docx"
    
    print("Initializing Stage 7: Browser Automation...")
    run_job_application_bot(resume_file)
    print("Stage 7 complete!")