color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
person = input("Enter a person's name: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + person)



year = input("Enter a year (first/second/etc): ")
adjective = input("Enter an adjective: ")
fav_subject = input("Enter your favorite subject: ")
hate_subject = input("Enter a subject you hate: ")

print(f"\nIn my {year} year of college, I was a very {adjective} student.")
print(f"My favorite subject was {fav_subject} and I hated {hate_subject}.")


name = input("Enter a name: ")
emotion = input("Enter an emotion: ")
place = input("Enter a place: ")
verb = input("Enter a verb ending with -ing: ")

story = f"""
One day, {name} was feeling very {emotion}.
Suddenly, {name} found themselves in {place}.
Without thinking, they started {verb}.
It was the strangest day ever!
"""

print(story)
