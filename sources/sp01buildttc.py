import sys
import fontforge

print('Processing...')
fonts=list()
for fontfile in sys.argv[2:]:
	font=fontforge.open(fontfile)
	fonts.append(font)
print('Generating TTC...')
fonts[0].generateTtc(sys.argv[1], fonts[1:], ttcflags = ("merge"), layer = 1)
print('Finished!')
