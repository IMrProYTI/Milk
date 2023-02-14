from time import sleep

def main():
	i = 0
	print("Milk", end='')
	while True:
		if i % 10 == 0:
			print(" inside a bag of\n\nMilk", end='')
		elif i % 2 == 0:
			print(" inside a bag of\nMilk", end='')
		else:
			print(" outside a bag of\nMilk", end='')
		sleep(1)
		i += 1



if __name__ == '__main__':
	main()