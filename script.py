import sys
import random

#create list for storing lines with the word "fake"
fake_lines = list()

#loop over lines of command line input
for line in sys.stdin:
	#remove TRUMP, QUESTIONS, and /n from lines
	line = line.strip("TRUMP:")
	line = line.strip("QUESTION:")
	line = line.strip()
	#split the lines into words along single spaces
	words = line.split(" ")
	
	#check if fake is one of the words in a line
	if "fake" in words:
		#if fake is present, add the line to list fake_lines
		fake_lines.append(line)

#shuffled the contents of fake_lines
random.shuffle(fake_lines)

#loop over the lines in list fake_lines
for line in fake_lines:
	#print the lines
	print line
