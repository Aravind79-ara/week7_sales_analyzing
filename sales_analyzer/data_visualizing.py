import matplotlib.pyplot as plt
import os

class Visualizer:
  def __init__(self,output="data/report_data"):
     self.output=output
     os.makedirs(output,exist_ok=True)
     
  def sales_trend(self,monthly_sales):
    plt.figure()
    monthly_sales.plot(kind="line",marker="o")
    plt.title("Monthly Sales Trend")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.savefig(f"{self.output}/monthly_trend.png")
    plt.close()
  def category_chart(self, data):
        plt.figure()
        data.plot(kind="pie", autopct="%1.1f%%")
        plt.ylabel("")
        plt.title("Sales by Category")
        plt.savefig(f"{self.output}/category_sales.png")
        plt.close()
    
  def top_products(self,products):
    plt.figure()
    products.plot(kind="bar")
    plt.title("Top Products")
    plt.tight_layout()
    plt.savefig(f"{self.output}/top_products.png")
    plt.close()