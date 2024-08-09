import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Function to get account balance and switch off date from the website
def get_amount_due_date(number):
    url = f'https://www.dishtv.in/pages/Instant-Recharge-Payment.aspx?txtMobile={number}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Send GET request
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the account balance
        account_balance = soup.find('ul', id='userulli').find('span').text.strip()

        # Extract the switch off date
        switch_off_date = soup.find('ul', id='userulli').find_all('span')[1].text.strip()

        print(f'Switch Off Date: {switch_off_date}')
        print(f'Account Balance: {account_balance}')
        
        return account_balance, switch_off_date
    else:
        return None, None

# Read Excel file
current_dir = os.path.dirname(__file__)  # Directory where the script is located
relative_path = os.path.join(current_dir, 'DISHSAMPLEDATA.xlsx')
df = pd.read_excel(relative_path)
print(df)

# Create a list to store the results
results = []

# Iterate through the numbers
for number in df['RMN']:
    amount, due_date = get_amount_due_date(number)
    results.append({'Number': number, 'Amount': amount, 'Due Date': due_date})

# Create a DataFrame with the results
results_df = pd.DataFrame(results)

# Save the results to a new Excel file
results_df.to_excel('results.xlsx', index=False)
