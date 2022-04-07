# xml_reader
Works on an xml file with the following structure;

- File has one `root`
    - `DOC` has 4 subtags `HEADLINE`, `DATELINE`, `TEXT`, `sentences`
        - `sentences` has subtags `sentence`
            - `sentence` each sentence has `tokens`, `parse`, `basic-dependencies`, `collapsed-dependencies`, `collapsed-ccprocessed-dependencies`
                - `tokens` have `token`
                    - `token` has `word`, `lemma`, `CharacterOffsetBegin`, `CharacterOffsetEnd`, `POS`, `NER`

** If save == True, it saves the extracted data to disk in the current working directory **

