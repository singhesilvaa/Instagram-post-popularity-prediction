import pandas as pd

# Load the dataset from the CSV file with 'latin-1' encoding
df = pd.read_csv('F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/after_removing_postType_2n3.csv', encoding='latin-1')

# Select the 16th column
column_16 = df.iloc[:, 15]

# Calculate the z-scores for the selected column
z_scores = (column_16 - column_16.mean()) / column_16.std()

# Set a threshold for z-score (e.g., 3)
threshold = 3

# Identify outliers in the 16th column by comparing z-scores to the threshold
outliers = df[abs(z_scores) > threshold]

# Save the outliers to a new CSV file
outliers.to_csv('F:/Needed stuff/Computer Science/Research stuff/predict-viral-instagram-posts-advanced - editing/postIDs/outliers_followers.csv', index=False)

# Print a confirmation message
print("Outliers saved to 'outliers.csv'")
