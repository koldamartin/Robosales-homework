import pandas as pd
import numpy as np
import re
import os


def clean_tennis_balls_data():
    """
    Clean tennis balls data from raw CSV file according to specified requirements.
    """
    # Load the data - handle both running from project root and from src/ directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)  # Go up one level from src/ to project root
    
    input_path = os.path.join(project_root, 'data', 'raw_tenisove_micky.csv')
    output_path = os.path.join(project_root, 'data', 'cleaned_tenisove_micky.csv')
    
    # Alternative paths in case script is run from project root
    if not os.path.exists(input_path):
        input_path = os.path.join('data', 'raw_tenisove_micky.csv')
        output_path = os.path.join('data', 'cleaned_tenisove_micky.csv')
    
    try:
        df = pd.read_csv(input_path)
        print(f"Loaded {len(df)} rows from {input_path}")
    except FileNotFoundError:
        print(f"Error: Could not find file {input_path}")
        print("Make sure you're running the script from the project root directory or that the data/ folder exists")
        return
    
    # 1. Remove all rows that are not tennis balls (remove baskets and collection tubes)
    print("Filtering for tennis balls only...")
    # Remove rows containing basket keywords
    df = df[~df['title'].str.contains('Koš na tenisové míče', na=False)]
    df = df[~df['title'].str.contains('Koše na tenisové míče', na=False)]
    # Remove rows containing collection tube keywords
    df = df[~df['title'].str.contains('Tuba na sbírání míčků', na=False)]
    df = df[~df['title'].str.contains('Tuby na sbírání míčků', na=False)]
    print(f"After filtering: {len(df)} rows remaining")
    
    # 2. Remove double spaces from all columns before processing
    print("Removing double spaces from all columns...")
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(r'\s+', ' ', regex=True).str.strip()
            df[col] = df[col].replace('nan', np.nan)
    
    # 3. Remove prefixes from title column
    print("Removing prefixes from title column...")
    prefixes_to_remove = [
        'Tenisové míče ',
        'Dětské tenisové míče ',
        'Velký tenisový míč '
    ]
    
    for prefix in prefixes_to_remove:
        df['title'] = df['title'].str.replace(prefix, '', regex=False)
    
    # 4. Create a 'group_title' column
    df['group_title'] = df['title'].copy()
    
    # 5. Convert 'price_czk' column to numerical values
    print("Converting price_czk to numerical values...")
    df['price_czk'] = df['price_czk'].astype(str).str.replace(' CZK', '', regex=False).str.replace(' ', '', regex=False)
    df['price_czk'] = pd.to_numeric(df['price_czk'], errors='coerce')
    
    # 6. Convert 'Balení míčků' column to numerical values
    print("Converting 'Balení míčků' to numerical values...")
    def extract_ball_count(text):
        if pd.isna(text) or text == 'nan':
            return np.nan
        text = str(text)
        # Extract numbers from strings like "dóza po 4 ks", "36 ks", etc.
        numbers = re.findall(r'\d+', text)
        if numbers:
            return int(numbers[0])
        return np.nan
    
    df['Balení míčků'] = df['Balení míčků'].apply(extract_ball_count)
    
    # 7. Create unit_price_czk column
    print("Creating unit_price_czk column...")
    df['unit_price_czk'] = df['price_czk'] / df['Balení míčků']
    
    # 8. Create age_min and age_max columns from 'Doporučený věk'
    print("Processing age information...")
    def extract_age_range(age_text):
        if pd.isna(age_text) or age_text == 'nan':
            return np.nan, np.nan
        age_text = str(age_text)
        # Extract age ranges like "5-8 let", "8-9 let"
        age_match = re.findall(r'(\d+)-(\d+)', age_text)
        if age_match:
            min_age, max_age = age_match[0]
            return int(min_age), int(max_age)
        # Extract single ages like "8 let"
        single_age = re.findall(r'(\d+)', age_text)
        if single_age:
            age = int(single_age[0])
            return age, age
        return np.nan, np.nan
    
    age_ranges = df['Doporučený věk'].apply(extract_age_range)
    df['age_min'] = [x[0] for x in age_ranges]
    df['age_max'] = [x[1] for x in age_ranges]
    
    # Drop the original age column
    df = df.drop('Doporučený věk', axis=1)
    
    # 9. Fill NaN values in 'Doporučený povrch' with 'všechny povrchy'
    print("Filling missing surface recommendations...")
    df['Doporučený povrch'] = df['Doporučený povrch'].fillna('všechny povrchy')
    
    # 10. Remove columns with redundant information
    print("Removing redundant columns...")
    # These columns appear to be duplicates or not needed for analysis
    redundant_columns = [
        'link_master',
        'image_link_master',
        'item_group_id'  # Same as id column for individual products
    ]
    
    existing_redundant = [col for col in redundant_columns if col in df.columns]
    if existing_redundant:
        df = df.drop(existing_redundant, axis=1)
        print(f"Removed columns: {existing_redundant}")
    
    # 11. Final cleanup - ensure no remaining double spaces
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].astype(str).str.replace(r'\s+', ' ', regex=True).str.strip()
            df[col] = df[col].replace('nan', np.nan)
    
    # 12. Save cleaned data
    print(f"Saving cleaned data to {output_path}...")
    df.to_csv(output_path, index=False)
    
    print(f"Data cleaning completed successfully!")
    print(f"Final dataset: {len(df)} rows, {len(df.columns)} columns")
    print(f"Cleaned data saved to: {output_path}")
    
    # Print summary statistics
    print("\n=== SUMMARY STATISTICS ===")
    print(f"Total tennis ball products: {len(df)}")
    print(f"Price range: {df['price_czk'].min():.0f} - {df['price_czk'].max():.0f} CZK")
    if not df['unit_price_czk'].isna().all():
        print(f"Unit price range: {df['unit_price_czk'].min():.2f} - {df['unit_price_czk'].max():.2f} CZK per ball")
    if not df['Balení míčků'].isna().all():
        print(f"Package sizes: {sorted(df['Balení míčků'].dropna().unique())}")
    if not (df['age_min'].isna().all() or df['age_max'].isna().all()):
        print(f"Age ranges: {df['age_min'].min():.0f}-{df['age_max'].max():.0f} years")
    print(f"Brands: {df['brand'].value_counts().to_dict()}")
    
    return df


if __name__ == "__main__":
    clean_tennis_balls_data()