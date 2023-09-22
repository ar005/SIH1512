import random
import csv

# Function to generate a random walk with a maximum step size
def random_walk_with_max_step(initial_value, num_points, max_step):
    data = [initial_value]
    for _ in range(num_points - 1):
        step = random.randint(-max_step, max_step)
        new_value = data[-1] + step
        # Ensure the new value stays within the specified range [0, 1023]
        new_value = max(0, min(1023, new_value))
        data.append(new_value)
    return data

# Specify the number of data points and the maximum step size
num_points = 10000
max_step = 10

# Generate the random dataset
random_data = random_walk_with_max_step(512, num_points, max_step)

# Specify the output file name
output_file = 'random_dataset.csv'

# Write the random dataset to a CSV file
with open(output_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['Data Point'])
    for data_point in random_data:
        csv_writer.writerow([data_point])

print(f'Random dataset saved to {output_file}')
