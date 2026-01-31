from sales_analyzer.data_analyzing import SalesAnalyzer
import pandas as pd

def test_stats():
  df=pd.DataFrame({
    "total_amount":[100,200],
    "customer_id":["A","B"],
    "order_date":["2024-01-01","2024-01-02"]
    })
  stats=SalesAnalyzer(df).basic_stats()
  assert stats["total_sales"]==300
  