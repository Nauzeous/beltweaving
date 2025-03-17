''' 
This is a fun challenge i took on after watching Michael Hendriks' video
https://youtu.be/2NKK_2v4jiE?si=TDIdW1tEbszvXW4q
It finds the longest line you can make by belt weaving in factorio, using the new
green belts
keep in mind that the printed lines arent all the best solutions, and the best solution is padded 
each number in the array represents an exit and entry underground belt
'''


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

global largest
largest = 0

def belt(arr):
	global largest
	if is_invalid_belt(arr):
		return
	belt(arr+[1])
	belt(arr+[2])
	belt(arr+[3])
	belt(arr+[4])
	length = len(arr)
	if length > largest:
		largest = length
		print(arr)
		print(length*2,"tiles long (including padding)")
belt([])