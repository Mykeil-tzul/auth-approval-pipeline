import pandas as pd

# Load CSV
df = pd.read_csv('data/daily_transactions.csv')

# Preview top rows
print("Sample Data:")
print(df.head())

# Show basic info
print("\nSchema Info:")
print(df.info())


# Convert timestamp to date
df['transaction_date'] = pd.to_datetime(df['timestamp']).dt.date

# Clean status column to upper case (if needed)
df['status'] = df['status'].str.upper()

# Calculate daily metrics
daily_summary = df.groupby('transaction_date').agg(
    total_transactions=('transaction_id', 'count'),
    approved_transactions=('status', lambda x: (x == 'APPROVED').sum()),
    declined_transactions=('status', lambda x: (x == 'DECLINED').sum())
).reset_index()

# Calculate approval rate
daily_summary['approval_rate_pct'] = round(
    daily_summary['approved_transactions'] / daily_summary['total_transactions'] * 100, 2
)

# Show result
print("\nDaily Approval Rate Summary:")
print(daily_summary)

# Save summary to CSV for dashboard
daily_summary.to_csv('data/daily_approval_summary.csv', index=False)

print("\n✅ Daily summary saved to data/daily_approval_summary.csv")
