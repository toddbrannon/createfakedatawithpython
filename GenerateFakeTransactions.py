# Import libraries, classes, and modules
import random
from datetime import datetime, timedelta
import csv
import pandas as pd
from google.colab import files

# Define the products
products = {
    "TruProducer Bootcamp": 597,
    "Getting Your Music Heard in 2023": 9,
    "TruDrums vol. 1": 29,
    "TruSynths vol. 1": 29,
    "TruGuitarLoops vol. 1": 29
}

# Define the pipelines (traffic sources)
pipelines = ["Organic Site Traffic",
             "Affiliates", "Facebook Ads", "YouTube Ads"]

# Define the date range
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 3, 31)

# Generate the transactions
transactions = []

for date in range((end_date - start_date).days + 1):
    current_date = start_date + timedelta(days=date)
    for _ in range(random.randint(1, 10)):  # Generate multiple transactions per day
        product = random.choice(list(products.keys()))
        pipeline = random.choice(pipelines)
        price = products[product]
        customer_id = random.randint(1001, 1400)
        transactions.append([current_date.strftime(
            "%Y-%m-%d"), product, pipeline, price, customer_id])

# Create a dataframe from the transactions list
df = pd.DataFrame(transactions, columns=[
                  "Date", "Product", "Pipeline", "Total Gross Sales", "Customer ID"])

# Print the dataframe
print(df)

# Save the dataframe as a CSV file
df.to_csv('transactions.csv', index=False)

# Download the CSV file to your local directory
files.download('transactions.csv')
