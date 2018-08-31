filepath = 'tt.txt'
arr1 = []
with open(filepath) as fp:  
	line = fp.readline()
        cnt = 1
        while line:       
		line = fp.readline()
		if(line !=  ''):
			arr1.append(line.strip())

T2 = map(int, arr1) 		
print(T2)
