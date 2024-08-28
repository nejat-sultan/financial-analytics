import pytest # type: ignore
import pandas as pd # type: ignore
from scripts.eda_data import count_articles_per_publisher, analyze_publication_dates

@pytest.fixture
def load_data():
    return pd.read_csv('tests/data/test_data.csv')

def test_count_articles_per_publisher(load_data):
    result = count_articles_per_publisher(load_data)
    
    assert isinstance(result, pd.Series)
    assert not result.empty

def test_analyze_publication_dates(load_data):
    result = analyze_publication_dates(load_data)
    
    assert isinstance(result, pd.Series)
    assert not result.empty