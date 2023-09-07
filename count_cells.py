import csv

def count_filled_cells(reader):
    filled_cells = 0

    for row in reader:
        for cell in row[2:]:
            if cell.strip(): filled_cells += 1

    return filled_cells


# Example usage
tsv_file_path = 'characters.tsv'

with open(tsv_file_path) as file:
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip the header row
    filled_cell_count = count_filled_cells(reader)
    print(f'Total filled cells: {filled_cell_count}')
