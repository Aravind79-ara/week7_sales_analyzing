from sales_analyzer.data_loading import Loading

def test_loader():
  df=Loading('data/sales_data.csv').load()
  assert not df.empty