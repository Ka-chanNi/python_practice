import random
import string

def generate_code(id, length=10):
	head = hex(int(id))[2:] + 'L'
	length = length - len(head)
	allstrings = string.ascii_letters + string.digits
	
	return head + ''.join([random.choice(allstrings) for i in range(length)])
	
def get_id(code):
	return str(int(code.upper(), 16))
	
if __name__ == '__main__':
	for i in range(100, 500, 35):
		code = generate_code(i)
		id_hex = code.split('L')[0]
		id = get_id(id_hex)
		print('The invitation code is: ' + code + ', and the id is: ' + id)