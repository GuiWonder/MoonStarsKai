import os, sys
import fontforge

chars='摇瑶謡谣遥飖鳐奂唤换涣焕痪吴俣娱娯悮误录剥渌禄𮬠𫘧绿彚彞彛写泻吕宫侣黄横奥粤虚嘘戯册删姗栅带滞毁揺戸戻抜涙髪歩渉毎晩絶舎舗巻圏呉薫黒黙諌仭刄劔卽厩廏旣曁郷囱徴殻郉釼緑縁録靱郞埓勻戋栈笺残浅践刬溅盏篯线贱钱饯𬣡為偽媯溈蒍没殁内呐昷媪愠揾榅氲温煴緼腽蒀蕰藴輼醖鰛真填巔慎槙鎮顛鷏教别术剎弒怵摋殺沭秫脎術述鉥鎩俞偷喻媮榆告尚秃查頽户彦産顔舌恬憇憩栝湉甛甜舐舔銛铦𦧲𦧺壬任凭侹妊姙婬庭廷恁挺梃涏淫烶珽紝絍纴艇荏莛蜓衽袵賃赁鋌铤霆霪頲颋飪餁饪鵀䗴𬘩𬸊𠄶風嵐楓渢瘋碸諷颪颭颮颯颱颳颴颶颷颸颺颻颼颿飀飃飄飆飇飈具俱埧惧危佹卼垝姽峗桅洈硊脆臲詭诡跪陒頠鮠𠱓𬱟𬶏及伋吸圾岌彶忣扱极汲笈級级芨趿鈒钑靸馺𥄫﨤唐傏塘搪溏煻瑭禟糖螗赯鄌醣餹𨶈𲉅成城娍宬晟珹盛筬膥臹荿誠诚郕鋮铖𡷫𣚺傯悤憁摠熜牕璁窗窻總聰蔥蟌驄骢𩕄冗沉慤亡匄吂塃妄嬴巟忘忙惘慌望杗杧棢氓瀛牤甿盲硭籝網罔羸肓臝芒茫荒莣菵虻蝄蠃謊谎贏赢輞辋邙鋩铓魍龬𩷶𱇮巨佢奆岠巪弡拒柜榘洰渠炬煚矩磲秬粔苣蕖詎讵距鉅钜鮔𠳔圍韋偉媁幃徫暐椲湋潿煒禕葦衛褘諱讆躗違郼鍏闈韌韓韔韙韛韜韝韞韠韡韤𬉧俈喾嚳慥晧梏浩澔焅牿皓硞窖筶簉糙誥诰造郜酷鋯锆靠鵠鹄㸆骨嗗搰榾滑猾磆蓇餶馉骫骭骯骰骱骳骴骵骶骷骸骹骺骼骽骾骿髁髂髃髄髅髆髈髋髌髎髑髒髓體髕髖髗鶻鹘䱻咼剮卨喎堝媧撾旤檛渦禍窩簻緺腡萵蝸過鍋騧𡁜周倜凋啁奝婤彫惆椆淍琱睭碉稠簓綢绸蜩裯調调賙赒週雕鯛鲷鵰㨄鬼傀塊媿嵬巍廆愧槐櫆瑰磈蒐醜隗餽魁魂魄魅魆魇魈魉魊魋魌魎魏魑魔魘魙䰟凡巩帆恐杋梵汎矾筑築芃茿蛩跫釩銎钒鞏㧬𠆩𣎆𱝬关咲浂渕联妃屺忌改杞玘紀纪芑蓜記记跽配魢鱾𨥈夅洚絳绛胮逄降鿍䂫伛偃傴剾匹区医匼匽匾匿區呕嘔堰塸妪嫕嫗嫛岖嶇彄怄慝慪抠揠摳暱枢椻樞欧歐殴毆沤漚熰瓯甌眍瞘繄翳苉蓲蝘謳讴貙躯軀郾醫鏂駆驅驱鰋鴎鶠鷖鷗鸥鹥鼴鿀䁥䝙䞁𡂿𧏾𫪘𫭟𫸩𬉼𬥺𬸘𰰤𰽜曼墁嫚幔慢摱槾漫熳縵缦蔓蘰謾谩鏝镘饅馒鬘鰻鳗㿸價槚檟覂覆覇賈贾𠿪嵆嵇稽𥡴乑聚藂衆鄹驟骤前偂剪彅揃擶椾櫤湔煎箭糋翦謭譾谫鬋卿𦐇傝塌搨榻毾溻禢褟蹋遢闒阘鰨鳎䌈䑽𤌙𦈖羞饈馐鱃𱈌曷偈喝噶堨愒揭擖暍朅楬歇毼渴猲碣竭羯臈葛蔼藹蝎蠍褐謁譪谒轕遏霭靄鞨餲鶡鹖𨭛𮝺𮩝﨟陋旅膂令伶冷呤唥囹坽姈岭岺嶺怜拎昤朎柃泠澪玲瓴砱笭羚翎聆舲苓蛉詅軨邻鈴铃零領领鴒鸰齡齢龄鿅䙥𠍐𦊓今仱吟含唅唸埝妗岑念惗扲捻搇敜昑晗梣棯棽浛涔淰焓焾琀琴盦矜砛硶稔笒紟腍芩莟菍衾衿諗谂貪贪趻鈐钤霠頷颔騐鯰鲶黔㱃䫈𪁏𪘒𫄛𬠖𮭦𰡘𱮜卑俾啤埤婢庳捭椑牌琕痺睥碑稗箄簰粺聛脾萆薭蜱螷裨豍郫錍陴鞞顰颦髀鵯鹎鼙䫌𠜱𥱼𱰾傕搉榷確靏鶴鹤𤌍𦞦僭噆憯撍潛熸簪蠶譖谮𨅔虧侉刳匏咢咵圬垮夸姱嫮崿愕挎摴杇桍樗污洿湂瓠粵絝绔肟胯腭萼蕚袴誇諤谔跨遌鄂鄠銙鍔锷雩顎颚鰐鳄鶚鹗齶㻬𥔲𰽴鼠攛癙竄躥鑹鼢鼦鼧鼩鼪鼫鼬鼯鼱鼷鼹巤擸獵臘蠟躐邋鑞镴鬣鱲𫚭辰侲傉儂唇噥娠宸嶩憹振搙晨桭溽漘濃燶穠縟繷缛耨脣脤膿莀蓐薅蜃褥賑赈辱農辳辴鄏醲鋠鎒震鬞㫳䟴䣅婁僂嘍塿屢屨嶁廔摟擻數樓櫢漊瘻瞜窶簍籔縷耬膢蔞藪螻褸軁鏤髏𠞭𥕍犮坺妭帗拔绂茇祓胈韨盋秡袚钹紱菝跋鈸鲅䯋韍魃髮鮁黻鼥圮然嘫撚燃繎𬙇䡭侌冎埁壾枔獌獦玈瘑矝肣蒁蛫蟃谽貏輵酓𦬸𦳯𩨜慺瘣𩴾'

def getallcodesname(thfont):
	c_g = dict()
	g_c=dict()
	for gls in thfont.glyphs():
		g_c[gls.glyphname]=list()
		if gls.unicode > -1:
			c_g[gls.unicode]=gls.glyphname
			g_c[gls.glyphname].append(gls.unicode)
		if gls.altuni != None:
			for uni in gls.altuni:
				if uni[1] <= 0:
					c_g[uni[0]] = gls.glyphname
					g_c[gls.glyphname].append(uni[0])
	return c_g, g_c
def mergeft(font, fin2):
	print(f'Loading {fin2}...')
	code_glyph, glyph_codes=getallcodesname(font)
	font2 = fontforge.open(fin2)
	font2.reencode("unicodefull")
	font2.em = font.em
	code_glyph2, glyph_codes2=getallcodesname(font2)
	print('Adding glyphs...')
	code_codes2 = {}
	for n2 in glyph_codes2.keys():
		lc = [ac1 for ac1 in glyph_codes2[n2]]
		if len(lc) > 0:
			code_codes2[lc[0]] = lc[1:]
	font2.selection.select(*code_codes2.keys())
	font2.copy()
	font.selection.select(*code_codes2.keys())
	font.paste()
	font2.close()

def mergeftex(font, fin2):
	print('Remove glyphs...')
	code_glyph, glyph_codes=getallcodesname(font)

	glys={code_glyph[ord(ch)] for ch in chars}
	for gly in glys:
		glyph_codes[gly]=[cd for cd in glyph_codes[gly] if chr(cd) not in chars]
		if len(glyph_codes[gly])<1:
			font.removeGlyph(gly)
		else:
			gl=font[gly]
			lu=list()
			gl.unicode=glyph_codes[gly][0]
			for u1 in glyph_codes[gly][1:]:
				lu.append((u1, -1, 0))
			if len(lu) > 0: gl.altuni = tuple(lu)
			else: gl.altuni = None
	font.reencode("unicodefull")
	print(f'Loading {fin2}...')
	font2 = fontforge.open(fin2)
	font2.reencode("unicodefull")
	font2.em = font.em
	code_glyph2, glyph_codes2=getallcodesname(font2)
	code_glyph, glyph_codes=getallcodesname(font)
	print('Adding glyphs...')
	for ch in chars:
		uni=ord(ch)
		newg=font.createChar(-1, 'gly'+str(uni))
		g2=font2[code_glyph2[uni]]
		font2.selection.select(g2)
		font2.copy()
		font.selection.select(newg)
		font.paste()
		newg.unicode=g2.unicode
		#newg.altuni=g2.altuni
	font.reencode("unicodefull")
	font2.close()
	
def build(outft, inft, subft, subft2):
	print('Target', outft)
	print('Processing...')
	font=fontforge.open(inft)
	print('Merging glyphs...')
	mergeft(font, subft)
	if not (len(sys.argv)>5 and sys.argv[5].lower()=='cl'):
		mergeftex(font, subft2)
	print('Saving...')
	font.generate(outft)
	print('Finished', outft)

if __name__ == "__main__":
	build(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
