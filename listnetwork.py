""" 
A script to generate a basic network representation of users in a list

"""
import tweepy
import pandas as pd
import json

# Connect to Twitter API

auth = tweepy.OAuthHandler("pHtcl4ztpyy2FLH19LalgP9Ln", "Ju3XLIB8C7jK3ICvPasgDfphgrsPHjq6OyPz6v4dP30I1INjcn" )
auth.set_access_token("365249100-SNdXVVx71LoT4PDYwEjpVLUvFtjwNkWR31JSe3IJ", "K9eIHlKI7G3NaUaMndbwNZMwZdSJJVO86WtUNSDw7l1Fq")
api = tweepy.API(auth)


#Store members of crytogurus list as a ResultSet Object

cryptogurus = api.list_members(screen_name='@shingaithornton', slug = 'cryptogurus', owner_screen_name='@shingaithornton', count = 100)


#Store each user in list, print names
cryptogurus_list = []

for i in range(len(cryptogurus)):
    cryptogurus_list.append(cryptogurus[i].name)
    print (cryptogurus[i].name)


#Loop through list to determine which users are following each other (API limit issues? Need to start with small list, or persist data to avoid limits?)

checkfriends = api.show_friendship(source_screen_name ='user_1',target_screen_name='user_2')


#Create network with each user as a node


#Create edges between users who are following each other
