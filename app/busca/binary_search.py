import app.utils.list as lst


def binary_search(vetor, elemento, inicio=0):
    meio = len(vetor) // 2
    if meio == 0:
        return None
    if vetor[meio] == elemento:
        return inicio + meio
    if vetor[meio] < elemento:
        return binary_search(vetor[meio + 1:], elemento, inicio + meio + 1)
    else:
        return binary_search(vetor[:meio], elemento, inicio)


# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1


if __name__ == '__main__':
    entrada = lst.generate_sorted_list(10)
    print(entrada)
    print("Posição: {}".format(binary_search(entrada, 5)))
    exit(0)
