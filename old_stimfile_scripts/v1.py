# Import all relevant packages
import pandas as pd
import numpy as np

### Open prototype file and randomly select a prototype
proto_file = pd.read_csv('/Users/valdez3/Desktop/Prototype.csv', header = None)
randpro = (proto_file.sample())

### Open the training stimuli set
train_file = pd.read_csv('/Users/valdez3/Desktop/dev_train.csv', header = None)

### Automatically select base training set if the randsomly selected prototype is equal to all 1's


# convert randpro to numpy array for commparison
randpro_arr = np.array(randpro)
print(randpro_arr)

# compare whether the randomly selected prototype is equal to all 1 prototype
#comparison = (randpro_arr == [11111111]).all()

# count number of rows in training file
count = len(list(train_file.index))

# make variable that contains array of total number of rows in train_file
num_rows = []
for i in range(count):
	num_rows.append(i)

# make for loop that selects base stimulus set if the arrays are equal (i.e. randomly selected prototype = all 1's)

if (randpro_arr == [1,1,1,1,1,1,1,1,1,1]).all() == True:
	# convert pandas dataframe to numpy array to make importing to psychopy easier

	sum_feat = []
	code = []
	for n in train_file:
		pd2np = np.array((train_file.iloc[n]).to_numpy())
		
		#need to sum across all arrays to make a variable for categorization
		sums = np.sum(pd2np)
		sum_feat.append(sums)

		int2str = np.array2string(pd2np)
		code.append(int2str)
	#clean up array to match format of stim names
		base_stim = np.array(code)
		for x in code:
			base_stim = (np.char.strip(base_stim, '[]'))

elif (randpro_arr == [0000000000]).all() == True:

### If prototype does not = All 1's, then recode training set to match prototype

	
#go through each number in array (corresponding to a row) and compare it to the prototype
	#trying with pd series

	sums_feat = []
	recode = []
	for i in num_rows:
		single_row = np.array(train_file.iloc[i])
		compare = randpro_arr == single_row


		#convert bool phrases into integers
		bool2int = compare*1
		

		#need to sum across all arrays to make a variable for categorization
		sums = np.sum(bool2int)
		sums_feat.append(sums)
		

		#convert integers into string
		int2str = np.array2string(bool2int)
		pritn(type(in))
		#append each row to the last
		recode.append(int2str)


	sums_feat = np.asarray(sums_feat)
	print(type(recode))

	# clean up formatting of arrays to match format of stim name
	for x in recode:
		stim_id_arr = (np.char.strip(recode, '[]'))
	
	
	### create dataframe for reading in
	recoded_pd = pd.DataFrame(data = stim_id_arr, columns = None)
	recoded_pd['sums_feat'] = sums_feat.tolist()
	recoded_pd['category'] = ''
	recoded_pd.columns = ['stim_id_arr', 'sums_feat', 'category']
	print(recoded_pd)


	recoded_pd.loc[recoded_pd.sums_feat > 5, 'category'] = 'A'
	recoded_pd.loc[recoded_pd.sums_feat < 5, 'category'] = 'B'

	print(recoded_pd)

else: 
	print("Prototype Not Specified")
	
	