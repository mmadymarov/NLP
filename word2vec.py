import os


def pre_process(sentence):
    """The function will preprocess the raw data
        Argument: the raw sentence 
        return: list of processed words
     """
    # Convert to lower case
    sentence = sentence.lower()
    # Strip the newlines
    sentence = sentence.strip('\n')
    # split the sentence into words
    sentence = sentence.split(' ')

    return sentence


if __name__ == '__main__':

    words = []  # Keep each word in the list

    file_path = 'data/raw_data.txt'

    if os.path.isfile(file_path):

        #  open the file and read line by line
        fn = open(file_path, 'r')
        line = fn.readline()

        while line:
            w_processed = pre_process(line)
            words.extend(w_processed)
            line = fn.readline()
        # end loop
        fn.close()
        # Filter out the empty strings
        words = filter(None, words)


    else:
        print 'Could not find the file on the specified path'
