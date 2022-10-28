import pandas as pd
import numpy as np


# def create_city_df():
# 	city_df=pd.DataFrame(columns=['Name','State','No. of Theatres','Theatres'])
# 	city_df.to_csv("data\city_df.csv")



#city

city_df = pd.DataFrame(columns=['Name','State','no_of_theatres','theatres'])

class City:
	def __innit__(self, name, state, no_of_theatres, theatres):
		self.name = name
		self.state = state
		self.ntheatres = no_of_theatres
		self.theatres = theatres
		city_df.iloc[len(city_df),:]=[self.name,self.state,self.ntheatres,self.theatres]



#theatre

class Theatre:
	def __innit__(self,name,city,address,shows_playing):
		self.name = name
		self.city = city
		self.address = address
		self.shows_playing = shows_playing

	# def register(self):
	# 	theatre_df[len(theatre_df)]=[self.name,self.city,self.address,self.shows_playing]



#movie 

class Movie:
	def __innit__(self,name,lang,theatres):
		self.name = name
		self.lang = lang

		theatres=[]
		for (a,b) in theatre_df['Name','Shows'].iter_rows():
			if b['Shows']==self.name:
				theatres.append(str(b['Name']))

		self.theatres = theatres

	# def register(self):
	# 	movies_df[len(movies_df)]=[self.name,self.lang,self.theatres]



#user account

IDs={}
class User:
	def __innit__(self,user_ID,psswd,city):
		self.user_ID=user_ID
		self.psswd=psswd
		self.city=city
		IDs[user_ID]=psswd










def opening_screen():
	print("BookUrShow\u00A9")
	new=input("Hi! Are u a new user?[y/n]")
	if new in ['y','yes','Y','Yes']:
		user_ID=input('UserID: ')
		psswd=input('Password: ')
		city=input("The city u live in? ")
		client = User(user_ID,psswd,city)

	if new in ['n','no','N','No']:
		user_ID=input('UserID: ')
		psswd=input('Password: ')
		if IDs[user_ID]==psswd:
			theatre_screen()
		else:
			print("WRONG PASSWORD!")
			opening_screen()

	else:
		exit()



def theatre_screen():
	print("Here are a list of all shows available in ur city")
	print()














