import re
import os

class parser:
    def __init__(self, element, input_folder, output_folder) -> None:
        self.element = element
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.xml_files = [os.path.join(input_folder, xml) for xml in os.listdir(input_folder) if xml.endswith('.xml')]
    
    def _get_files(self):
        for file in self.xml_files:
            self.read_xml(file, self.element)

    def read_xml(self, xml_file, element):
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
                    if "'" in word:
                        keep_last_word = captured_records[-1]
                        captured_records = captured_records[:-1]
                        captured_word += keep_last_word + word.strip()
                    else:
                        captured_word += word
                if end_tag in line:
                    captured_records.append(captured_word)
                    start_tag_identified = False
                    captured_word = ''


        # join all words to form one text
        text = " ".join(captured_records)

        # save file to disk with the same file name in txt format.
        prefix = re.split('/|\.', xml_file)[-2]
        output_name = f'{self.output_folder}/{prefix}_text_result.txt'
        with open(output_name,  'w') as text_df:
                text_df.write(text)