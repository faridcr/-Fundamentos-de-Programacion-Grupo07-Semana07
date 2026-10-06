
notas=[85, 42 , 93 , 67 , 28 , 75]

# def bubblr_sort(notas):
#     n=len(notas)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if notas[j]>notas[j+1]:
#                 notas[j],notas[j+1]=notas[j+1], notas[j]
 
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
    
def promedio(notas):
    
    total=sum(notas)/len(notas) 
    return total   
    
                
def  minima(notas):
    return min(notas)

def maximo(notas):
    return max(notas)              
                
                
                
# bubblr_sort(notas)
selection_sort(notas)
print(notas)
print(promedio(notas))
print(min(notas))
print(max(notas))