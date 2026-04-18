# DATATHON 2026: THE GRIDBREAKERS - Project Workspace

This repository contains the source code, notebooks, and configuration files for our team (2 IT, 1 DS) participating in DATATHON 2026.

## ⚠️ STRICT DATA PRIVACY RULE

**DO NOT push any raw data files (`.csv`, `.xlsx`, `.json`) to this repository.** All data files must remain on your local machine. The `.gitignore` is already configured to prevent accidental uploads. Violating this rule will result in disqualification based on the competition's Data Ethics criteria.

---

## 1. Prerequisites

Before you begin, ensure you have the following installed on your machine:

- **Python 3.9+** (Added to system PATH)
- **Git** & **Git Bash** (For Windows users)
- **GitHub Desktop** (Optional but recommended for beginners)

---

## 2. Initial Setup (Do this once)

### Step 1: Clone the Repository

Open your terminal (or Git Bash) and run:
git clone https://github.com/tuongvii2327/Datathon.2026.git
cd Datathon.2026

### Step 2: Create a Virtual Environment (venv)

We use a virtual environment to ensure all team members run the exact same library versions without breaking their local machine setups.

**For Windows (using Git Bash or Command Prompt):**
python -m venv venv

**For macOS / Linux:**
python3 -m venv venv

### Step 3: Activate the Virtual Environment

You must activate the environment **every time** you work on this project.

**For Windows (Git Bash):**
source venv/Scripts/activate
_(If using Windows CMD: .\venv\Scripts\activate)_

**For macOS / Linux:**
source venv/bin/activate
_(Success indicator: You will see `(venv)` at the beginning of your terminal prompt)._

### Step 4: Install Dependencies

With `(venv)` activated, install the required Data Science packages:
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

---

## 3. Workflow for Updating Libraries

If you need a new library (e.g., `plotly`) for your EDA or ML models, follow these steps to ensure the whole team gets the update:

**Step 1: Install the library locally**
pip install plotly

**Step 2: Update the dependencies file**
pip freeze > requirements.txt

**Step 3: Push to GitHub**
Commit and push the updated `requirements.txt` to the repository.

**Step 4: How others sync the update**
When other members pull the latest code, they must run:
pip install -r requirements.txt

---

## 4. Daily Git Workflow (Quy trình code hàng ngày)

To avoid code conflicts between the 3 members, strictly follow these steps every day:

**Step 1: ALWAYS pull before you start coding**
git pull origin main

**Step 2: Make your changes and save**

# Edit your code in VS Code or Jupyter Notebook

**Step 3: Stage and Commit your changes**
git add .
git commit -m "Prefix: Short description of what you did"

# Examples of good commit messages:

# git commit -m "EDA: Add histogram plots for numerical variables"

# git commit -m "Fix: Clean missing values in preprocessing function"

**Step 4: Push to GitHub**
git push origin main

---

## 5. Branching Strategy (Làm việc song song)

Since 2 IT and 1 DS are working simultaneously, use branches for major features to prevent breaking the main codebase.

**Create and switch to a new branch:**
git checkout -b <branch-name>

# Example: git checkout -b data-cleaning

**Push your branch to GitHub:**
git push origin <branch-name>

**Merge your work back to main (Once confirmed working):**
git checkout main
git pull origin main
git merge <branch-name>
git push origin main

---

## 6. Project Structure

Datathon.2026/
├── .gitignore # Ignores data files and venv to secure raw data
├── requirements.txt # List of project dependencies
├── README.md # Project documentation
├── notebooks/ # Jupyter notebooks for Exploratory Data Analysis (EDA)
└── src/ # Python scripts for data processing and ML models
