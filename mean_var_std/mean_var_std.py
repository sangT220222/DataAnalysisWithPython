import numpy as np

def calculate(list):
    try:
        matrix = np.array(list).reshape(3,3)
    except ValueError:
        print("List must contain nine numbers.")
    #print(matrix)

    mean = [np.mean(matrix,axis=0), np.mean(matrix,axis=1), np.mean(matrix)]

    calculations = {
        'mean': [i.tolist() for i in mean]
    }

    print(calculations)

    return calculations
