import pandas as pd
import numpy as np
from random import randint

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.width = None

# backend(framework)


def val(a):
	return a.item()

#city

city_df = pd.DataFrame(columns=['Name'])

class City:
	def __init__(self, name):
		self.name = name


		city_df.loc[len(city_df),:]=[name]


#theatre

theatre_df = pd.DataFrame(columns=['Name','City','address'])

class Theatre:
	def __init__(self,name,city,address):
		self.name = name
		self.city = city
		self.address = address

		if city not in city_df['Name']:
			City(city)
		else:
			pass



		theatre_df.loc[len(theatre_df),['Name','City','address']]=[name,city,address]


#movie 

movie_df = pd.DataFrame(columns=['Name','Lang'])

class Movie:
	def __init__(self,name,lang):
		self.name = name
		self.lang = lang

		movie_df.loc[len(movie_df),:]=[name,lang]


#shows

shows_df = pd.DataFrame(columns=['Movie','Lang','Theatre','City','Day','Timing','Screen','Silver','Gold','Premium'])

class Shows:
	def __init__(self,movie,lang,theatre,day,timing,screen,priceS,priceG,priceP):
		self.movie = movie
		self.lang = lang
		self.theatre = theatre
		try:
			city = list(theatre_df[(theatre_df['Name'] == theatre)]['City'].values)[0]
		except:
			city='dummy'
		#self.city=city
		self.day = day
		self.timing = timing
		self.screen = screen
		self.priceS=priceS
		self.priceG=priceG
		self.priceP=priceP
		shows_df.loc[len(shows_df),:]=[movie,lang,theatre,city,day,timing,screen,priceS,priceG,priceP]



#user account

userlogin_df=pd.DataFrame(columns=['username','password','city'])

class User:
	def __init__(self,user_ID,psswd,city):
		self.user_ID=user_ID
		self.psswd=psswd
		self.city=city
		userlogin_df.loc[len(userlogin_df),:]=[user_ID,psswd,city]




#front end functions


#login screen




def opening_screen():
	print("BookUrShow\u00A9",end='\n\n')
	city = ''
	while city == '':

		new=input("Hi! Are u a new user?[y/n]")
		if new in ['y','yes','Y','Yes']:
			user_ID=input('UserID: ')
			psswd=input('Password: ')
			city=input("The city u live in? ")
			User(user_ID,psswd,city)
			print("""
	Account created successfully!
	Logging in.....""",end='\n\n')


		if new in ['n','no','N','No']:
			user_ID=input('UserID: ')
			psswd=input('Password: ')
			try:
				pass_try=val(userlogin_df[(userlogin_df['username']==user_ID)]['password'])
			except:
				pass_try=''
			if pass_try==psswd:
				print("Logging in.....",end='\n\n')
				print(city)
				city = val(userlogin_df[(userlogin_df['username']==user_ID)]['city'])
				print(city)
			else:
				print("WRONG PASSWORD!",end='\n\n')

		else:
			pass

	return city



#functions displaying dataframes

def movie_screen(city):
	print("Here are a list of all shows available in ur city",end='\n\n')
	print(pd.Series((shows_df[(shows_df['City']==city)]['Movie']).unique()).to_string(),end='\n\n')

def movie_booking_screen(city,movie):
	print(movie,end='\n\n')
	shows_df_city=shows_df[(shows_df['City'] == city)]
	shows_df_city_movie=shows_df_city[(shows_df_city['Movie']==movie)]
	print(shows_df_city_movie,end='\n\n')
	return shows_df_city_movie

def theatre_screen(city):
	print("Here are a list of all theatres available in ur city",end='\n\n')
	print(theatre_df[(theatre_df['City']==city)],end='\n\n')


def theatre_booking_screen(city,theatre):
	print(theatre,end='\n\n')
	shows_df_city=shows_df[(shows_df['City']==city)]
	shows_df_city_theatre=shows_df_city[(shows_df_city['Theatre']==theatre)]
	print(shows_df_city_theatre,end='\n\n')
	return shows_df_city_theatre


def booking_screen(dataframe,showID,type_,number):
	showID=int(showID)
	movie=dataframe.loc[showID,'Movie']
	lang=dataframe.loc[showID,'Lang']
	theatre=dataframe.loc[showID,'Theatre']
	theatre_address=list((theatre_df[(theatre_df['Name']==theatre)]['address']).values)[0]
	city=dataframe.loc[showID,'City']
	day=dataframe.loc[showID,'Day']
	timing=dataframe.loc[showID,'Timing']
	screen=dataframe.loc[showID,'Screen']
	if type_ == 's':
		_type_='Silver'
	elif type_ == 'g':
		_type_='Gold'
	elif type_ == 'p':
		_type_='Premium'
	else:
		raise Exception("The command doesn'nt seem right")

	rate=int(dataframe.loc[showID,_type_])
	total=int(dataframe.loc[showID,_type_])*int(number)

	details=[movie,lang,theatre,theatre_address,city,day,timing,screen,_type_,rate,number,total]


	details_series=pd.Series(details,index=["Movie","Lang","Theatre","Theatre address","City","Day","Timing","Screen","Class","Price per Ticket","Number of seats","Amount payable"])

	print("""Your Ticket has been successfully booked! 
Find the details below - """,end='\n\n')

	print(details_series.to_string(),end='\n\n')

	return details





def prompt():
	x=input('>>>>')
	return x

def help():
	print('''

commands:
help (to display this screen)
movie (to display all the movies in ur city
movie -[movie name] (to see all the available shows)
book -[show id] -[s/g/p] -[number of tickets] (to book tickets from the movie database)
theatre (to display all the theatres in ur city
theatre -[theatre name] (to see all the available shows)
book -[show id] -[s/g/p] -[number of tickets] (to book tickets from the movie database)
exit (to exit this appliacation)

''',end='\n\n')




#imports the data

def load_data():
	df_temp1=pd.read_csv('data/theatres.csv',names=['Name','City','address'])
	for (a,b) in df_temp1.iterrows():
		Theatre(b['Name'],b['City'],b['address'])


	df_temp3=pd.read_csv('data/shows.csv',names=['Movie','Lang','Theatre','Day','Timing','Screen','Silver','Gold','Premium'])
	for (a,b) in df_temp3.iterrows():
		Shows(b['Movie'],b['Lang'],b['Theatre'],b['Day'],b['Timing'],f'Screen-{randint(1,10)}',b['Silver'],b['Gold'],b['Premium'])


	# for (a,b) in theatre_df.iterrows():
	# 	theatre_name=b['Name']
	# 	shows_playing=[]
	# 	for (c,d) in shows_df[shows_df['Theatre']==theatre_name].iterrows():
	# 		movie_name=d['Movie']
	# 		shows_playing.append(movie_name)
	# 	theatre_df[theatre_df['Name']==theatre_name]['shows_playing']=shows_playing


	df_temp2=pd.read_csv('data/movies.csv',names=['Name','Lang'])
	for (a,b) in df_temp2.iterrows():
		Movie(b['Name'],b['Lang'])

	df_temp4=pd.read_csv('data/user_logins.csv',names=['username','password','city'])
	for (a,b) in df_temp4.iterrows():
		User(b['username'],b['password'],b['city'])



#saves the data

def save_data():
	userlogin_df.to_csv('data/user_logins.csv',header=False,index=False)




def loop():
	load_data()
	
	user_city=opening_screen()
	
	help()

	command=['']

	while command != 'exit':
		command = prompt().split(' -')

		
		if command[0]=='movie':
			if len(command)==1:
				movie_screen(user_city)
			elif len(command)==2:
				try:
					x=movie_booking_screen(user_city,command[1])
					print("book -[show id] -[s/g/p] -[number of tickets] (to book tickets from the movie database)",end='\n\n')
				except:
					help()
			else:
				pass


		if command[0]=='theatre':
			if len(command)==1:
				theatre_screen(user_city)
			elif len(command)==2:
				try:
					x=theatre_booking_screen(user_city,command[1])
					print("book -[show id] -[s/g/p] -[number of tickets] (to book tickets from the theatre database)",end='\n\n')
				except:
					help()
			else:
				pass


		elif command[0]=='book':
			if len(command)==4:
				try:
					y=booking_screen(x,command[1],command[2],command[3])
				except:
					print("sry, there was an error",end='\n\n')
					help()
			
		elif command[0]=='help':
			help()
		elif command[0]=='exit':
			save_data()
			break
		else:
			pass

print()
loop()


