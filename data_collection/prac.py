#This file will contain code that I'll test things out on. None of the code in this file will actually 
#be placed into the project. It's simply a place to test ideas. 

#This file I'll be trying to sort through strings
# tweet = """RT @AnnCoulter: No wonder Guillermo del Toro  refuses to go back to Mexico!  
# He better hope Trump builds a really big wall! https://t.co/vZ\u2026"""

# tweet_two = "RT @MadDog20470: @POTUS always has this option, https://t.co/R9BYmwBCHj"

# tweet = tweet_two.split()
# print(tweet)

# #Loop through the array looking for @ and 'https'
# count = 0
# while count < len(tweet):

#   if tweet[count][0:2]  == 'RT':
#     del tweet[count]
#   elif tweet[count][0:5] == 'https':
#     del tweet[count]
#   elif tweet[count][0] == '@':
#     del tweet[count]
#   else: 
#     count += 1

  
# # put the list back into a string 
# tweet = ' '.join(tweet)
# print(tweet)


location = "Venice, CA"
location = location.split()
print(location)

correct_size = []
count = 0
while count < len(location):
    loc = location[count].lower()
    correct_size.append(loc)
    print(count)
    count += 1
print(correct_size)


# count = 0
# print(len(location))
# while count < len(location):
#     loc = location[count].lower()
#     location.append(loc)
#     count += 1
#     print(count)
# print(location)


# one = "Alabama"
# one = one.split()
# print(one)
# print(one[0].lower())
# if one[0].lower() == 'alabam':
#   print('yay')
# else:
#   print('nay')


# for w in location:
#     w = w.lower()
#     location.append(w)
#     print(w)

