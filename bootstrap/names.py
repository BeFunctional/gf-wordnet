import ijson
import bz2

def extract():
    with bz2.open("wikidata-2022-07-31.json.bz2", "rb") as f:
        with open("names.txt", "w") as out:
            for record in ijson.items(f, "item"):
                name_type = None
                gender = None
                for claim in record["claims"].get("P31",[]):
                    if "datavalue" not in claim["mainsnak"]:
                        continue
                    typ = claim["mainsnak"]["datavalue"]["value"]["id"]
                    if typ in ["Q12308941","Q11879590","Q101352"]:
                        name_type = typ
                    if typ in ["Q18972245","Q18972207"]:
                        gender = typ
                if name_type:
                    if gender:
                        name_type = gender
                    names = {}
                    for lang,val in record["labels"].items():
                        names[lang] = val["value"]
                    out.write(str((record["id"],name_type,names))+"\n")

def cyr(s):
    #DOUBLE LETTERS UPPERCASE
    s = s.replace("YU", "Ю")
    s = s.replace("YA", "Я")
    s = s.replace("ZH", "Ж")
    s = s.replace("TS", "Ц")
    s = s.replace("CH", "Ч")
    s = s.replace("SHT", "Щ")
    s = s.replace("SH", "Ш")
    s = s.replace("QU", "КУ")
    s = s.replace("FF", "Ф")
    s = s.replace("KK", "К")
    s = s.replace("OO", "О")
    #DOUBLE LETTERS MIXED CASE
    s = s.replace("Yu", "Ю")
    s = s.replace("Ya", "Я")
    s = s.replace("Zh", "Ж")
    s = s.replace("Ts", "Ц")
    s = s.replace("Ch", "Ч")
    s = s.replace("Sht", "Щ")
    s = s.replace("Sh", "Ш")
    s = s.replace("Qf", "Ку")
    s = s.replace("Ff", "Ф")
    s = s.replace("Kk", "К")
    s = s.replace("Oo", "О")
    #DOUBLE LETTERS LOWERCASE
    s = s.replace("yu", "ю")
    s = s.replace("ya", "я")
    s = s.replace("zh", "ж")
    s = s.replace("ts", "ц")
    s = s.replace("ch", "ч")
    s = s.replace("sht", "щ")
    s = s.replace("sh", "ш")
    s = s.replace("qu", "ку")
    s = s.replace("ff", "ф")
    s = s.replace("kk", "k")
    s = s.replace("oo", "о")
    #UPPERCASE LETTERS
    s = s.replace("A", "A")
    s = s.replace("B", "Б")
    s = s.replace("C", "К")
    s = s.replace("V", "В")
    s = s.replace("G", "Г")
    s = s.replace("D", "Д")
    s = s.replace("E", "E")
    s = s.replace("Z", "З")
    s = s.replace("I", "И")
    s = s.replace("J", "Й")
    s = s.replace("K", "К")
    s = s.replace("L", "Л")
    s = s.replace("M", "M")
    s = s.replace("N", "Н")
    s = s.replace("O", "O")
    s = s.replace("P", "П")
    s = s.replace("R", "Р")
    s = s.replace("S", "С")
    s = s.replace("T", "T")
    s = s.replace("Ț", "T")
    s = s.replace("W", "В")
    s = s.replace("F", "Ф")
    s = s.replace("H", "X")
    s = s.replace("U", "У")
    s = s.replace("Y", "Й")
    s = s.replace("Æ", "Е")
    s = s.replace("Ä", "Е")
    s = s.replace("É", "Е")
    s = s.replace("Ə", "А")
    s = s.replace("Î", "И")
    s = s.replace("Ö", "Йо")
    s = s.replace("Ø", "Йо")
    s = s.replace("Õ", "Йо")
    s = s.replace("Ó", "О")
    s = s.replace("Å", "А")
    s = s.replace("A", "А")
    s = s.replace("E", "Е")
    s = s.replace("M", "М")
    s = s.replace("O", "О")
    s = s.replace("Q", "К")
    s = s.replace("T", "Т")
    s = s.replace("X", "Кс")
    s = s.replace("À", "А")
    s = s.replace("Á", "А")
    s = s.replace("Â", "А")
    s = s.replace("Ç", "Ч")
    s = s.replace("È", "Е")
    s = s.replace("Ê", "Е")
    s = s.replace("Í", "И")
    s = s.replace("Ñ", "Н")
    s = s.replace("Ò", "О")
    s = s.replace("Ô", "О")
    s = s.replace("Ú", "У")
    s = s.replace("Ü", "У")
    s = s.replace("Ý", "Й")
    s = s.replace("Þ", "Т")
    s = s.replace("Ā", "А")
    s = s.replace("Ą", "А")
    s = s.replace("Ć", "Ц")
    s = s.replace("Č", "Ц")
    s = s.replace("Ď", "Д")
    s = s.replace("Đ", "Д")
    s = s.replace("Ē", "Е")
    s = s.replace("Ė", "Е")
    s = s.replace("Ě", "Е")
    s = s.replace("Ĝ", "Г")
    s = s.replace("Ğ", "Г")
    s = s.replace("Ġ", "Г")
    s = s.replace("Ģ", "Г")
    s = s.replace("Ī", "И")
    s = s.replace("İ", "И")
    s = s.replace("Ķ", "К")
    s = s.replace("Ļ", "Л")
    s = s.replace("Ľ", "Л")
    s = s.replace("Ł", "Л")
    s = s.replace("Ņ", "Н")
    s = s.replace("Ō", "О")
    s = s.replace("Ř", "Р")
    s = s.replace("Œ", "Е")
    s = s.replace("Ś", "С")
    s = s.replace("Ş", "С")
    s = s.replace("Š", "С")
    s = s.replace("Ţ", "Т")
    s = s.replace("Ť", "Т")
    s = s.replace("Ū", "У")
    s = s.replace("Ź", "З")
    s = s.replace("Ż", "З")
    s = s.replace("Ž", "З")
    s = s.replace("Ǎ", "А")
    s = s.replace("Ș", "Ш")
    s = s.replace("Ё", "Е")
    s = s.replace("Є", "Е")
    s = s.replace("Ј", "Й")
    s = s.replace("Љ", "Л")
    s = s.replace("Њ", "Н")
    s = s.replace("Џ", "У")
    s = s.replace("Э", "Е")
    s = s.replace("Ḥ", "Х")
    s = s.replace("Ṣ", "С")
    s = s.replace("Ỷ", "Й")
    #LOWERCASE LETTERS
    s = s.replace("a", "а")
    s = s.replace("b", "б")
    s = s.replace("c", "к")
    s = s.replace("v", "в")
    s = s.replace("g", "г")
    s = s.replace("d", "д")
    s = s.replace("e", "е")
    s = s.replace("z", "з")
    s = s.replace("i", "и")
    s = s.replace("j", "й")
    s = s.replace("k", "к")
    s = s.replace("l", "л")
    s = s.replace("m", "м")
    s = s.replace("n", "н")
    s = s.replace("o", "о")
    s = s.replace("p", "п")
    s = s.replace("r", "р")
    s = s.replace("s", "с")
    s = s.replace("t", "т")
    s = s.replace("ț", "т")
    s = s.replace("w", "в")
    s = s.replace("f", "ф")
    s = s.replace("h", "х")
    s = s.replace("u", "у")
    s = s.replace("y", "и")
    s = s.replace("æ", "е")
    s = s.replace("ä", "е")
    s = s.replace("é", "е")
    s = s.replace("ə", "а")
    s = s.replace("î", "и")
    s = s.replace("ö", "йо")
    s = s.replace("ø", "йо")
    s = s.replace("õ", "йо")
    s = s.replace("ó", "о")
    s = s.replace("å", "о")
    s = s.replace("ß", "с")
    s = s.replace("à", "а")
    s = s.replace("á", "а")
    s = s.replace("â", "а")
    s = s.replace("ã", "а")
    s = s.replace("ç", "ч")
    s = s.replace("è", "е")
    s = s.replace("ê", "е")
    s = s.replace("ë", "е")
    s = s.replace("ì", "и")
    s = s.replace("í", "и")
    s = s.replace("ï", "и")
    s = s.replace("ð", "о")
    s = s.replace("ñ", "н")
    s = s.replace("ò", "о")
    s = s.replace("ô", "о")
    s = s.replace("ù", "у")
    s = s.replace("ú", "у")
    s = s.replace("û", "у")
    s = s.replace("ü", "у")
    s = s.replace("ý", "й")
    s = s.replace("þ", "т")
    s = s.replace("ÿ", "й")
    s = s.replace("ā", "а")
    s = s.replace("ă", "а")
    s = s.replace("ą", "а")
    s = s.replace("ć", "ч")
    s = s.replace("ċ", "ч")
    s = s.replace("č", "ч")
    s = s.replace("ď", "д")
    s = s.replace("đ", "д")
    s = s.replace("ē", "е")
    s = s.replace("ė", "е")
    s = s.replace("ę", "е")
    s = s.replace("ě", "е")
    s = s.replace("ğ", "г")
    s = s.replace("ģ", "г")
    s = s.replace("ī", "и")
    s = s.replace("ĭ", "и")
    s = s.replace("ı", "и")
    s = s.replace("ķ", "к")
    s = s.replace("ĺ", "л")
    s = s.replace("ļ", "л")
    s = s.replace("ľ", "л")
    s = s.replace("ł", "л")
    s = s.replace("ń", "н")
    s = s.replace("ņ", "н")
    s = s.replace("ň", "н")
    s = s.replace("ō", "о")
    s = s.replace("ő", "о")
    s = s.replace("œ", "е")
    s = s.replace("ŕ", "г")
    s = s.replace("ř", "г")
    s = s.replace("ś", "с")
    s = s.replace("ş", "с")
    s = s.replace("š", "с")
    s = s.replace("ţ", "л")
    s = s.replace("ť", "л")
    s = s.replace("ũ", "у")
    s = s.replace("ū", "у")
    s = s.replace("ŭ", "у")
    s = s.replace("ů", "у")
    s = s.replace("ű", "у")
    s = s.replace("ŷ", "й")
    s = s.replace("ź", "з")
    s = s.replace("ż", "з")
    s = s.replace("ž", "з")
    s = s.replace("ơ", "о")
    s = s.replace("ư", "у")
    s = s.replace("ǎ", "а")
    s = s.replace("ǐ", "и")
    s = s.replace("ǒ", "о")
    s = s.replace("ǔ", "у")
    s = s.replace("ș", "ш")
    s = s.replace("ϊ", "и")
    s = s.replace("э", "е")
    s = s.replace("ё", "е")
    s = s.replace("є", "е")
    s = s.replace("і", "и")
    s = s.replace("ј", "й")
    s = s.replace("љ", "л")
    s = s.replace("њ", "н")
    s = s.replace("ў", "й")
    s = s.replace("џ", "у")
    s = s.replace("ḥ", "х")
    s = s.replace("ṅ", "н")
    s = s.replace("ṇ", "н")
    s = s.replace("ṣ", "с")
    s = s.replace("ạ", "а")
    s = s.replace("ả", "а")
    s = s.replace("ấ", "а")
    s = s.replace("ầ", "а")
    s = s.replace("ẫ", "а")
    s = s.replace("ậ", "а")
    s = s.replace("ắ", "а")
    s = s.replace("ặ", "а")
    s = s.replace("ế", "е")
    s = s.replace("ề", "е")
    s = s.replace("ễ", "е")
    s = s.replace("ệ", "е")
    s = s.replace("ọ", "о")
    s = s.replace("ố", "о")
    s = s.replace("ồ", "о")
    s = s.replace("ổ", "о")
    s = s.replace("ỗ", "о")
    s = s.replace("ớ", "о")
    s = s.replace("ợ", "о")
    s = s.replace("ụ", "у")
    s = s.replace("ứ", "у")
    s = s.replace("ử", "у")
    s = s.replace("ữ", "у")
    s = s.replace("ỳ", "й")
    s = s.replace("ỹ", "й")
    s = s.replace("q", "к")
    s = s.replace("x", "кс")

    return s

def generate():
    with open("names.txt", "r") as f:
        gf_ids = {}
        q_ids  = {}
        for line in f:
            record = eval(line)
            if len(record[2]) == 0:
                continue
            name = record[2].get("en",next(record[2].items().__iter__())[0])
            name = name.split('/')[0].strip()
            name = name.lower()
            paren = name.find("(")
            if paren >= 0:
                name = name[:paren].strip()
            if record[1] in ["Q12308941","Q11879590"]:
                tag = "GN"
            else:
                tag = "SN"
            nt = (name,tag)
            info = gf_ids.get(nt)
            if not info:
                gf_ids[nt] = [record[0]]
                gf_id = name+"_"+tag
            else:
                if len(info) == 1:
                    q_ids[info[0]] = (name+"_1_"+tag,tag,record[1],record[2])
                info.append(record[0])
                gf_id = name+"_"+str(len(info))+"_"+tag
            q_ids[record[0]] = (gf_id,tag,record[1],record[2])

        def quote(s):
            plain = True
            if s[0].isdigit():
                plain = False
            else:
                for c in s:
                    if c not in "abcdefghijklmnopqrstuvwxyz_SGN0123456789":
                        plain=False
                        break

            if plain:
                q = s
            else:
                q = "'"
                for c in s:
                    if c == "'":
                        q = q + "\\'"
                    else:
                        q = q + c
                q = q + "'"

            return q

        with open("Names.gf","w") as out:
            out.write("abstract Names = Cat ** {\n")
            out.write("\n")
            out.write("cat GN ; SN ;\n")
            out.write("\n")
            for q_id,(gf_id,tag,name_type,labels) in sorted(q_ids.items(),key=lambda p: p[1]):
                out.write(("fun "+quote(gf_id)+" : "+tag+" ;").ljust(40)+"-- "+q_id+"\n")
            out.write("}\n")

        langs = [
          ("Afr",["af","nl","en"]),
          ("Bul",["bg","sr","ru","en"]),
          ("Cat",["ca","en"]),
          ("Chi",["zh"]),
          ("Dut",["nl","en"]),
          ("Eng",["en"]),
          ("Fin",["fi","en"]),
          ("Ger",["de","en"]),
          ("Kor",["ko"]),
          ("Pol",["pl","en"]),
          ("Ron",["ro","en"]),
          ("Som",["so","en"]),
          ("Swa",["sw","en"]),
          ("Tha",["th"]),
          ("Est",["fi","en"]),
          ("Fre",["fr","en"]),
          ("Ita",["it","en"]),
          ("Mlt",["mt","en"]),
          ("Por",["pt","en"]),
          ("Slv",["sl","en"]),
          ("Spa",["es","en"]),
          ("Swe",["sv","en"]),
          ("Tur",["tr","en"]),
          ]

        for lang,lang_codes  in langs:
            with open("Names"+lang+".gf","w") as out:
                out.write("concrete Names"+lang+" of Names = Cat"+lang+" ** open Paradigms"+lang+" in {\n")
                out.write("\n")
                out.write("lincat GN, SN = PN ;\n")
                out.write("\n")
                for q_id,(gf_id,tag,name_type,labels) in sorted(q_ids.items(),key=lambda p: p[1]):
                    lins = []
                    lin_list = []
                    for lang_code in lang_codes:
                        s = labels.get(lang_code)
                        if s:
                            paren = s.find("(")
                            if paren >= 0:
                                s = s[:paren]
                            if lang == "Bul" and lang_code != "bg":
                                s  = cyr(s)
                            lin_list = s.split("/")
                            break
                    for lin in lin_list:
                        lin = lin.strip()
                        if lang in ["Afr","Chi","Dut","Est","Fin","Kor","Swe","Tha","Tur"]:
                            lin = "mkPN \""+lin+"\""
                        elif lang in ["Som"]:
                            if name_type in ["Q12308941","Q18972245"]:
                                lin = "mkPN \""+lin+"\" sgMasc"
                            elif name_type in ["Q11879590","Q18972207"]:
                                lin = "mkPN \""+lin+"\" sgFem"
                            else:
                                lin = "mkPN \""+lin+"\""
                        else:
                            if name_type in ["Q12308941","Q18972245"]:
                                lin = "mkPN \""+lin+"\" masculine"
                            elif name_type in ["Q11879590","Q18972207"]:
                                lin = "mkPN \""+lin+"\" feminine"
                            else:
                                lin = "mkPN \""+lin+"\""
                        lins.append(lin)
                    if len(lins) == 1:
                        out.write("lin "+quote(gf_id)+" = "+lins[0]+" ;\n")
                    else:
                        out.write("lin "+quote(gf_id)+" = variants {"+"; ".join(lins)+"} ;\n")
                out.write("}\n")

generate()