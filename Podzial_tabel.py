import os
import re

source_file = "C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_T\\Tables_ODS_TER.sql"
output_directory = "C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_T"

def extract_create_table_code(source_file, output_directory):
    with open(source_file, 'r') as source:
        source_code = source.read()

    create_table_blocks = re.findall(r'CREATE TABLE (\w+)\s*\((.*?)\);', source_code, re.DOTALL | re.IGNORECASE)

    for table_name, table_code in create_table_blocks:
        # Preserve the original formatting
        original_formatting = re.search(r'CREATE TABLE ' + table_name + r'\s*\(\n(.*?)\);', source_code, re.DOTALL | re.IGNORECASE).group(1)
        formatted_code = f'CREATE TABLE {table_name} \n(\n  {original_formatting.strip()}\n);'

        table_file_name = os.path.join(output_directory, f'{table_name}.sql')
        with open(table_file_name, 'w') as table_file:
            table_file.write(formatted_code)

        print(f"Utworzono plik '{table_file_name}' z kodem tabeli '{table_name}'.")

if __name__ == "__main__":
    extract_create_table_code(source_file, output_directory)
