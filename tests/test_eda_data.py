import pytest # type: ignore
import pandas as pd # type: ignore
import tempfile
from scripts.eda_data import count_articles_per_publisher, analyze_publication_dates

@pytest.fixture
def load_data():
    # mock data for testing
    test_data = pd.DataFrame({
        'publisher': ['A', 'B', 'A', 'C', 'B'],
        'date': ['2023-08-01', '2023-08-02', '2023-08-03', '2023-08-01', '2023-08-02']
    })
  
    with tempfile.NamedTemporaryFile(suffix=".csv", mode='w+', delete=False) as tmp_file:
        test_data.to_csv(tmp_file.name, index=False)
        tmp_file.seek(0) 
        yield pd.read_csv(tmp_file.name)

def test_count_articles_per_publisher(load_data):
    result = count_articles_per_publisher(load_data)
    
    assert isinstance(result, pd.Series)
    assert not result.empty

def test_analyze_publication_dates(load_data):
    result = analyze_publication_dates(load_data)
    
    assert isinstance(result, pd.Series)
    assert not result.empty
