import sys, os
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables import otTables

def setcg(code, glyf):
	for table in font["cmap"].tables:
		if (table.format==4 and code<=0xFFFF) or table.format==12 or (table.format==6 and code<=0xFF) or code in table.cmap:
			table.cmap[code]=glyf
def addlk(lktg, sgtb):
	stsig=otTables.Lookup()
	stsig.LookupType=1
	stsig.LookupFlag=0
	sgsb=otTables.SingleSubst()
	stsig.SubTable=[sgsb]
	sgsb.mapping=sgtb
	for lkp in font["GSUB"].table.LookupList.Lookup:
		for st in lkp.SubTable:
			if st.LookupType in (5, 6) and hasattr(st, 'SubstLookupRecord'):
				for sbrcd in st.SubstLookupRecord:
					sbrcd.LookupListIndex+=1
	for ft in font["GSUB"].table.FeatureList.FeatureRecord:
		ft.Feature.LookupListIndex=[i+1 for i in ft.Feature.LookupListIndex]
	font["GSUB"].table.LookupList.Lookup.insert(0, stsig)
	stft=otTables.FeatureRecord()
	stft.Feature=otTables.Feature()
	stft.FeatureTag=lktg
	stft.Feature.LookupListIndex=[0, ]
	font["GSUB"].table.FeatureList.FeatureRecord.insert(0, stft)
	for sr in font["GSUB"].table.ScriptList.ScriptRecord:
		sr.Script.DefaultLangSys.FeatureIndex=[i+1 for i in sr.Script.DefaultLangSys.FeatureIndex]
		sr.Script.DefaultLangSys.FeatureIndex.insert(0, 0)
		for lsr in sr.Script.LangSysRecord:
			lsr.LangSys.FeatureIndex=[i+1 for i in lsr.LangSys.FeatureIndex]
			lsr.LangSys.FeatureIndex.insert(0, 0)
def mergelk():
	for i in range(len(font["GSUB"].table.LookupList.Lookup)):
		lk1=font["GSUB"].table.LookupList.Lookup[i]
		lk2=fontmn["GSUB"].table.LookupList.Lookup[i]
		for j in range(len(lk1.SubTable)):
			st1=lk1.SubTable[j]
			st2=lk2.SubTable[j]
			assert st1.LookupType==st2.LookupType
			if st1.LookupType==1:
				tabl1=st1.mapping
				tabl2=st2.mapping
				for g1, g2 in list(tabl2.items()):
					if g1 not in tabl1:
						tabl1[g1]=g2
			elif st1.LookupType==4:
				lg1=st1.ligatures
				lg2=st2.ligatures
				for g1 in lg2:
					if g1 not in lg1:
						lg1[g1]=lg2[g1]
					else:
						if lg1[g1]!=lg2[g1]:
							for lgi1 in lg2[g1]:
								if lgi1 not in lg1[g1]:
									lg1[g1].append(lgi1)
			elif st1.LookupType==6:
				lk1.SubTable.append(st2)
			else:
				raise

def rmlogo(fontlx):
	for table in fontlx["cmap"].tables:
		if 0xFFFFD in table.cmap: del table.cmap[0xFFFFD]

def rmlklg(fontlx):
	for ki in font["GSUB"].table.LookupList.Lookup:
		for st in ki.SubTable:
			if st.LookupType==7:
				stbl=st.ExtSubTable
			else:
				stbl=st
			lktp=stbl.LookupType
			if lktp==4:
				for li in list(stbl.ligatures):
					for lg in list(stbl.ligatures[li]):
						if lg.LigGlyph in ('uFFFFD', 'uFFFFD#1'):
							stbl.ligatures[li].remove(lg)
					if len(stbl.ligatures[li])<1:
						del stbl.ligatures[li]


inft=sys.argv[1]
outft=sys.argv[2]
font=TTFont(inft, fontNumber=0)
fontmn=TTFont(inft, fontNumber=1)
rmlogo(font)
rmlogo(fontmn)
mergelk()
cmap=font.getBestCmap()
cmapmn=fontmn.getBestCmap()
glod=font.getGlyphOrder()
for gl in glod:
	if font['hmtx'][gl][0] in (498, 499, 501, 502):font['hmtx'][gl]=(500, font['hmtx'][gl][1])
	if font['hmtx'][gl][0] in (998, 999, 1001, 1002):font['hmtx'][gl]=(1000, font['hmtx'][gl][1])

lktb=dict()
for cd in cmap:
	if cd in cmapmn and cmap[cd]!=cmapmn[cd]:
		lktb[cmap[cd]]=cmapmn[cd]
for cd in cmapmn:
	if cd not in cmap:
		setcg(cd, cmapmn[cd])
addlk('hwid', lktb)
lkfw=dict()
cmap=font.getBestCmap()
with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'fwid.txt'),'r',encoding='utf-8') as f:
	for line in f.readlines():
		litm=line.strip()
		if '\t' not in litm: continue
		s, t=litm.split('\t')
		if ord(s) not in cmap:
			print('Skip', s)
			continue
		if ord(t) not in cmap:
			print('Skip', t)
			continue
		if cmap[ord(s)]!=cmap[ord(t)]:
			lkfw[cmap[ord(s)]]=cmap[ord(t)]
addlk('fwid', lkfw)
rmlklg(font)
newft=TTFont(inft, fontNumber=0)
newft['GSUB']=font['GSUB']
newft['cmap']=font['cmap']
newft.save(outft)
