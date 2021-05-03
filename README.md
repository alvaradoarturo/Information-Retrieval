# CS172 - Assignment 1 (Tokenization)

## Team member 1 - Arturo Alvarado
## Team member 2 - Firstname Lastname

Language Used: Python 3.9.4

### Instructions To Run Program
Git clone repository into local directory
If you're using a MAC, you can input commands by simply using "./parsing_input {query type} {doc/term name}"
If you're using a Windows, you can input commands by simply using "python3 ./parsing_input {query type} {doc/term name}"

### Brief Overview of Desing
The entire document was first parsed by docno number followed by all text. This was then normalized by first removing punctuation.Then
converting the entire text to lower-case. After text was normalized, the entire text was then split into single words or collection of characters. Then I created a local dictionary that kept track of all distinct terms while removing stop words. Terms kept position location and the frequency of each term for that specific document. Then once the document had a list of each distinct terms as well as relevanr information, I then added each document to a global document dictionary that contained each document as well as its relevant information.
