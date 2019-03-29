events_dict={'1':'cs', '2':'google it', '3':'tresure hunt'}

participant_details = {}

def add_participant():
	name = input('enter the participant name:')
	event= input('select the event from the list:\n 1.CS \n 2.google it \n 3.treasure hunt\n')

	participant_details[name] = events_dict[event]

	return participant_details
	

def see_participant():
	for key,value in participant_details.items():
		print(key,value, sep=' - ')

if __name__ == '__main__':
	add_participant()
	print(participant_details)
	see_participant()

