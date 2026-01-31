from sales_analyzer.data_cleaning import Datacleaning
import pandas as pd

def test_clean():
    df = pd.DataFrame({"a":[1,None,1]})
    clean = Datacleaning(df).clean()
    assert clean.isnull().sum().sum() == 0
