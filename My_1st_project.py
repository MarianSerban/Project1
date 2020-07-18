
#find out name

name = input("What is your name?: ").strip()

#find out city

city = input("What city are you living? ").strip()

#find out age

age = input("How old are you?: ")

#find out how many years untill 65

age = int(age)
retirement_age = 65
years_to_retirement = retirement_age - age


#find out email

email = input("What is your email address?: ").strip()

#slice email and extract domain

domain = email[email.index("@")+1:email.index(".com")]

#output message

output = """Hello {}, how are you today?

I'm glad to hear that you are living in {}, a beautiful place with amazing people.

In regards to your retirement account, you have {} years left and we encourage you to continue saving so that you can enjoy your well deserved benefits.

We would like to thank you for using a {} address and we hope you are enjoying using their services.""".format(name.capitalize(),city.capitalize(),years_to_retirement,domain.capitalize())

#dispay message

print(output)
