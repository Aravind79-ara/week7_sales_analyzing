from .data_loading import Loading
from .data_cleaning import Datacleaning
from .data_analyzing import SalesAnalyzer
from .data_visualizing import Visualizer
from .data_reporter import Reporter

def main():
  loader=Loading("data/raw/sales_data.csv")
  df=loader.load()
  
  cleaner=Datacleaning(df)
  df=cleaner.clean()
  
  analyzer=SalesAnalyzer(df)
  vis=Visualizer()
  
  stats = analyzer.basic_stats()
  categories = analyzer.top_categories()
  monthly=analyzer.monthly_sales()
  top=analyzer.top_products()
  
  vis.sales_trend(monthly)
  vis.top_products(top)
  vis.category_chart(categories)
  
  print("\n📊 SALES DATA ANALYSIS REPORT")
  print("=" * 35)

  print("\n📅 Analysis Period: Jan 2024 - Dec 2024")

  print("\n📈 BASIC STATISTICS:")
  print(f"- Total Sales: ${stats['total_sales']:,.0f}")
  print(f"- Average Order Value: ${stats['avg_order']:,.2f}")
  print(f"- Total Customers: {stats['customers']}")

  print("\n🏆 TOP PRODUCT CATEGORIES:")
  for i, (cat, val) in enumerate(categories.head(5).items(), 1):
        print(f"{i}. {cat}: ${val:,.0f}")

  print("\n📈 MONTHLY SALES TREND:")
  for m, v in monthly.items():
        print(f"- {m}: ${v:,.0f}")

  print("\n📦 TOP 5 PRODUCTS:")
  for i, (p, v) in enumerate(top.items(), 1):
        print(f"{i}. {p}: ${v:,.0f}")

  print("\n✅ Charts saved in /output folder")
  
  
if __name__=="__main__":
  main()