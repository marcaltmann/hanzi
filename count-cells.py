import csv

def count_filled_cells(tsv_file):
    filled_cells = 0

    with open(tsv_file, 'r') as file:
        reader = csv.reader(file, delimiter='\t')
        next(reader)  # Skip the header row

        for row in reader:
            for cell in row[2:]:
                if cell.strip():  # Check if cell is not empty
                    filled_cells += 1

    return filled_cells

# Example usage
tsv_file_path = 'characters.tsv'
filled_cell_count = count_filled_cells(tsv_file_path)
print(f'Total filled cells: {filled_cell_count}')
