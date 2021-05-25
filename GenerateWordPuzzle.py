from CoverGenerator import CoverGenerator
import sys


height = 0
width = 0
numer_of_words = 0
path_words = ""
path_spezialwords = ""
path_output = ""

print ('Number of arguments:', len(sys.argv), ' arguments')
path_words = sys.argv[1]
path_spezialwords = sys.argv[2]
path_output = sys.argv[3]
height = sys.argv[4]
width = sys.argv[5]
number_of_words = sys.argv[6]

# print('path_words: ', path_words)
# print('path_spezialwords: ', path_spezialwords)
# print('path_output: ', path_output)
# print('height: ', height)
# print('width: ', width)

c = CoverGenerator()
c.main()