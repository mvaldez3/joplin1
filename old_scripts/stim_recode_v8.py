# have to import pandas and np into program before running 
import pandas as pd
import numpy as np 

def randpro_select(prototype_file):

	### Open prototype file and randomly select a prototype
	proto_file = pd.read_csv(prototype_file, header = None)

	#select a random prototype from the file
	randpro = np.array(proto_file.sample(n = 1, random_state = None))

	return randpro 

	'''Selects a random prototype from a prototype file.
	
	Inputs:
	prototype_file - .csv file containing a list of prototypes. Each prototype should be its own row and each feature should be its own column. 

	Output:
	Numpy array of randomly selected prototype
	'''


def stim_build(stim_file, random_prototype_selection):

	from stim_file_script import randpro_select

#define possible prototypes as numpy arrays for later comparison
	all1proto = np.array([[1,1,1,1,1,1,1,1,1,1]])


### Open the training stimuli set
	train_file = pd.read_csv(stim_file, header = None)

#count the number of rows in the training file
	count = len(list(train_file.index))

#make a variable that contains a list of the total number of rows in the training file

	num_rows = []
	for i in range(count):
		num_rows.append(i)


# make for loop that selects base stimulus set if randomly selected prototype = All 1's and recodes the stimulus if not

	if np.array_equal(random_prototype_selection, all1proto) == True:
		sum_feat = []
		stim_id = []
		for n in train_file:
			#convert the pandas series to numpy array for easier manipulation 
			pd2np = np.array((train_file.iloc[n]).to_numpy())
		
			#need to sum across all arrays to make a variable for categorization
			sums = np.sum(pd2np)
			sum_feat.append(sums)

			#convert all elements in array from integers to strings to use in psychopy
			int2str = np.array2string(pd2np)
			stim_id.append(int2str)

		#convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
		sum_feat = np.asarray(sum_feat)
		stim_id = np.asarray(stim_id)

		#clean up array to match format of stim names in stim folder
		stim_id = np.array(stim_id)
		for x in stim_id:
			stim_id = (np.char.strip(stim_id, '[]'))


	

		### create dataframe for reading into psychopy
		id_df = pd.DataFrame(data = stim_id, columns = None)
		id_df = id_df.astype(str)
		id_df['sum_feat'] = sum_feat.tolist()
		id_df['category'] = ''
		id_df['correct_key'] = ''
		id_df.columns = ['stim_id', 'sums_feat', 'category', 'correct_key']


		#specify parameters for categorization 

		id_df.loc[id_df.sums_feat > 5, 'category'] = 'batmans'
		id_df.loc[id_df.sums_feat < 5, 'category'] = 'robins'

		id_df.loc[id_df.category == 'batmans', 'correct_key'] = 'f'
		id_df.loc[id_df.category == 'robins', 'correct_key'] = 'j'
		print(id_df)

		#convert to csv so psychopy can read
		csv_file = id_df.to_csv('_stimfile.csv', header = True, index = False)

	else:
		sums_feat = []
		recoded_id = []
	
		for i in num_rows:
			single_row = np.array(train_file.iloc[i])
		
			# convert randpro to numpy array for commparison
			randpro_arr = np.array(random_prototype_selection)

			#compare each element in the randomly selected prototype to each element in the row
			compare = randpro_arr == single_row

			#convert the bool phrases into integers to get the new code
			new_code = compare*1

			# compare the new_code to the prototype to get a sum of the number of features that match to we can categorize
			compare_cat = randpro_arr == new_code
		
			# convert the boolean phrases to integers so we can sum
			cat = compare_cat*1
			
			#sum across the new code to get the umber of features that match the prototype. Append this to the sum_feat array
			sums = np.sum(cat)
			sums_feat.append(sums)
		

			#convert integers into string
			new_code = np.array2string(new_code)
			#append each row to the last
			recoded_id.append(new_code)

		#convert the sums_feat into an array in order to add it as a column in the new pandas dataframe
		sums_feat = np.asarray(sums_feat)
		recoded_id = np.asarray(recoded_id)

		#clean up formatting of arrays to match format of stim name
		for x in recoded_id:
			recoded_id = (np.char.strip(recoded_id, '[]'))
			recoded_id = (np.char.strip(recoded_id, ' '))
	
	
		### create dataframe for reading into psychopy
		id_df = pd.DataFrame(data = recoded_id, columns = None)
		id_df = id_df.astype(str)
		id_df['sums_feat'] = sums_feat.tolist()
		id_df['category'] = ''
		id_df['correct_key'] = ''
		id_df.columns = ['stim_id', 'sums_feat', 'category', 'correct_key']


		id_df.loc[id_df.sums_feat < 5, 'category'] = 'batmans'
		id_df.loc[id_df.sums_feat > 5, 'category'] = 'robins'

		id_df.loc[id_df.category == 'batmans', 'correct_key'] = 'f'
		id_df.loc[id_df.category == 'robins', 'correct_key'] = 'j'

		print(id_df)

		#convert to csv so pyshchopy can read
		csv_file = id_df.to_csv('_stimfile.csv', header = True, index = False)
	
		return csv_file

	''' Recodes stimulus set with regard to the randomly selected prototype
	Inputs:
	stim_file - csv file with stimulus set. Each stimulus should be in its own row and each feature should be its own column. 
	random_prototype_selection - this will be the variable containing the output from randpro_select()

	Output:
	csv file containing the recoded stim ID, the category it belongs to, and the correct key for that category
	'''
if __name__ == '__main__':
	randpro = randpro_select('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/Prototype.csv')
	print(randpro)
	stim_build('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/dev_train.csv', randpro)
