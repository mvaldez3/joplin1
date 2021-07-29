import csv
import random

with open('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/Prototype.csv', encoding='utf-8-sig') as proto_file:
	proto_file = csv.reader(proto_file)
	
	# create a list of lists containing each for in the prototype file
	proto_list = []
	for row in proto_file:
		proto_list.append(row)
	# Add a random seed. Randomly choose a row from the prototype file and assign it as the random prototype
random.seed(None)
randpro = random.choice(proto_list)

	# Turn the randomp prototype into a list of integers instead of strings to make comparisons
for item in range(0, len(randpro)):
	randpro[item] = int(randpro[item])

print(randpro)

	# Open training file and turn each row into a list of integers instead of strings. Count the number of stimulus (rows) there are in the file. 
with open('/Volumes/shares/Cabi/exp/joplin/joplin1/stim_files/dev_train.csv', encoding='utf-8-sig') as sf:
	sf = csv.reader(sf)
	rows = list(sf)
	count = (list(range(len(rows))))

	# Make a new list that contains a list for each row in the stimlus file as integers instead of strings.
	stimulus_list = []
	for i in count:
		new_row = []
		for element in rows[i]:
			new_row.append(int(element))
		stimulus_list.append(new_row)

	# create a list of all 1's to compare to the randomly selected prototype later
all1proto = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

	# Compare the randomly selected prototype to the all 1's. If it is the same, then take the stimulus file as is and add the necessary columns.
if randpro == all1proto:
	
	stim_id = []
	sums_feat = []
	category = []
	correct_key = []
	for item in stimulus_list:
		# calculate the sum of the number of features each stimulus has in common with the protoype
		sums = sum(item)
		sums_feat.append(sums)

		# define the categories based on sum_feat 
		if sums > 5:
			cat = 'batmans'
		else:
			cat = 'robins'

	# define which key is correct based on the category it is assigned
		if cat == 'batmans':
			key_corr = 'f'
		elif cat == 'robins':
			key_corr = 'j'
		correct_key += [key_corr]

		# append cat to category. Have to use different operation because .append doesn't work for strings
		category += [cat]

		# now that all the manipulations are done, we need to concatenate the recoded stimuli to match the file names. 
		string = ''.join([str(item) for item in item])
		string = ''.join('\'' + string + '\'')
		stim_id += [string]

	# If the randomly selected prototype is not all 1's then we need to recode the stimulus and add the necessary rows. 
	else:
		# get the number of stimuli in the stim_file and create a list of the range of numbers.
		count_stim_list = list(range(len(stimulus_list)))
		
		# count the number of items in the prototype and create a list for the range of numbers. Should always be 10 for the 10 features.
	count_randpro = (list(range(len(randpro))))
	
		# create empty list for each column we want in our csv
	comparison = []
	stim_id = []
	sums_feat = []
	category = []
	correct_key = []

		# make a new variable defining the stimulus we are currently working with as "stim"
	for i in count_stim_list:
		stim = stimulus_list[i]

			# create another empty list to store the comparisons between the prototype and the current stimulus
		new_code = []
		for n in count_randpro:
			if stim[n] == randpro[n]:
				output = bool('True')
			else:
				output = bool('')

				# turn the boolean phrases into into integers for the new code. Append each item to the rest of the items within the stimulus
			new_code.append(output * 1)

			# Add the recoded stimuli into the same list. We only need this list to check that the recode worked. It won't be going in the csv
		comparison.append(new_code)

			# compare the new code to the stimuli to get the number of features that match so we can add them up and determine the category
		compare_cat = []
		for x in count_randpro:
			if new_code[x] == randpro[x]:
				output = bool('True')
			else:
				output = bool('')
			compare_cat.append(output*1)

			# find a sum of the number of features each stimulus has in common with the prototype
		sums = sum(compare_cat)
		sums_feat.append(sums)
		
			# define the categories based on the number of features each stimulus has in common with the prototype
		if sums > 5:
			cat = 'batmans'
		else:
			cat = 'robins'
		category += [cat]

			# define which key is correct based on the category it is assigned
		if cat == 'batmans':
			key_corr = 'f'
		elif cat == 'robins':
			key_corr = 'j'
		correct_key += [key_corr]

			# now that all the manipulations are done, we can to concatenate the recoded stimuli to match the file names
		string = ''.join([str(item) for item in new_code])
			# added quotations so that the leading zeros are not removed when writing to the csv file. Will take them off in psychopy
		string = ''.join('\'' + string + '\'')
		stim_id += [string]

	# write the results to a new csv file. 
	with open('/Volumes/shares/Cabi/exp/joplin/joplin1/data/_stimfile.csv', 'w', newline='') as stim_file:
		writer = csv.writer(stim_file)
		writer.writerow(('stim_id', 'sums_feat', 'category', 'correct_key'))
		for i in range(len(stim_id)):
			writer.writerow((stim_id[i], sums_feat[i], category[i], correct_key[i]))
