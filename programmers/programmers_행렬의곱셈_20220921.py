import numpy as np

def solution(arr1, arr2):
    answer = [[]]
    # a1 = np.array(arr1)
    # a2 = np.array(arr2)
    answer = np.dot(arr1, arr2).tolist() # dot()은 numpy에서 행렬 곱을 해주는 것
					# tolist()를 사용하여 numpy.array()를 list로 변환 
    return answer
