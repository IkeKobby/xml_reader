import re
import os

def read_xml(xml_file, element):
    """
    Return only needed information
    """
    start_tag = f'<{element}>' # get the beginning tag of the needed content
    end_tag = f'</{element}>' # the end tag of the content

    start_tag_identified = False # to keep track of finding the required head
    captured_records = []
    captured_word = ''

    # open the file and iterate through
    with open(xml_file) as f:
        for line in f:
            if start_tag in line:
                start_tag_identified = True
            if start_tag_identified:
                split = re.split('>|<', line)
                word = split[2]
                if word.startswith("'") and word.split("'")[-1].isalpha():
                    keep_last_word = captured_records[-1]
                    captured_records.remove(keep_last_word)
                    captured_word += keep_last_word + word
                else:
                    captured_word += word
            if end_tag in line:
                captured_records.append(captured_word)
                start_tag_identified = False
                captured_word = ''
    text = " ".join(captured_records)
    prefix = xml_file.split('.')[0]
    output_name = 'res.txt'
    with open(output_name, 'w') as text_df:
        text_df.write(text)


read_xml('/Users/sugar/Documents/icrisat/nlp/xml-files/ltw_eng_200810.xml', "word")