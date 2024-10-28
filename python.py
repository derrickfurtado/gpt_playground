
# """
# inputArr, represents the list containing N elements.
# """
# def funcMeanMode(inputArr):
# 	total = 0
# 	frequency = {}
# 	mode = None
# 	largest_freq = 0

# 	for num in inputArr:
# 		total = num + total
# 		if num in frequency:
# 			frequency[num] += 1
# 		else:
# 			frequency[num] = 1
	
# 	mean = total / len(inputArr)

# 	for key, value in frequency.items():
# 		if value > largest_freq:
# 			largest_freq = value
# 			mode = key

# 	final_value = str(int(mean)) + " " + str(mode)
# 	return final_value

# def main():
# 	# input for inputArr
# 	inputArr = []
# 	inputArr_size  = int(raw_input())
# 	inputArr = list(map(int,raw_input().split()))
	
# 	result = funcMeanMode(inputArr)
# 	print result,	

# if __name__ == "__main__":
# 	main()

#########################################################

"""
inputNum1, represents the number X.
inputNum2, represents the number Y.
"""
def funcCount(inputNum1, inputNum2):
	counter = 0
	for i in range(1, inputNum1):
		left_num = i
		for i in range(inputNum1, 1, -1):
			right_num = i
			if left_num == right_num or left_num > right_num:
				break
			elif left_num + right_num == inputNum2:
				counter = counter + 1
	return counter

def main():
	# input for inputNum1
	inputNum1 = int(raw_input())
	# input for inputNum2
	inputNum2 = int(raw_input())
	
	result = funcCount(inputNum1, inputNum2)
	print result,	

if __name__ == "__main__":
	main()

########################################################


"""
inputStr, represents the given string for the puzzle
"""
def funcSubstring(inputStr):
	if len(inputStr) % 2 == 1:
		return None

	wordBank = {}

	print(wordBank)
	for letter in inputStr:
		

	return

def main():
	# input for inputStr
	inputStr = str(raw_input())
	
	result = funcSubstring(inputStr)
	print result,	

if __name__ == "__main__":
	main()