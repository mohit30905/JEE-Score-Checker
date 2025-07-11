# JEE-Score-Checker
This project provide us to calculate our India's top Entrance Exam JEE Score.

## 🎯 Objective
This project helps JEE (Joint Entrance Examination) candidates evaluate their performance by comparing their attempted answers with the official answer key. It parses HTML files downloaded from the JEE portal and computes the score based on correct and incorrect answers.

## 🧠 Techniques Used
This project uses HTML parsing and data extraction techniques to compute the JEE exam score. 
- Web scraping with requests to fetch the official answer key HTML.
- HTML parsing using BeautifulSoup to extract question IDs and answers from both the official answer sheet and the student's response sheet.
- Dictionary matching logic to compare corresponding question-answer pairs.
- Conditional filtering to determine correct and incorrect answers.
- Scoring algorithm based on JEE marking scheme: +4 for correct, -1 for wrong, and 0 for unanswered.
- This approach automates manual checking and provides a quick and efficient way to analyze performance from raw HTML data.

## 🖥️ Requirements
-  Python 3
-  beautifulsoup4
-  requests

## 📂 Project Explanation
# 1. get content.py
This script allows you to extract web content from the official website by providing the URL. It downloads the HTML page and saves it with your desired filename inside the jee folder. An example of the saved file can be found in the jee directory.

# 2. parsing.py
This file helps us extract question IDs and their correct answers from the official JEE answer key. By providing the exam date and shift, it opens the corresponding HTML file stored in the jee folder, parses the content using BeautifulSoup, and creates a dictionary of question-answer pairs for further comparison.

# 3. parsing_student.py
This file helps us extract the student's attempted answers from their response HTML file. By providing your name, it opens the corresponding file from the jee folder, parses the content using BeautifulSoup, and creates a dictionary of question IDs with the answers you selected. This data is used later to compare with the official answer key.

# 4. Jee score checker.py
This file helps us calculate the JEE score by comparing the official answer key with the student's responses. It matches question IDs and checks if the answers are correct or incorrect. Based on the JEE marking scheme (+4 for correct, -1 for wrong), it calculates and displays the total score out of 300 along with the number of correct and incorrect answers.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/JEE-Score-Checker.git
   cd JEE-Score-Checker
   
2. Install appropriate modules.
   pip install beautifulsoup4 requests

4. Follow these steps:
- Run get content.py to download the official key.
- Run parsing.py and parsing_student.py with correct input.
- Run jee score checker.py to get your final score.

## ⚠️ Warning
Enter your name, exam date, and shift exactly as you saved the files, or update the main code accordingly. Otherwise, the program may throw an error due to mismatched file names or incorrect inputs.
