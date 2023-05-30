import csv
from sqlalchemy import create_engine
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
import os
import pandas as pd
from deep_translator import GoogleTranslator
import numpy as np
from tqdm import tqdm
from num2words import num2words
batch = False


user = "user1"
password = "1234"
host = "145.101.164.141"
port = "5432"
database = "adsai_1d"

connection_string = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)
metadata = MetaData()
metadata.reflect(bind=engine)


def create_CSV_dir():
    path = './csv_files'
    if not os.path.exists(path):
        os.mkdir(path)
        print("Folder %s created!" % path)
    else:
        print("Folder %s already exists" % path)
    return path


print(create_CSV_dir())

for table_name, table_object in metadata.tables.items():
    print(table_name)
    table = Table(table_name, metadata, autoload=True, autoload_with=engine)
    with engine.connect() as connection:
        result = connection.execute(table.select())
        data = result.fetchall()

    csv_file_directory = create_CSV_dir()
    csv_file_path = csv_file_directory + '/' + table_name + '.csv'
    print(csv_file_path)

    # Write data to the CSV file
    with open(csv_file_path, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([column.name for column in table.columns])
        for row in data:
            writer.writerow(row)

    print(f"CSV file created for table '{table_name}' successfully.")

print("All tables converted to CSV format.")
