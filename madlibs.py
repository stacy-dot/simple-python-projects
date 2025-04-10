print("Let's create a fun story.Answer the questions below!")
name=input("Enter a name")
place=input("Enter a place")
animal=input("enter an animal")
verb=input("enter a verb")
fav_food=input("enter your favorite food")

print("\n Here's your story\n")
story= f"One day {name},went to {place},with a pet{animal}." \
       f"They decided to {verb} all the way to the food court, " \
       f"where they found a huge plate of {fav_food}. It was the best day ever!"
print(story)