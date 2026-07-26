# 💼 Automated Job Agent Pro

An end-to-end Python pipeline designed to automate the remote job search and application process. 

## 🚀 Features

* **Live Job Scraping:** Integrates with remote job APIs (`requests`) to fetch real-time listings, salaries, and geographic requirements based on target roles.
* **Resume Analyzer:** Uses `PyPDF2` to extract text from a base PDF resume, comparing it against required job keywords to calculate a match score.
* **Resume Generator:** Automatically generates a customized `.docx` resume using `python-docx` to inject missing keywords and bypass ATS filters.
* **Browser Automation:** Utilizes `Playwright` to autonomously navigate web browsers, interact with web elements, and fill out application forms.
* **Interactive Dashboard:** Features a sleek, user-friendly web interface built with `Streamlit` to manage the entire pipeline from a single page.

## 🛠️ Tech Stack

* **Language:** Python
* **Frontend UI:** Streamlit
* **Automation:** Playwright
* **Data Processing:** PyPDF2, python-docx, Requests

## 💻 Local Installation

To run this project locally on your machine:

1. Clone the repository:
   ```bash
   git clone [https://github.com/Phunkie07/Job-Agent.git](https://github.com/Phunkie07/Job-Agent.git)