# import turtles
import turtle as trtl
import random

#intro to weather calculator
print("Welcome to the weather calculator. Type your temperature in Fahrenheit to see possible weather conditions, what to wear, and more.")
print(" ")
#type in temperature
tempInput = int(input())

# image declaration
ac_image = "ac.gif"
drinks_image = "drinks.gif"
beach_image = "beach.gif"
soccer_image = "soccer.gif"
jogging_image = "jogging.gif"
fireplace_image = "fireplace.gif"
rain_image = "rain.gif"
tv_image = "tv.gif"
warmdrink_image = "warmdrink.gif"

# turtle declaration
wn = trtl.Screen()
wn.addshape(ac_image)
acImg = trtl.Turtle()

acImg.penup()
acImg.goto(-100,100)

wn.addshape(drinks_image)
drinkImg = trtl.Turtle()

drinkImg.penup()
drinkImg.goto(100,-100)

wn.addshape(beach_image)
beachImg = trtl.Turtle()

beachImg.penup()
beachImg.goto(-100,100)

wn.addshape(soccer_image)
soccerImg = trtl.Turtle()

soccerImg.penup()
soccerImg.goto(-100,80)

wn.addshape(jogging_image)
jogImg = trtl.Turtle()

jogImg.penup()
jogImg.goto(100,-100)

wn.addshape(fireplace_image)
fireImg = trtl.Turtle()

fireImg.penup()
fireImg.goto(100,-100)

wn.addshape(warmdrink_image)
warmImg = trtl.Turtle()

warmImg.penup()
warmImg.goto(-100,100)

wn.addshape(tv_image)
tvImg = trtl.Turtle()

tvImg.penup()
tvImg.goto(100,-100)

wn.addshape(rain_image)
rainImg = trtl.Turtle()
rainImg.penup()
rainImg.goto(-100,100)




#list of suggestion to deal with temperature
hotTempList = ["Get out of the oven","Blast your AC","Get a cold drink"]
warmTempList = ["Go somewhere relaxing","Get a cool drink","Wear shorts, t-shirt, sunscreen, and sunglasses"]
coolTempList = ["Wear a jacket","Play some sports","Do some jogging"]
rainTempList = ["Get an umbrella if you're going outside","Stay at home", "Make a cold drink and watch TV"]
coldTempList = ["Go to somewhere warm","Turn on a heater","Wrap yourself in a blanket","Make a warm drink"]

#list of suggestion
suggestionList = ["A. Better Visuals", "B. Better Advices","C. More User Friendly"]

factList = ["Raindrops are shaped more like hamburger buns. As a rain drop falls, it becomes less spherical in shape and becomes more flattened on the bottom like a hamburger bun","The Sun is almost a perfect sphere.","Fridges in Antarctica warm food.","Weather patterns can be disturbed by destructive volcanic eruption.","You can tell the temperature by counting a cricket's chirps!"]


#functions to call list elements
def hotTemp():
  for hotTempSuggestion in hotTempList:
    print(hotTempSuggestion)
    acImg.shape(ac_image)
    drinkImg.shape(drinks_image)
    


def warmTemp():
  for warmTempSuggestion in warmTempList:
    print(warmTempSuggestion)
    beachImg.shape(beach_image)
    drinkImg.shape(drinks_image)
    
    
def coolTemp():
  for coolTempSuggestion in coolTempList:
    print(coolTempSuggestion)
    soccerImg.shape(soccer_image)
    jogImg.shape(jogging_image)
    
def rainTemp():
  for rainTempSuggestion in rainTempList:
    print(rainTempSuggestion)
    rainImg.shape(rain_image)
    tvImg.shape(tv_image)
    
    
def coldTemp():
  for coldTempSuggestion in coldTempList:
    print(coldTempSuggestion)
    warmImg.shape(warmdrink_image)
    fireImg.shape(fireplace_image)
    
    
def printSuggestion():
  print("Oh no! What can we do to improve? Answer with Uppercase Letters")
  for suggestion in suggestionList:
    print(suggestion)
  print("")
  suggestion = input()
  print("Sorry. I'll do better next time.")

def askForSuggestion():
  print(" ")
  print("Is the suggestion helpful? Yes or No only.")
  helpful = input()
  if helpful == "Yes":
    print("Thanks. Have a good day.")
  elif helpful == "No":
    printSuggestion()

def showFact():
  print("")
  print("Fun Fact: " + random.choice(factList))
  
#display output bases on temperature input
if tempInput >= 90:
  print("ALSO 33 DEGREES CELSIUS. YOU GOTTA CHILL DOWN DO NOT SIT IN AN OVEN OR SOMETHING. YOU SHOULD:")
  hotTemp()
  showFact()
  askForSuggestion()
    
elif tempInput >= 60 and tempInput < 90:
  print("Between 16 degrees Celsius to 33 degrees celsius. It’s sunny outside. This is like summer weather! You should: ")
  warmTemp()
  showFact()
  askForSuggestion()
  
    
elif tempInput >= 40 and tempInput < 60:
  isRaining = input(" Is it raining on your side? Yes or No only (case sensitive) ")
  if isRaining == "No":
    print("Between 4 degrees Celsius to 16 degrees Celsius. It’s cool outside. Go outside! Have some fun with the weather!")
    coolTemp()
    showFact()
    askForSuggestion()
  if isRaining == "Yes":
    print("Between 4 degrees Celsius to 16 degrees Celsius. You must be getting poured on the head or something... Get inside.")
    rainTemp()
    showFact()
    askForSuggestion()

elif tempInput < 40:
  print("Below 4 degrees Celsius. Get inside warm. You must be in Antarctica or something.")
  coldTemp()
  showFact()
  askForSuggestion()
#elif tempInput

wn.listen()
wn.mainloop()