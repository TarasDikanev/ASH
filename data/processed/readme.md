# Datasets

`an_good.json`, `an_bad.json` - lists of good and bad anecdotes from anekdot.ru. Each anecdote is list of text,
date string, ratind, number of votes, number of upvotes, number of downvotes. Consider anecdote good if it is in 
top 3 of the day and its rating is more than 100. Consider bad all anecdotes with rating less than 50. 

`bash_good.json`, `bash_bad.json` - lists of good and bad jokes from bash.im. Each joke is list of text, datetime 
string, timestamp, id and rating. Each joke was compared with 100 other jokes nearest in time (+/- 50 jokes around). 
If it is in 25% best it is good, in 25% worst it is bad.

`an_good_eq.json`, `an_bad_eq.json`, `bash_good_eq.json`, `bash_bad_eq.json` - datasets with equal numbers of good 
and bad jokes. Also jokes lengths (number of tokens) distribution was equqalized. 