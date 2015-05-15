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
	
	for filtered_word in checklist:
		if filtered_word in words:
			words = words.replace(filtered_word, '*' * len(filtered_word))
	print(words)
			
			
if __name__ == '__main__':
	input_words = input('Enter some words: ')
	filtered_word(input_words)