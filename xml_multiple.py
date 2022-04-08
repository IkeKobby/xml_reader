# import library
import xml.etree.ElementTree as ET
import os


class xmlReader:
    """
    Reads xml files from folder and returns text data for each file.

    Args: path; path containing the files

    Returns:
            Saves text from each file in the folder.
    """
    def __init__(self, path) -> None:
        self.path = path
        self.xml_files = [os.path.join(path, xml) for xml in  os.listdir(path) if xml.endswith('.xml')]

    def sentence_encoder(self, file):
         # create the tree parser
        tree = ET.parse(file)

        # Get the root of the file
        root = tree.getroot()
        # loop  over the number of documents in the file.
        sentences = []

        # loop  over the number of documents in the file.
        for doc in range(len(root)):
            # loop over the number of sentences in the file
            for sent in range(len(root[doc][3])):

                # get the sentence tag
                sentence = root[doc][3][sent]

                # get the tokens for each sentence; a sentence contain several tokens, that is, several words
                tokens = sentence[0]

                # set the beginning of a sentence 
                sent = ''

                # loop over all the tokens
                for token in tokens:
                    if content := [subtag.text for subtag in token]:
                        sent += f'{content[0]} '  

                # keep records of each sentence 
                sentences.append(sent)

                # convert sentences to a string
        return " ".join(sentences), file

    def get_text(self):
        for file in self.xml_files:
            text, file = self.sentence_encoder(file)
        # save file to disk
        prefix = file.split('.')[0]
        output_name = f'{prefix}_text_result.txt'
        with open(output_name,  'w') as text_df:
                text_df.write(text)