import re

def read_xml(xml_file, element):
    """
    Return only needed information
    """
    # get the beginning tag of the needed content
    start_tag = f'<{element}>' 

    # the end tag of the content
    end_tag = f'</{element}>'

    # to keep track of finding the required head
    start_tag_identified = False

    # record all the words 
    captured_records = []

    # record word by each line
    captured_word = ''

    # open the file and iterate through
    with open(xml_file) as f:
        for line in f:
            if start_tag in line:
                start_tag_identified = True
            if start_tag_identified:
                split = re.split('>|<', line)
                word = split[2]
                captured_word += word
            if end_tag in line:
                captured_records.append(captured_word)
                start_tag_identified = False
                captured_word = ''

    # join all words to form one text
    text = " ".join(captured_records)

    # save file to disk with the same file name in txt format.
    prefix = xml_file.split('.')[0]
    output_name = f'{prefix}_text_result.txt'
    with open(output_name,  'w') as text_df:
            text_df.write(text)

