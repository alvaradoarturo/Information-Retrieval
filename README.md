# CS172 - Assignment 2 (Retrieval)

## Team member 1 - Arturo Alvarado

Language Used: Python 3.9.4

### Instructions To Run Program
`Git clone repository into local directory.`

`If you're using a MAC, you can input commands by simply using "././VSP.py query_list.txt results.txt {docno #} {queryID}".`

`If you're using a Windows, you can input commands by simply using "python3 ./VSP.py query_list.txt results.txt {docno #} {queryID}".`

### Brief Overview of Design
I have implemented a retrieval that outputs the cosine similarity between a document number(docno) and a query ID. My design is based on the 
indexing that was done in the previous assignment. When given the query ID, I first search the provided query list for the specific ID. Once found, 
I can then begin extracting the specific query that is associated with the ID as opposed to the entire list. This query is then normalized
by removing punctuation, converting to lower case, and finally converting the sentence into a list which has each word as a element entry in the list.

Given a specific docno, the same normaliztion techniques were applied. 

Two new vectors were created with the size of the query after being normalized. I then procedded to find the binary weights of the document test by 
seeing whether or not, the specific document element was inside the query array. If a term was found in both, then a 1 was given for the binary weights. 
The binary weights of the query vector were all set to one initially.

After having the binary weights inside both vectors, I used an external library called `numpy` that helped me with the cosine similarity.
