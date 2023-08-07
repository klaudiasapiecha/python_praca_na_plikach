import os
import re

def extract_grants_to_files(input_file):
    with open(input_file, "r") as f:
        grants_content = f.read()

    grant_statements = re.findall(r"GRANT.*?TO\s+([\w_]+);", grants_content, re.IGNORECASE | re.DOTALL)

    grants_dict = {}
    for statement in grant_statements:
        # Przechwytujemy całą linię uprawnienia
        grant_statement = f"  {statement};"
        grants_dict.setdefault("GRANT", []).append(grant_statement)

    if not os.path.exists("tescik"):
        os.mkdir("tescik")

    for obj_name, grants in grants_dict.items():
        output_file_path = os.path.join("tescik", f"{obj_name}.sql")
        with open(output_file_path, "w") as output_file:
            output_file.write("\n".join(grants))

if __name__ == "__main__":
    input_file = "C:\\Users\\KlaudiaSapiecha\\Desktop\\granty_obiekty_ter.txt"
    extract_grants_to_files(input_file)
