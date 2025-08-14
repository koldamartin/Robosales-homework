# Tennis Balls Data Cleaning

This project is a homework assignment focused on cleaning raw tennis balls data from a CSV file using Python and pandas.  
It loads raw data, applies several cleaning steps, and saves the cleaned result to a new file.

---

## How to Clone the Project

Clone the repository using HTTPS:
```bash
git clone https://github.com/koldamartin/Robosales-homework.git
```

Or using SSH:
```bash
git clone git@github.com:koldamartin/Robosales-homework.git
```

---

## How to Start the Environment

This project uses [uv](https://github.com/astral-sh/uv) for virtual environment management.

1. Create a new virtual environment (Python 3.8+ required):
```bash
uv venv
```
2. Activate the environment:
   - **Windows (PowerShell)**:
     ```bash
     .\.venv\Scripts\Activate.ps1
     ```
   - **Windows (CMD)**:
     ```bash
     .\.venv\Scripts\activate.bat
     ```
   - **macOS / Linux**:
     ```bash
     source .venv/bin/activate
     ```

---

## How to Install Dependencies

Install required packages:
```bash
uv pip install pandas numpy
```

---

## Data Cleaning Steps

The script `clean_data.py` performs the following operations on the raw dataset:

1. **Remove non-tennis ball rows**  
   Deletes rows where the `title` contains unwanted items such as "Koše na tenisové míče" or "Tuby na sbírání míčků" (even if followed by extra text).

2. **Remove prefixes from titles**  
   Strips leading phrases like "Tenisové míče", "Dětské tenisové míče", "Velký tenisový míč" from the `title` column.

3. **Create `group_title` column**  
   A duplicate of the cleaned `title` column for grouping purposes.

4. **Convert `price_czk` to numbers**  
   Removes currency symbols and converts values to floats.

5. **Convert `Balení míčků` to numbers**  
   Extracts numeric values from text (e.g., "Balení 3 ks" → `3`).

6. **Create `unit_price_czk`**  
   Calculates the unit price per ball (`price_czk / Balení míčků`).

7. **Extract age range**  
   Creates `age_min` and `age_max` columns from `Doporučený věk` and drops the original column.

8. **Fill missing surface recommendations**  
   Sets empty `Doporučený povrch` values to "všechny povrchy".

9. **Remove double spaces**  
   Ensures all string columns have only single spaces between words.

10. **Drop redundant columns**  
    Removes unnecessary columns that duplicate existing data.

---

## How to Run the Script

After activating the virtual environment, run:
```bash
python src/clean_data.py
```

This will:
- Load the file `data/raw_tenisove_micky.csv`
- Clean the data according to the steps above
- Save the result as `data/cleaned_tenisove_micky.csv`

---
