import pandas as pd

class Loading:
  def __init__(self,path):
     self.path=path
     
  def load(self):
    try: 
      df=pd.read_csv(self.path)
      if "order_date" in df.columns:
        df["order_date"]=pd.to_datetime(df["order_date"])
      return df
    
    except Exception as e:
      raise RuntimeError(f"Error to load data:{e}")