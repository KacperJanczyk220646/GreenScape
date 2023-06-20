import pandas as pd

file_path = 'EDA/Simona/scripts/Preprocessed_Dataset.csv'
df = pd.read_csv(file_path, index_col=0)

def read_file_from_relative_path(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content.index
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None
    except IOError:
        print(f"Error reading file '{file_path}'.")
        return None


file_content = read_file_from_relative_path(file_path)
if file_content:
    df_read = pd.read_csv(file_path, index_col=0)
    print('Sucessfully read the .csv!')


def group_months(df):
    df_groupby_months = df.groupby(by=['months'])['green_score',
                                                  'livability_score_x', 'TotalHouses', 'Population', 'income', 'Registered nuisance (number)'].mean()

    return df_groupby_months


def preprocess(df):
    df['Year'] = df['Year'].astype(str)
    df['date'] = pd.to_datetime(df['date'])
    df['months'] = df['date'].dt.month_name(locale='English')
    df = df.sort_values(by='date', ascending=True)
    df = df.groupby(by=['date', 'Year', 'months',
                    'Neighborhood', 'regions']).mean()
    df.reset_index(inplace=True)
    return df

def check_preprocessing(df):
    if type(df['Year']) == object:
        print('correct dtype')
    if type(df['date']) == datetime32:
