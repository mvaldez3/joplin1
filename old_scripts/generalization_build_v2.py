import pandas as pd
import numpy as np
import random

def gen_build(train_file, prototype_file, num_rows2add, random_seed = None):

	random.seed(random_seed)

	#read in the training file.
	train_file = pd.read_csv(train_file, header=None)
	'''Rename it to gen_file starting because we will want to use the original training file to refer back to. gen_file_starting will be used as the base number of 
	rows we started with, but will change with each iteration of the loop'''
	gen_file_starting = train_file
	#gen_file will be the file we append the new rows two during each iteration of the loop. At the end of every loop, gen_file will become the new gen_file starting. 
	gen_file = gen_file_starting


	#create an example of each of the possible distances, specify the number of rows to add for each distance, create an array to loop through
	dist_1 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 1, 0])
	dist_2 = np.array([1, 1, 1, 1, 1, 1, 1, 1, 0, 0])
	dist_3 = np.array([1, 1, 1, 1, 1, 1, 1, 0, 0, 0])
	dist_4 = np.array([1, 1, 1, 1, 1, 1, 0, 0, 0, 0])
	dist_6 = np.array([1, 1, 1, 1, 0, 0, 0, 0, 0, 0])
	dist_7 = np.array([1, 1, 1, 0, 0, 0, 0, 0, 0, 0])
	dist_8 = np.array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0])

	#specify the number of rows to add in total for each distance.
	rows_to_add = num_rows2add

	#create a varible that counts the number of training stimuli we have in the training file
	num_of_stim = len(train_file.index)


	#read in the prototype file
	prototypes = pd.read_csv(prototype_file, header = None)

	#make a file that includes the prototypes and the traiing stimuli. This will be the base of both generalization files.

	#append the training file to the prototype file
	gf_base = prototypes.append(train_file, ignore_index = True)
	gf1_base = gf_base
	gf2_base = gf_base

	# make a list of all the distances to loop through 
	distances = [dist_1, dist_2, dist_3, dist_4, dist_6, dist_7, dist_8]

	for dist in distances:
		isokay = True
		while isokay:
			#randomly shuffle the distance array to generate a possible new stimulus
			random.shuffle(dist)
			curr_arr = np.array(dist)
			#compare the generated possible stimulus with all the already added stimuli. This will return a boolean phrase for the comparison to each row.
			all_comparison = []
			for i in list(range(len(gen_file.index))):
				single_row = np.array(gen_file.iloc[i])
				compare = np.array_equal(curr_arr, single_row, equal_nan = False) * 1
				all_comparison.append(compare)
			#convert boolean phrases to integers to make it easier to compare. 1 = True = duplicate = don't add
			duplicate = 1
			if duplicate in all_comparison:
				continue
			#if there it is not a dupicate, add it to the file
			else: 
				data_to_append =  {}
				for i in list(range(len(gen_file.columns))):
					data_to_append[gen_file.columns[i]] = dist[i]
				gen_file = gen_file.append(data_to_append, ignore_index = True)
				#calculate the number of added rows by subtracting the current number of rows by the starting number of rows (starting # changes each iteration of the loop)
				added_rows = (len(gen_file.index) - len(gen_file_starting))
				#recalculate isokay variable. 
				isokay = added_rows < rows_to_add
		#set gen_file_starting equal to the gen_file we just created because we want this to be the new number of rows for when we calculate added_rows in the next iteration
		gen_file_starting = gen_file

	#separate the whole dataframe into 2 separate gen_files that each contain all stimuli, prototypes, and a random 5 rows of each distance

	#calculate which row the gen stim actually start 
	gen_stim_start = num_of_stim

	#index the rows for each distance
	d1_index = list(range(gen_stim_start, gen_stim_start+rows_to_add))
	d2_index = list(range(d1_index[-1]+1, d1_index[-1]+1+rows_to_add))
	d3_index = list(range(d2_index[-1]+1, d2_index[-1]+1+rows_to_add))
	d4_index = list(range(d3_index[-1]+1, d3_index[-1]+1+rows_to_add))
	d6_index = list(range(d4_index[-1]+1, d4_index[-1]+1+rows_to_add))
	d7_index = list(range(d6_index[-1]+1, d6_index[-1]+1+rows_to_add))
	d8_index = list(range(d6_index[-1]+1, d6_index[-1]+1+rows_to_add))

	#randomly shuffle all of lists to get random rows of each distance
	random.shuffle(d1_index)
	random.shuffle(d2_index)
	random.shuffle(d3_index)
	random.shuffle(d4_index)
	random.shuffle(d6_index)
	random.shuffle(d7_index)
	random.shuffle(d8_index)

	#split the shuffled list in half so that half of the rows for each distance go in each file
	half = int(rows_to_add/2)
	d1_1 = d1_index[0:half]
	d1_2 = d1_index[half:rows_to_add]
	d2_1 = d2_index[0:half]
	d2_2 = d2_index[half:rows_to_add]
	d3_1 = d3_index[0:half]
	d3_2 = d3_index[half:rows_to_add]
	d4_1 = d4_index[0:half]
	d4_2 = d4_index[half:rows_to_add]
	d6_1 = d6_index[0:half]
	d6_2 = d6_index[half:rows_to_add]
	d7_1 = d7_index[0:half]
	d7_2 = d7_index[half:rows_to_add]
	d8_1 = d8_index[0:half]
	d8_2 = d8_index[half:rows_to_add]

	# create a list of which rows go in the 1st gen file.
	gf1_data2add = [d1_1, d2_1, d3_1, d4_1, d6_1, d7_1, d8_1]


	#create the first data set
	for distance in gf1_data2add:
		for row in distance:
			row = list(gen_file.iloc[row])
			data_to_append =  {}
			for i in list(range(len(gf1_base.columns))):
				data_to_append[gen_file.columns[i]] = row[i]
			gf1_base = gf1_base.append(data_to_append, ignore_index = True)
	gf1 = gf1_base
	gen_file1 = gf1.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile1.csv', header = None, index = False)

	#create the second data set
	gf2_data2add = [d1_2, d2_2, d3_2, d4_2, d6_2, d7_2, d8_2]
	for distance in gf2_data2add:
		for row in distance:
			row = list(gen_file.iloc[row])
			data_to_append =  {}
			for i in list(range(len(gf2_base.columns))):
				data_to_append[gen_file.columns[i]] = row[i]
			gf2_base = gf2_base.append(data_to_append, ignore_index = True)
	gf2 = gf2_base
	gen_file2 = gf2.to_csv('/Volumes/shares/Cabi/exp/joplin/joplin1/data/genfile2.csv', header = None, index = False)

	return gen_file1, gen_file2

#gen_build('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/train_file.csv', '/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/prototype.csv', 10)
