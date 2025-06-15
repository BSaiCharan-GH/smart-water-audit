import pandas as pd

def get_zone_averages(df):
    return df.groupby('Zone')['Water_Usage_Liters'].mean()

def weekly_trends(df):
    df['Week'] = df['Date'].dt.isocalendar().week
    return df.groupby('Week')['Water_Usage_Liters'].sum()

def detect_anomalies(df, threshold=850):
    return df[df['Water_Usage_Liters'] > threshold]
