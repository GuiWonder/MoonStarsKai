import os
import sys

BK='BrightMoonKai'
AK='ArrayStarsKai'
SP='Super'
if len(sys.argv)>1 and sys.argv[1].lower()=='cl':
	BK+='CL'
	AK+='CL'
	SP+='CL'

sevenz='7z'

wts=('Regular', 'Bold', 'Light')
for fts in (BK, AK):
	ttfs=list()
	ttcs=list()
	ttfs.append('LICENSE.txt')
	ttcs.append('LICENSE.txt')
	for wt in wts:
		ttfs.append(f'{fts}-{wt}.ttf')
		ttfs.append(f'{fts}Mono-{wt}.ttf')
		ttcs.append(f'{fts}-{wt}.ttc')
	os.system(f'{sevenz} a ./{fts}TTFs.zip {" ".join(ttfs)}')
	os.system(f'{sevenz} a ./{fts}TTCs.zip {" ".join(ttcs)}')

spftfl=list()
spftfl.append('LICENSE.txt')
for wt in wts:
	spftfl.append(f'{SP}-{wt}.ttc')
os.system(f'{sevenz} a ./{SP}TTCs.zip {" ".join(spftfl)}')

