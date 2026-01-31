import numpy as np

class Datacleaning:
  def __init__(self,df):
    self.df=df
    
  def clean(self):
    self.df=self.df.drop_duplicates()
    for col in self.df.select_dtypes(include=np.number):
        self.df[col].fillna(self.df[col].median(),inplace=True)
        
    for col in self.df.select_dtypes(include="object"):
      self.df[col].fillna(self.df[col].mode()[0],inplace=True)
      
    return self.df
    