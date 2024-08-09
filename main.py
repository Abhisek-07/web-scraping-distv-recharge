import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

# Function to get account balance and switch off date from the website
def get_amount_due_date(number):
    url = 'https://www.dishtv.in/pages/Instant-Recharge-Payment.aspx'

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '.ASPXANONYMOUS=tMWsVJsS2wEkAAAAMDJmZjliZDMtYTc5MC00MmFlLWFjZWYtZDJkYjQ3ZjgwZjA5uhlQ5Lb1D4jBWJcpas9xQ1TTsv0pw1mw5AWEsNJ3YJ81; ASP.NET_SessionId=qkxyrzojovlxdphapghmxgsb; _gcl_au=1.1.134726671.1721633630; TriedTohack=True; _fbp=fb.1.1721633642335.18020831134870583; WZRK_G=491c210057c5441c83bd353ff2e23825; ApplicationGatewayAffinityCORS=0d641b264d12af4d709f7e74c52fa9e4; ApplicationGatewayAffinity=0d641b264d12af4d709f7e74c52fa9e4; __AntiXsrfToken=811ab28e19964c67b3fc8e22b027e1ff; __tr_jr=W3sidXRtcyI6Im9yZ2FuaWMiLCJ0cyI6IjIwMjQtMDgtMDlUMDY6NDI6MzIuNTYyWiIsImVuYyI6InllcyJ9XQ==; __tr_luptv=1723185752563; _gid=GA1.2.857866745.1723185753; _gat=1; _clck=kanfnb%7C2%7Cfo6%7C0%7C1664; _ga_MRPGQ7PG2N=GS1.1.1723185753.1.0.1723185753.0.0.0; _ga=GA1.2.1642748990.1721633652; _uetsid=95db4240561a11efb8a6e1067b58849b; _uetvid=ca2074a047fc11efa89f7f1195b896c3; WZRK_S_848-8Z5-786Z=%7B%22p%22%3A2%2C%22s%22%3A1723185753%2C%22t%22%3A1723185765%7D; _clsk=oerfyh%7C1723185766456%7C1%7C1%7Cq.clarity.ms%2Fcollect; _ga_RF2E19HSKJ=GS1.1.1723185752.3.1.1723185805.7.0.0',
        'Origin': 'https://www.dishtv.in',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
        'X-MicrosoftAjax': 'Delta=true',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = {
    'objScriptManager': 'UPInstantRecharge|btnInstantRechageSubmit',
    '__EVENTTARGET': 'btnInstantRechageSubmit',
    '__EVENTARGUMENT': '',
    '__LASTFOCUS': '',
    'hidoutstanding': '',
    'txtminiumrechargeamount': '10',
    'txtuseremail': '',
    'txtmob': '',
    'hdcontent': '',
    'txtseoammount': '',
    'txtseoorderid': '',
    'hidissmartstick': 'false',
    'hidisalexakit': 'false',
    'hidsettopbox': 'false',
    'hdIsUserValidate': 'false',
    'hidstep1': '',
    'hidstep2': '',
    'hidstep3': '',
    'hidthreezeroone': '',
    'hdfsdsofy': '',
    'hdfsdsofyflag': '0',
    'hidUserLogin': 'No',
    'hidmonthlyrechargeamout': '0',
    'HidRechargeOfferMonth': '0',
    'HidRechargeOfferid': '',
    'HidRechargeAmount': '0',
    'hidIsPayTerm': '0',
    'hidIsOfferSelected': '0',
    'hidzoneID': '0',
    'hidvalueforsearch': '0',
    'hidofferid': '0',
    'hidIsHybrid': '0',
    'hidHybridAmt': '0',
    'hdnfinalprice': '0',
    'hidtotalvasprice': '0',
    'hidIds': '',
    'HidWhatsappconset': '0',
    'hidUserEnteredAmount': '0',
    'hidvas': '',
    'hidvassession': '',
    'hidpaysession': '',
    'hidamsession': '',
    'hidpaymodesession': '',
    'hidminrechargeamont': '',
    'hidstatusid': '',
    'hidstatusname': '',
    'hidrmn': '',
    'hidIsEligiblePrimeSubs': '',
    'hidDonationAmount': '0',
    'hidcashfree': 'true',
    'hidpayu': 'true',
    'hidpaytm': 'true',
    'hidisqrcodeenabled': 'true',
    'hidselectedpaymentoption': 'JusPay',
    'hidcardbin': '',
    'hidvvc': '',
    'txtMobile': {number},  # Update this with the actual mobile number
    'txtAmount': '',
    'txtCardHolderName': '',
    'txtCardNumber': '',
    'txtValidThruMonth': '0',
    'txtValidThruYear': '0',
    'txtValidThru': '',
    'txtCVV': '',
    'txtCardNickName': '',
    'savecarddetails': 'on',
    'upiTextId': '',
    'searchchannelslist': '',
    '__ASYNCPOST': 'true',
}

    response = requests.post(url, headers=headers, data=data)

    # print(response.text)
    # url = f'https://www.dishtv.in/pages/Instant-Recharge-Payment.aspx'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    #     'Content-Type': 'application/x-www-form-urlencoded'
    # }

    # # Send GET request
    # response = requests.post(url, data={"txtMobile": {number}.__str__}, headers=headers)
    
    if response.status_code == 200:
        # print(response.text)  # Print the raw HTML to inspect it
        soup = BeautifulSoup(response.content, 'html.parser')

        # Try to find the expected elements
        account_balance_element = soup.find('ul', id='userulli').find('span')
        switch_off_date_element = soup.find('ul', id='userulli').find_all('span')[1] if account_balance_element else None

        if account_balance_element and switch_off_date_element:
            account_balance = account_balance_element.text.strip()
            switch_off_date = switch_off_date_element.text.strip()
            print(f'Phone Number: {number}')
            print(f'Switch Off Date: {switch_off_date}')
            print(f'Account Balance: {account_balance}')
            return account_balance, switch_off_date
        else:
            print("Could not find the account balance or switch off date.")
            return None, None
    else:
        print(f"Failed to retrieve data for number {number}")
        return None, None


# amount, due_date = get_amount_due_date(9701041690)
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
