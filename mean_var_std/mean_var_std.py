import numpy as np

def calculate(list):
    try:
        matrix = np.array(list).reshape(3,3)
    except ValueError:
        print("List must contain nine numbers.")




    return calculations