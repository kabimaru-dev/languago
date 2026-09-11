import subprocess



def languageChoose(sourceLanguage, targetLanguage, sentance):
    return subprocess.run(
        'curl -X POST http://localhost:5000/translate -d q="' + sentance + 
        '" -d source=' + sourceLanguage +
        ' -d target=' + targetLanguage, 
        shell=True, 
        check=True
    )

def checkSupportedLanguage(sourceLanguage, targetLanguage, choose):
    
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

    print("size of arrayLanguages : ", supportedLanguage.__len__())



    for i in range(supportedLanguage.__len__()):
        if (i-1) % 2:
            # print(type(supportedLanguage[i][0]), "==", type(choose))
            # print(supportedLanguage[i][0], "==", choose)
            # print(supportedLanguage[i][0] == choose)
            if supportedLanguage[i][0] == choose:
                return True
        
    return False

        # else:
        #     return False

    # supportedLanguage[]

    # for i in range(supportedLanguage.__len__()):
    #     if supportedLanguage[i] == choose :
    #         return True


    # return True or False

def pseudoGui():
    #     for i in range(0-100):
            

    #     return (
    #         "Choose: " + "\n" +
    #         "1. en->bg" + "\n" +
    #         "2. en->ru" + "\n" +
    #         "3. bg->en" + "\n" +
    #         "4. bg->ru" + "\n" +
    #         "5. ru->en" + "\n" +
    #         "6. ru->bg" + "\n"
    #     )
    print("Nothing")

def pseudoSwitch(choose):
    # if choose == "1" or choose == "en->bg" :
    if checkSupportedLanguage("en", "bg", choose):
        if choose == "en->bg" :
            while True:
                source = input("Write translation from EN to BG: " + "\n")
                
                languageChoose("en", "bg", source)
        else :
            print("error") # in the future when we separate en->es as en, es.
    else:
        print("Language is not supported")



def main():
    while True:
        choose = input(
            "You need to choose, for example, write: en->es" + "\n"
        )

        pseudoSwitch(choose)

        print("error") # in the future when we separate en->es as en, es.





main()