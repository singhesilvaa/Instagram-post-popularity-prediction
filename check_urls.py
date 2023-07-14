import csv

def get_instagram_post_url(post_id):
    base_url = "https://www.instagram.com/p/"
    post_url = base_url + post_id
    return post_url

# Open the input CSV file
with open('F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/input_file.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # Open the output CSV file
    with open('F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/output_file.csv', 'w', newline='') as output_file:
        csv_writer = csv.writer(output_file)

        # Process each row in the input file
        for row in csv_reader:
            if len(row) >= 1:  # Check if the row has at least one element
                post_id = row[0]  # Assuming the post IDs are in the first column
                url = get_instagram_post_url(post_id)
                csv_writer.writerow([url])
            else:
                print("Invalid row encountered:", row)
