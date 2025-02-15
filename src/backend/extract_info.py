from selenium.webdriver.common.by import By
import pandas as pd
from utils.csv_convert import convert_to_csv

def extract_table_data(driver):
    # Find the table by ID
    table = driver.find_element(By.ID, 'tbl_idx_tst')
    
    # Find all rows in the table (excluding the header)
    rows = table.find_elements(By.TAG_NAME, 'tr')[1:]  # Ignore the first header row
    
    data = []
    
    for row in rows:
        # Extract the cells from the row
        cols = row.find_elements(By.TAG_NAME, 'td')
        if len(cols) > 0:  # If the row has cells
            test_id = cols[0].find_element(By.TAG_NAME, 'a').get_attribute('class')
            fallos = cols[2].text
            realizado = cols[3].text
            ultimo = cols[4].text

            # Create a dictionary with the row data
            if realizado:
                row_data = {
                    'test': test_id,
                    'fallos': fallos,
                    'realizado': realizado,
                    'ultimo': ultimo,
                }
                data.append(row_data)

    df = pd.DataFrame(data)
    df['ultimo_datetime'] = pd.to_datetime(df['ultimo'], dayfirst=True)  # Convertir a datetime
    df = df.sort_values(by='ultimo_datetime')
    print(df.to_string())
    convert_to_csv(df, 'data/test_results.csv')

    driver.quit()
    return df