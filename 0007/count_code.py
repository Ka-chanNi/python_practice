#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import glob
import re

# get all files in designated path
def get_files(path):
	outputDir = []
	finalDir = []
	currentDir = glob.glob(path + r'\*')
	for direct in currentDir:
		if os.path.isfile(direct):
			outputDir.append(direct)
		elif os.path.isdir(direct):
			nextDir = get_files(direct)
			outputDir += nextDir
	for i in range(len(outputDir)):
		cutDir = re.split(r'[\\ .]\s*', outputDir[i])
		if cutDir[-1] != 'txt':
			if cutDir[-1] != 'py':
				pass
			else:
				finalDir.append(outputDir[i])
		else:
			finalDir.append(outputDir[i])
	return finalDir
	
# Count lines and blank lines and note lines in designated files
def count_lines(files):
	line, blank, note = 0, 0, 0
	for filename in files:
		f = open(filename, 'rb')
		print(f)
		for i in f:
			i = i.strip()
			i = i.decode()
			line += 1
			if i == '':
				blank += 1
			elif i[0] == '#' or i[0] == '/':
				note += 1
		f.close()
	return (line, blank, note)
	
if __name__ == '__main__':
	files = get_files('..')
	print(files)
	lines = count_lines(files)
	print('Line(s): %d, blank line(s): %d, note line(s): %d'% (lines[0], lines[1], lines[2]))