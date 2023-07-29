from afdko import otf2otc
import sys
wts=('Regular', 'Bold', 'Light')

BK='BrightMoonKai'
AK='ArrayStarsKai'
SP='Super'
if len(sys.argv)>1 and sys.argv[1].lower()=='cl':
	BK+='CL'
	AK+='CL'
	SP+='CL'
for wt in wts:
	for fts in (BK, AK):
		ttcarg=['-o', f'{fts}-{wt}.ttc', f'{fts}-{wt}.ttf', f'{fts}Mono-{wt}.ttf']
		otf2otc.run(ttcarg)
	ttcarg=['-o', f'{SP}-{wt}.ttc', f'{BK}-{wt}.ttf', f'{BK}Mono-{wt}.ttf', f'{AK}-{wt}.ttf', f'{AK}Mono-{wt}.ttf']
	otf2otc.run(ttcarg)
