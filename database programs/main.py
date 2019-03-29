from models import * # * indicates all 

def add_events():
	event_name = input("enter the name of the event you want to add: ")

	EventsList.create(event_name=event_name)

def see_events():
	events =EventsList.select()
	for event in events:
		print(event.id, event.event_name, sep=" - ")

def add_participants():
	participant_name = input("enter the name of the participants: ")
	events =EventsList.select()
	for event in events:
		print(event.id, event.event_name, sep=" - ")
		event_id = int(input("select the event in which the participant wants to participate in: \n"))

		ParticipantList.create(participant_name =participant_name, event_name=event_id)

def see_participants():
	for participant in ParticipantList.select():
		#print(EventsList.get(participant.event_name_id))
		print(participant.id, participant_name, EventsList.get(participant.event_name_id).event_name, sep=" - ")


while True:
	choice = input("enter the action that you want do: \n 1.Add event\n 2. see_events \n 3.Add participants \n 4.See participants \n 5.Exit")

	if choice==1:
		add_events()
	elif choice==2:
		see_events()
	elif chioce==3:
		add_participants()
	elif chioce==4:
		see_participants()
	else:
		break
