#!/usr/bin/python
# -*- coding: utf-8 -*-

def filtered_word(words):
	file_object = open('filtered_words.txt', 'rb')
	file_words = file_object.read().decode('utf-8')
	file_final = ''.join(file_words).split('\r')
	checklist = []
	for word in file_final:
		checklist.append(word.strip('\n'))
	file_object.close()
	print(checklist)
	
	filtered_word = False
	for word in checklist:
		if word in words:
			filtered_word = True
			break
			
	if filtered_word is True:
		print('Freedom')
	else:
		print('Human Rights')
		
	
if __name__ == '__main__':
	input_words = input('Enter some words: ')
	filtered_word(input_words)