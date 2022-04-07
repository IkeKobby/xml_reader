# import library
import xml.etree.ElementTree as ET

def sentence_encoder(xml_filename, format = None, save = True):
    """
    Takes xml file and returns a list of sentences from the file;
    The code is not generic, it is file specific.

    Args:
        xml_filename; the xml file to convert to text
        format; the format of the output, whether to return as one text or a list of sentences.
        save:   if true, it saves the text to a file.

    Returns: 
            List of sentences. 
    """
    # create the tree parser
    tree = ET.parse(xml_filename)

    # Get the root of the file
    root = tree.getroot()

    # list to save sentences
    sentences = []

    # loop over the number of sentences in the file
    for sent in range(len(root[0][3])):

        # get the sentence tag
        sentence = root[0][3][sent]

        # get the tokens for each sentence; a sentence contain several tokens, that is, several words
        tokens = sentence[0]

        # set the beginning of a sentence 
        sent = ''

        # loop over all the tokens
        for token in tokens:
            # each token has subtags, take the text part of all subtags.
            content = [subtag.text for subtag in token] 

            # concat the `0` index text, which is the `word` token. 
            sent += f'{content[0]} '  

        # keep records of each sentence 
        sentences.append(sent)

    # convert sentences to a string
    text = " ".join(sentences)

    # save file to disk
    if save:
        prefix = xml_filename.split('.')[0]
        output_name = f'{prefix}_text_result.txt'
        with open(output_name,  'w') as text_df:
                text_df.write(text)
    # for text output
    if format == 'text':
        return text
    # returns list of sentences by default.
    return sentences

    
