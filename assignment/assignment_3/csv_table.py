import csv

def display_csv_table(filename):
    """
    Reads a CSV file and displays its contents in a neatly formatted table.
    Each column is aligned based on the widest entry in that column.
    If the file is empty or not found, an appropriate message is displayed.
    """
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            if not rows:
                print("The file is empty.")
                return
            # Calculate column widths
            col_widths = [max(len(str(item)) for item in col) for col in zip(*rows)]
            # Print each row with proper spacing
            for i, row in enumerate(rows):
                print(" | ".join(str(item).ljust(col_widths[idx]) for idx, item in enumerate(row)))
                # Print a separator after the header
                if i == 0:
                    print("-+-".join('-' * w for w in col_widths))
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

# Display the table from 'table.csv'
display_csv_table('table.csv')