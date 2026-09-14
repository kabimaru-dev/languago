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

    # for i in range(supportedLanguage.__len__()):
    #     if (i-1) % 2:
    #         print(supportedLanguage[i][0])


    # print("size of arrayLanguages : ", supportedLanguage.__len__())

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
    mainLanguage = input(
        "Write, for example: en->ru" + "\n"
    )

    while True:
        first, second = "", ""
        first += mainLanguage[0]
        first += mainLanguage[1]
        second += mainLanguage[4]
        second += mainLanguage[5]

        if checkSupportedLanguage(mainLanguage) == True:
            source = input()
            print(strConverter(languageChoose(first, second, source)))
        elif checkSupportedLanguage(mainLanguage) == False:
            source = input()
            source = strConverter(languageChoose(first, "en", source))
            print(strConverter(languageChoose("en", second, source)))
        else:
            print("??? wrong type")

main()