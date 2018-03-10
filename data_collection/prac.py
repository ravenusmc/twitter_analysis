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


one = ['"douglassville,', 'pa"']
two = ['"chicago,', 'il"']
three = ['"murrysville,pa"']
# ['"Poinciana,', 'FL"']
# ['"Upstate', 'NY"']

print(two[1])
  
if 'il"' in two or 'Illinois"':
  print('yay')
else:
  print('nay')

if 'pa"' in three:
  print('yay')
else:
  print('nay')


