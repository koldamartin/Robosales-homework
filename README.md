# Tennis Ball Data Cleaning Project

## Project Description

This project is a data cleaning assignment focused on processing tennis ball product data from a Czech e-commerce website. The goal is to clean and standardize raw CSV data containing tennis ball products, applying various data transformation techniques using Python, pandas, and numpy.

The script filters tennis ball products, cleans title prefixes, converts price and packaging information to numerical formats, processes age recommendations, and creates calculated fields like unit pricing.

## How to Copy the Project

Clone the repository to your local machine using one of the following methods:

**Using HTTPS:**
```bash
git clone https://github.com/koldamartin/Robosales-homework.git
cd Robosales-homework
```

**Using SSH:**
```bash
git clone git@github.com/koldamartin/Robosales-homework.git
cd Robosales-homework
```

## How to Start the Environment

This project uses `uv` for Python environment management. Follow these steps to set up and activate the virtual environment:

1. **Ensure you have `uv` installed.** If not, install it using:
   ```bash
   pipx install uv
   ```

2. **The project is already initialized with a `pyproject.toml` file.** To activate the virtual environment:
   ```bash
   uv sync
   ```

3. **Activate the virtual environment:**
   ```bash
   source .venv/bin/activate  # On Linux/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

Alternatively, you can run commands directly with uv without activating the environment by prefixing commands with `uv run`.

## How to Install All Dependencies

The required dependencies (pandas and numpy) are already specified in the `pyproject.toml` file. Install them using:

```bash
uv sync
```

Or if you want to install them manually:
```bash
uv add pandas numpy
```

## How to Run the Script

Execute the data cleaning script using one of the following commands:

**Using uv (recommended):**
```bash
uv run python src/clean_data.py
```

**Using activated virtual environment:**
```bash
python src/clean_data.py
```

The script will:
1. Load the raw data from `data/raw_tenisove_micky.csv`
2. Apply all cleaning transformations
3. Save the cleaned data to `data/cleaned_tenisove_micky.csv`
4. Display summary statistics and processing information

## Data Cleaning Operations

The script performs the following cleaning operations:

1. **Filter tennis balls only**: Removes non-tennis ball products (baskets, collection tubes, etc.)
2. **Remove title prefixes**: Strips "Tenisové míče", "Dětské tenisové míče", "Velký tenisový míč" prefixes
3. **Create group_title column**: Duplicate of cleaned title for grouping purposes
4. **Convert prices to numeric**: Transforms "259 CZK" format to numerical values
5. **Convert packaging info**: Extracts numbers from "dóza po 4 ks" or "36 ks" formats
6. **Calculate unit prices**: Creates price per tennis ball column
7. **Process age ranges**: Converts "5-8 let" to separate age_min and age_max columns
8. **Fill missing surface info**: Replaces NaN values with "všechny povrchy"
9. **Remove double spaces**: Cleans up formatting inconsistencies
10. **Remove redundant columns**: Eliminates unnecessary duplicate columns

## Project Structure

```
Robosales-homework/
├── data/
│   ├── raw_tenisove_micky.csv        # Input data
│   └── cleaned_tenisove_micky.csv    # Output data (generated)
├── src/
│   └── clean_data.py                 # Main cleaning script
├── docs/
│   └── guide.md                      # Assignment instructions
├── pyproject.toml                    # Project dependencies
├── uv.lock                          # Dependency lock file
└── README.md                        # This file
```

## Requirements

- Python 3.8+
- pandas
- numpy
- uv (for environment management)

## Output

The cleaned dataset will contain only tennis ball products with:
- Cleaned product titles
- Numerical price and packaging information
- Calculated unit prices
- Structured age recommendations
- Standardized surface recommendations
- Removed redundant information