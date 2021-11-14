def getTaxesInCents(amount:float, tax:float):
  '''
      Function to get the amount of taxes of the given amount (amount) and given percentage (tax) - PYTHON
  '''
  # check arguments to be numbers
  if (type(amount) == int or type(amount) == float) and (type(tax) == int or type(tax) == float):
    #return corresponding taxes in cents and tax percentage
    return [amount*tax,tax]

print(getTaxesInCents(100,10))


from random import randint

def shuffleCards(cards_list):
  '''
      Function to shuffle the given cards
  '''
  a=[]
  while len(a)<len(cards_list):
    random_card = cards_list[randint(0,len(cards_list)-1)]
    if random_card not in a:
      a.append(random_card)
  
  return a



print(shuffleCards(['A',1,2,3,4,5,6,7,8,9,10,'J','K','Q']))


def countVowelsValue(phrase):
  vowels_arr=['a','e','i','o','u']
  counter=0
  
  #Change phrase to lowercase
  phrase=phrase.lower()
  
  #create a list with vowels found in phrase
  phrase_vowels = [i for i in phrase if i in vowels_arr]
  
  #add to counter each vowel's value from vowels list and return result
  for vowel in phrase_vowels:
    counter += vowels_arr.index(vowel)+1
  return counter

# def countVowelsValueRecursive(phrase):
#   vowels_arr=['a','e','i','o','u']
#   counter=0
  
#   #Change phrase to lowercase
#   phrase=phrase.lower()
  
#   #create a list with vowels found in phrase
#   # counter += [vowels_arr.index(i)+1 for i in phrase if i in vowels_arr]
#   for i in phrase:
#     if i in vowels_arr:
#       counter += vowels_arr.index(i)+1
  
#   return counter

def countVowelsValueRecursive(phrase):
  vowels_arr=['a','e','i','o','u']
  
  phrase=phrase.lower()
  if len(phrase) > 1:
    if phrase[0] in vowels_arr:
      
      return countVowelsValueRecursive(phrase[1:]) + vowels_arr.index(phrase[0])+1 
    else:
      return countVowelsValueRecursive(phrase[1:])
    
  else:
    if phrase[0] in vowels_arr:
      return vowels_arr.index(phrase[0])+1
    else:
      return 0
  

print(countVowelsValueRecursive('aeiou'))    
  