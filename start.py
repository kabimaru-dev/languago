import subprocess



def languageChoose(sourceLanguage, targetLanguage, sentance):
    return subprocess.run(
        'curl -X POST http://localhost:5000/translate -d q="' + sentance + 
        '" -d source=' + sourceLanguage +
        ' -d target=' + targetLanguage, 
        shell=True, 
        check=True
    )

def pseudoSwitch(choose):
    if choose == "1" or choose == "en->bg" :
        while True:
            source = input("Write translation from EN to BG: " + "\n")
            
            languageChoose("en", "bg", source)

    elif choose == "bg->en" :
        print("bg->en")
    elif choose == "ru->en" :
        print("ru->en")
    elif choose == "en->ru" :
        print("en->ru")
    else :
        print("try again")

def checkSupportedLanguage(sourceLanguage, targetLanguage):
    
    supportedLanguage = ["en->bg"]

    for i in range(supportedLanguage.__len__()):
        if supportedLanguage[i] == en->bg

    # return True or False

# def pseudoGui():
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

def main():


    # for i in range(0-100):

    # choose = input(
    #     "You need to choose, for example, write: en->es" + "\n"
    # )

    # print(languageChoose("en", "bg", "asdsad"))

    checkSupportedLanguage("en", "bg")


    

main()