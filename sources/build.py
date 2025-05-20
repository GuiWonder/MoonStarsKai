import os, json, sys, copy
from fontTools.ttLib import TTFont, newTable
from fontTools.ttLib.tables import otTables

ftversion='1.103'
fthyen='Moon Stars Kai'
fthytc='月星楷'
fthysc='月星楷'
fthyjp='月星楷'
ftfxen='Moon Stars Kai T'
ftfxtc='月星楷 繁'
ftfxsc='月星楷 繁'
ftfxjp='月星楷 繁'

comid='GUIW'
fturl='https://github.com/GuiWonder/MoonStarsKai'

hy=dict()
hy['en']=fthyen
hy['tc']=fthytc
hy['sc']=fthysc
hy['jp']=fthyjp
hy['vs']=ftversion
fx=dict()
fx['en']=ftfxen
fx['tc']=ftfxtc
fx['sc']=ftfxsc
fx['jp']=ftfxjp
fx['vs']=ftversion

iscl=False
if len(sys.argv)>3 and sys.argv[3].lower()=='cl':
	iscl=True

if iscl:
	hy['en']+=' CL'
	fx['en']+=' CL'
	for nmtg in ['tc', 'sc']:
		hy[nmtg]+='CL'
		fx[nmtg]+='CL'

pydir=os.path.abspath(os.path.dirname(__file__))

def prouv(font, ispr):
	cmap=font.getBestCmap()
	for table in font["cmap"].tables:
		if table.format==14:
			for vsl in table.uvsDict.keys():
				newl=list()
				for cg in table.uvsDict[vsl]:
					if cg[1]==None and ispr:
						newl.append((cg[0], cmap[cg[0]]))
					elif cg[0] in cmap and cg[1]==cmap[cg[0]] and not ispr:
						newl.append((cg[0], None))
					else:
						newl.append((cg[0], cg[1]))
				table.uvsDict[vsl]=newl

def glyrepl(font, repdic):
	for table in font["cmap"].tables:
		for cd in table.cmap:
			if table.cmap[cd] in repdic:
				table.cmap[cd]=repdic[table.cmap[cd]]
def setcg(tables, code, glyf):
	for table in tables:
		if table.format==12 or (table.format==4 and code<=0xFFFF) or (table.format==0 and code<=0xFF) or code in table.cmap:
			table.cmap[code]=glyf
def rmlk(font, tbnm, i):
	font[tbnm].table.LookupList.Lookup.pop(i)
	for ki in font[tbnm].table.FeatureList.FeatureRecord:
		newft=list()
		for j in ki.Feature.LookupListIndex:
			if j>i: newft.append(j-1)
			elif j<i: newft.append(j)
		ki.Feature.LookupListIndex=newft
	if tbnm=='GSUB':
		for lkp in font[tbnm].table.LookupList.Lookup:
			for st in lkp.SubTable:
				if st.LookupType in (5, 6) and hasattr(st, 'SubstLookupRecord'):
					for sbrcd in st.SubstLookupRecord:
						if sbrcd.LookupListIndex>i:
							sbrcd.LookupListIndex-=1
def rmft(font, tbnm, i):
	font[tbnm].table.FeatureList.FeatureRecord.pop(i)
	for sr in font[tbnm].table.ScriptList.ScriptRecord:
		newdl=list()
		for j in sr.Script.DefaultLangSys.FeatureIndex:
			if j>i: newdl.append(j-1)
			elif j<i: newdl.append(j)
		sr.Script.DefaultLangSys.FeatureIndex=newdl
		for lsr in sr.Script.LangSysRecord:
			newln=list()
			for j in lsr.LangSys.FeatureIndex:
				if j>i: newln.append(j-1)
				elif j<i: newln.append(j)
			lsr.LangSys.FeatureIndex=newln
def hwcmp(font):
	cmap=font.getBestCmap()
	exp='、。，．・：；？！゛゜｀＾￣＿ー―‐／＼～｜（）〔〕［］｛｝〈〉《》「」『』【】＋－＝＜＞♂♀℃￥＄￠￡％＃＆＊＠▲〒〓０１２３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶ〝〟￤＇＂〘〙｟｠〞'
	expg={cmap[ord(ch)] for ch in exp}
	repgl=dict()
	
	itlk, itft=list(), list()
	for i in range(len(font["GSUB"].table.FeatureList.FeatureRecord)):
		if font["GSUB"].table.FeatureList.FeatureRecord[i].FeatureTag=='hwid':
			itlk+=font["GSUB"].table.FeatureList.FeatureRecord[i].Feature.LookupListIndex
			font["GSUB"].table.FeatureList.FeatureRecord[i].Feature.LookupListIndex.clear()
			itft.append(i)
	itlk=list(set(itlk))
	itlk.sort(reverse=True)
	itft=list(set(itft))
	itft.sort(reverse=True)
	for i in itlk:
		for st in font["GSUB"].table.LookupList.Lookup[i].SubTable:
			if st.LookupType==7:
				stbl=st.ExtSubTable
			else:
				stbl=st
			assert stbl.LookupType==1
			tabl=stbl.mapping
			repgl={hwg:tabl[hwg] for hwg in tabl if hwg not in expg}
			glyrepl(font, repgl)
	for i in itft: rmft(font, 'GSUB', i)
	for i in itlk: rmlk(font, 'GSUB', i)
def hwgps(font):
	torm=['kern', 'palt', 'vkrn', 'vpal']
	hwlks, hwfts=list(), list()
	for i in range(len(font["GPOS"].table.FeatureList.FeatureRecord)):
		if font["GPOS"].table.FeatureList.FeatureRecord[i].FeatureTag in torm:
			hwlks+=font["GPOS"].table.FeatureList.FeatureRecord[i].Feature.LookupListIndex
			hwfts.append(i)
	hwlks=list(set(hwlks))
	hwlks.sort(reverse=True)
	hwfts=list(set(hwfts))
	hwfts.sort(reverse=True)
	for i in hwfts: rmft(font, 'GPOS', i)
	for i in hwlks: rmlk(font, 'GPOS', i)
def stlks(font, chrdic, phrdic):
	cmap=font.getBestCmap()
	glod=font.getGlyphOrder()
	stmul=otTables.Lookup()
	stsig=otTables.Lookup()
	stsig1=otTables.Lookup()
	stsig2=otTables.Lookup()
	stsig3=otTables.Lookup()
	stlkups=[stmul, stsig, stsig1, stsig2, stsig3]
	sgtb, sgtb1, sgtb2, sgtb3=dict(), dict(), dict(), dict()
	for lk in stlkups[1:]:
		lk.LookupType=1
		lk.LookupFlag=0
	sgsb=otTables.SingleSubst()
	sgsb1=otTables.SingleSubst()
	sgsb2=otTables.SingleSubst()
	sgsb3=otTables.SingleSubst()
	stsig.SubTable=[sgsb]
	stsig1.SubTable=[sgsb1]
	stsig2.SubTable=[sgsb2]
	stsig3.SubTable=[sgsb3]
	stmul.SubTable=list()
	stmul.LookupType=6
	stmul.LookupFlag=0

	ltc=dict()
	for phdc in phrdic:
		s, t=phdc['s'], phdc['t']
		dics=phdc['p']
		sg=cmap[ord(s)]
		tg=cmap[ord(t)]
		i=dics.index(s)
		assert i>-1
		bkcov=dics[0:i]
		bkcov.reverse()
		lahcov=dics[i+1:]
		if sg!=tg and tg not in ltc:
			if sg not in sgtb1:
				sgtb1[sg]=tg
				ltc[tg]=2
			elif sg not in sgtb2:
				sgtb2[sg]=tg
				ltc[tg]=3
			elif sg not in sgtb3:
				sgtb3[sg]=tg
				ltc[tg]=4
			else:
				raise
		bklst=list()
		for strs in bkcov:
			cvobjbk=otTables.Coverage()
			cvobjbk.glyphs=list(set([cmap[ord(ch)] for ch in strs if ord(ch) in cmap]))
			assert len(cvobjbk.glyphs)>0, strs
			cvobjbk.glyphs=list(sorted([g for g in cvobjbk.glyphs], key=lambda g:glod.index(g)))
			bklst.append(cvobjbk)
		ahlst=list()
		for strs in lahcov:
			cvobjah=otTables.Coverage()
			cvobjah.glyphs=list(set([cmap[ord(ch)] for ch in strs if ord(ch) in cmap]))
			assert len(cvobjah.glyphs)>0, strs
			cvobjah.glyphs=list(sorted([g for g in cvobjah.glyphs], key=lambda g:glod.index(g)))
			ahlst.append(cvobjah)
		cvobjip=otTables.Coverage()
		cvobjip.glyphs=[cmap[ord(s)]]
		mulsb=otTables.ChainContextSubst()
		mulsb.Format=3
		mulsb.BacktrackCoverage=bklst
		mulsb.InputCoverage=[cvobjip]
		mulsb.LookAheadCoverage=ahlst
		if sg!=tg:
			sblrd=otTables.SubstLookupRecord()
			sblrd.SequenceIndex=0
			sblrd.LookupListIndex=ltc[tg]
			mulsb.SubstLookupRecord=[sblrd]
		stmul.SubTable.append(mulsb)
	sgsb1.mapping=sgtb1
	sgsb2.mapping=sgtb2
	sgsb3.mapping=sgtb3
	for s, t in list(chrdic.items()):
		if ord(s) in cmap and ord(t) in cmap and cmap[ord(s)]!=cmap[ord(t)]:
			sgtb[cmap[ord(s)]]=cmap[ord(t)]
	sgsb.mapping=sgtb
	for lkp in font["GSUB"].table.LookupList.Lookup:
		for st in lkp.SubTable:
			if st.LookupType in (5, 6) and hasattr(st, 'SubstLookupRecord'):
				for sbrcd in st.SubstLookupRecord:
					sbrcd.LookupListIndex+=len(stlkups)
	for ft in font["GSUB"].table.FeatureList.FeatureRecord:
		ft.Feature.LookupListIndex=[i+len(stlkups) for i in ft.Feature.LookupListIndex]
	font["GSUB"].table.LookupList.Lookup=stlkups+font["GSUB"].table.LookupList.Lookup
	stft=otTables.FeatureRecord()
	stft.Feature=otTables.Feature()
	stft.FeatureTag='ccmp'
	stft.Feature.LookupListIndex=[0, 1]
	font["GSUB"].table.FeatureList.FeatureRecord.insert(0, stft)
	for sr in font["GSUB"].table.ScriptList.ScriptRecord:
		sr.Script.DefaultLangSys.FeatureIndex=[i+1 for i in sr.Script.DefaultLangSys.FeatureIndex]
		sr.Script.DefaultLangSys.FeatureIndex.insert(0, 0)
		for lsr in sr.Script.LangSysRecord:
			lsr.LangSys.FeatureIndex=[i+1 for i in lsr.LangSys.FeatureIndex]
			lsr.LangSys.FeatureIndex.insert(0, 0)
def stcmp(font, chrdic):
	cmap=font.getBestCmap()
	for s, t in list(chrdic.items()):
		if ord(s) not in cmap and ord(t) in cmap:
			setcg(font['cmap'].tables, ord(s), cmap[ord(t)])
def getstdic():
	newdic=dict()
	with open(os.path.join(pydir, 'stoneo.dt'),'r',encoding='utf-8') as f:
		for line in f.readlines():
			litm=line.split('#')[0].strip()
			if '-' not in litm: continue
			s, t=litm.split(' ')[0].split('-')
			s, t=s.strip(), t.strip()
			if s and t and s!=t:
				newdic[s]=t
	for s, t in list(newdic.items()):
		if t in newdic: newdic[s]=newdic[t]
	newlst=list()
	with open(os.path.join(pydir, 'stonem.dt'),'r',encoding='utf-8') as f:
		for line in f.readlines():
			litm=line.split('#')[0].strip()
			if '-' not in litm: continue
			dic1=dict()
			ls=litm.strip().split(' ')
			s, t=ls[0].split('-')
			dic1['s'], dic1['t']=s, t
			dic1['p']=ls[1:]
			newlst.append(dic1)
	return newdic, newlst

def setname(names, wt, ishw=False):
	fmlName=names['en']
	scn=names['tc']
	tcn=names['sc']
	jpn=names['jp']
	version=names['vs']
	if ishw:
		fmlName+=' HW'
		scn+=' 半宽'
		tcn+=' 半寬'
		jpn+=' HW'
	ftName=fmlName
	ftNamesc=scn
	ftNametc=tcn
	ftNamejp=jpn
	if wt not in ('Regular', 'Bold'):
		ftName+=' '+wt
		ftNamesc+=' '+wt
		ftNametc+=' '+wt
		ftNamejp+=' '+wt
	subfamily='Regular'
	if wt=='Bold':
		subfamily='Bold'
	psName=fmlName.replace(' ', '')+'-'+wt
	uniqID=version+';'+comid.strip()+';'+psName
	if wt in ('Regular', 'Bold'):
		fullName=ftName+' '+wt
		fullNamesc=ftNamesc+' '+wt
		fullNametc=ftNametc+' '+wt
		fullNamejp=ftNamejp+' '+wt
	else:
		fullName=ftName
		fullNamesc=ftNamesc
		fullNametc=ftNametc
		fullNamejp=ftNamejp
	newnane=newTable('name')
	newnane.setName(f'Copyright 2023-2025 {names["en"]} Project Authors ({fturl})', 0, 3, 1, 1033)
	newnane.setName(ftName, 1, 3, 1, 1033)
	newnane.setName(subfamily, 2, 3, 1, 1033)
	newnane.setName(uniqID, 3, 3, 1, 1033)
	newnane.setName(fullName, 4, 3, 1, 1033)
	newnane.setName('Version '+version, 5, 3, 1, 1033)
	newnane.setName(psName, 6, 3, 1, 1033)
	newnane.setName('GuiWonder', 9, 3, 1, 1033)
	newnane.setName(fturl, 11, 3, 1, 1033)
	newnane.setName('This Font Software is licensed under the SIL Open Font License, Version 1.1. This license is available with a FAQ at: https://scripts.sil.org/OFL', 13, 3, 1, 1033)
	newnane.setName('https://scripts.sil.org/OFL', 14, 3, 1, 1033)
	if wt not in ('Regular', 'Bold'):
		newnane.setName(fmlName, 16, 3, 1, 1033)
		newnane.setName(wt, 17, 3, 1, 1033)
	for lanid in (1028, 3076, 5124):
		newnane.setName(ftNametc, 1, 3, 1, lanid)
		newnane.setName(subfamily, 2, 3, 1, lanid)
		newnane.setName(fullNametc, 4, 3, 1, lanid)
		if wt not in ('Regular', 'Bold'):
			newnane.setName(tcn, 16, 3, 1, lanid)
			newnane.setName(wt, 17, 3, 1, lanid)
	for lanid in (2052, 4100):
		newnane.setName(ftNamesc, 1, 3, 1, lanid)
		newnane.setName(subfamily, 2, 3, 1, lanid)
		newnane.setName(fullNamesc, 4, 3, 1, lanid)
		if wt not in ('Regular', 'Bold'):
			newnane.setName(scn, 16, 3, 1, lanid)
			newnane.setName(wt, 17, 3, 1, lanid)
	newnane.setName(ftNamejp, 1, 3, 1, 1041)
	newnane.setName(subfamily, 2, 3, 1, 1041)
	newnane.setName(fullNamejp, 4, 3, 1, 1041)
	if wt not in ('Regular', 'Bold'):
		newnane.setName(jpn, 16, 3, 1, 1041)
		newnane.setName(wt, 17, 3, 1, 1041)
	return newnane

def setrbbb(font, stylename):
	assert stylename in {"regular", "bold", "italic", "bold italic", 'other'}
	if stylename == "bold":
		font["head"].macStyle = 0b01
	elif stylename == "bold italic":
		font["head"].macStyle = 0b11
	elif stylename == "italic":
		font["head"].macStyle = 0b10
	else:
		font["head"].macStyle = 0b00
	selection = font["OS/2"].fsSelection
	# First clear...
	selection &= ~(1 << 0)
	selection &= ~(1 << 5)
	selection &= ~(1 << 6)
	# ...then re-set the bits.
	if stylename == "regular":
		selection |= 1 << 6
	elif stylename == "bold":
		selection |= 1 << 5
	elif stylename == "italic":
		selection |= 1 << 0
	elif stylename == "bold italic":
		selection |= 1 << 0
		selection |= 1 << 5
	font["OS/2"].fsSelection = selection

def saveft(font, mono=False):
	newtf=TTFont(infile)
	newtf['vmtx']['.null']=(0, 0)
	if mono:
		newtf['OS/2'].panose.bProportion=9
		newtf['OS/2'].xAvgCharWidth=500
	newtf['head'].fontRevision=float(ftversion)
	newtf['OS/2'].achVendID=comid
	for tb in ('name', 'cmap', 'GSUB', 'GPOS'):
		newtf[tb]=font[tb]
	if weight.lower()=='bold':
		newtf['OS/2'].usWeightClass=700
		setrbbb(newtf, 'bold')
	elif weight.lower()=='light':
		newtf['OS/2'].usWeightClass=300
		setrbbb(newtf, 'other')
	elif weight.lower()=='regular':
		newtf['OS/2'].usWeightClass=400
		setrbbb(newtf, 'regular')
	ftfile=font['name'].getDebugName(6)+'.'+exn
	print('Saving', ftfile)
	newtf.save(ftfile)

infile=sys.argv[1]
weight=sys.argv[2]
exn=infile.split('.')[-1].lower()

infont=TTFont(infile)
infont['cmap'].tables=[table for table in infont['cmap'].tables if table.format!=0]

infont['name']=setname(hy, weight)
saveft(infont)

prouv(infont, True)
hwcmp(infont)
infont['name']=setname(hy, weight, True)
prouv(infont, False)
saveft(infont, True)

infont=TTFont(infile)
infont['cmap'].tables=[table for table in infont['cmap'].tables if table.format!=0]
prouv(infont, True)
chrdic, phrdic=getstdic()
stcmp(infont, chrdic)
stlks(infont, chrdic, phrdic)
infont['name']=setname(fx, weight)
prouv(infont, False)
saveft(infont)

prouv(infont, True)
hwcmp(infont)
infont['name']=setname(fx, weight, True)
prouv(infont, False)
saveft(infont, True)
