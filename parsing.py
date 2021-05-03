#!/usr/bin/python3

import re
import os
import zipfile


def parsing_input(docToPrint):
    # Regular expressions to extract data from the corpus
    doc_regex = re.compile("<DOC>.*?</DOC>", re.DOTALL)
    docno_regex = re.compile("<DOCNO>.*?</DOCNO>")
    text_regex = re.compile("<TEXT>.*?</TEXT>", re.DOTALL)

    # Delcar all punctuations we wish to remove
    removeThesePunctuations = '''!()-[]{};:'"\,\`<>./?@#$%^&*_~'''

    # (term_id, doc_id, position) We want specific identifiers for each term and document
    idTerm = {}
    idDoc = {}

    # Declare Dictionaries
    documentNumberDictionary = {}
    uniqueWordDictionary = {}

    # Extract list of stopwords we wish to remove
    fi = open("./stopwords.txt", "r")
    stopWords = fi.read()

    with zipfile.ZipFile("ap89_collection_small.zip", 'r') as zip_ref:
        zip_ref.extractall()

    # Retrieve the names of all files to be indexed in folder ./ap89_collection_small of the current directory
    for dir_path, dir_names, file_names in os.walk("ap89_collection_small"):
        allfiles = [os.path.join(dir_path, filename).replace(
            "\\", "/") for filename in file_names if (filename != "readme" and filename != ".DS_Store")]

    for file in allfiles:
        with open(file, 'r', encoding='ISO-8859-1') as f:
            filedata = f.read()
            # Match the <DOC> tags and fetch documents
            result = re.findall(doc_regex, filedata)

            for document in result[0:]:
                # Retrieve contents of DOCNO tag
                docno = re.findall(docno_regex, document)[0].replace(
                    "<DOCNO>", "").replace("</DOCNO>", "").strip()
                # Retrieve contents of TEXT tag
                text = "".join(re.findall(text_regex, document))\
                    .replace("<TEXT>", "").replace("</TEXT>", "")\
                    .replace("\n", " ")

                # step 1 - remove stop-words, etc.
                # step 2 - create tokens
                # step 3 - build index

                # Step 1.1- remove punctuations
                noPunctuations = ""
                for char in text:
                    if char not in removeThesePunctuations:
                        noPunctuations = noPunctuations + char
                # Step 1.2 covert sentences to lower-case then create a list of all words
                noPuncAllLower = (noPunctuations.lower()).split()

                # Calculate total terms minus stop words
                lenWithoutStopWords = []
                for nonStopWord in noPuncAllLower:
                    if nonStopWord not in stopWords:
                        lenWithoutStopWords.append(nonStopWord)

                # Obtain frequency & pos
                currentDocumentDictionary = {}
                positionFound = 0

                for element in noPuncAllLower:
                    if element not in currentDocumentDictionary:  # word is not registered in current dictionary
                        # store position found, and new frequency which is 1
                        currentDocumentDictionary[element] = [
                            [positionFound], 1]
                    else:  # word is already registered in current dictionary
                        # add new position where same word has been found
                        currentDocumentDictionary[element][0].append(
                            positionFound)
                        # update frequenct
                        currentDocumentDictionary[element][1] += 1
                        # Add document number to every term
                    positionFound += 1

                # Now we can remove stop words, cant modify dict and loop over at the same time
                noDuplicateDictionary = {}
                for entry in currentDocumentDictionary:
                    if entry not in stopWords:
                        noDuplicateDictionary[entry] = currentDocumentDictionary[entry]

                # Add all entries into global document dictionary
                documentNumberDictionary[docno] = [len(lenWithoutStopWords), len(
                    noDuplicateDictionary), noDuplicateDictionary]

                # print (docno)
                # print(noPuncAllLower)
                # print(noDuplicateDictionary)

    # docValues = documentNumberDictionary[docToPrint]
    # print(docValues)
    totalTerms = documentNumberDictionary[docToPrint][0]
    distinctTerms = documentNumberDictionary[docToPrint][1]

    print("Total Terms: " + str(totalTerms))
    print("Distinct Terms: " + str(distinctTerms))

    return
