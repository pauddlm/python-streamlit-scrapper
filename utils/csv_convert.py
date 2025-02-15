import os

def convert_to_csv(df, data_path):

    if not os.path.exists('data'):
        os.makedirs('data')  

    if not os.path.exists(data_path):
        df.to_csv(data_path, index=False)
        print(f"✔️ Datos guardados en {data_path}")