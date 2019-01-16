
# --------------------------------------------- #
# Author: Christian Armatas    		   			#
# Project: String Alignment Implementation		#
# Date: 2/20/2017            		   			#
# Command: python imp2_runtime_test.python		#
# --------------------------------------------- #

#		DESCRIPTION
#
#		This program will process create random "ATCG" strings of length 500, 1000, 2000,
#	4000, and 5000. Ten pairs of each length of n will be created and placed into the input file
#	 "imp2input.txt. This program will process the input file, line by line, by comparing
#	the first and second strings on each line (parsed at ","). This program will find the
#	minimum edit distance between the two strings, reconstruct the edit sequences, and output
#	the results to the file "imp2ouput.txt". 
#
#	NOTE:	The output file "imp2output.txt" will be created if one does not exist. If the file
#			already exists, the results will be APPENDED onto the end of the previous content.
#	

import os.path
import sys, getopt
import numpy as np
import bisect
import random
import time

str1 = ""
str2 = ""


# Create random strings of ATCG: lengths 500, 1000, 2000, 4000, and 5000
def randomATCG(n):
  alphabet = list('ATCG')
  randString = [random.choice(alphabet) for i in range(n)]		# Select random chars
  randString = ''.join(randString)								# Join all chars
  
  return randString

  
  # Declare global string variables
def declareVars(n):
	global str1
	global str2
	
	str1 = randomATCG(n)
	str2 = randomATCG(n)
	
	return str1, str2

	
# Recursively called function
def levenshtein_distance(first, second):
	# Find the minimum edit distance between two strings
	if len(first) > len(second):
		first, second = second, first

	if len(second) == 0:
		return len(first)*2
	if len(first) == 0:
		return len(second)*2	

	first_length = len(first) + 1
	second_length = len(second) + 1
	distance_matrix = [[0] * second_length for x in range(first_length)]

	# Fill in first column with first string
	for i in range(first_length):
		distance_matrix[i][0] = i
	
	# Fill in first row with second string
	for j in range(second_length):
		distance_matrix[0][j] = j
	
	# Create distance matrix
	for i in xrange(1, first_length):
		for j in range(1, second_length):
			deletion = distance_matrix[i-1][j] + 1		# Deletion
			insertion = distance_matrix[i][j-1] + 1		# Insertion
			substitution = distance_matrix[i-1][j-1]	# Substitution
					
			if first[i-1] != second[j-1]:
				substitution += 2
				
			# Recursively find fastest route
			distance_matrix[i][j] = min(insertion, deletion, substitution)
	
	# Print matrix
	# print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in distance_matrix]))
	# print "\n"
	
	# Traceback to form distance strings
	i = (first_length-1)
	j = (second_length-1)
	str1 = ""
	str2 = ""

	while (i > 0):
		# Check to see if we are traveling to the left, down, or diagonal
		if distance_matrix[i-1][j-1] <= (distance_matrix[i][j-1]) & (distance_matrix[i-1][j]):
			i -= 1
			j -= 1
			str1 = first[i] + str1 
			str2 = second[j] + str2
		elif distance_matrix[i-1][j] <= (distance_matrix[i][j-1]) & (distance_matrix[i-1][j-1]):
			i -= 1
			str1 = first[i] + str1 
			str2 = "-" +  str2
		else:
			j -= 1
			str1 = "-" + str1 
			str2 = second[j]+ str2
		
		# If we reach the end of one string, but the other has characters remaining...
		if (j <= 0):
			while (i != 0):
				i -= 1
				str1 = first[i] + str1 
				str2 = "-" +  str2
			break
		elif (i <= 0):
			while (j != 0):
				j -= 1
				str1 = "-" + str1
				str2 = second[j] + str2 
			break
	
	# Concatenate output string for "imp2output_our.txt"
	concatOutput = str1 + "," + str2 + ":"
	concatOutput += str(distance_matrix[first_length-1][second_length-1])
	
	# Write the newest string to "imp2output_our.txt"
	text_file = open("imp2output.txt", "a")
	text_file.write("%s\n" % concatOutput)
	text_file.close()
	
	# Return minimum edit distance
	return distance_matrix[first_length-1][second_length-1]
	
	
# MAIN
def main():
	# Create and execute minDistance for 10 pairs of strings (length = 500)
	print "\n\n  ----- \n\nFinding minimum edit distance and edit sequences for 10 pairs of strings: LENGTH = 500\n"
	n_500_start_time = time.time()
	for x in range(0,10):
		# Set and check parameters
		print "Iteration: %d\n" % x
		n = 500
		str1, str2 = declareVars(n)
		
		# Create input string for "imp2input.txt"
		inputStr = str1 + "," + str2
		
		# Write the newest string to "imp2input.txt"
		text_file = open("imp2input.txt", "a")
		text_file.write("%s\n" % inputStr)
		text_file.close()
		
		# Find and print results
		minDistance = levenshtein_distance(str1, str2)
		
	n_500_total_time = (time.time() - n_500_start_time)
	print("RUN TIME for n=500: --- %s seconds ---\n" % (n_500_total_time)) 
	
	# Create and execute minDistance for 10 pairs of strings (length = 1000)
	print "Finding minimum edit distance and edit sequences for 10 pairs of strings: LENGTH = 1000\n"
	n_1000_start_time = time.time()
	for x in range(0,10):
		# Set and check parameters
		print "Iteration: %d\n" % x
		n = 1000
		str1, str2 = declareVars(n)
		
		# Create input string for "imp2input.txt"
		inputStr = str1 + "," + str2
		
		# Write the newest string to "imp2input.txt"
		text_file = open("imp2input.txt", "a")
		text_file.write("%s\n" % inputStr)
		text_file.close()
		
		# Find and print results
		minDistance = levenshtein_distance(str1, str2)
		
	n_1000_total_time = (time.time() - n_1000_start_time)
	print("RUN TIME for n=1000: --- %s seconds ---\n" % (n_1000_total_time)) 
	
	# Create and execute minDistance for 10 pairs of strings (length = 2000)
	print "Finding minimum edit distance and edit sequences for 10 pairs of strings: LENGTH = 2000\n"
	n_2000_start_time = time.time()
	for x in range(0,10):
		# Set and check parameters
		print "Iteration: %d\n" % x
		n = 2000
		str1, str2 = declareVars(n)
		
		# Create input string for "imp2input.txt"
		inputStr = str1 + "," + str2
		
		# Write the newest string to "imp2input.txt"
		text_file = open("imp2input.txt", "a")
		text_file.write("%s\n" % inputStr)
		text_file.close()
		
		# Find and print results
		minDistance = levenshtein_distance(str1, str2)
		
	n_2000_total_time = (time.time() - n_2000_start_time)
	print("RUN TIME for n=2000: --- %s seconds ---\n" % (n_2000_total_time))
	
	# Create and execute minDistance for 10 pairs of strings (length = 4000)
	print "Finding minimum edit distance and edit sequences for 10 pairs of strings: LENGTH = 4000\n"
	n_4000_start_time = time.time()
	for x in range(0,10):
		# Set and check parameters
		print "Iteration: %d\n" % x
		n = 4000
		str1, str2 = declareVars(n)
		
		# Create input string for "imp2input.txt"
		inputStr = str1 + "," + str2
		
		# Write the newest string to "imp2input.txt"
		text_file = open("imp2input.txt", "a")
		text_file.write("%s\n" % inputStr)
		text_file.close()
		
		# Find and print results
		minDistance = levenshtein_distance(str1, str2)
		
	n_4000_total_time = (time.time() - n_4000_start_time)
	print("RUN TIME for n=4000: --- %s seconds ---" % (n_4000_total_time))
	
	# Create and execute minDistance for 10 pairs of strings (length = 5000)
	print "Finding minimum edit distance and edit sequences for 10 pairs of strings: LENGTH = 5000\n"
	n_5000_start_time = time.time()
	for x in range(0,10):
		# Set and check parameters
		print "Iteration: %d\n" % x
		n = 5000
		str1, str2 = declareVars(n)
		
		# Create input string for "imp2input.txt"
		inputStr = str1 + "," + str2
		
		# Write the newest string to "imp2input.txt"
		text_file = open("imp2input.txt", "a")
		text_file.write("%s\n" % inputStr)
		text_file.close()
		
		# Find and print results
		minDistance = levenshtein_distance(str1, str2)
		
	n_5000_total_time = (time.time() - n_5000_start_time)
	print("RUN TIME for n=5000: --- %s seconds ---\n" % (n_5000_total_time))	
	
if __name__== "__main__":
	start_time = time.time()
	main()
	print("TOTAL RUN TIME: --- %s seconds ---\n\n" % (time.time() - start_time))



