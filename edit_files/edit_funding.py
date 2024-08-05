
def remove_quotations(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        funding_file = file.read()

        # remove all quotation marks
        funding_file = funding_file.replace(' "', '').replace('"', '')

        # write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(funding_file)
