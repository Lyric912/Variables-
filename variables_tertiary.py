# author: <Lyric>
# date: <July 2, 2021>
#
# description: <fill in>

# Choose a song that you enjoy listening to. For this song you should pull up the lyrics.
# I suggest using Genius since it breaks down the song's structure into its individual parts.

# --------------- Section 3 --------------- #

# 3.1
# Variables
#   1) Create a variable to represent each part of the song. By parts, I mean the verses, chorus, bridges, etc. Each
#   part should exist as a string. You may need to use string combination to combine longer verses and choruses.
#
#   Use the newline or \n escape character at the end of every line.
#
# Hint: When combining long strings, it may be nicer to utilize individual lines for each line in a verse or chorus.
# See below for an example. Surround the combination with a (), and then hit enter when the cursor is in between. It
# should make the form you see below of:
#
# variable = (
#    'lyrics go here'
# )
#
# Anything between these () are included in the operation.

example_verse = (
    'round your city, round the clock\n' +
    'everybody needs you\n' +
    'no, you can\'t make everybody equal\n'
)
# The song I chose is Here by Alessia Cara
# WRITE CODE BELOW
intro = (
    'I guess right now you\'ve got the last laugh'
)
verse_1 = (
     ' I\'m sorry if I seem uninterested' 
     ' Or I\'m not listening or I\'m indifferent'
     ' Truly I ain\'t got no business here'
     ' But since my friends are here, I just came to kick it'
     ' But really I would rather be at home all by myself'
     ' Not in this room'
     ' With people who don\'t even care about my well-being'
     ' I don\'t dance, don\'t ask, I don\'t need a boyfriend'
     ' So you can go back, please enjoy your party' 
     ' I\'ll be here'
     ' Somewhere in the corner under clouds of marijuana'
     ' With this boy who\'s hollering I can hardy hear'
     ' Over this music I don\'t listen to'
     ' And I don\'t wanna get with you'
     ' So tell my friends that I\'ll be over here'
 )

chorus = (
    ' Oh-oh-oh here, oh-oh-oh here'
    ' Oh-oh-oh here, oh-oh-oh here'
    ' And I can\'t wait \'til we can break up out of here'
)

verse_2 = (
    ' Excuse me if I seem a little unimpressed with this'
    ' An anti-social pessimist, but usually I don]\'t mess with this'
    ' And I know you mean only the best'
    '  But honestly I\'d rather be'
    ' Somewhere with my people'
    ' We can kick and just listen to'
    ' Some music with a message, like we usually do'
    ' And we\'ll discuss our big dreams'
    ' How we plan to take over the planet'
    ' So pardon my manners'
    ' I hope you\'ll understand that I\'ll be here'
    ' Not there in the kitchen'
    ' With the girl who\'s always gossiping about her friends'
    ' So tell them I\'ll be here'
    ' Right next to the boy who\'s throwing up'
    '  Cause he can\'t take what\'s in his cup no more'
    ' Oh God, why am I here?'
)

chorus = (
    ' Oh-oh-oh here, oh-oh-oh here'
    ' Oh I ask myself, what am I doin\' here?'
    ' Oh-oh-oh here, oh-oh-oh here'
    ' And I can\'t wait \'til we can break up out of here'
)

bridge = (
    ' Hours later congregating next to the refrigerator'
    ' Some girl\'s talking \'bout her haters, she ain\'t got none'
    ' How did it ever come to this? I should\'ve never come to this'
' So holla at me, I\'ll be in the car when you\'re done'
' I\'m stand-offish, don\'t want what you\'re offerin\''
' And I\'m done talking, awfully sad it had to be that way'
' So tell my people when they\'re ready that I\'m ready'
' And I\'m standing by the TV with my beanie low'
' Yo, I\'ll be over here'
)
chorus = (
    ' Oh-oh-oh here, oh-oh-oh here'
    ' Oh I ask myself, what am I doin\' here?'
    ' Oh-oh-oh here, oh-oh-oh here'
    ' And I can\'t wait \'til we can break up out of here'
)
# 3.2
# Print
#   1) Print the variables out so that they form the song in correct order when outputted to the terminal.
#   2) Insert blank print statements so that there is a blank line in between different verses / choruses.
#
#   Remember you can re-use variables (like the chorus) if it's the same.
#
# WRITE CODE BELOW
print(intro)
print()
print(verse_1)
print()
print(chorus)
print()
print(verse_2)
print()
print(chorus)
print()
print(bridge)
print()
print(chorus)
