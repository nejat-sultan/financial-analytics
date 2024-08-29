import pandas as pd # type: ignore

def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

def count_articles_per_publisher(df: pd.DataFrame) -> pd.Series:
    return df['publisher'].value_counts()

def analyze_publication_dates(df: pd.DataFrame) -> pd.Series:
    df['date'] = pd.to_datetime(df['date']) 
    return df['date'].dt.date.value_counts() 
