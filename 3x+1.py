from time import sleep

def write_to_file(file,words,mode):
	with open(file, "w") as f:
		if mode:
			for word in words:
				f.write(str(word) + "|")
		else:
			f.write(str(words))

def read_file(file, mode):
	with open(file, "r") as f:
		str_nums = f.read().split("|")
		if mode:
			return [int(num) for num in str_nums if num.isdigit()]
		else:
			return (int(str_nums[len(str_nums)-1]))

x = read_file("nums tried.txt", False)
i = x
nums_not_work = read_file("nums not work.txt",True)
temp_nums = []

while True:
	if i%2 == 0:
		i = i/2
	elif i%2 == 1:
		i = (3*i)+1

	if i in nums_not_work:
		write_to_file("nums tried.txt", x,False)
		x = x+1
		i = x
		nums_not_work.extend(temp_nums)
		write_to_file("nums not work.txt", nums_not_work,True)
		temp_nums.clear()
		print("----- " + str(i)) 
	else:
		temp_nums.append(int(i))
		print(int(i))
	#sleep(0.5)