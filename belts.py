def is_invalid_belt(arr):
	df1=df2=df3=df4=0 
	for item in arr:
		df1+=2
		df2+=2
		df3+=2
		df4+=2
		match item:
			case 1:
				df1=0
			case 2:
				df2=0
			case 3:
				df3=0
			case 4:
				df4=0
		if df1 > 4 or df2>6 or df3>8 or df4>10:
			return True
	return False

largest = 0
sols = []

def belt(arr):
	global largest
	global sols
	if is_invalid_belt(arr):
		return
	belt(arr+[1])
	belt(arr+[2])
	belt(arr+[3])
	belt(arr+[4])
	length = len(arr)
	if length > largest:
		sols = []
		largest = length
	if length == largest:
		sols+=[arr]


belt([])

for i in sols:
	print(*i)
print(largest*2,"tiles long")
print("each number is an exit and entry underground belt, \
	1 represents a yellow belt, 2 represents a red, etc.")
print("printed solutions dont account for belt input and output")