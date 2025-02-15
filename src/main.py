from utils.auth_utils import authenticator
from utils.driver_utils import driver_init
from src.autenticate import login
from src.extract_info import extract_table_data
from src.navigator import navigate_to_tests
from src.frontend.app import show_dashboard
import pandas as pd
import os

data_file = "data/test_results.csv"

csv_path = 'data/test_results.csv'

# Check if the CSV file already exists
if os.path.exists(csv_path):
    print("⚡ Loading data from the existing CSV.")
    # If the CSV file exists, load the data directly
    df = pd.read_csv(csv_path)
    show_dashboard(df)
else:

    user_email, user_password = authenticator()

    driver = driver_init()

    # Call the login function with the credentials
    if user_email and user_password:
        login(driver, user_email, user_password)
    else:
        print("❌ Credentials not found in environment variables.")

    navigate_to_tests(driver=driver)

    data_file = "data/test_results.csv"

    if not os.path.exists(data_file):
        df = extract_table_data(driver)
    else:
        df = pd.read_csv(data_file)
        
    show_dashboard(df)

