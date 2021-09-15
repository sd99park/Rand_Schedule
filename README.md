# Scheduler

Over the summer of 2020, I was a lifeguard, at my job the manager who created the 
schedule never did a very good job at it. She would schedule her favorites for 50-60 
hours a week, while everyone else got stuck with 20 hour weeks. This drove me crazy 
and so I decided to build a scheduling program that took in names of employees, and 
days that they had asked off, to turn it into an even, randomized schedule where no 
one drew the short straw due to bias.

It was written in python and takes a .txt file as the input. Currently the program 
is still under development but the logic behind everything has been finished. the 
output of this program is still in the terminal, but I have plans to add a front 
end with Django to make this more user friendly.

# How the algorithm works

I created this to be randomized, and not nessesarily efficient. It begins by randomly 
assigning people to work each day, this has no consideration for making a even schedule 
yet. Once people have been assigned to each shift, it then compares the person working 
the most to the person working the least. It then gives a random shift of the person 
working the most, to the person works the least. It then repeats this comparison until 
the person with the most shifts has most less more than 2 shifts then the person with 
the least shifts. The number 2 can be adjusted, it works best for the number of 
employees used at my lifeguarding job (roughly 40), but might need to be raised if the 
number of people increased. To keep days off from causing a problem when we compare and
balance the total number of shifts per employee we consider a day off the same as having 
a shift.

# Todo List

-Create a React front end

-Fix bugs as they are found

-Create an API using this
