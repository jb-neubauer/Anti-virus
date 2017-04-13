from sys import argv

#These are the arguments and allows for prompting
script, user_name = argv
prompt = '-> '

#This is the main code that asks the questions below and prompts for an answer
print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s? " % user_name 
lives = raw_input(prompt)

print "What kind of computer do you have?" 
computer = raw_input(prompt)

#Reiterates what the answers were
print """
Alright, so you said %r about liking me.
You live in %r. Not quite sure where that is.
And that you have a %r computer.  Nice.
""" % (likes, lives, computer)
