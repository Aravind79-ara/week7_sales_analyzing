class SalesAnalyzer:
    def __init__(self, df):
        self.df = df

    def basic_stats(self):
        return {
            "total_sales": self.df["total_amount"].sum(),
            "avg_order": self.df["total_amount"].mean(),
            "orders": len(self.df),
            "customers": self.df["customer_id"].nunique()
        }
    def top_categories(self):
        return (
            self.df.groupby("category")["total_amount"]
            .sum()
            .sort_values(ascending=False)
        )

    def top_products(self, n=5):
        return (
            self.df.groupby("product_name")["total_amount"]
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def monthly_sales(self):
        self.df["month"] = self.df["order_date"].dt.to_period("M")
        return self.df.groupby("month")["total_amount"].sum()
