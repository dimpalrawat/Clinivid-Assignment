import re as re;
import json;


string = 'profile|73241232|<Aamir><Hussain><Khan>|<Mumbai><<72.872075><19.075606>>|73241232.jpg**followers|54543342|<Anil><><Kapoor>|<Delhi><<23.23><12.07>>|54543342.jpg@@|12311334|<Amit><><Bansal>|<Bangalore><<><>>|12311334.jpg';
profile_fields = ['id', 'name', 'location', 'imageId', 'followers']
profile  = {};

items = string.split('**')

user_profile = items[0].replace('profile', '').split('|');
user_profile.pop(0)

i = 0 

location_keys = {'name':'', 'coords': {'long':'','lat':''} }
name_keys = {'first':'' , 'middle':'' , 'last':''}

for item in user_profile:
	if(i==2):
		profile[profile_fields[i]] = re.findall(r'<(.+?)>', item)
		j=0
		for val in re.findall(r'<([^>]*)>', item):
			if(j==0):
				location_keys['name'] = val.replace("<", "").replace(">","");
			elif(j==1):
				location_keys['coords']['long'] = val.replace("<", "").replace(">","");				
			else:
				location_keys['coords']['lat'] = val.replace("<", "").replace(">","");	
			j = j + 1

 		profile[profile_fields[i]] = location_keys
		# print profile[profile_fields[i]]

	elif(i==1):
		j=0
		for val in re.findall(r'<([^>]*)>', item):
			if(j==0):
				name_keys['first'] = val.replace("<", "").replace(">","");
			elif(j==1):
				name_keys['middle'] = val.replace("<", "").replace(">","");			
			else:
				name_keys['last'] = val.replace("<", "").replace(">","");
			j=j+1
		profile[profile_fields[i]] = name_keys
	else:
		profile[profile_fields[i]] = item
	i = i + 1
# print profile

followers = items[1].replace('followers', '').split('@@'); 
user_followers = []

followers_fields = ['id', 'name', 'location', 'imageId', 'followers']

for items in followers:
	follow_profile = {}

	follower = items.split('|');
	follower.pop(0)
	i=0
	for item in follower:
		if(i==2):
			j=0
			flwr_location_keys = dict()
			for val in re.findall(r'<([^>]*)>', item):
				if(j==0):
					flwr_location_keys['name'] = val.replace("<", "").replace(">","");
					flwr_location_keys['coords'] = {}
				elif(j==1):
					flwr_location_keys['coords']['long'] = val.replace("<", "").replace(">","");			
				else:
					flwr_location_keys['coords']['lat'] = val.replace("<", "").replace(">","");
				j = j + 1

	 		follow_profile[followers_fields[i]] = flwr_location_keys

		elif(i==1):
			j=0
			flwr_name_keys = dict()
			for val in re.findall(r'<([^>]*)>', item):
				if(j==0):
					flwr_name_keys['first'] = val.replace("<", "").replace(">","");
				elif(j==1):
					flwr_name_keys['middle'] = val.replace("<", "").replace(">","");		
				else:
					flwr_name_keys['last'] = val.replace("<", "").replace(">","");
				
				j=j+1
			follow_profile[followers_fields[i]] = flwr_name_keys

		else:
			follow_profile[followers_fields[i]] = item

		i = i + 1

	# print follow_profile
	user_followers.append(follow_profile)
# print user_followers;
profile[profile_fields[i]] = user_followers;

print json.dumps(profile, sort_keys=True, indent=2, separators=(',', ': '));