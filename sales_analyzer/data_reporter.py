import pandas as pd

class Reporter:
    def __init__(self, df):
        self.df = df

    def export_excel(self, path):
        self.df.to_excel(path, index=False)
