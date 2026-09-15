# Why I Chose This Dataset
I chose the Film Permits dataset because it connects film and television production to locations in New York City. The borough 
and production category columns make it possible to compare where permitted activity is recorded and what types of productions 
appear most often. It also provides a useful example of how data quality and the meaning of a row affect the questions a 
dataset can answer.

# Three Data Questions
# Question 1: How many permit records are listed in Manhattan?
# Output: 9706
# Why the data structure supports this question:
This works because the dataset is tabular: each row is one permit record, and the Borough column stores a location label. 
Counting the rows where that column equals "Manhattan" gives the total number of Manhattan permit records.

# Question 2: How many Television vs Film permit records are there?
# Output: Television: 7894 Film: 2793
# Why the data structure supports this question:
This works because Category is a single column that labels the production type for each permit record. Filtering for 
"Television" and "Film" and counting the frequency of each category summarizes how many records fall into each group.

# Question 3: How many Television permit records are listed in Manhattan?
# Output: 3121
# Why the data structure supports this question:
This works because each row contains both the production category and the borough, so we can examine those details together. 
Counting records that have Television as their category and Manhattan as their borough tells us how many permits meet both conditions.

# What the Data Cannot Answer
A question I would like to answer is: “Which borough earned the most money from the productions represented in these permits?” 
The CSV has no production budgets, local spending, wages, or revenue, and it does not provide a production title or a shared 
production identifier that would let me reliably link multiple permits to the same project. It would be misleading to assume 
that every permit represents a different production, that all permitted activities actually happened, or that each permit 
generated the same amount of money. A borough with more permit records therefore cannot automatically be described as earning 
more money from production activity.
