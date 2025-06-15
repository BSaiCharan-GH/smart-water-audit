from src.dataloader import load_data
from src.preprocessing import add_total_usage, convert_dates
from src.analytics import get_zone_averages, detect_anomalies, weekly_trends
from src.utils import print_summary

# Load and preprocess
df = load_data("data/simulated_data.csv")
df = convert_dates(df)
df = add_total_usage(df)

# Print summary
print_summary(df)

# Analytics
print("Zone Averages:\n", get_zone_averages(df))
print("Weekly Trends:\n", weekly_trends(df))
print("Anomalies:\n", detect_anomalies(df))
