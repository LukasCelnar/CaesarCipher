print('----------------------------------')
print('|                                |')
print('|          Caesar Cipher         |')
print('|                                |')
print('----------------------------------')

# Alphabet
alphabet = ' abcdefghijklmnopqrstuvwxyz'

# Function that encrypts a given string
def encryption():
	inp = input('\nEnter your Text: ').lower()
	key = int(input('Enter your Key value: '))
	output = ''

	for i in inp:
			index = (alphabet.index(i))
			if index + key > 26:
				index = (index + key) % 27
			else:
				index += key
			output += (alphabet[index])
	print('-' + (len(output) * '-') + '-')
	print('|' + str(output) + '|')
	print('-' + (len(output) * '-') + '-')

# Function that decrypts encryptet string using key
def decryption_with_key():
    inp = input("\nEnter your Encrypted String: ").lower()
    key = int(input("Enter Your Key: "))
    output = ''

    for i in inp:
        index = alphabet.index(i)
        if key > 26:
            key = key % 27
        index -= key
        output += alphabet[index]
    print('-' + (len(output) * '-') + '-')
    print('|' + str(output) + '|')
    print('-' + (len(output) * '-') + '-')

# Function that decrypts encryptet without a key
def decryption_without_key():
	inp = input('\nEnter the Encrypted letters: ').lower()
	# Mostly used letters in alphabets
	mostly_used_letters = [' ', 'e', 'a', 'r', 'i', 'o']
	# lst = [Mosty used letter, How many time it was used]
	lst = ['', 0]

	print('\nNote that this works better when text is longer !')
	print('\nAlphabet letters in encrypted list:')

	for i in range(len(alphabet)):
		count = inp.count(alphabet[i])
		letter = alphabet[i]
		if lst[1] < count:
			lst[0] = letter
			lst[1] = count
	# Most used letter
	letter = lst[0]
	# How many times it was used
	count = lst[1]

	for i in range(len(mostly_used_letters)):
		output = ''
		key = (alphabet.index(letter) - alphabet.index(mostly_used_letters[i]))
		if key < 0:
			key *= -1
		print('\n(' + str(key) + ')')

		for i in inp:
			index = alphabet.index(i)
			if key > 26:
				key = key % 27
			index -= key
			output += alphabet[index]
		print('-' + (len(output) * '-') + '-')
		print('|' + str(output) + '|')
		print('-' + (len(output) * '-') + '-')


def frequency_analysis():
	inp = input('\nCopy the string of letters: ').lower()
	print('\nPossible Keys: \n')

	for i in range(len(alphabet)):
		count = inp.count(alphabet[i])
		# three dots (...) is uequal one use
		print(alphabet[i], 'x', count, count * '...')

while True:
    try:
        main_input = int(input('\n(1) for Encryption\n(2) for Decryption With Key\n(3) for Decryption Without Key\n(4) for Frequency Analysis\n(5) to exit this program\n\nWhich one you want to chose: '))
        if main_input == 1:
            encryption()
        elif main_input == 2:
            decryption_with_key()
        elif main_input == 3:
            decryption_without_key()
        elif main_input == 4:
            frequency_analysis()
        elif main_input == 5:
            break
        else:
            print("\nEnter a valid number please !")

	# If somebody types something different than he should, it will print Invalid Input and reset
    except:
        print("\nInvalid Input")

# When program ends it prints this
print("\nThanks for using")
