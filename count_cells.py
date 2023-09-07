import csv

def prepare_reader():
    tsv_file_path = 'characters.tsv'
    file = open(tsv_file_path)
    reader = csv.reader(file, delimiter='\t')
    next(reader)  # Skip the header row
    return reader


def count_filled_cells(reader):
    filled_cells = 0

    for row in reader:
        for cell in row[2:]:
            if cell.strip(): filled_cells += 1

    return filled_cells


# Example usage
reader = prepare_reader()
filled_cell_count = count_filled_cells(reader)
print(f'Total filled cells: {filled_cell_count}')
