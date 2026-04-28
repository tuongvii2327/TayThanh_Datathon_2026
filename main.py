import os
import subprocess
import sys
import webbrowser

NOTEBOOK_DIR = "notebooks"
REPORT_DIR = "reports_html"

os.makedirs(REPORT_DIR, exist_ok=True)

notebooks = [
    "01_data_cleaning.ipynb",
    "02_MCQs_answers.ipynb",
    # "03_EDA_huong1.ipynb",
    # "04_EDA_huong2.ipynb",
    # "05_EDA_huong3.ipynb",
    # "05_features_engineering.ipynb",
    # "06_modeling.ipynb"
]

generated_html = []


def run_notebook(nb):
    nb_path = os.path.join(NOTEBOOK_DIR, nb)

    if not os.path.exists(nb_path):
        print(f"Skipped: {nb}")
        return
    print(f"\nRunning: {nb}")

    subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "notebook",
            "--execute",
            "--inplace",
            "--ExecutePreprocessor.timeout=600"
        ] + [nb_path],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print(f"Done: {nb}")


def export_html(nb):
    nb_path = os.path.join(NOTEBOOK_DIR, nb)

    if not os.path.exists(nb_path):
        return
    print(f"Exporting: {nb}")

    subprocess.run(
        [
            sys.executable, "-m", "jupyter", "nbconvert",
            "--to", "html",
            "--output-dir", REPORT_DIR,
            nb_path
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    html_file = os.path.join(REPORT_DIR, nb.replace(".ipynb", ".html"))

    if os.path.exists(html_file):
        generated_html.append(html_file)


def open_reports():
    print("\n🌐 Opening reports...\n")

    for html in generated_html:
        webbrowser.open(f"file://{os.path.abspath(html)}")


if __name__ == "__main__":
    print("\n🚀 START PIPELINE...")
    # 1. Run notebooks
    for nb in notebooks:
        run_notebook(nb)
    # 2. Export HTML
    print("\nExporting reports...\n")
    for nb in notebooks:
        export_html(nb)
    # 3. Open ALL at once
    open_reports()

    print("\nALL DONE!")