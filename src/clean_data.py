import pandas as pd
import numpy as np
import re
import os

def clean_data():
    # File paths
    input_file = "data/raw_tenisove_micky.csv"
    output_file = "data/cleaned_tenisove_micky.csv"

    # Load CSV into a DataFrame
    df = pd.read_csv(input_file)

    # Remove rows that are not tennis balls (exact match patterns)
    exclude_patterns = [
        r"^Koš na tenisové míče",
        r"^Tuba na sbírání míčků"
    ]
    pattern = "|".join(exclude_patterns)
    df = df[~df['title'].str.contains(pattern, case=False, na=False)]

    # Remove prefixes from the title column
    prefixes = [
        "Tenisový míč",
        "Tenisové míče",
        "Dětské tenisové míče",
        "Velký tenisový míč"
    ]
    pattern = r"^(?:" + "|".join(map(re.escape, prefixes)) + r")\s*"
    df['title'] = df['title'].str.replace(pattern, "", regex=True)

    # Create 'group_title' column (copy of title without prefixes)
    df['group_title'] = df['title']

    # Convert 'price_czk' to numeric values
    df['price_czk'] = (
        df['price_czk']
        .astype(str)
        .str.replace(r"[^\d,\.]", "", regex=True)  # remove non-numeric characters
        .str.replace(",", ".", regex=False)        # replace comma with dot
        .astype(float)
    )

    # Convert 'Balení míčků' to numeric values
    df['Balení míčků'] = (
        df['Balení míčků']
        .astype(str)
        .str.extract(r"(\d+)")
        .astype(float)
    )

    # Calculate 'unit_price_czk' = price per single ball
    df['unit_price_czk'] = df['price_czk'] / df['Balení míčků']

    # Extract 'age_min' and 'age_max' from 'Doporučený věk'
    def parse_age_range(val):
        if pd.isna(val):
            return np.nan, np.nan
        numbers = re.findall(r"\d+", str(val))
        if len(numbers) == 1:
            return int(numbers[0]), int(numbers[0])
        elif len(numbers) >= 2:
            return int(numbers[0]), int(numbers[1])
        else:
            return np.nan, np.nan

    df[['age_min', 'age_max']] = df['Doporučený věk'].apply(
        lambda x: pd.Series(parse_age_range(x))
    )

    # Drop the original 'Doporučený věk' column
    df.drop(columns=['Doporučený věk'], inplace=True)

    # Fill NaN values in 'Doporučený povrch' with "všechny povrchy"
    if 'Doporučený povrch' in df.columns:
        df['Doporučený povrch'] = df['Doporučený povrch'].fillna('všechny povrchy')

    # Remove double spaces in all string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.replace(r"\s{2,}", " ", regex=True)

    # Drop redundant columns if any
    redundant_columns = []  # add column names here if you know they are duplicates
    df.drop(columns=redundant_columns, errors='ignore', inplace=True)

    # Save cleaned data to a new CSV file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    df.to_csv(output_file, index=False, encoding="utf-8-sig")

    print(f"Data has been cleaned and saved to: {output_file}")

if __name__ == "__main__":
    clean_data()
