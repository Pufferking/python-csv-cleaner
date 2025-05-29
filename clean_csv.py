import pandas as pd

def clean_csv(file_path, fill_value="-"):
    """
    Enhanced CSV Cleaner
    -------------------
    Loads a messy CSV file robustly, cleans and standardizes it.
    """

    try:
        df = pd.read_csv(file_path, encoding="utf-8", on_bad_lines="skip")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="latin1", on_bad_lines="skip")

    df = df.drop_duplicates()

    df.columns = [col.strip().replace(" ", "_") for col in df.columns]

    df.fillna(fill_value, inplace=True)

    string_cols = df.select_dtypes(include=["object"]).columns
    for col in string_cols:
        df[col] = df[col].str.strip()

    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.strftime("%Y-%m-%d")

    numeric_cols = df.select_dtypes(include=["object"]).columns
    for col in numeric_cols:
        coerced_col = pd.to_numeric(df[col].str.replace(",", ""), errors="coerce")
        if coerced_col.notna().sum() / len(df) > 0.5:
            df[col] = coerced_col.fillna(fill_value)

    return df

if __name__ == "__main__":
    cleaned_df = clean_csv("sample_input.csv")
    print(cleaned_df)
