class CoverGenerator:
    #self -> required
    #number_words -> number of words from the word list to be included
    #height -> height of picture in number of chars
    #width -> widht of picture in number of chars
    #words_path -> path to words_file txt
    #spezialwords_apth = path to words with given coorinates
    #outout_path -> path where png file will be stored
    def __init__(self, number_words, height, width, words_path, spezialwords_path, output_path):
        self.number_words = number_words
        self.height = height
        self.width = width
        self.words_path = words_path
        self.spezialwords_path = spezialwords_path
        self.output_path = output_path

    #main method generates the word puzzle
    def main(self):
        self.words, self.spezialwords = self.load_data()
        self.char_array = self.generate_array()
        self.print_png(self.char_array)


    #load the files and returns a list of words and a list of words with coordinates
    def load_data(self, path_words, path_spezialwords):
        print('load data')

    #creates the char array which will be seen on the png
    def generate_array(self, words, spezialwords):
        print('generate array')

    #creates the png from the char array
    def print_png(self, char_array):
        print('print png')