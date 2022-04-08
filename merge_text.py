import os
import pathlib

def merge_text(path):
    """
    Function to merge multiple text files;
    Args: Takes a folder containing `txt` files;

    Returns:
            Saves files to the same folder. 
    """
    files = [os.path.join(path, txt) for txt in  os.listdir(path) if txt.endswith(".txt")]

    master_text = ""
    for file in files:
        data = pathlib.Path(file).read_text()
        master_text += data + "\n"
    
    output_name = os.path.join(path, '_text_result.txt')
    with open(output_name, 'w') as f:
        f.write(master_text)