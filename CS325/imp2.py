
# --------------------------------------------- #
# Author: Christian Armatas    		   			#
# Project: String Alignment Implementation		#
# Date: 2/20/2017            		   			#
# Command: python imp2.python					#
# --------------------------------------------- #

#	--- DESCRIPTION ---
#	
#		This program will process an input file "imp2input.txt, line by line, by comparing
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
	# Create and execute minDistance for "imp2input.txt"
	with open("imp2input.txt", "r") as infile:
		i = 0
		for line in infile:	
			i += 1
			print "Processing line [%d] of \"imp2input.txt\"\n" % i
			temp = line
			value = temp.split(",")
			str1 = value[0]
			value2 = value[1].split("\n")
			str2 = value2[0]
			
			# Find and print results
			minDistance = levenshtein_distance(str1, str2)


if __name__== "__main__":
	start_time = time.time()
	main()
	print("TOTAL RUN TIME: --- %s seconds ---\n\n" % (time.time() - start_time))



