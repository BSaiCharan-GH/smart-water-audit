import pandas as pd

def convert_dates(df):
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def add_total_usage(df):
    df['Total_Usage'] = df.groupby('Date')['Water_Usage_Liters'].transform('sum')
    return df
