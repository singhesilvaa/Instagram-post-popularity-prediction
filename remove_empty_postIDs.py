import csv

def filter_csv(input_file, output_file, encoding='utf-8'):
    # Open the input CSV file
    with open(input_file, 'r', encoding=encoding, errors='replace') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Create a list to store the filtered rows
        filtered_rows = []

        # Process each row in the input file
        for row in csv_reader:
            # Check if the row has at least 7 elements
            if len(row) >= 7 and row[6].strip():  # Assuming the 7th column is at index 6 (0-based indexing)
                filtered_rows.append(row)

    # Write the filtered rows to the output CSV file
    with open(output_file, 'w', newline='', encoding=encoding) as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(filtered_rows)

# Specify the input and output file paths
input_file = 'F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/train_advance_input.csv'
output_file = 'F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/train_advance_output.csv'

# Call the filter_csv function with the file paths
filter_csv(input_file, output_file, encoding='latin-1')
