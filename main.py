import pandas as pd
import numpy as np


# def create_city_df():
# 	city_df=pd.DataFrame(columns=['Name','State','No. of Theatres','Theatres'])
# 	city_df.to_csv("data\city_df.csv")



#city

city_df = pd.DataFrame(columns=['Name','theatres'])
city_ID={}

class City:
	def __innit__(self, name, theatres):
		self.name = name
		self.theatres = theatres

		city_ID[name]=len(city_df)

		city_df.loc[len(city_df),:]=[name,theatres]



#theatre

theatre_df = pd.DataFrame(columns=['Name','City','address','shows_playing'])
theatre_ID={}

class Theatre:
	def __innit__(self,name,city,address,shows_playing):
		self.name = name
		self.city = city
		self.address = address
		self.shows_playing = shows_playing
		if city not in city_df['Name']:
			City(city,[name])
		else:
			city_df.loc[city,'theatres'].append(name)

		theatre_ID[name]=len(theatre_df)

		theatre_df.loc[len(theatre_df),:]=[name,city,address,shows_playing]



#movie 

movie_df = pd.DataFrame(columns=['Name','Lang','theatres'])
movie_ID={}

class Movie:
	def __innit__(self,name,lang):
		self.name = name
		self.lang = lang

		theatres=[]
		for (a,b) in theatre_df['Name','shows_playing'].iter_rows():
			if b['Shows']==self.name:
				theatres.append(str(b['Name']))

		self.theatres = theatres

		movie_ID[name]=len(movie_df)

		movie_df.loc[len(movie_df),:]=[name,lang,theatres]





#user account

IDs={}
user_cities={}
class User:
	def __innit__(self,user_ID,psswd,city):
		self.user_ID=user_ID
		self.psswd=psswd
		self.city=city
		IDs[user_ID]=psswd
		user_cities[user_ID]=city



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
		theatre_screen(user_cities[user_ID])


	if new in ['n','no','N','No']:
		user_ID=input('UserID: ')
		psswd=input('Password: ')
		print("Logging in.....")
		if IDs[user_ID]==psswd:
			theatre_screen(user_cities[user_ID])
		else:
			print("WRONG PASSWORD!")
			opening_screen()

	else:
		exit()



#screen showing all the movies somewhat like the homescreen
def theatre_screen(city):
	print("Here are a list of all shows available in ur city")
	movies_this_city=pd.DataFrame(columns=['Shows'])
	
	theatres = city_df.loc[city_ID[city],'theatres']
	for theatre in theatres:
		movies = theatre_df[theatre_ID[theatre],'shows_playing']
		for movie in movies:
			movies_this_city.loc[len(movies_this_city),:]=movie

	print(movies_this_city)





		














