# Junior Programmer Homework Assignment: Data Cleaning with Python

Welcome to your homework assignment! This task is designed to assess your ability to set up a Python project, manage dependencies, perform basic data manipulation, and follow a standard Git workflow.

This project will be hosted publicly on GitHub.

## 1. Project Setup and Environment Management

Your first task is to set up the project using `uv`.

### Prerequisites:
*   Ensure you have `uv` installed on your system. If not, you can install it via `pipx`:
    ```bash
    pipx install uv
* Or, use standalone installer (Options differ for Linux, macOS, and Windows):

## 2. Steps

1. Clone the project from GitHub to your local machine using https:
    ```bash
    git clone https://github.com/koldamartin/Robosales-homework.git
    ```
    or using SSH
    ```bash
    git clone git@github.com:koldamartin/Robosales-homework.git
    ```
2. Initialize the project and create a virtual environment using `uv` (Use Python > 3.8):
3. Activate the virtual environment
4. Install required libraries using `uv`, you will need `pandas` and possibly `numpy`:

## 3. The Data Cleaning Task

You will find a CSV file named `raw_tenisove_micky.csv` in the `data/` folder of this project. Your goal is to write a Python script that cleans this data.

**Task Requirements:**
1. **Create a Python script:** Name it clean_data.py and place it in a new directory, e.g., src/.
2. **The script will:**
   - **Load the data:** Use pandas to load `data/raw_tenisove_micky.csv` into a DataFrame.
   - **Clean the data:** Apply appropriate data cleaning techniques using pandas and numpy:
     * Remove all rows that are not 'Tenisové míče' in its `title` column. (e.g. Koše na tenisové míče, Tuby na sbírání míčků)
     * Remove these prefixes from title column: "Tenisové míče", "Dětské tenisové míče", "Velký tenisový míč", (e.g. "Tenisové míče Head Pro (3 Pack)" -> "Head Pro (3 Pack)")
     * Create a 'group_title' column, that will have same values as 'title' (also without prefixes)
     * Convert 'price_czk' column to numerical values
     * Convert 'Balení míčků' column to numerical values
     * Create a new column called 'unit_price_czk' based on 'price_czk' and 'Balení míčků' (it will be numerical column that tells the unit proce for 1 tennis ball)
     * Create two new columns: 'age_min' and 'age_max' (it will be numerical columns) based on 'Doporučený věk' column. Then drop the 'Doporučený věk' column.
     * Fill all NaN values in 'Doporučený povrch' column with value 'všechny povrchy'
     * In all columns drop the double spaces. (e.g. "Tenisové míče Head  Pro (3 Pack)" notice the double space between "Head" and "Pro")
     * Leave all other columns unchanged

   - **Save the cleaned data:** Save the cleaned DataFrame to a new CSV file named `cleaned_tenisove_micky.csv` in the `data/` folder.


## 4. README.md Requirements
In addition to your Python script, you must create a README.md file in the root of your project. This README.md should serve as a guide for someone else to understand and run your project.
Your README.md must include:
1. **Project Title and Description:** A brief overview of the project. (in English)
2. **How to Copy the Project:** Instructions on how to clone the repository to local machine.
3. **How to Start the Environment:** Steps to activate the uv virtual environment.
4. **How to Install All Dependencies:** Instructions on installing pandas and numpy using uv.
5. **How to Run the Script:** Clear steps on how to execute your clean_data.py script.

## 5. Submission guidelines
You will submit your homework by creating a Pull Request (PR) to the main branch of this repository.

**Steps:**

1. Create a new feature branch: Before you start coding, create a new branch for your work.
2. Implement your solution: Write your `clean_data.py` script, the `README.md` file and the cleaned csv.
3. Commit your changes: Commit your changes to the new branch.
4. Push your branch to the Github repository to the newly created branch
5. Create a PR: Create a Pull Request (PR) from your branch to the main branch.
