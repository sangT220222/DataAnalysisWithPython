import numpy as np

def calculate(list):
    try:
        matrix = np.array(list).reshape(3,3)
        mean = [np.mean(matrix,axis=0), np.mean(matrix,axis=1), np.mean(matrix)]
        variance = [np.var(matrix, axis = 0), np.var(matrix, axis = 1), np.var(matrix)]
        std = [np.std(matrix, axis = 0), np.std(matrix, axis = 1), np.std(matrix)]
        m_max = [np.max(matrix, axis = 0), np.max(matrix, axis = 1), np.max(matrix)]
        m_min = [np.min(matrix, axis = 0), np.min(matrix, axis = 1), np.min(matrix)]
        m_sum = [np.sum(matrix, axis = 0), np.sum(matrix, axis = 1), np.sum(matrix)]


        calculations = {
            'mean': [i.tolist() for i in mean],
            'variance' : [i.tolist() for i in variance],
            'standard deviation': [i.tolist() for i in std],
            'max': [i.tolist() for i in m_max],
            'min': [i.tolist() for i in m_min],
            'sum':[i.tolist() for i in m_sum]
        }

        return calculations
        
    except ValueError:
        print("List must contain nine numbers.")
   
