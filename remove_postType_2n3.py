import csv

def filter_csv(input_file, output_file, encoding='utf-8'):
    # Open the input CSV file
    with open(input_file, 'r', encoding=encoding, errors='replace') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Create a list to store the filtered rows
        filtered_rows = []

        # Process each row in the input file
        for row in csv_reader:
            # Check if the row has at least 9 elements and the 9th column is not '2' or '3'
            if len(row) >= 9 and row[8] not in ['2', '3']:  # Assuming the 9th column is at index 8 (0-based indexing)
                filtered_rows.append(row)

    # Write the filtered rows to the output CSV file
    with open(output_file, 'w', newline='', encoding=encoding) as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(filtered_rows)

# Specify the input and output file paths
input_file = 'F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/after_removing_NULL_postIDS.csv'
output_file = 'F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/after_removing_postType_2n3.csv'

# Call the filter_csv function with the file paths
filter_csv(input_file, output_file)
