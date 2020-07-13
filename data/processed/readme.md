# Datasets

`an_ru{0-2}.json` - lists of good and bad anecdotes from anekdot.ru. Each anecdote is list of text,
date string, ratind, number of votes, number of upvotes, number of downvotes and class (good ~ 1, bad ~ 0).
Anecdote is supposed to be good if it is in top 3 of the day and its rating is more than 100. All anecdotes 
with rating less than 50 supposed to be bad. Bad anecdotes are divided into 3 files to keep each file size 
less than 50 Mb.

`bash_jokes.json` - lists of good and bad jokes from bash.im. Each joke is list of text, datetime 
string, timestamp, id, rating and class (good ~ 1, bad ~ 0). Each joke was compared with 100 other 
jokes nearest in time (+/- 50 jokes around). If it is in 25% best it is good, in 25% worst it is bad.

`an_jokes_eq.json`, `bash_jokes_eq.json` - datasets with equal numbers of good 
and bad jokes. Also jokes lengths (number of tokens) distribution was equqalized. 