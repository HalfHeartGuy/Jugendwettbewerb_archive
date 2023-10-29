def read_file_to_matrix(file_path):
    # Initialize an empty list to store the matrix
    matrix = []

    # Open the file and read its lines
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into elements and convert them to integers
            row = list(map(int, line.strip().split()))
            # Append the row to the matrix
            matrix.append(row)


    return matrix


# Example usage
file_path = 'Aufgabe1.txt'  # Replace this with the actual file path
result_matrix = read_file_to_matrix(file_path)
print(result_matrix)
