import pandas as pd
import numpy as np



#city

city_df = pd.DataFrame(columns=['Name','theatres'],dtype=object)

class City:
	def __init__(self, name, theatres):
		self.name = name
		self.theatres = theatres



		city_df.loc[len(city_df),:]=[name,theatres]



#theatre

theatre_df = pd.DataFrame(columns=['Name','City','address','shows_playing'],dtype=object)


class Theatre:
	def __init__(self,name,city,address):
		self.name = name
		self.city = city
		self.address = address

		if city not in city_df['Name']:
			City(city,[name])
		elif name not in city_df.loc[city,'theatres']:
			city_df.loc[city,'theatres'].append(name)
		else:
			pass



		theatre_df.loc[len(theatre_df),['Name','City','address']]=[name,city,address]



#movie 

movie_df = pd.DataFrame(columns=['Name','Lang','theatres'],dtype=object)

class Movie:
	def __init__(self,name,lang):
		self.name = name
		self.lang = lang

		theatres=[]
		for (a,b) in theatre_df['Name','shows_playing'].iter_rows():
			if b['shows_playing']==self.name:
				theatres.append(str(b['Name']))

		self.theatres = theatres



		movie_df.loc[len(movie_df),:]=[name,lang,theatres]



#shows

shows_df = pd.DataFrame(columns=['Movie','Lang','Theatre','City','Day','Timing','Screen','Price'])

class Shows:
	def __init__(self,movie,lang,theatre,day,timing,screen,price):
		self.movie = movie
		self.lang = lang
		self.theatre = theatre
		self.city=theatre_df[theatre_df['Name']==theatre]['City']
		self.day = day
		self.timing = timing
		self.screen = screen
		self.price=price

		shows_df.loc[len(shows_df),:]=[movie,lang,theatre,city,day,timing,screen,price]




#user account

userlogin_df=pd.DataFrame(columns=['username','password','city'])

class User:
	def __init__(self,user_ID,psswd,city):
		self.user_ID=user_ID
		self.psswd=psswd
		self.city=city
		userlogin_df.loc[len(userlogin_df),:]=[user_ID,psswd,city]




#login screen

def opening_screen():
	print("BookUrShow\u00A9")
	new=input("Hi! Are u a new user?[y/n]")
	if new in ['y','yes','Y','Yes']:
		user_ID=input('UserID: ')
		psswd=input('Password: ')
		city=input("The city u live in? ")
		client = User(user_ID,psswd,city)
		print("""
Account created successfully!
Logging in.....""")
		theatre_screen(userlogin_df[userlogin_df['username']==user_ID]['city'])


	if new in ['n','no','N','No']:
		user_ID=input('UserID: ')
		psswd=input('Password: ')
		if userlogin_df[userlogin_df['username']==user_ID]['password']==psswd:
			print("Logging in.....")
			theatre_screen(userlogin_df[userlogin_df['username']==user_ID]['city'])
		else:
			print("WRONG PASSWORD!")
			opening_screen()

	else:
		exit()



#screen showing all the movies somewhat like the homescreen

def theatre_screen(city):
	print("Here are a list of all shows available in ur city")
	print(shows_df[shows_df['City']==city])



#imports the data

def load_data():
	df_temp1=pd.read_csv('data/theatres.csv',names=['Name','City','address'])
	for (a,b) in df_temp1.iter_rows():
		Theatre(b['Name'],b['City'],b['address'])

	df_temp2=pd.read_csv('data/movies.csv',names=['Name','Lang'])
	for (a,b) in df_temp2.iter_rows():
		Movie(b['Name'],b['Lang'])

	df_temp3=pd.read_csv('data/shows.csv',names=['Movie','Lang','Theatre','Day','Timing','Screen','Price'])
	for (a,b) in df_temp3.iter_rows():
		Shows(b['Movie'],b['Lang'],b['Theatre'],b['Day'],b['Timing'],b['Screen'],b['Price'])


	for (a,b) in theatre_df.iter_rows():
		theatre_name=b['Name']
		shows_playing=[]
		for (c,d) in shows_df[shows_df['Theatre']==theatre_name].iter_rows():
			movie_name=d['Movie']
			shows_playing.append(movie_name)
		theatre_df[theatre_df['Name']==theatre_name]['shows_playing']=shows_playing


	df_temp4=pd.read_csv('data/userlogins.csv',names=['username','password','city'])
	for (a,b) in df_temp4.iter_rows():
		User(b['username'],b['password'],b['city'])



#saves the data

def save_data():
	userlogin_df.to_csv('data/userlogins.csv',header=False,index=False)





opening_screen()









