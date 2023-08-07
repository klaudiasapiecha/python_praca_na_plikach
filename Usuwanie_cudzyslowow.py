import os

def remove_double_quotes_from_files(directory):
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            content_without_quotes = content.replace('"', '')

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content_without_quotes)

if __name__ == "__main__":
    directory_to_scan = "C:\\Users\\KlaudiaSapiecha\\Desktop\\ODS_TER_PROD\\TABLES\\"

    remove_double_quotes_from_files(directory_to_scan)
