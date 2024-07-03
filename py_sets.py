data_science_users = [15,23,43,26]

machine_learning_users = [13,23,56,42]

#I have 2 datasets data_science_users and machine_learning_users 
#now I'm gonna combine them in another list watched = [] using the list functions
# first copy to copy the first list and then extend to extend the second list
#because I wanna send them an email notifying them a new course is available

watched = []

watched = data_science_users.copy()

watched.extend(machine_learning_users)

print(watched)

print(len(watched))

# Now I send emails to 8 people but I also get back 2 complaints because I have my list
# [15, 23, 43, 26, 13, 23, 56, 42]
# Notice I have 23 duplicate so I sent 2 emails to person 23
#so I can use the conjunto "set" function of Python to convert my list into a set

set_watched = set(watched)
print(set_watched)

#voila the result is {42, 43, 13, 15, 23, 56, 26} notice that now I don't have any duplicate in my list
#a set has many elements but not duplicate elements
#set is cool to use because it excludes the duplicates I don't wanna use
#if the order doesn't matter can use a set right away instead of a list where the order matters
#it depends on what I need to do 
#a set doesn't have indexing that means the alleatory access to a position
#the advantage of the set is that I don't have duplicates the disavantage is that I don't have an order in the like the list
# but it's possible to iterate

for user in set_watched:
    print(user)

#another example creating to sets right away and print using | "ou" that will print all the elements
#in this case python joins the 2 sets


set_data_science_users = {15,23,43,56}

set_machine_learning_users = {13,23,56,42}

print(set_data_science_users | set_machine_learning_users)

#What if now I want to notify people that took both courses how do I get that the intersection of both sets

print(set_data_science_users & set_machine_learning_users)

#the result is {56,23} that's right only 56 and 23 took both courses

#now I just want to send message to users that are in data science but are not is machine learning

print (set_data_science_users - set_machine_learning_users)

#my result is {43,15} that's right

done_dtasci_but_not_ml = set_data_science_users - set_machine_learning_users

print(15 in done_dtasci_but_not_ml)

#my result is True

print(23 in done_dtasci_but_not_ml)

#my result is False

#I could also use an exclusive "ou" ^ to get users that have done data_science or ml

print(set_data_science_users ^ set_machine_learning_users)

#result {42, 43, 13, 15} these numbers just appear in one of the sets
