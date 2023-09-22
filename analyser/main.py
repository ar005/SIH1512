import csv

 
X_range = range(1, 3)  #network name
Y_range = range(1, 4)  #node name

# files reads 
def read_last_n_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return lines[-n:]

# Initialize flags for network and node status
# network_down = False
# node_down = False

network_status = []
node_status = []


# allvalues of x and y
for X in X_range:
    # network status
    network_X_status = []
    #network_X_down = True
    
    for Y in Y_range:
        # check all csv`s
        csv_filename = f"data_{X}_{Y}.csv"

        try:
            # data reads
            last_line = read_last_n_lines(csv_filename, 1)[0]
            _, data1, data2 = last_line.strip().split(',')

            
            data1 = int(data1)
            data2 = int(data2)

            # # node check
            # if data1 < 980 and data2 < (980 - data1):
            #     node_down = True
            #     print(f"node_{X}_{Y} is down")
            
            # # network check
            # if data1 >= 980 or data2 >= (980 - data1):
            #     network_X_down = False
            
            # Check individual condition
            if data1 < 980 and data2 < (980 - data1):
                node_X_Y_status = 0
                network_X_status.append(0)
            else:
                node_X_Y_status = 1
                network_X_status.append(1)
            
            node_status.append(f"node_X{X}_Y{Y}={node_X_Y_status}")

        except FileNotFoundError:
            print(f"File '{csv_filename}' not found.")
            
    if all(network_X_status):
        network_status.append(1)
    else:
        network_status.append(0)
with open("network_status.csv", "w", newline="") as network_csv_file:
    network_csv_writer = csv.writer(network_csv_file)
    network_csv_writer.writerow(network_status)

# Write node status to the node CSV file
with open("node_status.csv", "w", newline="") as node_csv_file:
    node_csv_writer = csv.writer(node_csv_file)
    node_csv_writer.writerow(node_status)





#     # network status 
#     if network_X_down:
#         print(f"Network {X} is down")

# # Print a general message if no network or node is down
# if not node_down:
#     print("All nodes are operational")
# if not network_down:
#     print("All networks are operational")

