import requests



def languageChoose(source_language, target_language, sentence):
    response = requests.post(
        "http://localhost:5000/translate",
        data={
            "q": sentence,
            "source": source_language,
            "target": target_language,
        }
    )

    response.raise_for_status()
    return response.text

def checkSupportedLanguage(choose):
    
    supportedLanguage = [
        ["sq->en"], [["Albanian"], ["English"]],
        ["ar->en"], [["Arabic"], ["English"]],
        ["az->en"], [["Azerbaijani"], ["English"]],
        ["eu->en"], [["Basque"], ["English"]],
        ["bn->en"], [["Bengali"], ["English"]],
        ["bg->en"], [["Bulgarian"], ["English"]],
        ["ca->en"], [["Catalan"], ["English"]],
        ["zt->en"], [["Chinese (traditional)"], ["English"]],
        ["zh->en"], [["Chinese"], ["English"]],
        ["cs->en"], [["Czech"], ["English"]],
        ["da->en"], [["Danish"], ["English"]],
        ["nl->en"], [["Dutch"], ["English"]],
        ["en->sq"], [["English"], ["Albanian"]],
        ["en->ar"], [["English"], ["Arabic"]],
        ["en->az"], [["English"], ["Azerbaijani"]],
        ["en->eu"], [["English"], ["Basque"]],
        ["en->bn"], [["English"], ["Bengali"]],
        ["en->bg"], [["English"], ["Bulgarian"]],
        ["en->ca"], [["English"], ["Catalan"]],
        ["en->zh"], [["English"], ["Chinese"]],
        ["en->zt"], [["English"], ["Chinese (traditional)"]],
        ["en->cs"], [["English"], ["Czech"]],
        ["en->da"], [["English"], ["Danish"]],
        ["en->nl"], [["English"], ["Dutch"]],
        ["en->eo"], [["English"], ["Esperanto"]],
        ["en->et"], [["English"], ["Estonian"]],
        ["en->fi"], [["English"], ["Finnish"]],
        ["en->fr"], [["English"], ["French"]],
        ["en->gl"], [["English"], ["Galician"]],
        ["en->de"], [["English"], ["German"]],
        ["en->el"], [["English"], ["Greek"]],
        ["en->he"], [["English"], ["Hebrew"]],
        ["en->hi"], [["English"], ["Hindi"]],
        ["en->hu"], [["English"], ["Hungarian"]],
        ["en->id"], [["English"], ["Indonesian"]],
        ["en->ga"], [["English"], ["Irish"]],
        ["en->it"], [["English"], ["Italian"]],
        ["en->ja"], [["English"], ["Japanese"]],
        ["en->ko"], [["English"], ["Korean"]],
        ["en->ky"], [["English"], ["Kyrgyz"]],
        ["en->lv"], [["English"], ["Latvian"]],
        ["en->lt"], [["English"], ["Lithuanian"]],
        ["en->ms"], [["English"], ["Malay"]],
        ["en->nb"], [["English"], ["Norwegian"]],
        ["en->fa"], [["English"], ["Persian"]],
        ["en->pl"], [["English"], ["Polish"]],
        ["en->pt"], [["English"], ["Portuguese"]],
        ["en->pb"], [["English"], ["Portuguese (Brazil)"]],
        ["en->ro"], [["English"], ["Romanian"]],
        ["en->ru"], [["English"], ["Russian"]],
        ["en->sk"], [["English"], ["Slovak"]],
        ["en->sl"], [["English"], ["Slovenian"]],
        ["en->es"], [["English"], ["Spanish"]],
        ["en->sv"], [["English"], ["Swedish"]],
        ["en->tl"], [["English"], ["Tagalog"]],
        ["en->th"], [["English"], ["Thai"]],
        ["en->tr"], [["English"], ["Turkish"]],
        ["en->uk"], [["English"], ["Ukrainian"]],
        ["en->ur"], [["English"], ["Urdu"]],
        ["en->vi"], [["English"], ["Vietnamese"]],
        ["eo->en"], [["Esperanto"], ["English"]],
        ["et->en"], [["Estonian"], ["English"]],
        ["fi->en"], [["Finnish"], ["English"]],
        ["fr->en"], [["French"], ["English"]],
        ["gl->en"], [["Galician"], ["English"]],
        ["de->en"], [["German"], ["English"]],
        ["el->en"], [["Greek"], ["English"]],
        ["he->en"], [["Hebrew"], ["English"]],
        ["hi->en"], [["Hindi"], ["English"]],
        ["hu->en"], [["Hungarian"], ["English"]],
        ["id->en"], [["Indonesian"], ["English"]],
        ["ga->en"], [["Irish"], ["English"]],
        ["it->en"], [["Italian"], ["English"]],
        ["ja->en"], [["Japanese"], ["English"]],
        ["ko->en"], [["Korean"], ["English"]],
        ["ky->en"], [["Kyrgyz"], ["English"]],
        ["lv->en"], [["Latvian"], ["English"]],
        ["lt->en"], [["Lithuanian"], ["English"]],
        ["ms->en"], [["Malay"], ["English"]],
        ["nb->en"], [["Norwegian"], ["English"]],
        ["fa->en"], [["Persian"], ["English"]],
        ["pl->en"], [["Polish"], ["English"]],
        ["pb->en"], [["Portuguese (Brazil)"], ["English"]],
        ["pt->en"], [["Portuguese"], ["English"]],
        ["pt->es"], [["Portuguese"], ["Spanish"]],
        ["ro->en"], [["Romanian"], ["English"]],
        ["ru->en"], [["Russian"], ["English"]],
        ["sk->en"], [["Slovak"], ["English"]],
        ["sl->en"], [["Slovenian"], ["English"]],
        ["es->en"], [["Spanish"], ["English"]],
        ["es->pt"], [["Spanish"], ["Portuguese"]],
        ["sv->en"], [["Swedish"], ["English"]],
        ["tl->en"], [["Tagalog"], ["English"]],
        ["th->en"], [["Thai"], ["English"]],
        ["tr->en"], [["Turkish"], ["English"]],
        ["uk->en"], [["Ukrainian"], ["English"]],
        ["ur->en"], [["Urdu"], ["English"]],
        ["vi->en"], [["Vietnamese"], ["English"]]
    ]

    for i in range(supportedLanguage.__len__()):
        if (i-1) % 2:
            print(supportedLanguage[i][0])


    print("size of arrayLanguages : ", supportedLanguage.__len__())

    for i in range(supportedLanguage.__len__()):
        if (i-1) % 2:
            if supportedLanguage[i][0] == choose:
                return True

    return False

def pseudoGui():

    print("Nothing")

def strConverter(input):
    result = ""
    # print(type(str(input)))
    input = str(input)
    # print(input)
    # print(input.__len__())
    for i in range(input.__len__()):
        i += 18
        if "\"" in input[i-1]:
            i += 1
            while not "\"" in input[i-1]:
                result += input[i-1]
                i += 1
            
            return result
    

def main():
    while True:
        mainLanguage = input(
            "You need to choose, for example, write: en" + "\n"
        )

        if checkSupportedLanguage(mainLanguage) == True:
            first, second = "", ""
            first += mainLanguage[0]
            first += mainLanguage[1]
            second += mainLanguage[4]
            second += mainLanguage[5]
            source = input()
            print(strConverter(languageChoose(first, second, source)))




        # match choose1:
        #     case "sq":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease") 
        #     case "sq":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")         
        #     case "ar":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "az":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "eu":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "bn":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "bg":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case "en":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source = input()
        #                     languageChoose(choose1, choose2, source)
        #             case "ru":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source1 = input()
        #                     source2 = strConverter(languageChoose("bg", "en", source1))
        #                     print(source1 + " > " + source2 + " > ", end='')
        #                     source3 = strConverter(languageChoose("en", "ru", source2))
        #                     print(source3)
        #     case "ca":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "zt":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "zh":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "cs":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "da":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "nl":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "en":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case "sq":
        #                 print("In realease")
        #             case "ar":
        #                 print("In realease")
        #             case "az":
        #                 print("In realease")
        #             case "eu":
        #                 print("In realease")
        #             case "bn":
        #                 print("In realease")
        #             case "bg":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source = input()
        #                     languageChoose(choose1, choose2, source)
        #             case "ca":
        #                 print("In realease")
        #             case "zh":
        #                 print("In realease")
        #             case "zt":
        #                 print("In realease")
        #             case "cs":
        #                 print("In realease")
        #             case "da":
        #                 print("In realease")
        #             case "nl":
        #                 print("In realease")
        #             case "eo":
        #                 print("In realease")
        #             case "et":
        #                 print("In realease")
        #             case "fi":
        #                 print("In realease")
        #             case "fr":
        #                 print("In realease")
        #             case "gl":
        #                 print("In realease")
        #             case "de":
        #                 print("In realease")
        #             case "el":
        #                 print("In realease")
        #             case "he":
        #                 print("In realease")
        #             case "hi":
        #                 print("In realease")
        #             case "hu":
        #                 print("In realease")
        #             case "id":
        #                 print("In realease")
        #             case "ga":
        #                 print("In realease")
        #             case "it":
        #                 print("In realease")
        #             case "ja":
        #                 print("In realease")
        #             case "ko":
        #                 print("In realease")
        #             case "ky":
        #                 print("In realease")
        #             case "lv":
        #                 print("In realease")
        #             case "lt":
        #                 print("In realease")
        #             case "ms":
        #                 print("In realease")
        #             case "nb":
        #                 print("In realease")
        #             case "fa":
        #                 print("In realease")
        #             case "pl":
        #                 print("In realease")
        #             case "pt":
        #                 print("In realease")
        #             case "pb":
        #                 print("In realease")
        #             case "ro":
        #                 print("In realease")
        #             case "ru":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source = input()
        #                     languageChoose(choose1, choose2, source)
        #             case "sk":
        #                 print("In realease")
        #             case "sl":
        #                 print("In realease")
        #             case "es":
        #                 print("In realease")
        #             case "sv":
        #                 print("In realease")
        #             case "tl":
        #                 print("In realease")
        #             case "th":
        #                 print("In realease")
        #             case "tr":
        #                 print("In realease")
        #             case "uk":
        #                 print("In realease")
        #             case "ur":
        #                 print("In realease")
        #             case "vi":
        #                 print("In realease")
        #     case "et":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "fi":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "fr":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "gl":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "de":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "el":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "he":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "hi":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "hu":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "id":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ga":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "it":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ja":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ko":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ky":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "lv":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "lt":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ms":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "nb":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "fa":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "pl":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "pb":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "pt":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case "en":
        #                 print("In realease")
        #             case "es":
        #                 print("In realease")
        #     case "po":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ru":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case "en":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source = input()
        #                     languageChoose(choose1, choose2, source)
        #             case "bg":
        #                 print("Write translation from "+choose1+" to "+choose2+": ")
        #                 while True:
        #                     print("> ", end='')
        #                     source1 = input()
        #                     source2 = strConverter(languageChoose("ru", "en", source1))
        #                     print(source1 + " > " + source2 + " > ", end='')
        #                     source3 = strConverter(languageChoose("en", "bg", source2))
        #                     print(source3)
        #     case "sk":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "sl":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "es":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "sv":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "tl":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "th":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "tr":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "uk":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "ur":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")
        #     case "vi":
        #         choose2 = input(
        #             "You need to choose, for example, write: bg" + "\n"
        #         )
        #         match choose2:
        #             case en:
        #                 print("In realease")



main()