import subprocess



choose = input(
    "Choose: " + "\n" +
    "1. en->bg" + "\n" +
    "2. en->ru" + "\n" +
    "3. bg->en" + "\n" +
    "4. bg->ru" + "\n" +
    "5. ru->en" + "\n" +
    "6. ru->bg" + "\n"
)

if choose == "1" or choose == "en->bg" :
    while True:
        source = input("Write translation from EN to BG: " + "\n")
        
        subprocess.run('curl -X POST http://localhost:5000/translate -d q="'+ source +'" -d source=en -d target=bg', shell=True, check=True)
elif choose == "bg->en" :
    print("bg->en")
elif choose == "ru->en" :
    print("ru->en")
elif choose == "en->ru" :
    print("en->ru")
else :
    print("try again")