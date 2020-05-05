
# Python program for implementation of MergeSort 
def mergeSort(arr):
	if len(arr) >1: 
		mid = len(arr)//2 #Finding the mid of the array 
		L = arr[:mid] # Dividing the array elements  
		R = arr[mid:] # into 2 halves 

		mergeSort(L) # Sorting the first half 
		mergeSort(R) # Sorting the second half 

		i = j = k = 0
		
		# Copy data to temp arrays L[] and R[] 
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+=1
			else: 
				arr[k] = R[j] 
				j+=1
			k+=1
		
		# Checking if any element was left 
		while i < len(L): 
			arr[k] = L[i] 
			i+=1
			k+=1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+=1
			k+=1
# Code to print the list 
def printList(arr): 
	for i in range(len(arr)):         
		print(arr[i],end=" ") 
	print() 


def Change(parts):
	
	DiccionarioPartes = [[(Zoo.get(p),p)  for p in parts[q]] for q in range(len(parts))]

	TamañosEscenas = [[ p[0]  for p in DiccionarioPartes[q]]for q in range(len(DiccionarioPartes))]
	
	TotaltamañodePartes= [ sum(p) for p in TamañosEscenas]

	diccionario = (dict(zip(TotaltamañodePartes, DiccionarioPartes)))
	
	tupla = list(diccionario.items())

	for x in range(len(tupla)):
		mergeSort(tupla)
	#print(tupla)

	newlist = [tupla[p][1] for p in range(len(tupla))]

	for x in range(len(newlist)):
		mergeSort(newlist[x])
	a = [{p[1]:p[0] for p in newlist[q]} for q in range(len(newlist))]
	
	
	Final = [[y for y in a[x].keys()] for x in range(len(a)) ]
	print(Final)
	#
	#



	

# driver code to test the above code 
if __name__ == '__main__': 
	n = 6
	m = 3
	k = 2
	Zoo = {'Gato': 3, 'Libelula': 2, 'Ciempies': 1, 'Nutria': 6, 'Perro': 4, 'Tapir':5}
	
	apertura = [['Tapir', 'Nutria', 'Perro'], ['Tapir', 'Perro' ,'Gato'], ['Ciempies', 'Tapir', 'Gato'], ['Gato', 'Ciempies', 'Libelula']]

	parte1 = [['Tapir', 'Nutria', 'Perro'], ['Ciempies', 'Tapir', 'Gato']]

	parte2 = [['Gato', 'Ciempies', 'Libelula'], ['Tapir', 'Perro' 'Gato']]

	Change(apertura);
	
