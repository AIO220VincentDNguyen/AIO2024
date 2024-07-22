import numpy as np

# 1.a Lenght of a vector
def compute_vector_length(vector):
    sum_of_squares = np.sum(vector**2)
    len_of_vector = np.sqrt(sum_of_squares)
    return len_of_vector

# 1.b Dot product
def compute_dot_product(vector1, vector2):
    result = np.dot(vector1, vector2)
    return result

# 1.c Multiplying a vector by a matrix
def matrix_multi_vector(matrix, vector):
    result = np.dot(matrix,vector)
    return result

# 1.d Multiplying a matrix by a matrix
def matrix_multi_matrix(matrix1, matrix2):
    result = np.dot(matrix1, matrix2)
    return result

# 1e Matrix inverse
def inverse_matrix(matrix):
    try:
        result = np.linalg.inv(matrix)
    except np.linalg.LinAlgError:
        result = None
    return result

if __name__ == "__main__":
    # generate test case and use pre-defined function to check the result
    matrix = np.array([[1, 2], [3, 4]])
    vector = np.array([1, 2])
    print(compute_vector_length(vector))
    print(compute_dot_product(vector, vector))
    print(matrix_multi_vector(matrix, vector))
    print(matrix_multi_matrix(matrix, matrix))
    print(inverse_matrix(matrix))